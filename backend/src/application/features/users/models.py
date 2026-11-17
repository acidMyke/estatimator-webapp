from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from application.core.models import IdMixin, SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from application.features.auth.models import (
        UserPasskey,
        UserPassword,
        UserSession,
    )


class User(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    is_verified: bool = Field(default=False)
    emails: list[UserEmail] = Relationship(back_populates="user")
    passwords: list[UserPassword] = Relationship(back_populates="user")
    passkeys: list[UserPasskey] = Relationship(back_populates="user")
    sessions: list[UserSession] = Relationship(back_populates="user")


class UserEmail(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    email: str = Field(nullable=False)
    is_verified: bool = Field(default=False, nullable=False)
    is_active: bool = Field(default=False, nullable=False)

    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    user: User = Relationship(back_populates="emails")


class CreateUser(SQLModel):
    email: str = Field()
