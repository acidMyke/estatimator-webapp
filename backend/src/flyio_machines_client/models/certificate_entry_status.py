from enum import StrEnum


class CertificateEntryStatus(StrEnum):
    ACTIVE = "active"
    PENDING_OWNERSHIP = "pending_ownership"
    PENDING_VALIDATION = "pending_validation"

    def __str__(self) -> str:
        return str(self.value)
