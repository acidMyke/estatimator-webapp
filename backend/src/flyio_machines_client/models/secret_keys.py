from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret_key import SecretKey


T = TypeVar("T", bound="SecretKeys")


@_attrs_define
class SecretKeys:
    """
    Attributes:
        secret_keys (list[SecretKey] | Unset): The app's secret keys. Key material is never returned.
    """

    secret_keys: list[SecretKey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secret_keys, Unset):
            secret_keys = []
            for secret_keys_item_data in self.secret_keys:
                secret_keys_item = secret_keys_item_data.to_dict()
                secret_keys.append(secret_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret_keys is not UNSET:
            field_dict["secret_keys"] = secret_keys

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.secret_key import SecretKey

        d = dict(src_dict)
        _secret_keys = d.pop("secret_keys", UNSET)
        secret_keys: list[SecretKey] | Unset = UNSET
        if _secret_keys is not UNSET:
            secret_keys = []
            for secret_keys_item_data in _secret_keys:
                secret_keys_item = SecretKey.from_dict(secret_keys_item_data)

                secret_keys.append(secret_keys_item)

        secret_keys = cls(
            secret_keys=secret_keys,
        )

        secret_keys.additional_properties = d
        return secret_keys

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
