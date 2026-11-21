from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertMetadataKeyRequest")


@_attrs_define
class UpsertMetadataKeyRequest:
    """
    Attributes:
        updated_at (str | Unset): Time to record for the change in the Machine's `metadata_update` event. Defaults to
            now.
        value (str | Unset): Value to set. Must not be empty or whitespace only.
    """

    updated_at: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        updated_at = d.pop("updated_at", UNSET)

        value = d.pop("value", UNSET)

        upsert_metadata_key_request = cls(
            updated_at=updated_at,
            value=value,
        )

        upsert_metadata_key_request.additional_properties = d
        return upsert_metadata_key_request

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
