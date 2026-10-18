# If there is any changes that needed to be done here, please discuss with JJ
# Otherwise, the changes you made may be refactored/excluded
import secrets
from typing import Any

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from jwt import decode, encode

from .settings import settings

ph = PasswordHasher()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False


def get_password_hash(password: str) -> str:
    return ph.hash(password)


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


def generate_otp(length=6):
    otp = "".join(secrets.choice("0123456789") for _ in range(length))
    return otp
