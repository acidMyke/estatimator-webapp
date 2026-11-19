from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MacaroonNonce")


@_attrs_define
class MacaroonNonce:
    """
    Attributes:
        kid (list[int] | Unset):
        proof (bool | Unset):
        rnd (list[int] | Unset):
    """

    kid: list[int] | Unset = UNSET
    proof: bool | Unset = UNSET
    rnd: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kid: list[int] | Unset = UNSET
        if not isinstance(self.kid, Unset):
            kid = self.kid

        proof = self.proof

        rnd: list[int] | Unset = UNSET
        if not isinstance(self.rnd, Unset):
            rnd = self.rnd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kid is not UNSET:
            field_dict["kid"] = kid
        if proof is not UNSET:
            field_dict["proof"] = proof
        if rnd is not UNSET:
            field_dict["rnd"] = rnd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kid = cast(list[int], d.pop("kid", UNSET))

        proof = d.pop("proof", UNSET)

        rnd = cast(list[int], d.pop("rnd", UNSET))

        macaroon_nonce = cls(
            kid=kid,
            proof=proof,
            rnd=rnd,
        )

        macaroon_nonce.additional_properties = d
        return macaroon_nonce

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
