from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyTLSOptions")


@_attrs_define
class FlyTLSOptions:
    """
    Attributes:
        alpn (list[str] | Unset): ALPN protocols to offer, e.g. `h2`, `http/1.1`. Defaults to `h2` and `http/1.1`
        default_self_signed (bool | Unset): Use a self-signed certificate when there is no certificate for the requested
            hostname
        versions (list[str] | Unset): TLS versions to accept: `TLSv1.2`, `TLSv1.3`. Defaults to both
    """

    alpn: list[str] | Unset = UNSET
    default_self_signed: bool | Unset = UNSET
    versions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alpn: list[str] | Unset = UNSET
        if not isinstance(self.alpn, Unset):
            alpn = self.alpn

        default_self_signed = self.default_self_signed

        versions: list[str] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alpn is not UNSET:
            field_dict["alpn"] = alpn
        if default_self_signed is not UNSET:
            field_dict["default_self_signed"] = default_self_signed
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alpn = cast(list[str], d.pop("alpn", UNSET))

        default_self_signed = d.pop("default_self_signed", UNSET)

        versions = cast(list[str], d.pop("versions", UNSET))

        fly_tls_options = cls(
            alpn=alpn,
            default_self_signed=default_self_signed,
            versions=versions,
        )

        fly_tls_options.additional_properties = d
        return fly_tls_options

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
