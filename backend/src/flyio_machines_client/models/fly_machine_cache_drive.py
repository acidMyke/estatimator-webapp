from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineCacheDrive")


@_attrs_define
class FlyMachineCacheDrive:
    """
    Attributes:
        path (str | Unset): Absolute path in the Machine at which to mount the cache disk.
        size_mb (int | Unset): Size of the cache disk in MiB. Between 16 and 51200.
            Changing the size discards the disk's contents.
    """

    path: str | Unset = UNSET
    size_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        size_mb = self.size_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if size_mb is not UNSET:
            field_dict["size_mb"] = size_mb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        size_mb = d.pop("size_mb", UNSET)

        fly_machine_cache_drive = cls(
            path=path,
            size_mb=size_mb,
        )

        fly_machine_cache_drive.additional_properties = d
        return fly_machine_cache_drive

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
