from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListenSocket")


@_attrs_define
class ListenSocket:
    """
    Attributes:
        address (str | Unset): Local address and port the socket is bound to, such as `0.0.0.0:8080` or `[::]:8080`.
        proto (str | Unset): Protocol of the socket. Always `tcp`.
    """

    address: str | Unset = UNSET
    proto: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        proto = self.proto

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if proto is not UNSET:
            field_dict["proto"] = proto

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        proto = d.pop("proto", UNSET)

        listen_socket = cls(
            address=address,
            proto=proto,
        )

        listen_socket.additional_properties = d
        return listen_socket

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
