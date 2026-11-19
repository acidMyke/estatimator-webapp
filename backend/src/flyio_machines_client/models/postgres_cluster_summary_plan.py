from enum import StrEnum


class PostgresClusterSummaryPlan(StrEnum):
    BASIC = "basic"
    LAUNCH = "launch"
    PERFORMANCE = "Performance"
    SCALE = "scale"
    STARTER = "starter"

    def __str__(self) -> str:
        return str(self.value)
