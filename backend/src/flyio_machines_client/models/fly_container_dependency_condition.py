from enum import StrEnum


class FlyContainerDependencyCondition(StrEnum):
    EXITED_SUCCESSFULLY = "exited_successfully"
    HEALTHY = "healthy"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
