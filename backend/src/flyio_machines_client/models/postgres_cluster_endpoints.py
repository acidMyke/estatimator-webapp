from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgres_node_endpoints import PostgresNodeEndpoints


T = TypeVar("T", bound="PostgresClusterEndpoints")


@_attrs_define
class PostgresClusterEndpoints:
    """
    Attributes:
        primary (PostgresNodeEndpoints | Unset):
    """

    primary: PostgresNodeEndpoints | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.postgres_node_endpoints import PostgresNodeEndpoints

        d = dict(src_dict)
        _primary = d.pop("primary", UNSET)
        primary: PostgresNodeEndpoints | Unset
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = PostgresNodeEndpoints.from_dict(_primary)

        postgres_cluster_endpoints = cls(
            primary=primary,
        )

        postgres_cluster_endpoints.additional_properties = d
        return postgres_cluster_endpoints

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
