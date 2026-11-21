from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_challenge import AcmeChallenge
    from ..models.ownership_verification import OwnershipVerification


T = TypeVar("T", bound="DNSRequirements")


@_attrs_define
class DNSRequirements:
    """
    Attributes:
        a (list[str] | Unset): IPv4 addresses the hostname's A records can point to: the app's global IPv4 addresses
            and its shared IPv4 address.
        aaaa (list[str] | Unset): IPv6 addresses the hostname's AAAA records can point to: the app's global IPv6
            addresses.
        acme_challenge (AcmeChallenge | Unset):
        cname (str | Unset): Target the hostname can CNAME to instead of using A and AAAA records.
        ownership (OwnershipVerification | Unset):
    """

    a: list[str] | Unset = UNSET
    aaaa: list[str] | Unset = UNSET
    acme_challenge: AcmeChallenge | Unset = UNSET
    cname: str | Unset = UNSET
    ownership: OwnershipVerification | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a: list[str] | Unset = UNSET
        if not isinstance(self.a, Unset):
            a = self.a

        aaaa: list[str] | Unset = UNSET
        if not isinstance(self.aaaa, Unset):
            aaaa = self.aaaa

        acme_challenge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acme_challenge, Unset):
            acme_challenge = self.acme_challenge.to_dict()

        cname = self.cname

        ownership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ownership, Unset):
            ownership = self.ownership.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if aaaa is not UNSET:
            field_dict["aaaa"] = aaaa
        if acme_challenge is not UNSET:
            field_dict["acme_challenge"] = acme_challenge
        if cname is not UNSET:
            field_dict["cname"] = cname
        if ownership is not UNSET:
            field_dict["ownership"] = ownership

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.acme_challenge import AcmeChallenge
        from ..models.ownership_verification import OwnershipVerification

        d = dict(src_dict)
        a = cast(list[str], d.pop("a", UNSET))

        aaaa = cast(list[str], d.pop("aaaa", UNSET))

        _acme_challenge = d.pop("acme_challenge", UNSET)
        acme_challenge: AcmeChallenge | Unset
        if isinstance(_acme_challenge, Unset):
            acme_challenge = UNSET
        else:
            acme_challenge = AcmeChallenge.from_dict(_acme_challenge)

        cname = d.pop("cname", UNSET)

        _ownership = d.pop("ownership", UNSET)
        ownership: OwnershipVerification | Unset
        if isinstance(_ownership, Unset):
            ownership = UNSET
        else:
            ownership = OwnershipVerification.from_dict(_ownership)

        dns_requirements = cls(
            a=a,
            aaaa=aaaa,
            acme_challenge=acme_challenge,
            cname=cname,
            ownership=ownership,
        )

        dns_requirements.additional_properties = d
        return dns_requirements

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
