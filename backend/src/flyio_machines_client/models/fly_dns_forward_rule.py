from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyDnsForwardRule")


@_attrs_define
class FlyDnsForwardRule:
    """
    Attributes:
        addr (str | Unset): Address and port of the DNS server to forward queries to over TCP, e.g. `10.0.0.1:53`
        basename (str | Unset): Domain to forward queries for, including subdomains. Must end in a dot, e.g.
            `example.com.`
    """

    addr: str | Unset = UNSET
    basename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        basename = self.basename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if basename is not UNSET:
            field_dict["basename"] = basename

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        addr = d.pop("addr", UNSET)

        basename = d.pop("basename", UNSET)

        fly_dns_forward_rule = cls(
            addr=addr,
            basename=basename,
        )

        fly_dns_forward_rule.additional_properties = d
        return fly_dns_forward_rule

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
