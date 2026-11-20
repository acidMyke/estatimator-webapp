from enum import StrEnum


class CertificateEntrySource(StrEnum):
    CUSTOM = "custom"
    FLY = "fly"

    def __str__(self) -> str:
        return str(self.value)
