from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_guest import FlyMachineGuest
    from ..models.placement_weights import PlacementWeights


T = TypeVar("T", bound="MainGetPlacementsRequest")


@_attrs_define
class MainGetPlacementsRequest:
    """
    Attributes:
        org_slug (str): Slug of the organization to place Machines for, or `personal`. Required. Example: personal.
        compute (FlyMachineGuest | Unset):
        count (int | Unset): Number of machines to simulate placement.
            Defaults to 0, which returns the org-specific limit for each region.
        region (str | Unset): Region expression for placement as a comma-delimited set of regions or aliases.
            Defaults to the API endpoint's local region. When `count` is greater than 0, `any` is
            added as a fallback. Example: lhr,eu.
        volume_name (str | Unset): Currently unused.
        volume_size_bytes (int | Unset): Size of a volume each Machine will need, in bytes. Only hosts with room for it
            are
            considered.
        weights (PlacementWeights | Unset):
    """

    org_slug: str
    compute: FlyMachineGuest | Unset = UNSET
    count: int | Unset = UNSET
    region: str | Unset = UNSET
    volume_name: str | Unset = UNSET
    volume_size_bytes: int | Unset = UNSET
    weights: PlacementWeights | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_slug = self.org_slug

        compute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute, Unset):
            compute = self.compute.to_dict()

        count = self.count

        region = self.region

        volume_name = self.volume_name

        volume_size_bytes = self.volume_size_bytes

        weights: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weights, Unset):
            weights = self.weights.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_slug": org_slug,
            }
        )
        if compute is not UNSET:
            field_dict["compute"] = compute
        if count is not UNSET:
            field_dict["count"] = count
        if region is not UNSET:
            field_dict["region"] = region
        if volume_name is not UNSET:
            field_dict["volume_name"] = volume_name
        if volume_size_bytes is not UNSET:
            field_dict["volume_size_bytes"] = volume_size_bytes
        if weights is not UNSET:
            field_dict["weights"] = weights

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_guest import FlyMachineGuest
        from ..models.placement_weights import PlacementWeights

        d = dict(src_dict)
        org_slug = d.pop("org_slug")

        _compute = d.pop("compute", UNSET)
        compute: FlyMachineGuest | Unset
        if isinstance(_compute, Unset):
            compute = UNSET
        else:
            compute = FlyMachineGuest.from_dict(_compute)

        count = d.pop("count", UNSET)

        region = d.pop("region", UNSET)

        volume_name = d.pop("volume_name", UNSET)

        volume_size_bytes = d.pop("volume_size_bytes", UNSET)

        _weights = d.pop("weights", UNSET)
        weights: PlacementWeights | Unset
        if isinstance(_weights, Unset):
            weights = UNSET
        else:
            weights = PlacementWeights.from_dict(_weights)

        main_get_placements_request = cls(
            org_slug=org_slug,
            compute=compute,
            count=count,
            region=region,
            volume_name=volume_name,
            volume_size_bytes=volume_size_bytes,
            weights=weights,
        )

        main_get_placements_request.additional_properties = d
        return main_get_placements_request

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
