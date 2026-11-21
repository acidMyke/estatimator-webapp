from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPAssignmentNetwork")


@_attrs_define
class IPAssignmentNetwork:
    """The 6PN network a Flycast (private_v6) address belongs to. Null for all other IP types.

    Attributes:
        name (str | Unset): Network name; empty for the organization's default network.
        org_slug (str | Unset): Slug of the organization the network belongs to.
    """

    name: str | Unset = UNSET
    org_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        org_slug = self.org_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if org_slug is not UNSET:
            field_dict["org_slug"] = org_slug

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        org_slug = d.pop("org_slug", UNSET)

        ip_assignment_network = cls(
            name=name,
            org_slug=org_slug,
        )

        ip_assignment_network.additional_properties = d
        return ip_assignment_network

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
