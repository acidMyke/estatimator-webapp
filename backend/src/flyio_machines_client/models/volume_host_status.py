from enum import StrEnum


class VolumeHostStatus(StrEnum):
    OK = "ok"
    UNKNOWN = "unknown"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
