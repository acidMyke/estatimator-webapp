from enum import StrEnum


class FlyContainerHealthcheckScheme(StrEnum):
    HTTP = "http"
    HTTPS = "https"

    def __str__(self) -> str:
        return str(self.value)
