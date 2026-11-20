from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineSpot")


@_attrs_define
class FlyMachineSpot:
    """
    Attributes:
        max_price_fraction (float | Unset): MaxPriceFraction is the maximum fraction of the full Machine price you will
            pay for this Machine. Range: (0, 1.0]
    """

    max_price_fraction: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_price_fraction = self.max_price_fraction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_price_fraction is not UNSET:
            field_dict["max_price_fraction"] = max_price_fraction

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_price_fraction = d.pop("max_price_fraction", UNSET)

        fly_machine_spot = cls(
            max_price_fraction=max_price_fraction,
        )

        fly_machine_spot.additional_properties = d
        return fly_machine_spot

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
