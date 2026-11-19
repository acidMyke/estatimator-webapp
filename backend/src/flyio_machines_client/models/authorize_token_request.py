from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.main_token_access import MainTokenAccess


T = TypeVar("T", bound="AuthorizeTokenRequest")


@_attrs_define
class AuthorizeTokenRequest:
    """
    Attributes:
        access (MainTokenAccess | Unset):
        header (str | Unset): Value of the Authorization header to verify, e.g. `FlyV1 fm2_...`.
    """

    access: MainTokenAccess | Unset = UNSET
    header: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        header = self.header

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if header is not UNSET:
            field_dict["header"] = header

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.main_token_access import MainTokenAccess

        d = dict(src_dict)
        _access = d.pop("access", UNSET)
        access: MainTokenAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = MainTokenAccess.from_dict(_access)

        header = d.pop("header", UNSET)

        authorize_token_request = cls(
            access=access,
            header=header,
        )

        authorize_token_request.additional_properties = d
        return authorize_token_request

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
