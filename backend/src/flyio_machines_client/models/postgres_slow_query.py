from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresSlowQuery")


@_attrs_define
class PostgresSlowQuery:
    """
    Attributes:
        calls (int | Unset): Cumulative number of executions.
        database (str | Unset): Database name.
        max_exec_time_seconds (float | Unset): Maximum execution time in seconds.
        mean_exec_time_seconds (float | Unset): Mean execution time in seconds.
        query (str | Unset): Full query pattern.
        query_id (str | Unset): Query identifier.
        total_exec_time_seconds (float | Unset): Cumulative total execution time in seconds.
        user (str | Unset): User running the query.
    """

    calls: int | Unset = UNSET
    database: str | Unset = UNSET
    max_exec_time_seconds: float | Unset = UNSET
    mean_exec_time_seconds: float | Unset = UNSET
    query: str | Unset = UNSET
    query_id: str | Unset = UNSET
    total_exec_time_seconds: float | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        database = self.database

        max_exec_time_seconds = self.max_exec_time_seconds

        mean_exec_time_seconds = self.mean_exec_time_seconds

        query = self.query

        query_id = self.query_id

        total_exec_time_seconds = self.total_exec_time_seconds

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calls is not UNSET:
            field_dict["calls"] = calls
        if database is not UNSET:
            field_dict["database"] = database
        if max_exec_time_seconds is not UNSET:
            field_dict["max_exec_time_seconds"] = max_exec_time_seconds
        if mean_exec_time_seconds is not UNSET:
            field_dict["mean_exec_time_seconds"] = mean_exec_time_seconds
        if query is not UNSET:
            field_dict["query"] = query
        if query_id is not UNSET:
            field_dict["query_id"] = query_id
        if total_exec_time_seconds is not UNSET:
            field_dict["total_exec_time_seconds"] = total_exec_time_seconds
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        calls = d.pop("calls", UNSET)

        database = d.pop("database", UNSET)

        max_exec_time_seconds = d.pop("max_exec_time_seconds", UNSET)

        mean_exec_time_seconds = d.pop("mean_exec_time_seconds", UNSET)

        query = d.pop("query", UNSET)

        query_id = d.pop("query_id", UNSET)

        total_exec_time_seconds = d.pop("total_exec_time_seconds", UNSET)

        user = d.pop("user", UNSET)

        postgres_slow_query = cls(
            calls=calls,
            database=database,
            max_exec_time_seconds=max_exec_time_seconds,
            mean_exec_time_seconds=mean_exec_time_seconds,
            query=query,
            query_id=query_id,
            total_exec_time_seconds=total_exec_time_seconds,
            user=user,
        )

        postgres_slow_query.additional_properties = d
        return postgres_slow_query

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
