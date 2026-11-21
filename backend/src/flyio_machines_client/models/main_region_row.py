from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.main_region_row_geo_region import MainRegionRowGeoRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="MainRegionRow")


@_attrs_define
class MainRegionRow:
    """
    Attributes:
        code (str | Unset): Region code, such as `iad`, used to select the region in other requests.
        deprecated (bool | Unset): Whether the region is deprecated. Avoid creating new resources in it.
        gateway_available (bool | Unset): Whether the region has a WireGuard gateway that private network peers can
            connect to.
        geo_region (MainRegionRowGeoRegion | Unset): Geographic area the region belongs to.
        latitude (float | Unset): Latitude of the region's location.
        longitude (float | Unset): Longitude of the region's location.
        mpg_available (bool | Unset): Whether Managed Postgres clusters can be created in the region.
        name (str | Unset): Human-readable name of the region, such as `Ashburn, Virginia (US)`.
        requires_paid_plan (bool | Unset): Whether only organizations on a paid plan can use the region.
    """

    code: str | Unset = UNSET
    deprecated: bool | Unset = UNSET
    gateway_available: bool | Unset = UNSET
    geo_region: MainRegionRowGeoRegion | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    mpg_available: bool | Unset = UNSET
    name: str | Unset = UNSET
    requires_paid_plan: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        deprecated = self.deprecated

        gateway_available = self.gateway_available

        geo_region: str | Unset = UNSET
        if not isinstance(self.geo_region, Unset):
            geo_region = self.geo_region.value

        latitude = self.latitude

        longitude = self.longitude

        mpg_available = self.mpg_available

        name = self.name

        requires_paid_plan = self.requires_paid_plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if gateway_available is not UNSET:
            field_dict["gateway_available"] = gateway_available
        if geo_region is not UNSET:
            field_dict["geo_region"] = geo_region
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if mpg_available is not UNSET:
            field_dict["mpg_available"] = mpg_available
        if name is not UNSET:
            field_dict["name"] = name
        if requires_paid_plan is not UNSET:
            field_dict["requires_paid_plan"] = requires_paid_plan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        deprecated = d.pop("deprecated", UNSET)

        gateway_available = d.pop("gateway_available", UNSET)

        _geo_region = d.pop("geo_region", UNSET)
        geo_region: MainRegionRowGeoRegion | Unset
        if isinstance(_geo_region, Unset):
            geo_region = UNSET
        else:
            geo_region = MainRegionRowGeoRegion(_geo_region)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        mpg_available = d.pop("mpg_available", UNSET)

        name = d.pop("name", UNSET)

        requires_paid_plan = d.pop("requires_paid_plan", UNSET)

        main_region_row = cls(
            code=code,
            deprecated=deprecated,
            gateway_available=gateway_available,
            geo_region=geo_region,
            latitude=latitude,
            longitude=longitude,
            mpg_available=mpg_available,
            name=name,
            requires_paid_plan=requires_paid_plan,
        )

        main_region_row.additional_properties = d
        return main_region_row

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
