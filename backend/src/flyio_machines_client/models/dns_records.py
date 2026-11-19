from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSRecords")


@_attrs_define
class DNSRecords:
    """
    Attributes:
        a (list[str] | Unset): A records found for the hostname.
        aaaa (list[str] | Unset): AAAA records found for the hostname.
        acme_challenge_cname (str | Unset): Target of the `_acme-challenge` CNAME record, if found.
        cname (list[str] | Unset): CNAME records found for the hostname.
        ownership_txt (str | Unset): Value of the `_fly-ownership` TXT record, if found.
        resolved_addresses (list[str] | Unset): All addresses the hostname resolved to, after following CNAMEs.
        soa (str | Unset): Primary name server from the SOA record of the hostname's zone.
    """

    a: list[str] | Unset = UNSET
    aaaa: list[str] | Unset = UNSET
    acme_challenge_cname: str | Unset = UNSET
    cname: list[str] | Unset = UNSET
    ownership_txt: str | Unset = UNSET
    resolved_addresses: list[str] | Unset = UNSET
    soa: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a: list[str] | Unset = UNSET
        if not isinstance(self.a, Unset):
            a = self.a

        aaaa: list[str] | Unset = UNSET
        if not isinstance(self.aaaa, Unset):
            aaaa = self.aaaa

        acme_challenge_cname = self.acme_challenge_cname

        cname: list[str] | Unset = UNSET
        if not isinstance(self.cname, Unset):
            cname = self.cname

        ownership_txt = self.ownership_txt

        resolved_addresses: list[str] | Unset = UNSET
        if not isinstance(self.resolved_addresses, Unset):
            resolved_addresses = self.resolved_addresses

        soa = self.soa

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if aaaa is not UNSET:
            field_dict["aaaa"] = aaaa
        if acme_challenge_cname is not UNSET:
            field_dict["acme_challenge_cname"] = acme_challenge_cname
        if cname is not UNSET:
            field_dict["cname"] = cname
        if ownership_txt is not UNSET:
            field_dict["ownership_txt"] = ownership_txt
        if resolved_addresses is not UNSET:
            field_dict["resolved_addresses"] = resolved_addresses
        if soa is not UNSET:
            field_dict["soa"] = soa

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        a = cast(list[str], d.pop("a", UNSET))

        aaaa = cast(list[str], d.pop("aaaa", UNSET))

        acme_challenge_cname = d.pop("acme_challenge_cname", UNSET)

        cname = cast(list[str], d.pop("cname", UNSET))

        ownership_txt = d.pop("ownership_txt", UNSET)

        resolved_addresses = cast(list[str], d.pop("resolved_addresses", UNSET))

        soa = d.pop("soa", UNSET)

        dns_records = cls(
            a=a,
            aaaa=aaaa,
            acme_challenge_cname=acme_challenge_cname,
            cname=cname,
            ownership_txt=ownership_txt,
            resolved_addresses=resolved_addresses,
            soa=soa,
        )

        dns_records.additional_properties = d
        return dns_records

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
