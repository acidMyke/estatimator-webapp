from datetime import datetime
from enum import Enum
from uuid import UUID

from api_services.core.models import IdMixin, SoftDeleteMixin, TimestampMixin
from api_services.features.users.models import User
from sqlmodel import Field, Relationship


class AuthMethodType(str, Enum):
    PASSWORD = "password"
    PASSKEY = "passkey"


class UserAuthenticationMethod(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    method_type: AuthMethodType = Field()

    is_enabled: bool = Field(default=True)
    is_primary: bool = Field(default=False)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="auth_methods")


class UserPassword(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    hashed_password: str = Field(nullable=False)

    requires_reset: bool = Field(default=False)
    failed_login_attempts: int = Field(default=0)
    locked_until: datetime | None = Field(default=None)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="passwords")


class UserPasskey(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    credential_id: str = Field(index=True, unique=True, nullable=False)
    public_key: str = Field(nullable=False)
    sign_count: int = Field(default=0)
    transports: str | None = Field(default=None)

    device_name: str | None = Field(default=None)
    last_used_at: datetime | None = Field(default=None)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="passkeys")


class UserSession(IdMixin, TimestampMixin, table=True):
    session_token: str = Field(index=True, unique=True, nullable=False)
    expires_at: datetime = Field(nullable=False)
    ip_address: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="sessions")
