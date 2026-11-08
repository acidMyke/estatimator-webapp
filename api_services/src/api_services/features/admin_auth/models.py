from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import model_validator
from sqlmodel import Field, Relationship, SQLModel

from api_services.core.models import IdMixin, TimestampMixin
from api_services.features.admin.models import Admin
from api_services.features.auth.models import (
    AuthOtpBase,
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


class AdminOtp(AuthOtpBase, table=True):
    email: str = Field(nullable=False, index=True)


class AdminTotpSecret(IdMixin, TimestampMixin, table=True):
    admin_id: UUID = Field(nullable=False, unique=True, foreign_key="admin.id")
    secret: str = Field(nullable=False)
    is_enabled: bool = Field(default=False, nullable=False)
    verified_at: datetime | None = Field(default=None)
    last_used_at: datetime | None = Field(default=None)

    admin: Admin = Relationship()


AdminEphemeralTokenPurpose = Literal[
    "admin_registration",
    "admin_complete_registration",
    "admin_mfa",
]


class AdminEphemeralTokenData(SQLModel):
    purpose: AdminEphemeralTokenPurpose = Field()
    email: str = Field()
    name: str = Field()
    admin_id: UUID | None = Field(default=None)

    @model_validator(mode="after")
    def validate_purpose_requirements(self) -> AdminEphemeralTokenData:
        if self.purpose == "admin_mfa" and self.admin_id is None:
            raise ValueError("'admin_mfa' tokens require an admin_id")

        return self


class AdminRegisterPayload(SQLModel):
    email: str = Field()
    name: str = Field()


class AdminRegisterVerifyOtpPayload(SQLModel):
    otp: str = Field()


class AdminCompleteRegistrationPayload(SQLModel):
    password: str = Field()


class AdminLoginPayload(SQLModel):
    email: str = Field()
    password: str = Field()


class AdminLoginResponse(SQLModel):
    mfa_required: bool


class AdminTotpCodePayload(SQLModel):
    code: str = Field()


class AdminTotpSetupResponse(SQLModel):
    secret: str
    otpauth_uri: str


class AdminCheckAuthResponse(SQLModel):
    is_authenticated: bool
    email: str | None = None
