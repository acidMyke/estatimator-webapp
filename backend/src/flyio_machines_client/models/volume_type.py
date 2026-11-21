from enum import StrEnum


class VolumeType(StrEnum):
    CACHE = "cache"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
