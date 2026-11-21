from enum import StrEnum


class UpdatePostgresUserRoleRequestRole(StrEnum):
    READER = "reader"
    SCHEMA_ADMIN = "schema_admin"
    WRITER = "writer"

    def __str__(self) -> str:
        return str(self.value)
