from enum import StrEnum


class CheckStatusStatus(StrEnum):
    CRITICAL = "critical"
    PASSING = "passing"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
