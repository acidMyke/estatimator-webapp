from enum import StrEnum


class LeaseOkResponseStatus(StrEnum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
