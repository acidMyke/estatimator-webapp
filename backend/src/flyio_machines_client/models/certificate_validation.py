from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateValidation")


@_attrs_define
class CertificateValidation:
    """
    Attributes:
        alpn_configured (bool | Unset): Whether the hostname points at the app, allowing TLS-ALPN-01 validation.
        dns_configured (bool | Unset): Whether the `_acme-challenge` CNAME record is set up, allowing DNS-01 validation.
        http_configured (bool | Unset): Whether the hostname points at the app, allowing HTTP-01 validation.
        ownership_txt_configured (bool | Unset): Whether the `_fly-ownership` TXT record is set up.
    """

    alpn_configured: bool | Unset = UNSET
    dns_configured: bool | Unset = UNSET
    http_configured: bool | Unset = UNSET
    ownership_txt_configured: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alpn_configured = self.alpn_configured

        dns_configured = self.dns_configured

        http_configured = self.http_configured

        ownership_txt_configured = self.ownership_txt_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alpn_configured is not UNSET:
            field_dict["alpn_configured"] = alpn_configured
        if dns_configured is not UNSET:
            field_dict["dns_configured"] = dns_configured
        if http_configured is not UNSET:
            field_dict["http_configured"] = http_configured
        if ownership_txt_configured is not UNSET:
            field_dict["ownership_txt_configured"] = ownership_txt_configured

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alpn_configured = d.pop("alpn_configured", UNSET)

        dns_configured = d.pop("dns_configured", UNSET)

        http_configured = d.pop("http_configured", UNSET)

        ownership_txt_configured = d.pop("ownership_txt_configured", UNSET)

        certificate_validation = cls(
            alpn_configured=alpn_configured,
            dns_configured=dns_configured,
            http_configured=http_configured,
            ownership_txt_configured=ownership_txt_configured,
        )

        certificate_validation.additional_properties = d
        return certificate_validation

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
