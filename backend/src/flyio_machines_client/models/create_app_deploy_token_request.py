from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAppDeployTokenRequest")


@_attrs_define
class CreateAppDeployTokenRequest:
    """
    Attributes:
        expiry (str | Unset): How long the token is valid, as a Go duration string such as `720h`. If omitted, the
            token is valid for as long as the token used to make this request.
    """

    expiry: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry = self.expiry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry is not UNSET:
            field_dict["expiry"] = expiry

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        expiry = d.pop("expiry", UNSET)

        create_app_deploy_token_request = cls(
            expiry=expiry,
        )

        create_app_deploy_token_request.additional_properties = d
        return create_app_deploy_token_request

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
