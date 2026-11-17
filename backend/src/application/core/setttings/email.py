from base64 import b64encode
from typing import cast

from application.core.setttings.base import BaseAppSettings


class EmailSettings(BaseAppSettings):
    MAILPIT_HOST: str = "localhost"
    MAILPIT_PORT: int = 8025
    MAILJET_API_KEY: str | None = None
    MAILJET_API_SECRET: str | None = None
    FROM_EMAIL: str = "no-reply-for-fyp@acidmyke.link"
    FROM_NAME: str = "Final Year Project System"

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


email_settings = EmailSettings()  # pyright: ignore[reportCallIssue]
