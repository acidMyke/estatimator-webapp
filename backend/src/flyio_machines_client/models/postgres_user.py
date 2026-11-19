from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postgres_user_role import PostgresUserRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresUser")


@_attrs_define
class PostgresUser:
    """
    Attributes:
        role (PostgresUserRole | Unset): User role.
        username (str | Unset): User name.
    """

    role: PostgresUserRole | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _role = d.pop("role", UNSET)
        role: PostgresUserRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PostgresUserRole(_role)

        username = d.pop("username", UNSET)

        postgres_user = cls(
            role=role,
            username=username,
        )

        postgres_user.additional_properties = d
        return postgres_user

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
