from enum import StrEnum


class PostgresClusterCpuKind(StrEnum):
    PERFORMANCE = "performance"
    SHARED = "shared"

    def __str__(self) -> str:
        return str(self.value)
