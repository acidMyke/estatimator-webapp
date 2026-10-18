# High chance you won't need to modify this file.
# But if your feature requires API keys / tokens, sensitive configuration, feel free to add it here
# If there is new environment variables added, it also need to be in the deployed environment, get JJ to do this :D

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATABASE_URL: str
    DEBUG: bool = False
    SQL_ECHO: bool = True
    JWT_SECRET_KEY: str = Field(min_length=64, pattern=r"^[0-9a-fA-F]+$")
    ALGORITHM: str = "HS256"
    USER_SESSION_TOKEN_EXPIRE_DAYS: int = 7
    ADMIN_SESSION_TOKEN_EXPIRE_MINUTES: int = 20

    @field_validator("DATABASE_URL", mode="after")
    @classmethod
    def assemble_async_db_url(cls, v: str) -> str:
        if v is None or v == "":
            raise ValueError("DATABASE_URL is None or empty")

        if v.startswith("postgresql://"):
            v = v.replace("postgresql://", "postgresql+psycopg://", 1)

        if "+psycopg" not in v:
            raise ValueError(
                "DATABASE_URL must start with 'postgresql://' or 'postgresql+psycopg://'"
            )

        return v


settings = AppSettings()  # pyright: ignore[reportCallIssue]
