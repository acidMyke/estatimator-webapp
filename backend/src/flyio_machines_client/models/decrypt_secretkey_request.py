from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecryptSecretkeyRequest")


@_attrs_define
class DecryptSecretkeyRequest:
    """
    Attributes:
        associated_data (str | Unset): Additional data passed when encrypting, base64-encoded.
        ciphertext (str | Unset): Data to decrypt, as returned by the encrypt endpoint, base64-encoded.
    """

    associated_data: str | Unset = UNSET
    ciphertext: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_data = self.associated_data

        ciphertext = self.ciphertext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_data is not UNSET:
            field_dict["associated_data"] = associated_data
        if ciphertext is not UNSET:
            field_dict["ciphertext"] = ciphertext

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        associated_data = d.pop("associated_data", UNSET)

        ciphertext = d.pop("ciphertext", UNSET)

        decrypt_secretkey_request = cls(
            associated_data=associated_data,
            ciphertext=ciphertext,
        )

        decrypt_secretkey_request.additional_properties = d
        return decrypt_secretkey_request

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
