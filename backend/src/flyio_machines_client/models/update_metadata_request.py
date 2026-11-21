from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_metadata_request_metadata import UpdateMetadataRequestMetadata


T = TypeVar("T", bound="UpdateMetadataRequest")


@_attrs_define
class UpdateMetadataRequest:
    """
    Attributes:
        machine_version (str | Unset): Only apply the change if this is still the Machine's current version; otherwise
            fail
            with 412. Defaults to the current version.
        metadata (UpdateMetadataRequestMetadata | Unset): Keys to change. A string value sets the key; null, an empty
            string or whitespace removes
            it. Keys and values have surrounding whitespace trimmed. Keys not listed are left alone.
            Must contain at least one key.
        updated_at (str | Unset): Time to record for the change in the Machine's `metadata_update` event. Defaults to
            now.
    """

    machine_version: str | Unset = UNSET
    metadata: UpdateMetadataRequestMetadata | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        machine_version = self.machine_version

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if machine_version is not UNSET:
            field_dict["machine_version"] = machine_version
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_metadata_request_metadata import (
            UpdateMetadataRequestMetadata,
        )

        d = dict(src_dict)
        machine_version = d.pop("machine_version", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: UpdateMetadataRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateMetadataRequestMetadata.from_dict(_metadata)

        updated_at = d.pop("updated_at", UNSET)

        update_metadata_request = cls(
            machine_version=machine_version,
            metadata=metadata,
            updated_at=updated_at,
        )

        update_metadata_request.additional_properties = d
        return update_metadata_request

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
