from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppOrganizationInfo")


@_attrs_define
class AppOrganizationInfo:
    """
    Attributes:
        internal_numeric_id (int | Unset): Fly.io's internal numeric ID of the organization.
        name (str | Unset): Display name of the organization.
        slug (str | Unset): Slug of the organization, used to refer to it in API requests such as `org_slug`.
    """

    internal_numeric_id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_numeric_id = self.internal_numeric_id

        name = self.name

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internal_numeric_id is not UNSET:
            field_dict["internal_numeric_id"] = internal_numeric_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        internal_numeric_id = d.pop("internal_numeric_id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        app_organization_info = cls(
            internal_numeric_id=internal_numeric_id,
            name=name,
            slug=slug,
        )

        app_organization_info.additional_properties = d
        return app_organization_info

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
