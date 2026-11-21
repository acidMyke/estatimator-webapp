from enum import StrEnum


class OrgVolumeType(StrEnum):
    CACHE = "cache"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
