from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolumeSnapshot")


@_attrs_define
class VolumeSnapshot:
    """
    Attributes:
        created_at (str | Unset): When the snapshot finished, in RFC 3339 format. The zero time
            (0001-01-01T00:00:00Z) while the snapshot is in progress.
        digest (str | Unset): Content digest of the snapshot. Empty while the snapshot is in progress.
        id (str | Unset): Unique ID of the snapshot. Pass it as `snapshot_id` when creating a volume to restore it.
        retention_days (int | Unset): Number of days the snapshot is kept after it was created. Omitted while the
            snapshot is
            in progress.
        size (int | Unset): Size of the stored snapshot, in bytes. 0 while the snapshot is in progress.
        status (str | Unset): `created` for completed snapshots; other values while the snapshot is in progress.
        volume_size (int | Unset): Size of the volume the snapshot was taken of, in bytes.
    """

    created_at: str | Unset = UNSET
    digest: str | Unset = UNSET
    id: str | Unset = UNSET
    retention_days: int | Unset = UNSET
    size: int | Unset = UNSET
    status: str | Unset = UNSET
    volume_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        digest = self.digest

        id = self.id

        retention_days = self.retention_days

        size = self.size

        status = self.status

        volume_size = self.volume_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if digest is not UNSET:
            field_dict["digest"] = digest
        if id is not UNSET:
            field_dict["id"] = id
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if volume_size is not UNSET:
            field_dict["volume_size"] = volume_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        digest = d.pop("digest", UNSET)

        id = d.pop("id", UNSET)

        retention_days = d.pop("retention_days", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        volume_size = d.pop("volume_size", UNSET)

        volume_snapshot = cls(
            created_at=created_at,
            digest=digest,
            id=id,
            retention_days=retention_days,
            size=size,
            status=status,
            volume_size=volume_size,
        )

        volume_snapshot.additional_properties = d
        return volume_snapshot

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
