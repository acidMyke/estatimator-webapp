from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgres_endpoint import PostgresEndpoint


T = TypeVar("T", bound="PostgresNodeEndpoints")


@_attrs_define
class PostgresNodeEndpoints:
    """
    Attributes:
        direct (PostgresEndpoint | Unset):
        pooler (PostgresEndpoint | Unset):
    """

    direct: PostgresEndpoint | Unset = UNSET
    pooler: PostgresEndpoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direct: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direct, Unset):
            direct = self.direct.to_dict()

        pooler: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pooler, Unset):
            pooler = self.pooler.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct is not UNSET:
            field_dict["direct"] = direct
        if pooler is not UNSET:
            field_dict["pooler"] = pooler

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.postgres_endpoint import PostgresEndpoint

        d = dict(src_dict)
        _direct = d.pop("direct", UNSET)
        direct: PostgresEndpoint | Unset
        if isinstance(_direct, Unset):
            direct = UNSET
        else:
            direct = PostgresEndpoint.from_dict(_direct)

        _pooler = d.pop("pooler", UNSET)
        pooler: PostgresEndpoint | Unset
        if isinstance(_pooler, Unset):
            pooler = UNSET
        else:
            pooler = PostgresEndpoint.from_dict(_pooler)

        postgres_node_endpoints = cls(
            direct=direct,
            pooler=pooler,
        )

        postgres_node_endpoints.additional_properties = d
        return postgres_node_endpoints

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
