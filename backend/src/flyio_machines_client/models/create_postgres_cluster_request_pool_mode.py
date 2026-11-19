from enum import StrEnum


class CreatePostgresClusterRequestPoolMode(StrEnum):
    SESSION = "session"
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
