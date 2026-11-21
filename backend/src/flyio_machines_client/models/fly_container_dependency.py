from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_container_dependency_condition import FlyContainerDependencyCondition
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyContainerDependency")


@_attrs_define
class FlyContainerDependency:
    """
    Attributes:
        condition (FlyContainerDependencyCondition | Unset):
        name (str | Unset): Name of the container this one depends on
    """

    condition: FlyContainerDependencyCondition | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition: str | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition is not UNSET:
            field_dict["condition"] = condition
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _condition = d.pop("condition", UNSET)
        condition: FlyContainerDependencyCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = FlyContainerDependencyCondition(_condition)

        name = d.pop("name", UNSET)

        fly_container_dependency = cls(
            condition=condition,
            name=name,
        )

        fly_container_dependency.additional_properties = d
        return fly_container_dependency

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
