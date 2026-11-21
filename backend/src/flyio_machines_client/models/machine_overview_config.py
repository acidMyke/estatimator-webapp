from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_guest import FlyMachineGuest
    from ..models.machine_overview_config_metadata import MachineOverviewConfigMetadata


T = TypeVar("T", bound="MachineOverviewConfig")


@_attrs_define
class MachineOverviewConfig:
    """
    Attributes:
        guest (FlyMachineGuest | Unset):
        image (str | Unset): The image reference the Machine was configured with.
        metadata (MachineOverviewConfigMetadata | Unset): The Machine's metadata key-value pairs.
    """

    guest: FlyMachineGuest | Unset = UNSET
    image: str | Unset = UNSET
    metadata: MachineOverviewConfigMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest, Unset):
            guest = self.guest.to_dict()

        image = self.image

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guest is not UNSET:
            field_dict["guest"] = guest
        if image is not UNSET:
            field_dict["image"] = image
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_guest import FlyMachineGuest
        from ..models.machine_overview_config_metadata import (
            MachineOverviewConfigMetadata,
        )

        d = dict(src_dict)
        _guest = d.pop("guest", UNSET)
        guest: FlyMachineGuest | Unset
        if isinstance(_guest, Unset):
            guest = UNSET
        else:
            guest = FlyMachineGuest.from_dict(_guest)

        image = d.pop("image", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: MachineOverviewConfigMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MachineOverviewConfigMetadata.from_dict(_metadata)

        machine_overview_config = cls(
            guest=guest,
            image=image,
            metadata=metadata,
        )

        machine_overview_config.additional_properties = d
        return machine_overview_config

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
