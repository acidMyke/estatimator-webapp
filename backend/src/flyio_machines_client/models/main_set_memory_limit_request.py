from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainSetMemoryLimitRequest")


@_attrs_define
class MainSetMemoryLimitRequest:
    """
    Attributes:
        limit_mb (int | Unset): New limit in MiB. Must be at least 128 and at most the Machine's configured memory
            (`guest.max_memory_mb` if set, else `guest.memory_mb`).
    """

    limit_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_mb = self.limit_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_mb is not UNSET:
            field_dict["limit_mb"] = limit_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        limit_mb = d.pop("limit_mb", UNSET)

        main_set_memory_limit_request = cls(
            limit_mb=limit_mb,
        )

        main_set_memory_limit_request.additional_properties = d
        return main_set_memory_limit_request

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
