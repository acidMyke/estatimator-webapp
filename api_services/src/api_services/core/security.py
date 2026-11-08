# If there is any changes that needed to be done here, please discuss with JJ
# Otherwise, the changes you made may be refactored/excluded
import base64
import hashlib
import hmac
import secrets
import struct
from datetime import UTC, datetime, timedelta
from typing import Any
from urllib.parse import quote

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from jwt import decode, encode

from api_services.core.settings import settings

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


def jwt_encode(payload: dict[str, Any], *, max_age: timedelta):
    now = datetime.now(UTC)
    payload["iss"] = settings.JWT_ISSUER
    payload["iat"] = int(now.timestamp())
    payload["exp"] = int((now + max_age).timestamp())

    return encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def jwt_decode(token: str):
    return decode(
        token,
        settings.JWT_SECRET_KEY,
        issuer=[settings.JWT_ISSUER],
        algorithms=[settings.ALGORITHM],
    )


def generate_otp(length=6):
    otp = "".join(secrets.choice("0123456789") for _ in range(length))
    return otp


def generate_totp_secret(length: int = 20) -> str:
    return base64.b32encode(secrets.token_bytes(length)).decode("ascii").rstrip("=")


def build_otpauth_uri(secret: str, account: str, issuer: str = "estatimator") -> str:
    label = quote(f"{issuer}:{account}")
    return (
        f"otpauth://totp/{label}?secret={secret}"
        f"&issuer={quote(issuer)}&algorithm=SHA1&digits=6&period=30"
    )


def generate_totp(
    secret: str,
    for_time: datetime | None = None,
    *,
    period: int = 30,
    digits: int = 6,
) -> str:
    key = base64.b32decode(secret + "=" * (-len(secret) % 8))
    counter = int((for_time or datetime.now(UTC)).timestamp()) // period
    digest = hmac.new(key, struct.pack(">Q", counter), hashlib.sha1).digest()
    offset = digest[-1] & 0x0F
    code = (struct.unpack(">I", digest[offset : offset + 4])[0] & 0x7FFFFFFF) % (
        10**digits
    )
    return str(code).zfill(digits)


def verify_totp(
    secret: str,
    code: str,
    *,
    valid_window: int = 1,
    period: int = 30,
) -> bool:
    if not code or not code.isdigit():
        return False

    now = datetime.now(UTC)
    for offset in range(-valid_window, valid_window + 1):
        candidate = generate_totp(
            secret,
            now + timedelta(seconds=period * offset),
            period=period,
        )
        if hmac.compare_digest(candidate, code):
            return True

    return False
