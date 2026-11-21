from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_machine_rootfs_persist import FlyMachineRootfsPersist
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineRootfs")


@_attrs_define
class FlyMachineRootfs:
    """
    Attributes:
        persist (FlyMachineRootfsPersist | Unset): Whether changes to the root filesystem are kept. `never` (default):
            reset on every start.
            `restart`: kept across stops and restarts, reset when the Machine is updated. `always`: also
            kept across updates
        size_gb (int | Unset): Size of the root filesystem in GB. At most 50; 0 uses the default
    """

    persist: FlyMachineRootfsPersist | Unset = UNSET
    size_gb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persist: str | Unset = UNSET
        if not isinstance(self.persist, Unset):
            persist = self.persist.value

        size_gb = self.size_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persist is not UNSET:
            field_dict["persist"] = persist
        if size_gb is not UNSET:
            field_dict["size_gb"] = size_gb

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _persist = d.pop("persist", UNSET)
        persist: FlyMachineRootfsPersist | Unset
        if isinstance(_persist, Unset):
            persist = UNSET
        else:
            persist = FlyMachineRootfsPersist(_persist)

        size_gb = d.pop("size_gb", UNSET)

        fly_machine_rootfs = cls(
            persist=persist,
            size_gb=size_gb,
        )

        fly_machine_rootfs.additional_properties = d
        return fly_machine_rootfs

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
