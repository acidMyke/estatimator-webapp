# High chance you won't need to modify this file.
# But if your feature requires API keys / tokens, sensitive configuration, feel free to add it here
# If there is new environment variables added, it also need to be in the deployed environment, get JJ to do this :D

from urllib.parse import quote_plus

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    DATABASE_URL: str
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


settings = AppSettings()  # pyright: ignore[reportCallIssue]
