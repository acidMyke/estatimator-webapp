from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class IdMixin(SQLModel):
    id: UUID = Field(default_factory=uuid4, nullable=False, primary_key=True)


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        nullable=False, default_factory=lambda: datetime.now(UTC)
    )
    updated_at: datetime = Field(
        nullable=False,
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": lambda: datetime.now(UTC)},
    )


class SoftDeleteMixin(SQLModel):
    deleted_at: datetime | None = Field(default=None, nullable=True, index=True)
