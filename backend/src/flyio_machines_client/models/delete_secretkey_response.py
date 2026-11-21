from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSecretkeyResponse")


@_attrs_define
class DeleteSecretkeyResponse:
    """
    Attributes:
        Version (int | Unset): Same value as `version`.

            Deprecated: use `version`.
        version (int | Unset): The app's secrets version after this change.
    """

    Version: int | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        Version = self.Version

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if Version is not UNSET:
            field_dict["Version"] = Version
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        Version = d.pop("Version", UNSET)

        version = d.pop("version", UNSET)

        delete_secretkey_response = cls(
            Version=Version,
            version=version,
        )

        delete_secretkey_response.additional_properties = d
        return delete_secretkey_response

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
