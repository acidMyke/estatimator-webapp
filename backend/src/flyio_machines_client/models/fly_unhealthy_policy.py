from enum import StrEnum


class FlyUnhealthyPolicy(StrEnum):
    UNHEALTHY_POLICY_STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
