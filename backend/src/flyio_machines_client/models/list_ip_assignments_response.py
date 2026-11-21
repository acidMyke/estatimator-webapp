from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_assignment import IPAssignment


T = TypeVar("T", bound="ListIPAssignmentsResponse")


@_attrs_define
class ListIPAssignmentsResponse:
    """
    Attributes:
        ips (list[IPAssignment] | Unset): The app's IP addresses, including its shared IPv4 address and egress
            addresses.
    """

    ips: list[IPAssignment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ips, Unset):
            ips = []
            for ips_item_data in self.ips:
                ips_item = ips_item_data.to_dict()
                ips.append(ips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ips is not UNSET:
            field_dict["ips"] = ips

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_assignment import IPAssignment

        d = dict(src_dict)
        _ips = d.pop("ips", UNSET)
        ips: list[IPAssignment] | Unset = UNSET
        if _ips is not UNSET:
            ips = []
            for ips_item_data in _ips:
                ips_item = IPAssignment.from_dict(ips_item_data)

                ips.append(ips_item)

        list_ip_assignments_response = cls(
            ips=ips,
        )

        list_ip_assignments_response.additional_properties = d
        return list_ip_assignments_response

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
