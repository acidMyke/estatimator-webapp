from datetime import UTC, datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, Request, Response, status
from jwt import PyJWTError
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound

from api_services.core.database import DatabaseSession
from api_services.core.security import jwt_decode
from api_services.features.admin.models import Admin
from api_services.features.admin_auth.models import (
    AdminEphemeralTokenData,
    AdminEphemeralTokenPurpose,
    AdminSession,
)
from api_services.features.admin_auth.service import (
    ADMIN_EPHEMERAL_COOKIE,
    ADMIN_SESSION_COOKIE,
    get_admin_session_data_by_token,
    refresh_admin_session,
    revoke_admin_session,
)

ADMIN_SESSION_REFRESH_THRESHOLD = timedelta(minutes=5)


def get_optional_current_admin(
    request: Request, response: Response, db: DatabaseSession
) -> tuple[AdminSession | None, Admin | None]:
    session_token = request.cookies.get(ADMIN_SESSION_COOKIE)
    if not session_token:
        return None, None

    try:
        session = get_admin_session_data_by_token(db, session_token)
    except NoResultFound:
        revoke_admin_session(response=response)
        return None, None

    if datetime.now(UTC) + ADMIN_SESSION_REFRESH_THRESHOLD > session.expires_at:
        session = refresh_admin_session(db, session, response=response)

    admin = db.get(Admin, session.admin_id)
    if not admin or admin.deleted_at is not None:
        return None, None

    return session, admin


def get_current_admin(session_admin=Depends(get_optional_current_admin)) -> Admin:
    session, admin = session_admin

    if session is None or admin is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return admin


CurrentAdmin = Annotated[Admin, Depends(get_current_admin)]


def decode_admin_ephemeral_token(
    request: Request, expected_purpose: AdminEphemeralTokenPurpose
) -> AdminEphemeralTokenData:
    ephemeral_token = request.cookies.get(ADMIN_EPHEMERAL_COOKIE)

    if not ephemeral_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    try:
        raw_token_data = jwt_decode(ephemeral_token)
        token_data = AdminEphemeralTokenData.model_validate(raw_token_data)
    except PyJWTError, ValidationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if token_data.purpose != expected_purpose:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return token_data


def get_admin_registration_token(request: Request) -> AdminEphemeralTokenData:
    return decode_admin_ephemeral_token(request, "admin_registration")


AdminRegistrationToken = Annotated[
    AdminEphemeralTokenData, Depends(get_admin_registration_token)
]


def get_admin_complete_registration_token(request: Request) -> AdminEphemeralTokenData:
    return decode_admin_ephemeral_token(request, "admin_complete_registration")


AdminCompleteRegistrationToken = Annotated[
    AdminEphemeralTokenData, Depends(get_admin_complete_registration_token)
]


def get_admin_mfa_token(request: Request) -> AdminEphemeralTokenData:
    return decode_admin_ephemeral_token(request, "admin_mfa")


AdminMfaToken = Annotated[AdminEphemeralTokenData, Depends(get_admin_mfa_token)]
