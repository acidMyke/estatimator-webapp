from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.macaroon_caveat_set import MacaroonCaveatSet
    from ..models.macaroon_nonce import MacaroonNonce


T = TypeVar("T", bound="RootVerifiedToken")


@_attrs_define
class RootVerifiedToken:
    """
    Attributes:
        caveats (MacaroonCaveatSet | Unset):
        header (str | Unset):
        nonce (MacaroonNonce | Unset):
        permission_token (list[int] | Unset):
    """

    caveats: MacaroonCaveatSet | Unset = UNSET
    header: str | Unset = UNSET
    nonce: MacaroonNonce | Unset = UNSET
    permission_token: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caveats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.caveats, Unset):
            caveats = self.caveats.to_dict()

        header = self.header

        nonce: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nonce, Unset):
            nonce = self.nonce.to_dict()

        permission_token: list[int] | Unset = UNSET
        if not isinstance(self.permission_token, Unset):
            permission_token = self.permission_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caveats is not UNSET:
            field_dict["caveats"] = caveats
        if header is not UNSET:
            field_dict["header"] = header
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if permission_token is not UNSET:
            field_dict["permission_token"] = permission_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.macaroon_caveat_set import MacaroonCaveatSet
        from ..models.macaroon_nonce import MacaroonNonce

        d = dict(src_dict)
        _caveats = d.pop("caveats", UNSET)
        caveats: MacaroonCaveatSet | Unset
        if isinstance(_caveats, Unset):
            caveats = UNSET
        else:
            caveats = MacaroonCaveatSet.from_dict(_caveats)

        header = d.pop("header", UNSET)

        _nonce = d.pop("nonce", UNSET)
        nonce: MacaroonNonce | Unset
        if isinstance(_nonce, Unset):
            nonce = UNSET
        else:
            nonce = MacaroonNonce.from_dict(_nonce)

        permission_token = cast(list[int], d.pop("permission_token", UNSET))

        root_verified_token = cls(
            caveats=caveats,
            header=header,
            nonce=nonce,
            permission_token=permission_token,
        )

        root_verified_token.additional_properties = d
        return root_verified_token

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
