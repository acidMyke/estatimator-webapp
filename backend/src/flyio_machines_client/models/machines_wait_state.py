from enum import StrEnum


class MachinesWaitState(StrEnum):
    ARCHIVED = "archived"
    DESTROYED = "destroyed"
    FAILED = "failed"
    SETTLED = "settled"
    STARTED = "started"
    STOPPED = "stopped"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
