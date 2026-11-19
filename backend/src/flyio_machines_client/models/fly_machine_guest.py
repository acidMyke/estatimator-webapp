from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_machine_guest_persist_rootfs import FlyMachineGuestPersistRootfs
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineGuest")


@_attrs_define
class FlyMachineGuest:
    """
    Attributes:
        cpu_kind (str | Unset): Kind of CPU: shared or performance. Performance CPUs must be enabled for the
            organization.
            Defaults to shared when `guest` is omitted
        cpus (int | Unset): Number of CPUs: 1, 2, 4, 6, 8, 10, 12, 14, 16, 32, 64 or 128, up to 8 for shared and 16 for
            performance CPUs unless the organization's limit is higher. Defaults to 1 when `guest` is
            omitted
        gpu_kind (str | Unset): No longer supported. Requests that set it are rejected
        gpus (int | Unset): No longer supported. Requests that set it are rejected
        host_dedication_id (str | Unset): Place the Machine on hosts dedicated to the organization under this ID. Only
            available to
            organizations with dedicated hosts
        kernel_args (list[str] | Unset): Extra arguments appended to the guest kernel command line
        max_memory_mb (int | Unset): Memory in MiB that the Machine's memory limit can later be raised to without a
            restart, using
            the memory endpoints. Must be at least memory_mb and at most the per-CPU maximum. The Machine
            starts with a limit of memory_mb
        memory_mb (int | Unset): Memory in MiB. Must be a multiple of 256 for shared and 1024 for performance CPUs, and
            between 256 and 2048 (shared) or 2048 and 8192 (performance) per CPU. Defaults to 256 when
            `guest` is omitted
        persist_rootfs (FlyMachineGuestPersistRootfs | Unset): Deprecated: use MachineConfig.Rootfs instead
        required_host_features (list[str] | Unset): Host features the Machine's host must have, such as `storage-
            tier-1`. At most 16, each made
            of lowercase letters, digits and dashes. Each feature must be enabled for the organization
    """

    cpu_kind: str | Unset = UNSET
    cpus: int | Unset = UNSET
    gpu_kind: str | Unset = UNSET
    gpus: int | Unset = UNSET
    host_dedication_id: str | Unset = UNSET
    kernel_args: list[str] | Unset = UNSET
    max_memory_mb: int | Unset = UNSET
    memory_mb: int | Unset = UNSET
    persist_rootfs: FlyMachineGuestPersistRootfs | Unset = UNSET
    required_host_features: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_kind = self.cpu_kind

        cpus = self.cpus

        gpu_kind = self.gpu_kind

        gpus = self.gpus

        host_dedication_id = self.host_dedication_id

        kernel_args: list[str] | Unset = UNSET
        if not isinstance(self.kernel_args, Unset):
            kernel_args = self.kernel_args

        max_memory_mb = self.max_memory_mb

        memory_mb = self.memory_mb

        persist_rootfs: str | Unset = UNSET
        if not isinstance(self.persist_rootfs, Unset):
            persist_rootfs = self.persist_rootfs.value

        required_host_features: list[str] | Unset = UNSET
        if not isinstance(self.required_host_features, Unset):
            required_host_features = self.required_host_features

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_kind is not UNSET:
            field_dict["cpu_kind"] = cpu_kind
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if gpu_kind is not UNSET:
            field_dict["gpu_kind"] = gpu_kind
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if host_dedication_id is not UNSET:
            field_dict["host_dedication_id"] = host_dedication_id
        if kernel_args is not UNSET:
            field_dict["kernel_args"] = kernel_args
        if max_memory_mb is not UNSET:
            field_dict["max_memory_mb"] = max_memory_mb
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb
        if persist_rootfs is not UNSET:
            field_dict["persist_rootfs"] = persist_rootfs
        if required_host_features is not UNSET:
            field_dict["required_host_features"] = required_host_features

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cpu_kind = d.pop("cpu_kind", UNSET)

        cpus = d.pop("cpus", UNSET)

        gpu_kind = d.pop("gpu_kind", UNSET)

        gpus = d.pop("gpus", UNSET)

        host_dedication_id = d.pop("host_dedication_id", UNSET)

        kernel_args = cast(list[str], d.pop("kernel_args", UNSET))

        max_memory_mb = d.pop("max_memory_mb", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        _persist_rootfs = d.pop("persist_rootfs", UNSET)
        persist_rootfs: FlyMachineGuestPersistRootfs | Unset
        if isinstance(_persist_rootfs, Unset):
            persist_rootfs = UNSET
        else:
            persist_rootfs = FlyMachineGuestPersistRootfs(_persist_rootfs)

        required_host_features = cast(list[str], d.pop("required_host_features", UNSET))

        fly_machine_guest = cls(
            cpu_kind=cpu_kind,
            cpus=cpus,
            gpu_kind=gpu_kind,
            gpus=gpus,
            host_dedication_id=host_dedication_id,
            kernel_args=kernel_args,
            max_memory_mb=max_memory_mb,
            memory_mb=memory_mb,
            persist_rootfs=persist_rootfs,
            required_host_features=required_host_features,
        )

        fly_machine_guest.additional_properties = d
        return fly_machine_guest

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
