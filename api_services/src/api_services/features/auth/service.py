from datetime import UTC, datetime, timedelta
from uuid import UUID

from api_services.core.security import generate_session_token
from api_services.core.settings import settings
from api_services.features.auth.models import AuthMethodType, UserSession
from fastapi import Response
from sqlmodel import Session, select


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
            max_age=settings.USER_SESSION_TOKEN_EXPIRE_DAYS * 60,
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
