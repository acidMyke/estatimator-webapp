from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_secret import AppSecret


T = TypeVar("T", bound="AppSecrets")


@_attrs_define
class AppSecrets:
    """
    Attributes:
        secrets (list[AppSecret] | Unset): The app's secrets.
    """

    secrets: list[AppSecret] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_secret import AppSecret

        d = dict(src_dict)
        _secrets = d.pop("secrets", UNSET)
        secrets: list[AppSecret] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = AppSecret.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        app_secrets = cls(
            secrets=secrets,
        )

        app_secrets.additional_properties = d
        return app_secrets

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
