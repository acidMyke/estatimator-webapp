# High chance you won't need to modify this file.
# But if your feature requires API keys / tokens, sensitive configuration, feel free to add it here
# If there is new environment variables added, it also need to be in the deployed environment, get JJ to do this :D

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfiguration(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATABASE_URL: str = "postgresql://default:default@localhost:5432/mydatabase"
    DEBUG: bool = False
    SQL_ECHO: bool = True

    @field_validator("DATABASE_URL", mode="after")
    @classmethod
    def assemble_async_db_url(cls, v: str) -> str:
        if v is None or v == "":
            raise ValueError("DATABASE_URL is None or empty")

        if "default" in v:
            raise ValueError(
                "Please set the DATABASE_URL via environment variable or .env"
            )

        if v.startswith("postgresql://"):
            v = v.replace("postgresql://", "postgresql+asyncpg://", 1)

        if "?sslmode=" in v:
            raise ValueError

        if "+asyncpg" not in v:
            raise ValueError(
                "DATABASE_URL must start with 'postgresql://' or 'postgresql+asyncpg://'"
            )

        return v

    @property
    def SYNC_DATABASE_URL(self) -> str:
        return self.DATABASE_URL.replace("+asyncpg", "+psycopg")


app_configuration = AppConfiguration()
