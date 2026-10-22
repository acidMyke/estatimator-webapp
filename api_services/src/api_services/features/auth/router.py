from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlmodel import desc, select

from api_services.core.database import DatabaseSession
from api_services.features.auth.deps import (
    EphemeralToken,
    get_optional_current_user,
)
from api_services.features.auth.models import (
    AuthMethodType,
    AuthOtpUsageType,
    CheckAuthResponse,
    CompleteRegistrationPayload,
    EphemeralTokenData,
    LoginPayload,
    RegisterationVerifyOtpPayload,
    RegisterPayload,
)
from api_services.features.auth.service import (
    authenticate_user,
    create_session,
    create_user_otp,
    create_user_password,
    issue_ephemeral_token,
    verify_user_otp,
)
from api_services.features.users.models import User, UserEmail
from api_services.features.users.service import create_user

router = APIRouter(
    tags=["auth"],
)


@router.post("/register", status_code=status.HTTP_204_NO_CONTENT)
def register_user(db: DatabaseSession, payload: RegisterPayload, response: Response):
    user = create_user(db, payload)
    create_user_otp(db, user.id, AuthOtpUsageType.REGISTRATION)
    db.commit()
    issue_ephemeral_token(
        response, EphemeralTokenData(user_id=user.id, purpose="registration")
    )


@router.post("/register/verify-otp", status_code=status.HTTP_204_NO_CONTENT)
def register_verify_otp_user(
    db: DatabaseSession,
    payload: RegisterationVerifyOtpPayload,
    ephemeral_token: EphemeralToken,
    response: Response,
):
    if ephemeral_token.purpose != "registration":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = db.get(User, ephemeral_token.user_id)
    if not user or user.deleted_at is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    if not verify_user_otp(
        db,
        ephemeral_token.user_id,
        payload.otp,
        AuthOtpUsageType.REGISTRATION,
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP",
        )

    stmt = select(UserEmail).where(
        UserEmail.user_id == ephemeral_token.user_id,
        UserEmail.deleted_at == None,
    )
    user_emails = db.exec(stmt).all()
    for user_email in user_emails:
        user_email.is_verified = True
        user_email.is_active = True
        db.add(user_email)

    db.commit()

    issue_ephemeral_token(
        response,
        EphemeralTokenData(
            user_id=ephemeral_token.user_id,
            purpose="complete_registration",
        ),
    )


@router.post("/register/complete", status_code=status.HTTP_204_NO_CONTENT)
def register_complete_user(
    request: Request,
    db: DatabaseSession,
    payload: CompleteRegistrationPayload,
    ephemeral_token: EphemeralToken,
    response: Response,
):
    if ephemeral_token.purpose != "complete_registration":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = db.get(User, ephemeral_token.user_id)
    if not user or user.deleted_at is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    create_user_password(db, user.id, payload.password)

    user.is_verified = True
    db.add(user)

    stmt = select(UserEmail).where(
        UserEmail.user_id == user.id,
        UserEmail.deleted_at == None,
    )
    user_emails = db.exec(stmt).all()
    for user_email in user_emails:
        user_email.is_verified = True
        user_email.is_active = True
        db.add(user_email)

    db.commit()

    ip_address = request.headers.get("x-forwarded-for")
    user_agent = request.headers.get("user-agent")

    if ip_address:
        ip_address = ip_address.split(",")[0].strip()

    if (not ip_address or ip_address == "") and request.client:
        ip_address = request.client.host

    create_session(
        db,
        user_id=user.id,
        login_method_type=AuthMethodType.PASSWORD,
        user_agent=user_agent,
        ip_address=ip_address,
        response=response,
    )

    response.delete_cookie("ephemeral_token")


@router.post("/login")
def login_user(
    request: Request,
    db: DatabaseSession,
    payload: LoginPayload,
    response: Response,
):
    user = authenticate_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is not verified",
        )

    ip_address = request.headers.get("x-forwarded-for")
    user_agent = request.headers.get("user-agent")

    if ip_address:
        ip_address = ip_address.split(",")[0].strip()

    if (not ip_address or ip_address == "") and request.client:
        ip_address = request.client.host

    create_session(
        db,
        user_id=user.id,
        login_method_type=AuthMethodType.PASSWORD,
        user_agent=user_agent,
        ip_address=ip_address,
        response=response,
    )

    response.delete_cookie("ephemeral_token")


@router.get("/me", response_model=CheckAuthResponse)
def check_auth(
    db: DatabaseSession, user=Depends(get_optional_current_user)
) -> CheckAuthResponse:
    if not user or not user.is_verified:
        return CheckAuthResponse(is_authenticated=False, email=None)

    stmt = (
        select(UserEmail)
        .where(
            UserEmail.user_id == user.id,
            UserEmail.deleted_at == None,
        )
        .order_by(
            desc(UserEmail.is_active),
            desc(UserEmail.is_verified),
            desc(UserEmail.created_at),
        )
    )
    user_email = db.exec(stmt).first()
    email = user_email.email if user_email else None

    return CheckAuthResponse(
        is_authenticated=True,
        email=email,
    )
