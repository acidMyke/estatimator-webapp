from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCustomCertificateRequest")


@_attrs_define
class CreateCustomCertificateRequest:
    """
    Attributes:
        fullchain (str | Unset): PEM-encoded certificate, followed by any intermediate certificates. Required.
        hostname (str | Unset): Hostname the certificate is for. Required. Hostnames under `fly.dev` are not allowed.
        private_key (str | Unset): PEM-encoded private key of the certificate. Required.
    """

    fullchain: str | Unset = UNSET
    hostname: str | Unset = UNSET
    private_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fullchain = self.fullchain

        hostname = self.hostname

        private_key = self.private_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fullchain is not UNSET:
            field_dict["fullchain"] = fullchain
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fullchain = d.pop("fullchain", UNSET)

        hostname = d.pop("hostname", UNSET)

        private_key = d.pop("private_key", UNSET)

        create_custom_certificate_request = cls(
            fullchain=fullchain,
            hostname=hostname,
            private_key=private_key,
        )

        create_custom_certificate_request.additional_properties = d
        return create_custom_certificate_request

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
