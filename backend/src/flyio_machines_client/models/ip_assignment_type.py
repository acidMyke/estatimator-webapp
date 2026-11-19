from enum import StrEnum


class IPAssignmentType(StrEnum):
    IP_ASSIGNMENT_TYPE_EGRESS_PAIR = "egress_pair"
    IP_ASSIGNMENT_TYPE_EGRESS_V_4 = "egress_v4"
    IP_ASSIGNMENT_TYPE_EGRESS_V_6 = "egress_v6"
    IP_ASSIGNMENT_TYPE_PRIVATE_V_6 = "private_v6"
    IP_ASSIGNMENT_TYPE_SHARED_V_4 = "shared_v4"
    IP_ASSIGNMENT_TYPE_V_4 = "v4"
    IP_ASSIGNMENT_TYPE_V_6 = "v6"

    def __str__(self) -> str:
        return str(self.value)
