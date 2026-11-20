from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_region_row import MainRegionRow


T = TypeVar("T", bound="MainRegionResponse")


@_attrs_define
class MainRegionResponse:
    """
    Attributes:
        regions (list[MainRegionRow] | Unset): The regions available to the caller.
        nearest (str | Unset): Code of the region of the Fly.io edge that received the request, usually the one
            closest to the caller.
    """

    regions: list[MainRegionRow] | Unset = UNSET
    nearest: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        nearest = self.nearest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regions is not UNSET:
            field_dict["Regions"] = regions
        if nearest is not UNSET:
            field_dict["nearest"] = nearest

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.main_region_row import MainRegionRow

        d = dict(src_dict)
        _regions = d.pop("Regions", UNSET)
        regions: list[MainRegionRow] | Unset = UNSET
        if _regions is not UNSET:
            regions = []
            for regions_item_data in _regions:
                regions_item = MainRegionRow.from_dict(regions_item_data)

                regions.append(regions_item)

        nearest = d.pop("nearest", UNSET)

        main_region_response = cls(
            regions=regions,
            nearest=nearest,
        )

        main_region_response.additional_properties = d
        return main_region_response

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
