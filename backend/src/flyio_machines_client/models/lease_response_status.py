from enum import StrEnum


class LeaseResponseStatus(StrEnum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
