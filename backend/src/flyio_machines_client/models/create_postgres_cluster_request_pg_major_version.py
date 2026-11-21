from enum import StrEnum


class CreatePostgresClusterRequestPgMajorVersion(StrEnum):
    VALUE_0 = "16"
    VALUE_1 = "17"

    def __str__(self) -> str:
        return str(self.value)
