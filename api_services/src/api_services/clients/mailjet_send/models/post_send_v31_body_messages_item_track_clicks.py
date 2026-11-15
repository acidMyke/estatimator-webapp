from enum import StrEnum


class PostSendV31BodyMessagesItemTrackClicks(StrEnum):
    ACCOUNT_DEFAULT = "account_default"
    ANON = "anon"
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
