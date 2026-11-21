from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.placement_region_placement import PlacementRegionPlacement


T = TypeVar("T", bound="MainGetPlacementsResponse")


@_attrs_define
class MainGetPlacementsResponse:
    """
    Attributes:
        regions (list[PlacementRegionPlacement] | Unset): The regions Machines would be placed in. With `count` 0, every
            requested region with the
            organization's Machine limit in it.
    """

    regions: list[PlacementRegionPlacement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions is not UNSET:
            field_dict["Regions"] = regions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.placement_region_placement import PlacementRegionPlacement

        d = dict(src_dict)
        _regions = d.pop("Regions", UNSET)
        regions: list[PlacementRegionPlacement] | Unset = UNSET
        if _regions is not UNSET:
            regions = []
            for regions_item_data in _regions:
                regions_item = PlacementRegionPlacement.from_dict(regions_item_data)

                regions.append(regions_item)

        main_get_placements_response = cls(
            regions=regions,
        )

        main_get_placements_response.additional_properties = d
        return main_get_placements_response

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
