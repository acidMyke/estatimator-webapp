from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainReclaimMemoryRequest")


@_attrs_define
class MainReclaimMemoryRequest:
    """
    Attributes:
        amount_mb (int | Unset): Memory to reclaim, in MiB. Must be positive and at most the Machine's memory limit
            minus
            128 MiB.
    """

    amount_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_mb = self.amount_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_mb is not UNSET:
            field_dict["amount_mb"] = amount_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_mb = d.pop("amount_mb", UNSET)

        main_reclaim_memory_request = cls(
            amount_mb=amount_mb,
        )

        main_reclaim_memory_request.additional_properties = d
        return main_reclaim_memory_request

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
