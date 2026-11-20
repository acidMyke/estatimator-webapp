from enum import StrEnum


class AppStatus(StrEnum):
    DEPLOYED = "deployed"
    PENDING = "pending"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
