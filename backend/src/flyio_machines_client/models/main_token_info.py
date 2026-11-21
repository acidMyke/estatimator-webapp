from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainTokenInfo")


@_attrs_define
class MainTokenInfo:
    """
    Attributes:
        apps (list[str] | Unset): Names of the apps the token is restricted to. Omitted if the token is not restricted
            to
            specific apps.
        org_slug (str | Unset): Slug of the organization the token is scoped to.
        organization (str | Unset): Name of the organization the token is scoped to.
        restricted_to_machine (str | Unset): ID of the Machine the token may only be used from. Omitted if the token is
            not restricted
            to a Machine.
        source_machine_id (str | Unset): Never set.
        token_id (str | Unset): ID of the token.
        user (str | Unset): Opaque identifier of the user the token belongs to: the first 7 hex characters of a hash of
            the user's ID. Omitted for tokens that do not belong to a user.
    """

    apps: list[str] | Unset = UNSET
    org_slug: str | Unset = UNSET
    organization: str | Unset = UNSET
    restricted_to_machine: str | Unset = UNSET
    source_machine_id: str | Unset = UNSET
    token_id: str | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: list[str] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = self.apps

        org_slug = self.org_slug

        organization = self.organization

        restricted_to_machine = self.restricted_to_machine

        source_machine_id = self.source_machine_id

        token_id = self.token_id

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if org_slug is not UNSET:
            field_dict["org_slug"] = org_slug
        if organization is not UNSET:
            field_dict["organization"] = organization
        if restricted_to_machine is not UNSET:
            field_dict["restricted_to_machine"] = restricted_to_machine
        if source_machine_id is not UNSET:
            field_dict["source_machine_id"] = source_machine_id
        if token_id is not UNSET:
            field_dict["token_id"] = token_id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        apps = cast(list[str], d.pop("apps", UNSET))

        org_slug = d.pop("org_slug", UNSET)

        organization = d.pop("organization", UNSET)

        restricted_to_machine = d.pop("restricted_to_machine", UNSET)

        source_machine_id = d.pop("source_machine_id", UNSET)

        token_id = d.pop("token_id", UNSET)

        user = d.pop("user", UNSET)

        main_token_info = cls(
            apps=apps,
            org_slug=org_slug,
            organization=organization,
            restricted_to_machine=restricted_to_machine,
            source_machine_id=source_machine_id,
            token_id=token_id,
            user=user,
        )

        main_token_info.additional_properties = d
        return main_token_info

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
