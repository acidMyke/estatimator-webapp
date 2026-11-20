from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_assignment_network import IPAssignmentNetwork
    from ..models.ip_pair import IPPair


T = TypeVar("T", bound="AssignIPResponse")


@_attrs_define
class AssignIPResponse:
    """
    Attributes:
        created_at (str | Unset): When the address was assigned to the app, in RFC 3339 format.
        egress (bool | Unset): Whether this is an egress address.
        ip (str | Unset): The allocated IP address. Null for `egress_pair`; see `ip_pair`.
        ip_pair (IPPair | Unset):
        network (IPAssignmentNetwork | Unset): The 6PN network a Flycast (private_v6) address belongs to. Null for all
            other IP types.
        region (str | Unset): Region the address is scoped to, or `global` for addresses announced in all regions.
        service_name (str | Unset): Name of the service the address is scoped to, if any.
        shared (bool | Unset): Whether this is the app's shared IPv4 address.
    """

    created_at: str | Unset = UNSET
    egress: bool | Unset = UNSET
    ip: str | Unset = UNSET
    ip_pair: IPPair | Unset = UNSET
    network: IPAssignmentNetwork | Unset = UNSET
    region: str | Unset = UNSET
    service_name: str | Unset = UNSET
    shared: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        egress = self.egress

        ip = self.ip

        ip_pair: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_pair, Unset):
            ip_pair = self.ip_pair.to_dict()

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        region = self.region

        service_name = self.service_name

        shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if egress is not UNSET:
            field_dict["egress"] = egress
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ip_pair is not UNSET:
            field_dict["ip_pair"] = ip_pair
        if network is not UNSET:
            field_dict["network"] = network
        if region is not UNSET:
            field_dict["region"] = region
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_assignment_network import IPAssignmentNetwork
        from ..models.ip_pair import IPPair

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        egress = d.pop("egress", UNSET)

        ip = d.pop("ip", UNSET)

        _ip_pair = d.pop("ip_pair", UNSET)
        ip_pair: IPPair | Unset
        if isinstance(_ip_pair, Unset):
            ip_pair = UNSET
        else:
            ip_pair = IPPair.from_dict(_ip_pair)

        _network = d.pop("network", UNSET)
        network: IPAssignmentNetwork | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = IPAssignmentNetwork.from_dict(_network)

        region = d.pop("region", UNSET)

        service_name = d.pop("service_name", UNSET)

        shared = d.pop("shared", UNSET)

        assign_ip_response = cls(
            created_at=created_at,
            egress=egress,
            ip=ip,
            ip_pair=ip_pair,
            network=network,
            region=region,
            service_name=service_name,
            shared=shared,
        )

        assign_ip_response.additional_properties = d
        return assign_ip_response

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
