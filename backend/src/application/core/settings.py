# High chance you won't need to modify this file.
# But if your feature requires API keys / tokens, sensitive configuration, feel free to add it here
# If there is new environment variables added, it also need to be in the deployed environment, get JJ to do this :D

from base64 import b64encode
from typing import cast
from urllib.parse import quote_plus

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    DEBUG: bool = False
    SQL_ECHO: bool = True
    JWT_ISSUER: str = "estatimator"
    JWT_SECRET_KEY: str = Field(min_length=64, pattern=r"^[0-9a-fA-F]+$")
    ALGORITHM: str = "HS256"
    USER_SESSION_TOKEN_EXPIRE_DAYS: int = 7
    ADMIN_SESSION_TOKEN_EXPIRE_MINUTES: int = 20
    ADMIN_ALLOWED_EMAIL_DOMAINS: list[str] = Field(
        default=["acidmyke.link", "uowmail.edu.au", "sim.edu.sg"]
    )

    # EMAIL CONFIGS
    MAILPIT_HOST: str = "localhost"
    MAILPIT_PORT: int = 8025
    MAILJET_API_KEY: str | None = None
    MAILJET_API_SECRET: str | None = None
    FROM_EMAIL: str = "no-reply-for-fyp@acidmyke.link"
    FROM_NAME: str = "Final Year Project System"

    # DB CONFIGS
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: SecretStr = Field()
    POSTGRES_DB: str = "localdb"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    @property
    def _database_url(self) -> str:
        username = quote_plus(self.POSTGRES_USER)
        password = quote_plus(self.POSTGRES_PASSWORD.get_secret_value())

        return (
            f"{username}:{password}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    @property
    def sync_connection_string(self) -> str:
        return f"postgresql+psycopg://{self._database_url}"

    @property
    def async_connection_string(self) -> str:
        return f"postgresql+asyncpg://{self._database_url}"

    @field_validator("ADMIN_ALLOWED_EMAIL_DOMAINS", mode="after")
    @classmethod
    def normalize_admin_allowed_email_domains(cls, v: list[str]) -> list[str]:
        return [domain.strip().lower() for domain in v if domain.strip()]

    @property
    def is_mailjet_configured(self):
        return self.MAILJET_API_KEY is not None and self.MAILJET_API_SECRET is not None

    @property
    def mailjet_auth_token(self):
        if not self.is_mailjet_configured:
            raise ValueError("MAILJET_API_KEY or MAILJET_API_SECRET is not configured")
        username = cast(str, self.MAILJET_API_KEY)
        password = cast(str, self.MAILJET_API_SECRET)
        credentials = f"{username}:{password}".encode()
        return b64encode(credentials).decode("utf-8")


settings = AppSettings()  # pyright: ignore[reportCallIssue]
