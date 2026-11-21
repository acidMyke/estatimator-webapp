from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_volume_request_fstype import CreateVolumeRequestFstype
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_guest import FlyMachineGuest


T = TypeVar("T", bound="CreateVolumeRequest")


@_attrs_define
class CreateVolumeRequest:
    """
    Attributes:
        auto_backup_enabled (bool | Unset): Take daily automatic snapshots of the volume. Defaults to `true`.
        compute (FlyMachineGuest | Unset):
        compute_image (str | Unset): Ignored.
        encrypted (bool | Unset): Encrypt the volume at rest. Defaults to true. When forking, the source volume's
            setting
            is used.
        fstype (CreateVolumeRequestFstype | Unset): Filesystem to format the volume with: `ext4`, or `raw` for an
            unformatted block device.
        name (str | Unset): Name of the volume: at most 30 lowercase letters, digits, and underscores. Required.
        region (str | Unset): Region to create the volume in. Accepts the same values as the `region` of Create
            Machine. When forking, defaults to the source volume's region; otherwise defaults to the
            region of the API server handling the request.
        require_unique_zone (bool | Unset): Place the volume on a host that has no other volume of the app with the same
            name in the
            region, so that Machines using these volumes don't share a host. Fails with 400 if no
            such host is available.
        size_gb (int | Unset): Size of the volume in GiB, from 1 to the organization's maximum (500 by default).
            Required unless forking, in which case it must be omitted and the source volume's size
            is used.
        snapshot_id (str | Unset): ID of a snapshot to restore into the new volume. Mutually exclusive with
            `source_volume_id`.
        snapshot_retention (int | Unset): Number of days to keep snapshots of the volume, from 1 to 60. Defaults to 5.
        source_volume_id (str | Unset): ID of a volume to fork: the new volume starts as a copy of it. The volume must
            belong to
            an app in the same organization.
        unique_zone_app_wide (bool | Unset): With `require_unique_zone`, avoid hosts with any volume of the app in the
            region, not
            just volumes with the same name.
    """

    auto_backup_enabled: bool | Unset = UNSET
    compute: FlyMachineGuest | Unset = UNSET
    compute_image: str | Unset = UNSET
    encrypted: bool | Unset = UNSET
    fstype: CreateVolumeRequestFstype | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    require_unique_zone: bool | Unset = UNSET
    size_gb: int | Unset = UNSET
    snapshot_id: str | Unset = UNSET
    snapshot_retention: int | Unset = UNSET
    source_volume_id: str | Unset = UNSET
    unique_zone_app_wide: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_backup_enabled = self.auto_backup_enabled

        compute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute, Unset):
            compute = self.compute.to_dict()

        compute_image = self.compute_image

        encrypted = self.encrypted

        fstype: str | Unset = UNSET
        if not isinstance(self.fstype, Unset):
            fstype = self.fstype.value

        name = self.name

        region = self.region

        require_unique_zone = self.require_unique_zone

        size_gb = self.size_gb

        snapshot_id = self.snapshot_id

        snapshot_retention = self.snapshot_retention

        source_volume_id = self.source_volume_id

        unique_zone_app_wide = self.unique_zone_app_wide

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_backup_enabled is not UNSET:
            field_dict["auto_backup_enabled"] = auto_backup_enabled
        if compute is not UNSET:
            field_dict["compute"] = compute
        if compute_image is not UNSET:
            field_dict["compute_image"] = compute_image
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if fstype is not UNSET:
            field_dict["fstype"] = fstype
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if require_unique_zone is not UNSET:
            field_dict["require_unique_zone"] = require_unique_zone
        if size_gb is not UNSET:
            field_dict["size_gb"] = size_gb
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if snapshot_retention is not UNSET:
            field_dict["snapshot_retention"] = snapshot_retention
        if source_volume_id is not UNSET:
            field_dict["source_volume_id"] = source_volume_id
        if unique_zone_app_wide is not UNSET:
            field_dict["unique_zone_app_wide"] = unique_zone_app_wide

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_guest import FlyMachineGuest

        d = dict(src_dict)
        auto_backup_enabled = d.pop("auto_backup_enabled", UNSET)

        _compute = d.pop("compute", UNSET)
        compute: FlyMachineGuest | Unset
        if isinstance(_compute, Unset):
            compute = UNSET
        else:
            compute = FlyMachineGuest.from_dict(_compute)

        compute_image = d.pop("compute_image", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        _fstype = d.pop("fstype", UNSET)
        fstype: CreateVolumeRequestFstype | Unset
        if isinstance(_fstype, Unset):
            fstype = UNSET
        else:
            fstype = CreateVolumeRequestFstype(_fstype)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        require_unique_zone = d.pop("require_unique_zone", UNSET)

        size_gb = d.pop("size_gb", UNSET)

        snapshot_id = d.pop("snapshot_id", UNSET)

        snapshot_retention = d.pop("snapshot_retention", UNSET)

        source_volume_id = d.pop("source_volume_id", UNSET)

        unique_zone_app_wide = d.pop("unique_zone_app_wide", UNSET)

        create_volume_request = cls(
            auto_backup_enabled=auto_backup_enabled,
            compute=compute,
            compute_image=compute_image,
            encrypted=encrypted,
            fstype=fstype,
            name=name,
            region=region,
            require_unique_zone=require_unique_zone,
            size_gb=size_gb,
            snapshot_id=snapshot_id,
            snapshot_retention=snapshot_retention,
            source_volume_id=source_volume_id,
            unique_zone_app_wide=unique_zone_app_wide,
        )

        create_volume_request.additional_properties = d
        return create_volume_request

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
