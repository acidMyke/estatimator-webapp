from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnershipVerification")


@_attrs_define
class OwnershipVerification:
    """
    Attributes:
        app_value (str | Unset): TXT record value that proves ownership for this app.
        name (str | Unset): Name of the TXT record to create, such as `_fly-ownership.example.com`.
        org_value (str | Unset): TXT record value that proves ownership for every app in the organization.
    """

    app_value: str | Unset = UNSET
    name: str | Unset = UNSET
    org_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_value = self.app_value

        name = self.name

        org_value = self.org_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_value is not UNSET:
            field_dict["app_value"] = app_value
        if name is not UNSET:
            field_dict["name"] = name
        if org_value is not UNSET:
            field_dict["org_value"] = org_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        app_value = d.pop("app_value", UNSET)

        name = d.pop("name", UNSET)

        org_value = d.pop("org_value", UNSET)

        ownership_verification = cls(
            app_value=app_value,
            name=name,
            org_value=org_value,
        )

        ownership_verification.additional_properties = d
        return ownership_verification

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
