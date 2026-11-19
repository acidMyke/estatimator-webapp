from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineServiceConcurrency")


@_attrs_define
class FlyMachineServiceConcurrency:
    """
    Attributes:
        hard_limit (int | Unset): Fly Proxy sends no more than this many connections or requests to a Machine at once. 0
            means
            no hard limit
        soft_limit (int | Unset): Above this many connections or requests, Fly Proxy prefers other Machines. Defaults to
            20,
            and is lowered to hard_limit if higher
        type_ (str | Unset): What to count: `connections` (default) or `requests`
    """

    hard_limit: int | Unset = UNSET
    soft_limit: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hard_limit = self.hard_limit

        soft_limit = self.soft_limit

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hard_limit is not UNSET:
            field_dict["hard_limit"] = hard_limit
        if soft_limit is not UNSET:
            field_dict["soft_limit"] = soft_limit
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hard_limit = d.pop("hard_limit", UNSET)

        soft_limit = d.pop("soft_limit", UNSET)

        type_ = d.pop("type", UNSET)

        fly_machine_service_concurrency = cls(
            hard_limit=hard_limit,
            soft_limit=soft_limit,
            type_=type_,
        )

        fly_machine_service_concurrency.additional_properties = d
        return fly_machine_service_concurrency

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
