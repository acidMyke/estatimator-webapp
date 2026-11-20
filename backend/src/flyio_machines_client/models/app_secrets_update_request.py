from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_secrets_update_request_values import AppSecretsUpdateRequestValues


T = TypeVar("T", bound="AppSecretsUpdateRequest")


@_attrs_define
class AppSecretsUpdateRequest:
    """
    Attributes:
        values (AppSecretsUpdateRequestValues | Unset): Secrets to change, keyed by name. A string value sets the
            secret; null deletes it. Names
            may only contain letters, digits, and underscores. Secrets not listed are left alone.
    """

    values: AppSecretsUpdateRequestValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_secrets_update_request_values import (
            AppSecretsUpdateRequestValues,
        )

        d = dict(src_dict)
        _values = d.pop("values", UNSET)
        values: AppSecretsUpdateRequestValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AppSecretsUpdateRequestValues.from_dict(_values)

        app_secrets_update_request = cls(
            values=values,
        )

        app_secrets_update_request.additional_properties = d
        return app_secrets_update_request

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
