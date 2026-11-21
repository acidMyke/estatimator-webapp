from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartMachineResponse")


@_attrs_define
class StartMachineResponse:
    """
    Attributes:
        migrated (bool | Unset): Whether the Machine was moved to another host to be started
        new_host (str | Unset): The host the Machine was moved to, if it was migrated
        previous_state (str | Unset): The state the Machine was in before it was started
    """

    migrated: bool | Unset = UNSET
    new_host: str | Unset = UNSET
    previous_state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        migrated = self.migrated

        new_host = self.new_host

        previous_state = self.previous_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if migrated is not UNSET:
            field_dict["migrated"] = migrated
        if new_host is not UNSET:
            field_dict["new_host"] = new_host
        if previous_state is not UNSET:
            field_dict["previous_state"] = previous_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        migrated = d.pop("migrated", UNSET)

        new_host = d.pop("new_host", UNSET)

        previous_state = d.pop("previous_state", UNSET)

        start_machine_response = cls(
            migrated=migrated,
            new_host=new_host,
            previous_state=previous_state,
        )

        start_machine_response.additional_properties = d
        return start_machine_response

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
