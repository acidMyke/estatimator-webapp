from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_summary import CertificateSummary


T = TypeVar("T", bound="ListCertificatesResponse")


@_attrs_define
class ListCertificatesResponse:
    """
    Attributes:
        certificates (list[CertificateSummary] | Unset): The certificates on this page, ordered by when they were added.
        next_cursor (str | Unset): Pagination cursor for the next page. Absent when no more certificates remain.
        total_count (int | Unset): Number of certificates matching `filter` (and after `cursor`, if given), across all
            pages.
    """

    certificates: list[CertificateSummary] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()
                certificates.append(certificates_item)

        next_cursor = self.next_cursor

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.certificate_summary import CertificateSummary

        d = dict(src_dict)
        _certificates = d.pop("certificates", UNSET)
        certificates: list[CertificateSummary] | Unset = UNSET
        if _certificates is not UNSET:
            certificates = []
            for certificates_item_data in _certificates:
                certificates_item = CertificateSummary.from_dict(certificates_item_data)

                certificates.append(certificates_item)

        next_cursor = d.pop("next_cursor", UNSET)

        total_count = d.pop("total_count", UNSET)

        list_certificates_response = cls(
            certificates=certificates,
            next_cursor=next_cursor,
            total_count=total_count,
        )

        list_certificates_response.additional_properties = d
        return list_certificates_response

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
