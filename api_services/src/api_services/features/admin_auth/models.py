from uuid import UUID

from sqlmodel import Field, Relationship

from api_services.features.admin.models import Admin
from api_services.features.auth.models import (
    AuthPasskeyBase,
    AuthPasswordBase,
    AuthSessionBase,
)


class AdminPassword(AuthPasswordBase, table=True):
    admin_id: UUID = Field(nullable=False, foreign_key="admin.id")
    admin: Admin = Relationship(back_populates="passwords")


class AdminPasskey(AuthPasskeyBase, table=True):
    admin_id: UUID = Field(nullable=False, foreign_key="admin.id")
    admin: Admin = Relationship(back_populates="passkeys")


class AdminSession(AuthSessionBase, table=True):
    admin_id: UUID = Field(nullable=False, foreign_key="admin.id")
    admin: Admin = Relationship(back_populates="sessions")
