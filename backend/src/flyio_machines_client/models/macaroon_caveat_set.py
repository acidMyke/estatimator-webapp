from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.macaroon_caveat_set_caveats_item import MacaroonCaveatSetCaveatsItem


T = TypeVar("T", bound="MacaroonCaveatSet")


@_attrs_define
class MacaroonCaveatSet:
    """
    Attributes:
        caveats (list[MacaroonCaveatSetCaveatsItem] | Unset):
    """

    caveats: list[MacaroonCaveatSetCaveatsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caveats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.caveats, Unset):
            caveats = []
            for caveats_item_data in self.caveats:
                caveats_item = caveats_item_data.to_dict()
                caveats.append(caveats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caveats is not UNSET:
            field_dict["caveats"] = caveats

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.macaroon_caveat_set_caveats_item import (
            MacaroonCaveatSetCaveatsItem,
        )

        d = dict(src_dict)
        _caveats = d.pop("caveats", UNSET)
        caveats: list[MacaroonCaveatSetCaveatsItem] | Unset = UNSET
        if _caveats is not UNSET:
            caveats = []
            for caveats_item_data in _caveats:
                caveats_item = MacaroonCaveatSetCaveatsItem.from_dict(caveats_item_data)

                caveats.append(caveats_item)

        macaroon_caveat_set = cls(
            caveats=caveats,
        )

        macaroon_caveat_set.additional_properties = d
        return macaroon_caveat_set

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
