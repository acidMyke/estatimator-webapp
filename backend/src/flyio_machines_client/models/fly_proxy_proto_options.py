from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyProxyProtoOptions")


@_attrs_define
class FlyProxyProtoOptions:
    """
    Attributes:
        fly_src (bool | Unset): With version v2, add the Fly-Src header and its signature to the PROXY protocol header
        version (str | Unset): PROXY protocol version: v1 (default) or v2
    """

    fly_src: bool | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fly_src = self.fly_src

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fly_src is not UNSET:
            field_dict["fly_src"] = fly_src
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fly_src = d.pop("fly_src", UNSET)

        version = d.pop("version", UNSET)

        fly_proxy_proto_options = cls(
            fly_src=fly_src,
            version=version,
        )

        fly_proxy_proto_options.additional_properties = d
        return fly_proxy_proto_options

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
