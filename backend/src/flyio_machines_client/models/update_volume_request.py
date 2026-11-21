from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateVolumeRequest")


@_attrs_define
class UpdateVolumeRequest:
    """
    Attributes:
        auto_backup_enabled (bool | Unset): Take daily automatic snapshots of the volume. Unchanged if omitted.
        snapshot_retention (int | Unset): Number of days to keep snapshots of the volume, from 1 to 60. Unchanged if
            omitted.
    """

    auto_backup_enabled: bool | Unset = UNSET
    snapshot_retention: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_backup_enabled = self.auto_backup_enabled

        snapshot_retention = self.snapshot_retention

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_backup_enabled is not UNSET:
            field_dict["auto_backup_enabled"] = auto_backup_enabled
        if snapshot_retention is not UNSET:
            field_dict["snapshot_retention"] = snapshot_retention

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auto_backup_enabled = d.pop("auto_backup_enabled", UNSET)

        snapshot_retention = d.pop("snapshot_retention", UNSET)

        update_volume_request = cls(
            auto_backup_enabled=auto_backup_enabled,
            snapshot_retention=snapshot_retention,
        )

        update_volume_request.additional_properties = d
        return update_volume_request

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
