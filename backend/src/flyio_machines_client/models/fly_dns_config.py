from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_dns_forward_rule import FlyDnsForwardRule
    from ..models.fly_dns_option import FlyDnsOption


T = TypeVar("T", bound="FlyDNSConfig")


@_attrs_define
class FlyDNSConfig:
    """
    Attributes:
        dns_forward_rules (list[FlyDnsForwardRule] | Unset): Forward DNS queries for some domains to other DNS servers
        hostname (str | Unset): Hostname of the Machine. Defaults to the Machine ID. Also added to /etc/hosts with the
            Machine's 6PN address
        hostname_fqdn (str | Unset): Fully qualified domain name added to /etc/hosts for `hostname`
        nameservers (list[str] | Unset): Nameservers to use instead of the default, Fly.io's private DNS server
            `fdaa::3`
        options (list[FlyDnsOption] | Unset): Options for /etc/resolv.conf
        searches (list[str] | Unset): Search domains for /etc/resolv.conf
        skip_registration (bool | Unset): Currently has no effect
    """

    dns_forward_rules: list[FlyDnsForwardRule] | Unset = UNSET
    hostname: str | Unset = UNSET
    hostname_fqdn: str | Unset = UNSET
    nameservers: list[str] | Unset = UNSET
    options: list[FlyDnsOption] | Unset = UNSET
    searches: list[str] | Unset = UNSET
    skip_registration: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns_forward_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_forward_rules, Unset):
            dns_forward_rules = []
            for dns_forward_rules_item_data in self.dns_forward_rules:
                dns_forward_rules_item = dns_forward_rules_item_data.to_dict()
                dns_forward_rules.append(dns_forward_rules_item)

        hostname = self.hostname

        hostname_fqdn = self.hostname_fqdn

        nameservers: list[str] | Unset = UNSET
        if not isinstance(self.nameservers, Unset):
            nameservers = self.nameservers

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        searches: list[str] | Unset = UNSET
        if not isinstance(self.searches, Unset):
            searches = self.searches

        skip_registration = self.skip_registration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dns_forward_rules is not UNSET:
            field_dict["dns_forward_rules"] = dns_forward_rules
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if hostname_fqdn is not UNSET:
            field_dict["hostname_fqdn"] = hostname_fqdn
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers
        if options is not UNSET:
            field_dict["options"] = options
        if searches is not UNSET:
            field_dict["searches"] = searches
        if skip_registration is not UNSET:
            field_dict["skip_registration"] = skip_registration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_dns_forward_rule import FlyDnsForwardRule
        from ..models.fly_dns_option import FlyDnsOption

        d = dict(src_dict)
        _dns_forward_rules = d.pop("dns_forward_rules", UNSET)
        dns_forward_rules: list[FlyDnsForwardRule] | Unset = UNSET
        if _dns_forward_rules is not UNSET:
            dns_forward_rules = []
            for dns_forward_rules_item_data in _dns_forward_rules:
                dns_forward_rules_item = FlyDnsForwardRule.from_dict(
                    dns_forward_rules_item_data
                )

                dns_forward_rules.append(dns_forward_rules_item)

        hostname = d.pop("hostname", UNSET)

        hostname_fqdn = d.pop("hostname_fqdn", UNSET)

        nameservers = cast(list[str], d.pop("nameservers", UNSET))

        _options = d.pop("options", UNSET)
        options: list[FlyDnsOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = FlyDnsOption.from_dict(options_item_data)

                options.append(options_item)

        searches = cast(list[str], d.pop("searches", UNSET))

        skip_registration = d.pop("skip_registration", UNSET)

        fly_dns_config = cls(
            dns_forward_rules=dns_forward_rules,
            hostname=hostname,
            hostname_fqdn=hostname_fqdn,
            nameservers=nameservers,
            options=options,
            searches=searches,
            skip_registration=skip_registration,
        )

        fly_dns_config.additional_properties = d
        return fly_dns_config

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
