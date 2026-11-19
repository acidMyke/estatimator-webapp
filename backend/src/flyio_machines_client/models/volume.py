from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_host_status import VolumeHostStatus
from ..models.volume_type import VolumeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Volume")


@_attrs_define
class Volume:
    """
    Attributes:
        attached_alloc_id (str | Unset): Always null.

            Deprecated: volumes are no longer attached to Nomad allocations.
        attached_machine_id (str | Unset): ID of the Machine the volume is attached to, or null if it is not attached.
        auto_backup_enabled (bool | Unset): Whether daily automatic snapshots are taken.
        block_size (int | Unset): Size of a filesystem block, in bytes. See `blocks`.
        blocks (int | Unset): Size of the volume's filesystem, in blocks of `block_size` bytes, as last reported by a
            Machine that mounted the volume. 0 if never reported, if the host could not be reached,
            or with `summary=true`.
        blocks_avail (int | Unset): Number of filesystem blocks available to unprivileged users. See `blocks`.
        blocks_free (int | Unset): Number of free filesystem blocks, including blocks reserved for the root user. See
            `blocks`.
        bytes_total (int | Unset): Size of the volume, in bytes. 0 if the host could not be reached or with
            `summary=true`.
        bytes_used (int | Unset): Bytes of storage the volume occupies on its host. Volumes are thinly provisioned, so
            this
            grows as blocks are written and does not shrink when files are deleted. It is not the
            filesystem's usage; use `blocks` and `blocks_free` for that. 0 if the host could not be
            reached or with `summary=true`.
        created_at (str | Unset): When the volume was created.
        encrypted (bool | Unset): Whether the volume is encrypted at rest.
        fstype (str | Unset): Filesystem the volume was formatted with: `ext4`, or `raw` for an unformatted block
            device.
        host_features (list[str] | Unset): Features of the volume's host. Only returned when the request sets the
            `fly-include-host-features: true` header.
        host_status (VolumeHostStatus | Unset): Whether Fly.io could reach the volume's host: `ok` if it could,
            `unreachable` or
            `unknown` if it could not, in which case host-reported fields are missing.
        id (str | Unset): Unique ID of the volume, such as `vol_1234567890abcdef`.
        name (str | Unset): Name of the volume. Several volumes of an app can share a name.
        region (str | Unset): Code of the region the volume is in.
        required_host_features (list[str] | Unset): Host features the volume's host was required to have; see
            `compute.required_host_features`
            in the create request.
        size_gb (int | Unset): Size of the volume, in GiB.
        snapshot_retention (int | Unset): Number of days snapshots of the volume are kept.
        state (str | Unset): State of the volume, such as `creating`, `created`, `extending`, `restoring`,
            `hydrating`, `scheduling_destroy`, `pending_destroy`, `destroying`, `destroyed`, or
            `failed`.
        type_ (VolumeType | Unset): Kind of volume: `local` for regular volumes, or `cache` for volumes that hold
            disposable data and support neither snapshots nor restores.
        zone (str | Unset): Identifies the host the volume is on. Volumes with different zones are on different
            hosts.
    """

    attached_alloc_id: str | Unset = UNSET
    attached_machine_id: str | Unset = UNSET
    auto_backup_enabled: bool | Unset = UNSET
    block_size: int | Unset = UNSET
    blocks: int | Unset = UNSET
    blocks_avail: int | Unset = UNSET
    blocks_free: int | Unset = UNSET
    bytes_total: int | Unset = UNSET
    bytes_used: int | Unset = UNSET
    created_at: str | Unset = UNSET
    encrypted: bool | Unset = UNSET
    fstype: str | Unset = UNSET
    host_features: list[str] | Unset = UNSET
    host_status: VolumeHostStatus | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    required_host_features: list[str] | Unset = UNSET
    size_gb: int | Unset = UNSET
    snapshot_retention: int | Unset = UNSET
    state: str | Unset = UNSET
    type_: VolumeType | Unset = UNSET
    zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attached_alloc_id = self.attached_alloc_id

        attached_machine_id = self.attached_machine_id

        auto_backup_enabled = self.auto_backup_enabled

        block_size = self.block_size

        blocks = self.blocks

        blocks_avail = self.blocks_avail

        blocks_free = self.blocks_free

        bytes_total = self.bytes_total

        bytes_used = self.bytes_used

        created_at = self.created_at

        encrypted = self.encrypted

        fstype = self.fstype

        host_features: list[str] | Unset = UNSET
        if not isinstance(self.host_features, Unset):
            host_features = self.host_features

        host_status: str | Unset = UNSET
        if not isinstance(self.host_status, Unset):
            host_status = self.host_status.value

        id = self.id

        name = self.name

        region = self.region

        required_host_features: list[str] | Unset = UNSET
        if not isinstance(self.required_host_features, Unset):
            required_host_features = self.required_host_features

        size_gb = self.size_gb

        snapshot_retention = self.snapshot_retention

        state = self.state

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        zone = self.zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attached_alloc_id is not UNSET:
            field_dict["attached_alloc_id"] = attached_alloc_id
        if attached_machine_id is not UNSET:
            field_dict["attached_machine_id"] = attached_machine_id
        if auto_backup_enabled is not UNSET:
            field_dict["auto_backup_enabled"] = auto_backup_enabled
        if block_size is not UNSET:
            field_dict["block_size"] = block_size
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if blocks_avail is not UNSET:
            field_dict["blocks_avail"] = blocks_avail
        if blocks_free is not UNSET:
            field_dict["blocks_free"] = blocks_free
        if bytes_total is not UNSET:
            field_dict["bytes_total"] = bytes_total
        if bytes_used is not UNSET:
            field_dict["bytes_used"] = bytes_used
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if fstype is not UNSET:
            field_dict["fstype"] = fstype
        if host_features is not UNSET:
            field_dict["host_features"] = host_features
        if host_status is not UNSET:
            field_dict["host_status"] = host_status
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if required_host_features is not UNSET:
            field_dict["required_host_features"] = required_host_features
        if size_gb is not UNSET:
            field_dict["size_gb"] = size_gb
        if snapshot_retention is not UNSET:
            field_dict["snapshot_retention"] = snapshot_retention
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attached_alloc_id = d.pop("attached_alloc_id", UNSET)

        attached_machine_id = d.pop("attached_machine_id", UNSET)

        auto_backup_enabled = d.pop("auto_backup_enabled", UNSET)

        block_size = d.pop("block_size", UNSET)

        blocks = d.pop("blocks", UNSET)

        blocks_avail = d.pop("blocks_avail", UNSET)

        blocks_free = d.pop("blocks_free", UNSET)

        bytes_total = d.pop("bytes_total", UNSET)

        bytes_used = d.pop("bytes_used", UNSET)

        created_at = d.pop("created_at", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        fstype = d.pop("fstype", UNSET)

        host_features = cast(list[str], d.pop("host_features", UNSET))

        _host_status = d.pop("host_status", UNSET)
        host_status: VolumeHostStatus | Unset
        if isinstance(_host_status, Unset):
            host_status = UNSET
        else:
            host_status = VolumeHostStatus(_host_status)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        required_host_features = cast(list[str], d.pop("required_host_features", UNSET))

        size_gb = d.pop("size_gb", UNSET)

        snapshot_retention = d.pop("snapshot_retention", UNSET)

        state = d.pop("state", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: VolumeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VolumeType(_type_)

        zone = d.pop("zone", UNSET)

        volume = cls(
            attached_alloc_id=attached_alloc_id,
            attached_machine_id=attached_machine_id,
            auto_backup_enabled=auto_backup_enabled,
            block_size=block_size,
            blocks=blocks,
            blocks_avail=blocks_avail,
            blocks_free=blocks_free,
            bytes_total=bytes_total,
            bytes_used=bytes_used,
            created_at=created_at,
            encrypted=encrypted,
            fstype=fstype,
            host_features=host_features,
            host_status=host_status,
            id=id,
            name=name,
            region=region,
            required_host_features=required_host_features,
            size_gb=size_gb,
            snapshot_retention=snapshot_retention,
            state=state,
            type_=type_,
            zone=zone,
        )

        volume.additional_properties = d
        return volume

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
