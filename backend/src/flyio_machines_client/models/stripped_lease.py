from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StrippedLease")


@_attrs_define
class StrippedLease:
    """
    Attributes:
        description (str | Unset): Description given when the lease was acquired.
        expires_at (int | Unset): When the lease expires, in Unix seconds.
        owner (str | Unset): Email address of the user who acquired the lease.
    """

    description: str | Unset = UNSET
    expires_at: int | Unset = UNSET
    owner: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        expires_at = self.expires_at

        owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        owner = d.pop("owner", UNSET)

        stripped_lease = cls(
            description=description,
            expires_at=expires_at,
            owner=owner,
        )

        stripped_lease.additional_properties = d
        return stripped_lease

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
