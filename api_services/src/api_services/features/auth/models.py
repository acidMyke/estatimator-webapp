from datetime import datetime
from enum import Enum
from typing import Literal
from uuid import UUID

from api_services.core.models import IdMixin, SoftDeleteMixin, TimestampMixin
from api_services.features.users.models import CreateUser, User
from sqlmodel import Field, Relationship, SQLModel


class AuthPasswordBase(IdMixin, TimestampMixin, SoftDeleteMixin):
    hashed_password: str = Field(nullable=False)
    last_used_at: datetime | None = Field(default=None)


class AuthPasskeyBase(IdMixin, TimestampMixin, SoftDeleteMixin):
    credential_id: str = Field(index=True, unique=True, nullable=False)
    public_key: str = Field(nullable=False)
    sign_count: int = Field(default=0)
    transports: str | None = Field(default=None)
    device_name: str | None = Field(default=None)
    last_used_at: datetime | None = Field(default=None)


class AuthMethodType(str, Enum):
    PASSWORD = "PASSWORD"
    PASSKEY = "PASSKEY"


class AuthSessionBase(IdMixin, TimestampMixin):
    session_token: str = Field(index=True, unique=True, nullable=False)
    expires_at: datetime = Field(nullable=False)
    login_method_type: AuthMethodType = Field()
    parent_session_id: UUID | None = Field(default=None, nullable=True)


class AuthOtpUsageType(str, Enum):
    REGISTRATION = "REGISTRATION"
    EMAIL_CHANGE = "EMAIL_CHANGE"
    PASSWORD_RESET = "PASSWORD_RESET"
    TWO_FACTOR = "TWO_FACTOR"


class AuthOtpBase(AuthPasswordBase):
    expires_at: datetime = Field(nullable=False)
    used_at: datetime | None = Field(default=None)
    usage_type: AuthOtpUsageType = Field(nullable=False)


class UserPassword(AuthPasswordBase, table=True):
    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="passwords")


class UserPasskey(AuthPasskeyBase, table=True):
    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="passkeys")


class UserSession(AuthSessionBase, table=True):
    ip_address: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="sessions")


class UserOtp(AuthOtpBase, table=True):
    user_id: UUID = Field(foreign_key="user.id")
    user: User = Relationship()


class EphemeralTokenData(SQLModel):
    user_id: UUID = Field()
    purpose: Literal["registration", "complete_registration"] = Field()


class RegisterPayload(CreateUser):
    pass


class RegisterationVerifyOtpPayload(SQLModel):
    otp: str = Field()


class CompleteRegistrationPayload(SQLModel):
    password: str = Field()


class LoginPayload(SQLModel):
    email: str = Field()
    password: str = Field()


class CheckAuthResponse(SQLModel):
    is_authenticated: bool
    email: str | None = None
