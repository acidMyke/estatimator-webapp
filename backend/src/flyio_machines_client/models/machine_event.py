from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_event_request import MachineEventRequest


T = TypeVar("T", bound="MachineEvent")


@_attrs_define
class MachineEvent:
    """
    Attributes:
        id (str | Unset): Unique ID of the event (a ULID).
        request (MachineEventRequest | Unset): Details that depend on the event type. For example, `exit` events carry
            the exit
            code and whether the process was killed for running out of memory, and `update`
            events carry the new version.
        source (str | Unset): Who triggered the event: `user` for requests to this API, `flyd` for the host's
            Machine manager acting on its own (for example when a Machine exits or restarts), or
            `proxy` for Fly Proxy starting and stopping Machines.
        status (str | Unset): The state the Machine moved to with this event, such as `created`, `started`, or
            `stopped`. The Machine's `state` is the status of its latest event.
        timestamp (int | Unset): When the event happened, in Unix milliseconds.
        type_ (str | Unset): What happened, such as `launch`, `start`, `stop`, `exit`, `restart`, `update`,
            `suspension`, `cancel_suspension`, `migration`, `metadata_update`, `archive`, or
            `destroy`.
    """

    id: str | Unset = UNSET
    request: MachineEventRequest | Unset = UNSET
    source: str | Unset = UNSET
    status: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        source = self.source

        status = self.status

        timestamp = self.timestamp

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if request is not UNSET:
            field_dict["request"] = request
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.machine_event_request import MachineEventRequest

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _request = d.pop("request", UNSET)
        request: MachineEventRequest | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = MachineEventRequest.from_dict(_request)

        source = d.pop("source", UNSET)

        status = d.pop("status", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        type_ = d.pop("type", UNSET)

        machine_event = cls(
            id=id,
            request=request,
            source=source,
            status=status,
            timestamp=timestamp,
            type_=type_,
        )

        machine_event.additional_properties = d
        return machine_event

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
