from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_assignment_type import IPAssignmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignIPRequest")


@_attrs_define
class AssignIPRequest:
    """
    Attributes:
        network (str | Unset): Only for `private_v6`: name of the private network to allocate the Flycast address in.
            Defaults to the organization's default network.
        org_slug (str | Unset): Only for `private_v6`: slug of the organization whose private network the Flycast
            address
            is allocated in, to make the app reachable from that organization. Defaults to the app's
            organization.
        region (str | Unset): Region to scope the address to. Required for egress types. Optional for `v4` and `v6`,
            which default to `global` (announced in all regions). Must be empty or `global` for
            `shared_v4` and `private_v6`.
        service_name (str | Unset): Scope the address to a single service of the app. Not supported for egress types.
        type_ (IPAssignmentType | Unset): Type of IP address to allocate. "egress_pair" allocates both v4 and v6 egress
            IP addresses (recommended when using egress IPs).
    """

    network: str | Unset = UNSET
    org_slug: str | Unset = UNSET
    region: str | Unset = UNSET
    service_name: str | Unset = UNSET
    type_: IPAssignmentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        org_slug = self.org_slug

        region = self.region

        service_name = self.service_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network
        if org_slug is not UNSET:
            field_dict["org_slug"] = org_slug
        if region is not UNSET:
            field_dict["region"] = region
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network = d.pop("network", UNSET)

        org_slug = d.pop("org_slug", UNSET)

        region = d.pop("region", UNSET)

        service_name = d.pop("service_name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: IPAssignmentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IPAssignmentType(_type_)

        assign_ip_request = cls(
            network=network,
            org_slug=org_slug,
            region=region,
            service_name=service_name,
            type_=type_,
        )

        assign_ip_request.additional_properties = d
        return assign_ip_request

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
