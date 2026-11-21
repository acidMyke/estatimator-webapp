from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.certificate_entry_source import CertificateEntrySource
from ..models.certificate_entry_status import CertificateEntryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issued_certificate import IssuedCertificate


T = TypeVar("T", bound="CertificateEntry")


@_attrs_define
class CertificateEntry:
    """
    Attributes:
        created_at (str | Unset): When the certificate was added; for Fly.io-issued certificates, the earliest one.
        expires_at (str | Unset): When the certificate expires; for Fly.io-issued certificates, the latest one.
        issued (list[IssuedCertificate] | Unset): The individual Fly.io-issued certificates, newest first. Empty for
            custom certificates.
        issuer (str | Unset): Issuer of a custom certificate. Omitted for Fly.io-issued certificates.
        source (CertificateEntrySource | Unset): `custom` for an uploaded certificate, `fly` for certificates issued by
            Fly.io.
        status (CertificateEntryStatus | Unset): `active` once ownership of the hostname is verified. Until then,
            `pending_ownership` for
            custom certificates and `pending_validation` for Fly.io-issued certificates.
    """

    created_at: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    issued: list[IssuedCertificate] | Unset = UNSET
    issuer: str | Unset = UNSET
    source: CertificateEntrySource | Unset = UNSET
    status: CertificateEntryStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        expires_at = self.expires_at

        issued: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issued, Unset):
            issued = []
            for issued_item_data in self.issued:
                issued_item = issued_item_data.to_dict()
                issued.append(issued_item)

        issuer = self.issuer

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if issued is not UNSET:
            field_dict["issued"] = issued
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issued_certificate import IssuedCertificate

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        _issued = d.pop("issued", UNSET)
        issued: list[IssuedCertificate] | Unset = UNSET
        if _issued is not UNSET:
            issued = []
            for issued_item_data in _issued:
                issued_item = IssuedCertificate.from_dict(issued_item_data)

                issued.append(issued_item)

        issuer = d.pop("issuer", UNSET)

        _source = d.pop("source", UNSET)
        source: CertificateEntrySource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CertificateEntrySource(_source)

        _status = d.pop("status", UNSET)
        status: CertificateEntryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CertificateEntryStatus(_status)

        certificate_entry = cls(
            created_at=created_at,
            expires_at=expires_at,
            issued=issued,
            issuer=issuer,
            source=source,
            status=status,
        )

        certificate_entry.additional_properties = d
        return certificate_entry

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
