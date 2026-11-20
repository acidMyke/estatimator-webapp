from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnablePostgresExtensionRequest")


@_attrs_define
class EnablePostgresExtensionRequest:
    """
    Attributes:
        name (str): Extension to enable. Example: citext.
        create_schema (bool | Unset): Create the schema first if it does not exist.
        schema (str | Unset): Schema to install the extension into. Defaults to the database's default schema.
    """

    name: str
    create_schema: bool | Unset = UNSET
    schema: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        create_schema = self.create_schema

        schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if create_schema is not UNSET:
            field_dict["create_schema"] = create_schema
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        create_schema = d.pop("create_schema", UNSET)

        schema = d.pop("schema", UNSET)

        enable_postgres_extension_request = cls(
            name=name,
            create_schema=create_schema,
            schema=schema,
        )

        enable_postgres_extension_request.additional_properties = d
        return enable_postgres_extension_request

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
