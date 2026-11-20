from enum import StrEnum


class PostgresClusterPlan(StrEnum):
    BASIC = "basic"
    LAUNCH = "launch"
    PERFORMANCE = "Performance"
    SCALE = "scale"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
