from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotatePostgresPasswordRequest")


@_attrs_define
class RotatePostgresPasswordRequest:
    """
    Attributes:
        kill_sessions (bool | Unset): Terminate the user's existing sessions after rotating.
    """

    kill_sessions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kill_sessions = self.kill_sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kill_sessions is not UNSET:
            field_dict["kill_sessions"] = kill_sessions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kill_sessions = d.pop("kill_sessions", UNSET)

        rotate_postgres_password_request = cls(
            kill_sessions=kill_sessions,
        )

        rotate_postgres_password_request.additional_properties = d
        return rotate_postgres_password_request

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
