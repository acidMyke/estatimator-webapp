from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_volume import OrgVolume


T = TypeVar("T", bound="OrgVolumesResponse")


@_attrs_define
class OrgVolumesResponse:
    """
    Attributes:
        last_updated_at (str | Unset): `updated_at` of the last volume on this page.
        last_volume_id (str | Unset): ID of the last volume on this page.
        next_cursor (str | Unset): Pagination cursor for the next page. Absent when no more volumes remain.
        volumes (list[OrgVolume] | Unset): The volumes on this page.
    """

    last_updated_at: str | Unset = UNSET
    last_volume_id: str | Unset = UNSET
    next_cursor: str | Unset = UNSET
    volumes: list[OrgVolume] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_updated_at = self.last_updated_at

        last_volume_id = self.last_volume_id

        next_cursor = self.next_cursor

        volumes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()
                volumes.append(volumes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_updated_at is not UNSET:
            field_dict["last_updated_at"] = last_updated_at
        if last_volume_id is not UNSET:
            field_dict["last_volume_id"] = last_volume_id
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.org_volume import OrgVolume

        d = dict(src_dict)
        last_updated_at = d.pop("last_updated_at", UNSET)

        last_volume_id = d.pop("last_volume_id", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        _volumes = d.pop("volumes", UNSET)
        volumes: list[OrgVolume] | Unset = UNSET
        if _volumes is not UNSET:
            volumes = []
            for volumes_item_data in _volumes:
                volumes_item = OrgVolume.from_dict(volumes_item_data)

                volumes.append(volumes_item)

        org_volumes_response = cls(
            last_updated_at=last_updated_at,
            last_volume_id=last_volume_id,
            next_cursor=next_cursor,
            volumes=volumes,
        )

        org_volumes_response.additional_properties = d
        return org_volumes_response

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
