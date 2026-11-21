from enum import StrEnum


class MachinesListProcessesSortBy(StrEnum):
    CPU = "cpu"
    PID = "pid"
    RTIME = "rtime"
    STIME = "stime"

    def __str__(self) -> str:
        return str(self.value)
