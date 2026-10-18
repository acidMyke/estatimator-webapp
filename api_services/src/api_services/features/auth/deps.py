from datetime import UTC, datetime, timedelta

from api_services.features.auth.service import (
    get_session_data_by_token,
    refresh_session,
    revoke_session,
)
from fastapi import HTTPException, Request, Response, status

from ...core.database import DatabaseSession
from .models import User


def get_current_user(request: Request, response: Response, db: DatabaseSession) -> User:
    session_token = request.cookies.get("session_token")
    ip_address = request.headers.get("x-forwarded-for")
    user_agent = request.headers.get("user-agent")

    if ip_address:
        ip_address = ip_address.split(",")[0].strip()

    if (not ip_address or ip_address == "") and request.client:
        ip_address = request.client.host

    now = datetime.now(UTC)

    if not session_token or not user_agent:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user_session = get_session_data_by_token(db, session_token, user_agent)

    if not user_session:
        revoke_session(response=response)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if now + timedelta(days=1) > user_session.expires_at:
        refresh_session(db, user_session, ip_address=ip_address, response=response)

    user = db.get(User, user_session.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user
