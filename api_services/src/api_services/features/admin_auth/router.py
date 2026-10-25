from fastapi import APIRouter, Depends, HTTPException, Response, status

from api_services.core.database import DatabaseSession
from api_services.core.security import build_otpauth_uri
from api_services.features.admin.models import Admin
from api_services.features.admin.service import create_admin, get_admin_by_email
from api_services.features.admin_auth.deps import (
    AdminCompleteRegistrationToken,
    AdminMfaToken,
    AdminRegistrationToken,
    CurrentAdmin,
    get_optional_current_admin,
)
from api_services.features.admin_auth.models import (
    AdminCheckAuthResponse,
    AdminCompleteRegistrationPayload,
    AdminEphemeralTokenData,
    AdminLoginPayload,
    AdminLoginResponse,
    AdminRegisterPayload,
    AdminRegisterVerifyOtpPayload,
    AdminTotpCodePayload,
    AdminTotpSetupResponse,
)
from api_services.features.admin_auth.service import (
    ADMIN_EPHEMERAL_COOKIE,
    authenticate_admin,
    create_admin_password,
    create_admin_registration_otp,
    create_admin_session,
    create_or_reset_admin_totp_secret,
    get_admin_totp_secret,
    is_admin_email_domain_allowed,
    is_admin_totp_enabled,
    issue_admin_ephemeral_token,
    normalize_admin_email,
    revoke_admin_session,
    verify_admin_registration_otp,
    verify_admin_totp,
    verify_and_enable_admin_totp,
)
from api_services.features.auth.models import AuthMethodType

router = APIRouter()


@router.post("/register", status_code=status.HTTP_204_NO_CONTENT)
def register_admin(
    db: DatabaseSession, payload: AdminRegisterPayload, response: Response
):
    if not is_admin_email_domain_allowed(payload.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email domain is not allowed for admin registration",
        )

    if get_admin_by_email(db, payload.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An admin with this email already exists",
        )

    create_admin_registration_otp(db, payload.email)
    db.commit()

    issue_admin_ephemeral_token(
        response,
        AdminEphemeralTokenData(
            email=normalize_admin_email(payload.email),
            name=payload.name.strip(),
            purpose="admin_registration",
        ),
    )


@router.post("/register/verify-otp", status_code=status.HTTP_204_NO_CONTENT)
def register_verify_otp_admin(
    db: DatabaseSession,
    payload: AdminRegisterVerifyOtpPayload,
    ephemeral_token: AdminRegistrationToken,
    response: Response,
):
    if not verify_admin_registration_otp(db, ephemeral_token.email, payload.otp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP",
        )

    db.commit()

    issue_admin_ephemeral_token(
        response,
        AdminEphemeralTokenData(
            email=ephemeral_token.email,
            name=ephemeral_token.name,
            purpose="admin_complete_registration",
        ),
    )


@router.post("/register/complete", status_code=status.HTTP_204_NO_CONTENT)
def register_complete_admin(
    db: DatabaseSession,
    payload: AdminCompleteRegistrationPayload,
    ephemeral_token: AdminCompleteRegistrationToken,
    response: Response,
):
    if not is_admin_email_domain_allowed(ephemeral_token.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email domain is not allowed for admin registration",
        )

    if get_admin_by_email(db, ephemeral_token.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An admin with this email already exists",
        )

    admin = create_admin(db, ephemeral_token.email, ephemeral_token.name)
    create_admin_password(db, admin.id, payload.password)
    db.commit()

    create_admin_session(
        db,
        admin_id=admin.id,
        login_method_type=AuthMethodType.PASSWORD,
        response=response,
    )

    response.delete_cookie(ADMIN_EPHEMERAL_COOKIE)


@router.post("/login", response_model=AdminLoginResponse)
def login_admin(
    db: DatabaseSession,
    payload: AdminLoginPayload,
    response: Response,
) -> AdminLoginResponse:
    admin = authenticate_admin(db, payload.email, payload.password)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if is_admin_totp_enabled(db, admin.id):
        issue_admin_ephemeral_token(
            response,
            AdminEphemeralTokenData(
                email=admin.email,
                name=admin.name,
                purpose="admin_mfa",
                admin_id=admin.id,
            ),
        )
        return AdminLoginResponse(mfa_required=True)

    create_admin_session(
        db,
        admin_id=admin.id,
        login_method_type=AuthMethodType.PASSWORD,
        response=response,
    )
    response.delete_cookie(ADMIN_EPHEMERAL_COOKIE)

    return AdminLoginResponse(mfa_required=False)


@router.post("/login/totp", response_model=AdminLoginResponse)
def login_admin_totp(
    db: DatabaseSession,
    payload: AdminTotpCodePayload,
    mfa_token: AdminMfaToken,
    response: Response,
) -> AdminLoginResponse:
    admin = db.get(Admin, mfa_token.admin_id)
    if not admin or admin.deleted_at is not None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if not verify_admin_totp(db, admin.id, payload.code):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid TOTP code",
        )

    create_admin_session(
        db,
        admin_id=admin.id,
        login_method_type=AuthMethodType.PASSWORD,
        response=response,
    )

    response.delete_cookie(ADMIN_EPHEMERAL_COOKIE)

    return AdminLoginResponse(mfa_required=False)


@router.post("/totp/setup", response_model=AdminTotpSetupResponse)
def setup_admin_totp(
    db: DatabaseSession, admin: CurrentAdmin
) -> AdminTotpSetupResponse:
    existing_totp_secret = get_admin_totp_secret(db, admin.id)
    if existing_totp_secret and existing_totp_secret.is_enabled:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="TOTP is already enabled",
        )

    admin_totp_secret = create_or_reset_admin_totp_secret(db, admin.id)

    return AdminTotpSetupResponse(
        secret=admin_totp_secret.secret,
        otpauth_uri=build_otpauth_uri(admin_totp_secret.secret, admin.email),
    )


@router.post("/totp/verify", status_code=status.HTTP_204_NO_CONTENT)
def verify_admin_totp_setup(
    db: DatabaseSession,
    admin: CurrentAdmin,
    payload: AdminTotpCodePayload,
):
    if not verify_and_enable_admin_totp(db, admin.id, payload.code):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid TOTP code",
        )


@router.get("/me", response_model=AdminCheckAuthResponse)
def check_admin_auth(
    session_admin=Depends(get_optional_current_admin),
) -> AdminCheckAuthResponse:
    _session, admin = session_admin

    if admin is None:
        return AdminCheckAuthResponse(is_authenticated=False, email=None)

    return AdminCheckAuthResponse(is_authenticated=True, email=admin.email)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout_admin(
    db: DatabaseSession,
    response: Response,
    session_admin=Depends(get_optional_current_admin),
):
    session, _admin = session_admin

    revoke_admin_session(db=db, response=response, session=session)
    response.delete_cookie(ADMIN_EPHEMERAL_COOKIE)
