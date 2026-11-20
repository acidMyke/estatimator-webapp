from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_env_from_field_ref import FlyEnvFromFieldRef
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyEnvFrom")


@_attrs_define
class FlyEnvFrom:
    """EnvVar defines an environment variable to be populated from a machine field, env_var

    Attributes:
        env_var (str | Unset): EnvVar is required and is the name of the environment variable that will be set from the
            secret. It must be a valid environment variable name.
        field_ref (FlyEnvFromFieldRef | Unset): FieldRef selects a field of the Machine: supports id, version, app_name,
            private_ip, region, image.
    """

    env_var: str | Unset = UNSET
    field_ref: FlyEnvFromFieldRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_var = self.env_var

        field_ref: str | Unset = UNSET
        if not isinstance(self.field_ref, Unset):
            field_ref = self.field_ref.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env_var is not UNSET:
            field_dict["env_var"] = env_var
        if field_ref is not UNSET:
            field_dict["field_ref"] = field_ref

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        env_var = d.pop("env_var", UNSET)

        _field_ref = d.pop("field_ref", UNSET)
        field_ref: FlyEnvFromFieldRef | Unset
        if isinstance(_field_ref, Unset):
            field_ref = UNSET
        else:
            field_ref = FlyEnvFromFieldRef(_field_ref)

        fly_env_from = cls(
            env_var=env_var,
            field_ref=field_ref,
        )

        fly_env_from.additional_properties = d
        return fly_env_from

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
