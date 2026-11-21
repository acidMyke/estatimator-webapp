from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLeaseRequest")


@_attrs_define
class CreateLeaseRequest:
    """
    Attributes:
        description (str | Unset): Description or reason for the lease, shown to others who look at it.
        ttl (int | Unset): How long the lease is valid, in seconds. Defaults to 60.
    """

    description: str | Unset = UNSET
    ttl: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        ttl = self.ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        ttl = d.pop("ttl", UNSET)

        create_lease_request = cls(
            description=description,
            ttl=ttl,
        )

        create_lease_request.additional_properties = d
        return create_lease_request

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
