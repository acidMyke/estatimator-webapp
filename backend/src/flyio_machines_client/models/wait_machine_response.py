from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WaitMachineResponse")


@_attrs_define
class WaitMachineResponse:
    """
    Attributes:
        event_id (str | Unset): ID of the event that moved the Machine into `state`. Pass it as `from_event_id` to wait
            for a later state change.
        ok (bool | Unset): Always true.
        state (str | Unset): The state the Machine reached, one of the requested states.
        version (str | Unset): ID of the Machine version that reached `state`.
    """

    event_id: str | Unset = UNSET
    ok: bool | Unset = UNSET
    state: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        ok = self.ok

        state = self.state

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if ok is not UNSET:
            field_dict["ok"] = ok
        if state is not UNSET:
            field_dict["state"] = state
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        event_id = d.pop("event_id", UNSET)

        ok = d.pop("ok", UNSET)

        state = d.pop("state", UNSET)

        version = d.pop("version", UNSET)

        wait_machine_response = cls(
            event_id=event_id,
            ok=ok,
            state=state,
            version=version,
        )

        wait_machine_response.additional_properties = d
        return wait_machine_response

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
