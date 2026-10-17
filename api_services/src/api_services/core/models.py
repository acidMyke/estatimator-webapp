from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy.ext.hybrid import hybrid_property
from sqlmodel import Field, SQLModel


class IdMixin(SQLModel):
    id: UUID = Field(default_factory=uuid4, nullable=False, primary_key=True)


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        nullable=False, default_factory=lambda: lambda: datetime.now(UTC)
    )
    updated_at: datetime = Field(
        nullable=False,
        default_factory=lambda: lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": lambda: datetime.now(UTC)},
    )


class SoftDeleteMixin(SQLModel):
    deleted_at: datetime | None = Field(default=None, nullable=True, index=True)

    @hybrid_property
    def is_deleted(self):
        return self.deleted_at is not None and self.deleted_at < datetime.now(UTC)

    def set_deleted(self):
        if self.is_deleted is False:
            self.deleted_at = datetime.now(UTC)
        return self
