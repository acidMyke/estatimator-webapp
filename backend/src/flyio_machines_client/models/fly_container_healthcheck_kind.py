from enum import StrEnum


class FlyContainerHealthcheckKind(StrEnum):
    LIVENESS = "liveness"
    READINESS = "readiness"

    def __str__(self) -> str:
        return str(self.value)
