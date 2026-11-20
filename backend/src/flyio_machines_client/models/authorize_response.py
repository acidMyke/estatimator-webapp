from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flyio_access import FlyioAccess
    from ..models.root_verified_token import RootVerifiedToken


T = TypeVar("T", bound="AuthorizeResponse")


@_attrs_define
class AuthorizeResponse:
    """
    Attributes:
        access (FlyioAccess | Unset):
        verified_token (RootVerifiedToken | Unset):
    """

    access: FlyioAccess | Unset = UNSET
    verified_token: RootVerifiedToken | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        verified_token: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verified_token, Unset):
            verified_token = self.verified_token.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if verified_token is not UNSET:
            field_dict["verified_token"] = verified_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flyio_access import FlyioAccess
        from ..models.root_verified_token import RootVerifiedToken

        d = dict(src_dict)
        _access = d.pop("access", UNSET)
        access: FlyioAccess | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = FlyioAccess.from_dict(_access)

        _verified_token = d.pop("verified_token", UNSET)
        verified_token: RootVerifiedToken | Unset
        if isinstance(_verified_token, Unset):
            verified_token = UNSET
        else:
            verified_token = RootVerifiedToken.from_dict(_verified_token)

        authorize_response = cls(
            access=access,
            verified_token=verified_token,
        )

        authorize_response.additional_properties = d
        return authorize_response

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
