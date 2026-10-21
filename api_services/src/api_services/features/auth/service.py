from datetime import UTC, datetime, timedelta
from uuid import UUID

from api_services.core.security import (
    generate_otp,
    generate_session_token,
    get_password_hash,
    jwt_encode,
    verify_password,
)
from api_services.core.settings import settings
from api_services.features.auth.models import (
    AuthMethodType,
    AuthOtpUsageType,
    EphemeralTokenData,
    UserOtp,
    UserPassword,
    UserSession,
)
from fastapi import Response
from sqlmodel import Session, desc, select


def get_session_data_by_token(
    db: Session,
    session_token: str,
    user_agent: str | None = None,
):
    stmt = select(UserSession).where(
        UserSession.session_token == session_token,
        UserSession.expires_at > datetime.now(UTC),
    )
    if user_agent:
        stmt = stmt.where(UserSession.user_agent == user_agent)

    return db.exec(stmt).one()


def refresh_session(
    db: Session,
    existing_session: UserSession,
    *,
    ip_address: str | None = None,
    response: Response | None = None,
):
    revoke_session(db=db, session=existing_session)
    create_session(
        db,
        user_id=existing_session.user_id,
        user_agent=existing_session.user_agent,
        login_method_type=existing_session.login_method_type,
        ip_address=ip_address,
        parent_session_id=existing_session.id,
        response=response,
    )


def create_session(
    db: Session,
    *,
    user_id: UUID,
    login_method_type: AuthMethodType,
    user_agent: str | None = None,
    ip_address: str | None = None,
    parent_session_id: UUID | None = None,
    response: Response | None = None,
):
    session_token = generate_session_token()
    expires_at = datetime.now(UTC) + timedelta(
        days=settings.USER_SESSION_TOKEN_EXPIRE_DAYS
    )
    session = UserSession(
        user_id=user_id,
        session_token=session_token,
        expires_at=expires_at,
        login_method_type=login_method_type,
        user_agent=user_agent,
        ip_address=ip_address,
        parent_session_id=parent_session_id,
    )
    db.add(session)
    db.commit()

    if response:
        response.set_cookie(
            key="session_token",
            value=session_token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=int(
                timedelta(days=settings.USER_SESSION_TOKEN_EXPIRE_DAYS).total_seconds()
            ),
        )


def revoke_session(
    *,
    db: Session | None = None,
    response: Response | None = None,
    session: UserSession | None = None,
    session_token: str | None = None,
):
    if db:
        if session_token and not session:
            session = get_session_data_by_token(db, session_token)

        if session:
            session.expires_at = datetime.now(UTC)
            db.add(session)
            db.commit()

    if response:
        response.delete_cookie("session_token")


def create_user_otp(db: Session, user_id: UUID, usage_type: AuthOtpUsageType):
    otp = generate_otp()
    hashed_password = get_password_hash(otp)
    expires_at = datetime.now(UTC) + timedelta(minutes=5)
    # TODO: @acidMyke add email sending here
    print(f"OTP: {otp}")
    user_otp = UserOtp(
        user_id=user_id,
        usage_type=usage_type,
        hashed_password=hashed_password,
        expires_at=expires_at,
    )
    db.add(user_otp)


def issue_ephemeral_token(response: Response, data: EphemeralTokenData):
    max_age = timedelta(minutes=8)
    ephemeral_token = jwt_encode(
        data.model_dump(mode="json"),
        max_age=max_age,
    )
    response.set_cookie(
        key="ephemeral_token",
        value=ephemeral_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=int(max_age.total_seconds()),
    )


def verify_user_otp(
    db: Session, user_id: UUID, otp: str, usage_type: AuthOtpUsageType
) -> bool:
    now = datetime.now(UTC)
    stmt = (
        select(UserOtp)
        .where(
            UserOtp.user_id == user_id,
            UserOtp.usage_type == usage_type,
            UserOtp.used_at == None,
            UserOtp.deleted_at == None,
            UserOtp.expires_at > now,
        )
        .order_by(desc(UserOtp.created_at))
    )
    user_otp = db.exec(stmt).first()
    if not user_otp:
        return False

    if not verify_password(otp, user_otp.hashed_password):
        return False

    user_otp.used_at = now
    user_otp.last_used_at = now
    db.add(user_otp)
    return True


def create_user_password(
    db: Session,
    user_id: UUID,
    password: str,
) -> UserPassword:
    stmt = select(UserPassword).where(
        UserPassword.user_id == user_id,
        UserPassword.deleted_at == None,
    )
    existing_passwords = db.exec(stmt).all()
    now = datetime.now(UTC)
    for existing in existing_passwords:
        existing.deleted_at = now
        db.add(existing)

    hashed_password = get_password_hash(password)
    user_password = UserPassword(
        user_id=user_id,
        hashed_password=hashed_password,
    )
    db.add(user_password)
    return user_password
