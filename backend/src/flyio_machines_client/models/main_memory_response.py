from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainMemoryResponse")


@_attrs_define
class MainMemoryResponse:
    """
    Attributes:
        available_mb (int | Unset): Highest limit, in MiB, that the Machine could currently be raised to: its configured
            memory (`guest.max_memory_mb` if set, else `guest.memory_mb`), capped by the host's free
            memory.
        limit_mb (int | Unset): Memory, in MiB, the guest can currently use.
    """

    available_mb: int | Unset = UNSET
    limit_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_mb = self.available_mb

        limit_mb = self.limit_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_mb is not UNSET:
            field_dict["available_mb"] = available_mb
        if limit_mb is not UNSET:
            field_dict["limit_mb"] = limit_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available_mb = d.pop("available_mb", UNSET)

        limit_mb = d.pop("limit_mb", UNSET)

        main_memory_response = cls(
            available_mb=available_mb,
            limit_mb=limit_mb,
        )

        main_memory_response.additional_properties = d
        return main_memory_response

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
