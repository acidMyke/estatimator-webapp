from enum import StrEnum


class FlyMachineRootfsPersist(StrEnum):
    ALWAYS = "always"
    NEVER = "never"
    RESTART = "restart"

    def __str__(self) -> str:
        return str(self.value)
