from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetSecretkeyRequest")


@_attrs_define
class SetSecretkeyRequest:
    """
    Attributes:
        type_ (str | Unset): Type of the key: `hs256`, `hs384`, `hs512`, `xaes256gcm`, `nacl_auth`, `nacl_box`,
            `nacl_secretbox`, `nacl_sign`, or `es256`. Required.
        value (str | Unset): Key material, base64-encoded. Ignored when generating a key.
    """

    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        set_secretkey_request = cls(
            type_=type_,
            value=value,
        )

        set_secretkey_request.additional_properties = d
        return set_secretkey_request

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
