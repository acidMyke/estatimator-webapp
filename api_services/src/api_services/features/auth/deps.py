from datetime import UTC, datetime, timedelta
from typing import Annotated

from api_services.core.security import jwt_decode
from api_services.features.auth.service import (
    get_session_data_by_token,
    refresh_session,
    revoke_session,
)
from fastapi import Depends, HTTPException, Request, Response, status
from jwt import PyJWTError
from pydantic import ValidationError

from ...core.database import DatabaseSession
from .models import EphemeralTokenData, User


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


def get_ephemeral_token(request: Request):
    ephemeral_token = request.cookies.get("ephemeral_token")

    if not ephemeral_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        raw_token_data = jwt_decode(ephemeral_token)
        return EphemeralTokenData.model_validate(raw_token_data)
    except (PyJWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


EphemeralToken = Annotated[EphemeralTokenData, Depends(get_ephemeral_token)]
