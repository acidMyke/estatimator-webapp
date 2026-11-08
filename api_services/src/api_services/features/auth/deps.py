from datetime import UTC, datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, Request, Response, status
from jwt import PyJWTError
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound

from api_services.core.database import DatabaseSession
from api_services.core.security import jwt_decode
from api_services.features.auth.models import EphemeralTokenData, User
from api_services.features.auth.service import (
    get_session_data_by_token,
    refresh_session,
    revoke_session,
)


def get_optional_current_user(
    request: Request, response: Response, db: DatabaseSession
):
    session_token = request.cookies.get("session_token")
    user_agent = request.headers.get("user-agent")

    if not session_token or not user_agent:
        return None, None

    ip_address = request.headers.get("x-forwarded-for")
    if ip_address:
        ip_address = ip_address.split(",")[0].strip()

    if (not ip_address or ip_address == "") and request.client:
        ip_address = request.client.host

    now = datetime.now(UTC)

    try:
        session = get_session_data_by_token(db, session_token, user_agent)
    except NoResultFound:
        revoke_session(response=response)
        return None

    if now + timedelta(days=1) > session.expires_at:
        refresh_session(db, session, ip_address=ip_address, response=response)

    user = db.get(User, session.user_id)
    if not user or user.deleted_at is not None:
        return None

    return None, None


def get_current_user(session_user=Depends(get_optional_current_user)) -> User:
    session, user = session_user

    if session is None or user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_ephemeral_token(request: Request):
    ephemeral_token = request.cookies.get("ephemeral_token")

    if not ephemeral_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        raw_token_data = jwt_decode(ephemeral_token)
        return EphemeralTokenData.model_validate(raw_token_data)
    except PyJWTError, ValidationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


EphemeralToken = Annotated[EphemeralTokenData, Depends(get_ephemeral_token)]
