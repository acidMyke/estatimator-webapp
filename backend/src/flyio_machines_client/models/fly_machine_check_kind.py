from enum import StrEnum


class FlyMachineCheckKind(StrEnum):
    INFORMATIONAL = "informational"
    READINESS = "readiness"

    def __str__(self) -> str:
        return str(self.value)
