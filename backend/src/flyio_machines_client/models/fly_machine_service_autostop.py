from enum import StrEnum


class FlyMachineServiceAutostop(StrEnum):
    OFF = "off"
    STOP = "stop"
    SUSPEND = "suspend"

    def __str__(self) -> str:
        return str(self.value)
