from enum import StrEnum


class PostgresClusterStatus(StrEnum):
    CREATING = "creating"
    DELETED = "deleted"
    DELETING = "deleting"
    FAILED = "failed"
    INITIALIZING = "initializing"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
