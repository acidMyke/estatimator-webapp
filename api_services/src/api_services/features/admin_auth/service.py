from datetime import UTC, datetime, timedelta
from uuid import UUID

from fastapi import Response
from sqlmodel import Session, desc, func, select

from api_services.core.security import (
    generate_otp,
    generate_session_token,
    generate_totp_secret,
    get_password_hash,
    jwt_encode,
    verify_password,
    verify_totp,
)
from api_services.core.settings import settings
from api_services.features.admin.models import Admin
from api_services.features.admin.service import get_admin_by_email
from api_services.features.admin_auth.models import (
    AdminEphemeralTokenData,
    AdminOtp,
    AdminPassword,
    AdminSession,
    AdminTotpSecret,
)
from api_services.features.auth.models import AuthMethodType, AuthOtpUsageType

ADMIN_SESSION_COOKIE = "admin_session_token"
ADMIN_EPHEMERAL_COOKIE = "admin_ephemeral_token"

ADMIN_EPHEMERAL_TOKEN_MAX_AGES = {
    "admin_registration": timedelta(minutes=8),
    "admin_complete_registration": timedelta(minutes=8),
    "admin_mfa": timedelta(minutes=5),
}
ADMIN_OTP_MAX_AGE = timedelta(minutes=5)


def normalize_admin_email(email: str) -> str:
    return email.strip().lower()


def is_admin_email_domain_allowed(email: str) -> bool:
    normalized = normalize_admin_email(email)
    if "@" not in normalized:
        return False

    domain = normalized.rsplit("@", 1)[1].strip().rstrip(".")
    if not domain:
        return False

    return any(
        domain == allowed_domain or domain.endswith(f".{allowed_domain}")
        for allowed_domain in settings.ADMIN_ALLOWED_EMAIL_DOMAINS
    )


def create_admin_registration_otp(db: Session, email: str) -> AdminOtp:
    otp = generate_otp()
    expires_at = datetime.now(UTC) + ADMIN_OTP_MAX_AGE
    # TODO: @acidMyke add email sending here
    print(f"OTP: {otp}")
    admin_otp = AdminOtp(
        email=normalize_admin_email(email),
        usage_type=AuthOtpUsageType.REGISTRATION,
        hashed_password=get_password_hash(otp),
        expires_at=expires_at,
    )
    db.add(admin_otp)
    return admin_otp


def verify_admin_registration_otp(db: Session, email: str, otp: str) -> bool:
    now = datetime.now(UTC)
    stmt = (
        select(AdminOtp)
        .where(
            func.lower(AdminOtp.email) == normalize_admin_email(email),
            AdminOtp.usage_type == AuthOtpUsageType.REGISTRATION,
            AdminOtp.used_at == None,
            AdminOtp.deleted_at == None,
            AdminOtp.expires_at > now,
        )
        .order_by(desc(AdminOtp.created_at))
    )
    admin_otp = db.exec(stmt).first()
    if not admin_otp:
        return False

    if not verify_password(otp, admin_otp.hashed_password):
        return False

    admin_otp.used_at = now
    admin_otp.last_used_at = now
    db.add(admin_otp)
    return True


def create_admin_password(db: Session, admin_id: UUID, password: str) -> AdminPassword:
    stmt = select(AdminPassword).where(
        AdminPassword.admin_id == admin_id,
        AdminPassword.deleted_at == None,
    )
    now = datetime.now(UTC)
    for existing_password in db.exec(stmt).all():
        existing_password.deleted_at = now
        db.add(existing_password)

    admin_password = AdminPassword(
        admin_id=admin_id,
        hashed_password=get_password_hash(password),
    )
    db.add(admin_password)
    return admin_password


def authenticate_admin(db: Session, email: str, password: str) -> Admin | None:
    admin = get_admin_by_email(db, email)
    if not admin:
        return None

    stmt = (
        select(AdminPassword)
        .where(
            AdminPassword.admin_id == admin.id,
            AdminPassword.deleted_at == None,
        )
        .order_by(desc(AdminPassword.created_at))
    )
    admin_password = db.exec(stmt).first()
    if not admin_password:
        return None

    if not verify_password(password, admin_password.hashed_password):
        return None

    admin_password.last_used_at = datetime.now(UTC)
    db.add(admin_password)
    db.commit()

    return admin


def get_admin_session_data_by_token(db: Session, session_token: str) -> AdminSession:
    stmt = select(AdminSession).where(
        AdminSession.session_token == session_token,
        AdminSession.expires_at > datetime.now(UTC),
    )
    return db.exec(stmt).one()


def revoke_active_admin_sessions(db: Session, admin_id: UUID) -> None:
    now = datetime.now(UTC)
    stmt = select(AdminSession).where(
        AdminSession.admin_id == admin_id,
        AdminSession.expires_at > now,
    )
    for active_session in db.exec(stmt).all():
        active_session.expires_at = now
        db.add(active_session)


def create_admin_session(
    db: Session,
    *,
    admin_id: UUID,
    login_method_type: AuthMethodType,
    parent_session_id: UUID | None = None,
    response: Response | None = None,
) -> AdminSession:
    revoke_active_admin_sessions(db, admin_id)

    session_token = generate_session_token()
    expires_at = datetime.now(UTC) + timedelta(
        minutes=settings.ADMIN_SESSION_TOKEN_EXPIRE_MINUTES
    )
    session = AdminSession(
        admin_id=admin_id,
        session_token=session_token,
        expires_at=expires_at,
        login_method_type=login_method_type,
        parent_session_id=parent_session_id,
    )
    db.add(session)
    db.commit()

    if response:
        response.set_cookie(
            key=ADMIN_SESSION_COOKIE,
            value=session_token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=int(
                timedelta(
                    minutes=settings.ADMIN_SESSION_TOKEN_EXPIRE_MINUTES
                ).total_seconds()
            ),
        )

    return session


def refresh_admin_session(
    db: Session,
    existing_session: AdminSession,
    *,
    response: Response | None = None,
) -> AdminSession:
    return create_admin_session(
        db,
        admin_id=existing_session.admin_id,
        login_method_type=existing_session.login_method_type,
        parent_session_id=existing_session.id,
        response=response,
    )


def revoke_admin_session(
    *,
    db: Session | None = None,
    response: Response | None = None,
    session: AdminSession | None = None,
    session_token: str | None = None,
) -> None:
    if db:
        if session_token and not session:
            session = get_admin_session_data_by_token(db, session_token)

        if session:
            session.expires_at = datetime.now(UTC)
            db.add(session)
            db.commit()

    if response:
        response.delete_cookie(ADMIN_SESSION_COOKIE)


def issue_admin_ephemeral_token(
    response: Response, data: AdminEphemeralTokenData
) -> None:
    max_age = ADMIN_EPHEMERAL_TOKEN_MAX_AGES[data.purpose]
    ephemeral_token = jwt_encode(
        data.model_dump(mode="json"),
        max_age=max_age,
    )
    response.set_cookie(
        key=ADMIN_EPHEMERAL_COOKIE,
        value=ephemeral_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=int(max_age.total_seconds()),
    )


def get_admin_totp_secret(db: Session, admin_id: UUID) -> AdminTotpSecret | None:
    stmt = select(AdminTotpSecret).where(AdminTotpSecret.admin_id == admin_id)
    return db.exec(stmt).first()


def is_admin_totp_enabled(db: Session, admin_id: UUID) -> bool:
    admin_totp_secret = get_admin_totp_secret(db, admin_id)
    return bool(admin_totp_secret and admin_totp_secret.is_enabled)


def create_or_reset_admin_totp_secret(db: Session, admin_id: UUID) -> AdminTotpSecret:
    secret = generate_totp_secret()
    admin_totp_secret = get_admin_totp_secret(db, admin_id)
    if admin_totp_secret:
        admin_totp_secret.secret = secret
        admin_totp_secret.is_enabled = False
        admin_totp_secret.verified_at = None
        admin_totp_secret.last_used_at = None
    else:
        admin_totp_secret = AdminTotpSecret(admin_id=admin_id, secret=secret)

    db.add(admin_totp_secret)
    db.commit()
    return admin_totp_secret


def verify_and_enable_admin_totp(db: Session, admin_id: UUID, code: str) -> bool:
    admin_totp_secret = get_admin_totp_secret(db, admin_id)
    if not admin_totp_secret:
        return False

    if not verify_totp(admin_totp_secret.secret, code):
        return False

    now = datetime.now(UTC)
    admin_totp_secret.is_enabled = True
    admin_totp_secret.verified_at = now
    admin_totp_secret.last_used_at = now
    db.add(admin_totp_secret)
    db.commit()
    return True


def verify_admin_totp(db: Session, admin_id: UUID, code: str) -> bool:
    admin_totp_secret = get_admin_totp_secret(db, admin_id)
    if not admin_totp_secret or not admin_totp_secret.is_enabled:
        return False

    if not verify_totp(admin_totp_secret.secret, code):
        return False

    admin_totp_secret.last_used_at = datetime.now(UTC)
    db.add(admin_totp_secret)
    db.commit()
    return True
