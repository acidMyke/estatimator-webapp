from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_postgres_user_request_role import CreatePostgresUserRequestRole

T = TypeVar("T", bound="CreatePostgresUserRequest")


@_attrs_define
class CreatePostgresUserRequest:
    """
    Attributes:
        role (CreatePostgresUserRequestRole): Role to grant the user. Example: writer.
        username (str): Name for the new user. Must start and end with a lowercase alphanumeric
            character and may contain hyphens and underscores, up to 63 characters. Example: app_user.
    """

    role: CreatePostgresUserRequestRole
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role = CreatePostgresUserRequestRole(d.pop("role"))

        username = d.pop("username")

        create_postgres_user_request = cls(
            role=role,
            username=username,
        )

        create_postgres_user_request.additional_properties = d
        return create_postgres_user_request

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
