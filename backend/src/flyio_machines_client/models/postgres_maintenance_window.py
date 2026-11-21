from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postgres_maintenance_window_day import PostgresMaintenanceWindowDay
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresMaintenanceWindow")


@_attrs_define
class PostgresMaintenanceWindow:
    """
    Attributes:
        day (PostgresMaintenanceWindowDay | Unset): Day of the week the window starts on. Example: sunday.
        duration_hours (int | Unset): Length of the window in hours. Example: 3.
        start_hour (int | Unset): Hour of the day the window starts, in the cluster's timezone. Example: 1.
        timezone (str | Unset): IANA timezone the window is expressed in, derived from the cluster's region. Example:
            America/New_York.
    """

    day: PostgresMaintenanceWindowDay | Unset = UNSET
    duration_hours: int | Unset = UNSET
    start_hour: int | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day: str | Unset = UNSET
        if not isinstance(self.day, Unset):
            day = self.day.value

        duration_hours = self.duration_hours

        start_hour = self.start_hour

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if duration_hours is not UNSET:
            field_dict["duration_hours"] = duration_hours
        if start_hour is not UNSET:
            field_dict["start_hour"] = start_hour
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _day = d.pop("day", UNSET)
        day: PostgresMaintenanceWindowDay | Unset
        if isinstance(_day, Unset):
            day = UNSET
        else:
            day = PostgresMaintenanceWindowDay(_day)

        duration_hours = d.pop("duration_hours", UNSET)

        start_hour = d.pop("start_hour", UNSET)

        timezone = d.pop("timezone", UNSET)

        postgres_maintenance_window = cls(
            day=day,
            duration_hours=duration_hours,
            start_hour=start_hour,
            timezone=timezone,
        )

        postgres_maintenance_window.additional_properties = d
        return postgres_maintenance_window

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
