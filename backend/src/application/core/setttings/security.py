from pydantic import Field, field_validator

from application.core.setttings.base import BaseAppSettings


class SecuritySettings(BaseAppSettings):
    JWT_ISSUER: str = "hdbeeprice"
    JWT_SECRET_KEY: str = Field(min_length=64, pattern=r"^[0-9a-fA-F]+$")
    JWT_ALGORITHM: str = "HS256"

    USER_SESSION_TOKEN_EXPIRE_DAYS: int = 7
    ADMIN_SESSION_TOKEN_EXPIRE_MINUTES: int = 20
    ADMIN_ALLOWED_EMAIL_DOMAINS: list[str] = Field(
        default_factory=lambda: [
            "acidmyke.link",
            "uowmail.edu.au",
            "sim.edu.sg",
        ]
    )

    @field_validator("ADMIN_ALLOWED_EMAIL_DOMAINS", mode="after")
    @classmethod
    def normalize_admin_allowed_email_domains(cls, v: list[str]) -> list[str]:
        return [domain.strip().lower() for domain in v if domain.strip()]


security_settings = SecuritySettings()  # pyright: ignore[reportCallIssue]
