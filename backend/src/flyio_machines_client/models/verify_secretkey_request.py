from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifySecretkeyRequest")


@_attrs_define
class VerifySecretkeyRequest:
    """
    Attributes:
        plaintext (str | Unset): Data that was signed, base64-encoded.
        signature (str | Unset): Signature or MAC to check, base64-encoded.
    """

    plaintext: str | Unset = UNSET
    signature: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plaintext = self.plaintext

        signature = self.signature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plaintext is not UNSET:
            field_dict["plaintext"] = plaintext
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        plaintext = d.pop("plaintext", UNSET)

        signature = d.pop("signature", UNSET)

        verify_secretkey_request = cls(
            plaintext=plaintext,
            signature=signature,
        )

        verify_secretkey_request.additional_properties = d
        return verify_secretkey_request

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
