from uuid import UUID

from sqlmodel import Field, Relationship

from api_services.core.models import IdMixin, SoftDeleteMixin, TimestampMixin
from api_services.features.auth.models import (
    UserAuthenticationMethod,
    UserPasskey,
    UserPassword,
)


class User(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    emails: list["UserEmail"] = Relationship(back_populates="user")
    auth_methods: list[UserAuthenticationMethod] = Relationship(back_populates="user")
    passwords: list[UserPassword] = Relationship(back_populates="user")
    passkeys: list[UserPasskey] = Relationship(back_populates="user")


class UserEmail(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    email: str = Field(nullable=False)
    is_verified: bool = Field(default=False, nullable=False)
    is_active: bool = Field(default=False, nullable=False)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="emails")
