from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPPair")


@_attrs_define
class IPPair:
    """
    Attributes:
        v4 (str | Unset): The egress IPv4 address.
        v6 (str | Unset): The egress IPv6 address.
    """

    v4: str | Unset = UNSET
    v6: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        v4 = self.v4

        v6 = self.v6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v4 is not UNSET:
            field_dict["v4"] = v4
        if v6 is not UNSET:
            field_dict["v6"] = v6

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        v4 = d.pop("v4", UNSET)

        v6 = d.pop("v6", UNSET)

        ip_pair = cls(
            v4=v4,
            v6=v6,
        )

        ip_pair.additional_properties = d
        return ip_pair

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
