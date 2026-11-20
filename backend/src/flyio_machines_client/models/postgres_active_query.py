from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresActiveQuery")


@_attrs_define
class PostgresActiveQuery:
    """
    Attributes:
        application_name (str | Unset): Application connected to the backend.
        client (str | Unset): Client address.
        database (str | Unset): Database name.
        duration_seconds (float | Unset): Query duration in seconds.
        pid (int | Unset): Process ID of the backend running the query.
        query (str | Unset): Full query text.
        state (str | Unset): Current backend state.
        state_duration_seconds (float | Unset): Time spent in the current state, in seconds.
        user (str | Unset): User running the query.
        wait_event (str | Unset): Event the backend is waiting for.
        wait_event_type (str | Unset): Type of event the backend is waiting for.
    """

    application_name: str | Unset = UNSET
    client: str | Unset = UNSET
    database: str | Unset = UNSET
    duration_seconds: float | Unset = UNSET
    pid: int | Unset = UNSET
    query: str | Unset = UNSET
    state: str | Unset = UNSET
    state_duration_seconds: float | Unset = UNSET
    user: str | Unset = UNSET
    wait_event: str | Unset = UNSET
    wait_event_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        client = self.client

        database = self.database

        duration_seconds = self.duration_seconds

        pid = self.pid

        query = self.query

        state = self.state

        state_duration_seconds = self.state_duration_seconds

        user = self.user

        wait_event = self.wait_event

        wait_event_type = self.wait_event_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["application_name"] = application_name
        if client is not UNSET:
            field_dict["client"] = client
        if database is not UNSET:
            field_dict["database"] = database
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if pid is not UNSET:
            field_dict["pid"] = pid
        if query is not UNSET:
            field_dict["query"] = query
        if state is not UNSET:
            field_dict["state"] = state
        if state_duration_seconds is not UNSET:
            field_dict["state_duration_seconds"] = state_duration_seconds
        if user is not UNSET:
            field_dict["user"] = user
        if wait_event is not UNSET:
            field_dict["wait_event"] = wait_event
        if wait_event_type is not UNSET:
            field_dict["wait_event_type"] = wait_event_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_name = d.pop("application_name", UNSET)

        client = d.pop("client", UNSET)

        database = d.pop("database", UNSET)

        duration_seconds = d.pop("duration_seconds", UNSET)

        pid = d.pop("pid", UNSET)

        query = d.pop("query", UNSET)

        state = d.pop("state", UNSET)

        state_duration_seconds = d.pop("state_duration_seconds", UNSET)

        user = d.pop("user", UNSET)

        wait_event = d.pop("wait_event", UNSET)

        wait_event_type = d.pop("wait_event_type", UNSET)

        postgres_active_query = cls(
            application_name=application_name,
            client=client,
            database=database,
            duration_seconds=duration_seconds,
            pid=pid,
            query=query,
            state=state,
            state_duration_seconds=state_duration_seconds,
            user=user,
            wait_event=wait_event,
            wait_event_type=wait_event_type,
        )

        postgres_active_query.additional_properties = d
        return postgres_active_query

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
