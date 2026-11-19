from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class CommonSettings(BaseAppSettings):
    IS_PROD: bool = False
    DEBUG: bool = True


common_settings = CommonSettings()  # pyright: ignore[reportCallIssue]
