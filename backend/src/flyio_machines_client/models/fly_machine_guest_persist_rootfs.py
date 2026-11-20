from enum import StrEnum


class FlyMachineGuestPersistRootfs(StrEnum):
    ALWAYS = "always"
    NEVER = "never"
    RESTART = "restart"

    def __str__(self) -> str:
        return str(self.value)
