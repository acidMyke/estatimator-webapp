from datetime import UTC, datetime, timedelta
from uuid import UUID

from fastapi import Response
from sqlmodel import Session

from api_services.core.security import (
    generate_otp,
    get_password_hash,
)
from api_services.core.settings import settings
from api_services.features.admin.models import Admin
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

# A single ephemeral cookie backs every multi-step admin flow; the signed "purpose"
# claim (AdminEphemeralTokenData) decides which step is allowed to consume it.
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
    pass


def create_admin_password(db: Session, admin_id: UUID, password: str) -> AdminPassword:
    pass


def authenticate_admin(db: Session, email: str, password: str) -> Admin | None:
    pass


def get_admin_session_data_by_token(db: Session, session_token: str) -> AdminSession:
    pass


def revoke_active_admin_sessions(db: Session, admin_id: UUID) -> None:
    pass


def create_admin_session(
    db: Session,
    *,
    admin_id: UUID,
    login_method_type: AuthMethodType,
    parent_session_id: UUID | None = None,
    response: Response | None = None,
) -> AdminSession:
    pass


def refresh_admin_session(
    db: Session,
    existing_session: AdminSession,
    *,
    response: Response | None = None,
) -> AdminSession:
    pass


def revoke_admin_session(
    *,
    db: Session | None = None,
    response: Response | None = None,
    session: AdminSession | None = None,
    session_token: str | None = None,
) -> None:
    pass


def issue_admin_ephemeral_token(
    response: Response, data: AdminEphemeralTokenData
) -> None:
    pass


def get_admin_totp_secret(db: Session, admin_id: UUID) -> AdminTotpSecret | None:
    return True


def is_admin_totp_enabled(db: Session, admin_id: UUID) -> bool:
    return True


def create_or_reset_admin_totp_secret(db: Session, admin_id: UUID) -> AdminTotpSecret:
    pass


def verify_and_enable_admin_totp(db: Session, admin_id: UUID, code: str) -> bool:
    return True


def verify_admin_totp(db: Session, admin_id: UUID, code: str) -> bool:
    return True
