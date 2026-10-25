from httpx2 import AsyncClient

from api_services.core.settings import settings


class MailjetClient:
    BASE_URL = "https://mailjet.com"

    def __init__(self):
        if settings.MAILJET_API_KEY is None or settings.MAILJET_API_SECRET is None:
            raise NotImplementedError(
                "MAILJET_API_KEY & MAILJET_API_SECRET are not set"
            )
        self.auth = (settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET)
        self.client = AsyncClient(base_url=self.BASE_URL, auth=self.auth)
