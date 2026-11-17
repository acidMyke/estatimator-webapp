from urllib.parse import quote_plus

from pydantic import Field, SecretStr

from application.core.setttings.base import BaseAppSettings


class DatabaseSettings(BaseAppSettings):
    SQL_ECHO: bool = True
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


database_settings = DatabaseSettings()  # pyright: ignore[reportCallIssue]
