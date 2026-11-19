from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetSecretkeyResponse")


@_attrs_define
class SetSecretkeyResponse:
    """
    Attributes:
        Version (int | Unset): Same value as `version`.

            Deprecated: use `version`.
        created_at (str | Unset): When the key was first set.
        name (str | Unset): Name of the secret key.
        public_key (str | Unset): Public key of asymmetric keys (`nacl_box`, `nacl_sign`, `es256`), base64-encoded.
        type_ (str | Unset): Type of the key: `hs256`, `hs384`, `hs512`, `xaes256gcm`, `nacl_auth`, `nacl_box`,
            `nacl_secretbox`, `nacl_sign`, or `es256`.
        updated_at (str | Unset): When the key last changed.
        version (int | Unset): The app's secrets version after this change. Pass it as `min_version` to read the change
            back.
    """

    Version: int | Unset = UNSET
    created_at: str | Unset = UNSET
    name: str | Unset = UNSET
    public_key: str | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        Version = self.Version

        created_at = self.created_at

        name = self.name

        public_key = self.public_key

        type_ = self.type_

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if Version is not UNSET:
            field_dict["Version"] = Version
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if name is not UNSET:
            field_dict["name"] = name
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        Version = d.pop("Version", UNSET)

        created_at = d.pop("created_at", UNSET)

        name = d.pop("name", UNSET)

        public_key = d.pop("public_key", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        set_secretkey_response = cls(
            Version=Version,
            created_at=created_at,
            name=name,
            public_key=public_key,
            type_=type_,
            updated_at=updated_at,
            version=version,
        )

        set_secretkey_response.additional_properties = d
        return set_secretkey_response

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
