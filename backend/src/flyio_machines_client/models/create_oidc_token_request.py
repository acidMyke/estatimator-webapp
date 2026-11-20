from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOIDCTokenRequest")


@_attrs_define
class CreateOIDCTokenRequest:
    """Optional parameters

    Attributes:
        aud (str | Unset): Value of the token's `aud` claim. Defaults to `https://fly.io/<org-slug>`. Example:
            https://fly.io/org-slug.
        aws_principal_tags (bool | Unset): Add AWS principal tag claims
            (`https://aws.amazon.com/tags/principal_tags/<tag>`) for use
            with AWS IAM: FlyAppName, FlyOrgSlug, FlyOrgId, FlyMachineName and FlyRegion.
    """

    aud: str | Unset = UNSET
    aws_principal_tags: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aud = self.aud

        aws_principal_tags = self.aws_principal_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aud is not UNSET:
            field_dict["aud"] = aud
        if aws_principal_tags is not UNSET:
            field_dict["aws_principal_tags"] = aws_principal_tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        aud = d.pop("aud", UNSET)

        aws_principal_tags = d.pop("aws_principal_tags", UNSET)

        create_oidc_token_request = cls(
            aud=aud,
            aws_principal_tags=aws_principal_tags,
        )

        create_oidc_token_request.additional_properties = d
        return create_oidc_token_request

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
