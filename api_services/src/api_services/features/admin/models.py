from typing import TYPE_CHECKING

from api_services.core.models import IdMixin, SoftDeleteMixin, TimestampMixin
from api_services.features.admin_auth.models import AdminSession
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from api_services.features.admin_auth.models import (
        AdminPasskey,
        AdminPassword,
    )


class Admin(IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    email: str = Field(nullable=False)
    name: str = Field(nullable=False)

    passwords: list["AdminPasskey"] = Relationship(back_populates="admin")
    passkeys: list["AdminPassword"] = Relationship(back_populates="admin")
    sessions: list["AdminSession"] = Relationship(back_populates="admin")
