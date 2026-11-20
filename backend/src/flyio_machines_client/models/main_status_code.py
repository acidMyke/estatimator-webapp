from enum import StrEnum


class MainStatusCode(StrEnum):
    CAPACITY_ERR = "insufficient_capacity"
    EXEC_OUTPUT_TOO_LARGE_ERR = "exec_output_too_large"
    EXEC_REQUEST_TOO_LARGE_ERR = "exec_request_too_large"
    NAME_TAKEN_ERR = "name_taken"
    UNKNOWN = "unknown"
    VOLUME_PLACEMENT_CAPACITY_ERR = "volume_placement_capacity"

    def __str__(self) -> str:
        return str(self.value)
