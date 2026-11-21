from enum import StrEnum


class IssuedCertificateType(StrEnum):
    ECDSA = "ecdsa"
    RSA = "rsa"

    def __str__(self) -> str:
        return str(self.value)
