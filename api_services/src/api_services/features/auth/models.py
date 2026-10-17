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

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="passwords")


class UserPasskey(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    credential_id: str = Field(index=True, unique=True)
    public_key: str = Field(nullable=False)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="auth_methods")
