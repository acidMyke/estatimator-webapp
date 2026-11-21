from enum import StrEnum


class LeaseErrorResponseStatus(StrEnum):
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
