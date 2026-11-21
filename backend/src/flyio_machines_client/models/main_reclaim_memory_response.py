from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainReclaimMemoryResponse")


@_attrs_define
class MainReclaimMemoryResponse:
    """
    Attributes:
        actual_mb (int | Unset): Memory, in MiB, that the guest actually gave up. Can be less than requested.
    """

    actual_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_mb = self.actual_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_mb is not UNSET:
            field_dict["actual_mb"] = actual_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        actual_mb = d.pop("actual_mb", UNSET)

        main_reclaim_memory_response = cls(
            actual_mb=actual_mb,
        )

        main_reclaim_memory_response.additional_properties = d
        return main_reclaim_memory_response

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
