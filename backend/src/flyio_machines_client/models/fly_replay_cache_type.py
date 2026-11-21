from enum import StrEnum


class FlyReplayCacheType(StrEnum):
    COOKIE = "cookie"
    HEADER = "header"

    def __str__(self) -> str:
        return str(self.value)
