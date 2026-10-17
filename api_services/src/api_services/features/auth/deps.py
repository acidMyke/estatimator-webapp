from datetime import UTC, datetime
from uuid import UUID

import jwt
from fastapi import HTTPException, Request, Response, status
from sqlmodel import select

from ...core.database import DatabaseSession
from ...core.security import create_access_token
from ...core.settings import settings
from .models import User, UserSession


def get_current_user(request: Request, response: Response, db: DatabaseSession) -> User:
    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")

    if not access_token and not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated"
        )

    user_id = None

    if access_token:
        try:
            payload = jwt.decode(
                access_token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.ALGORITHM],
            )
            user_id = UUID(payload.get("sub"))
        except jwt.ExpiredSignatureError:
            pass  # Move to Step 2
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token"
            )

    if not user_id:
        if not refresh_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired"
            )

        session_data = db.exec(
            select(UserSession.user_id, UserSession.expires_at).where(
                UserSession.session_token == refresh_token
                and UserSession.expires_at > datetime.now(UTC)
            )
        ).first()

        if not session_data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired"
            )

        user_id, expires_at = session_data
        new_access_token = create_access_token(user_id, expires_at)

        response.set_cookie(
            key="access_token",
            value=new_access_token,
            httponly=True,
            secure=True,
            samesite="lax",
            max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )

    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )

    return user
