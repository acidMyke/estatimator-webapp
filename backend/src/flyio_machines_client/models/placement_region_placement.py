from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlacementRegionPlacement")


@_attrs_define
class PlacementRegionPlacement:
    """
    Attributes:
        concurrency (int | Unset): Number of distinct hosts those Machines would be spread over. 0 when the request's
            count
            is 0.
        count (int | Unset): Number of Machines that would be placed in the region. When the request's count is 0, the
            organization's Machine limit for the region instead.
        region (str | Unset): Code of the region.
    """

    concurrency: int | Unset = UNSET
    count: int | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concurrency = self.concurrency

        count = self.count

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concurrency is not UNSET:
            field_dict["Concurrency"] = concurrency
        if count is not UNSET:
            field_dict["Count"] = count
        if region is not UNSET:
            field_dict["Region"] = region

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        concurrency = d.pop("Concurrency", UNSET)

        count = d.pop("Count", UNSET)

        region = d.pop("Region", UNSET)

        placement_region_placement = cls(
            concurrency=concurrency,
            count=count,
            region=region,
        )

        placement_region_placement.additional_properties = d
        return placement_region_placement

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
