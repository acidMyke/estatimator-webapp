# If there is any changes that needed to be done here, please discuss with JJ
# Otherwise, the changes you made may be refactored/excluded
import secrets
from typing import Any

from jwt import decode, encode
from passlib.context import CryptContext

from .settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def generate_session_token() -> str:
    return secrets.token_urlsafe(32)


def jwt_encode(payload: dict[str, Any]):
    return encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def jwt_decode(token: str):
    return decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )
