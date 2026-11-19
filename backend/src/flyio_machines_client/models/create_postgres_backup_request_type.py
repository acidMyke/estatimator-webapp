from enum import StrEnum


class CreatePostgresBackupRequestType(StrEnum):
    DIFF = "diff"
    FULL = "full"
    INCR = "incr"

    def __str__(self) -> str:
        return str(self.value)
