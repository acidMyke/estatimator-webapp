from enum import StrEnum


class OrgVolumeHostStatus(StrEnum):
    OK = "ok"
    UNKNOWN = "unknown"
    UNREACHABLE = "unreachable"

    def __str__(self) -> str:
        return str(self.value)
