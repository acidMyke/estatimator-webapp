from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineMount")


@_attrs_define
class FlyMachineMount:
    """
    Attributes:
        add_size_gb (int | Unset): With automatic extension, grow the volume by this many GB at a time. Between 1 and
            100.
            Mutually exclusive with add_size_percent
        add_size_percent (int | Unset): AddSizePercent grows by a percentage of the current size, rounded up to GiB.
            It is mutually exclusive with AddSizeGb.
        encrypted (bool | Unset): Whether the volume is encrypted. Set by Fly.io; ignored in requests
        extend_threshold_percent (int | Unset): Enable automatic volume extension: grow the volume when its usage
            exceeds this percentage.
            Between 50 and 99; 0 disables it
        min_add_size_gb (int | Unset): MinAddSizeGb is the minimum proportional growth in GiB (default 1).
        name (str | Unset): Name of the volume. Set by Fly.io; ignored in requests
        path (str | Unset): Absolute path in the Machine to mount the volume at. Required
        size_gb (int | Unset): Size of the volume in GB. Set by Fly.io; ignored in requests
        size_gb_limit (int | Unset): With automatic extension, never grow the volume beyond this size in GB. At most the
            organization's maximum volume size
        volume (str | Unset): ID (`vol_...`) or name of the volume to mount. Required. With a name, any unattached
            volume
            of the app with that name in the Machine's region is used
    """

    add_size_gb: int | Unset = UNSET
    add_size_percent: int | Unset = UNSET
    encrypted: bool | Unset = UNSET
    extend_threshold_percent: int | Unset = UNSET
    min_add_size_gb: int | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    size_gb: int | Unset = UNSET
    size_gb_limit: int | Unset = UNSET
    volume: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_size_gb = self.add_size_gb

        add_size_percent = self.add_size_percent

        encrypted = self.encrypted

        extend_threshold_percent = self.extend_threshold_percent

        min_add_size_gb = self.min_add_size_gb

        name = self.name

        path = self.path

        size_gb = self.size_gb

        size_gb_limit = self.size_gb_limit

        volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_size_gb is not UNSET:
            field_dict["add_size_gb"] = add_size_gb
        if add_size_percent is not UNSET:
            field_dict["add_size_percent"] = add_size_percent
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if extend_threshold_percent is not UNSET:
            field_dict["extend_threshold_percent"] = extend_threshold_percent
        if min_add_size_gb is not UNSET:
            field_dict["min_add_size_gb"] = min_add_size_gb
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if size_gb is not UNSET:
            field_dict["size_gb"] = size_gb
        if size_gb_limit is not UNSET:
            field_dict["size_gb_limit"] = size_gb_limit
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        add_size_gb = d.pop("add_size_gb", UNSET)

        add_size_percent = d.pop("add_size_percent", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        extend_threshold_percent = d.pop("extend_threshold_percent", UNSET)

        min_add_size_gb = d.pop("min_add_size_gb", UNSET)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        size_gb = d.pop("size_gb", UNSET)

        size_gb_limit = d.pop("size_gb_limit", UNSET)

        volume = d.pop("volume", UNSET)

        fly_machine_mount = cls(
            add_size_gb=add_size_gb,
            add_size_percent=add_size_percent,
            encrypted=encrypted,
            extend_threshold_percent=extend_threshold_percent,
            min_add_size_gb=min_add_size_gb,
            name=name,
            path=path,
            size_gb=size_gb,
            size_gb_limit=size_gb_limit,
            volume=volume,
        )

        fly_machine_mount.additional_properties = d
        return fly_machine_mount

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
