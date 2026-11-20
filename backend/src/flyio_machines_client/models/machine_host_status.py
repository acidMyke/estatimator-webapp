from enum import StrEnum


class MachineHostStatus(StrEnum):
    OK = "ok"
    UNKNOWN = "unknown"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
