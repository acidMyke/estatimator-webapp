from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAppSecretResponse")


@_attrs_define
class SetAppSecretResponse:
    """
    Attributes:
        Version (int | Unset): Same value as `version`.

            Deprecated: use `version`.
        created_at (str | Unset): When the secret was first set. Only returned when reading secrets.
        digest (str | Unset): Short fingerprint of the value, to tell whether it changed without revealing it. Omitted
            for deleted secrets.
        name (str | Unset): Name of the secret.
        updated_at (str | Unset): When the secret's value last changed. Only returned when reading secrets.
        value (str | Unset): Value of the secret. Only returned with `show_secrets=true`, and when setting secrets.
        version (int | Unset): The app's secrets version after this change. Pass it as `min_secrets_version` when
            creating or
            updating Machines so that they are guaranteed to see the change.
    """

    Version: int | Unset = UNSET
    created_at: str | Unset = UNSET
    digest: str | Unset = UNSET
    name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    value: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        Version = self.Version

        created_at = self.created_at

        digest = self.digest

        name = self.name

        updated_at = self.updated_at

        value = self.value

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if Version is not UNSET:
            field_dict["Version"] = Version
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if digest is not UNSET:
            field_dict["digest"] = digest
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        Version = d.pop("Version", UNSET)

        created_at = d.pop("created_at", UNSET)

        digest = d.pop("digest", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        value = d.pop("value", UNSET)

        version = d.pop("version", UNSET)

        set_app_secret_response = cls(
            Version=Version,
            created_at=created_at,
            digest=digest,
            name=name,
            updated_at=updated_at,
            value=value,
            version=version,
        )

        set_app_secret_response.additional_properties = d
        return set_app_secret_response

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
