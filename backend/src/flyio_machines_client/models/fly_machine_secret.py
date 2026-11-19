from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineSecret")


@_attrs_define
class FlyMachineSecret:
    """A Secret needing to be set in the environment of the Machine. env_var is required

    Attributes:
        env_var (str | Unset): EnvVar is required and is the name of the environment variable that will be set from the
            secret. It must be a valid environment variable name.
        name (str | Unset): Name is optional and when provided is used to reference a secret name where the EnvVar is
            different from what was set as the secret name.
    """

    env_var: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_var = self.env_var

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env_var is not UNSET:
            field_dict["env_var"] = env_var
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        env_var = d.pop("env_var", UNSET)

        name = d.pop("name", UNSET)

        fly_machine_secret = cls(
            env_var=env_var,
            name=name,
        )

        fly_machine_secret.additional_properties = d
        return fly_machine_secret

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
