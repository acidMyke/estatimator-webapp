from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_status import AppStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_organization_info import AppOrganizationInfo


T = TypeVar("T", bound="App")


@_attrs_define
class App:
    """
    Attributes:
        id (str | Unset): Unique ID of the app, as used by Fly.io's GraphQL API.
        internal_numeric_id (int | Unset): Fly.io's internal numeric ID of the app.
        machine_count (int | Unset): Number of the app's Machines that have not been destroyed.
        name (str | Unset): Globally unique name of the app.
        network (str | Unset): Name of the private network the app is attached to: `default` for the organization's
            default network, or the name given when the app was created.
        network_cidr (str | Unset): The /48 IPv6 prefix of the private (6PN) network the app is attached to, such as
            `fdaa:0:1234::/48`. Apps on the same network share it.
        organization (AppOrganizationInfo | Unset):
        status (AppStatus | Unset): State of the app. `pending` until one of its Machines changes state. After that,
            updated
            asynchronously whenever a Machine changes state: `deployed` if at least one Machine is
            started, and `suspended` otherwise.
        volume_count (int | Unset): Number of the app's volumes that have not been destroyed or scheduled for
            destruction.
    """

    id: str | Unset = UNSET
    internal_numeric_id: int | Unset = UNSET
    machine_count: int | Unset = UNSET
    name: str | Unset = UNSET
    network: str | Unset = UNSET
    network_cidr: str | Unset = UNSET
    organization: AppOrganizationInfo | Unset = UNSET
    status: AppStatus | Unset = UNSET
    volume_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        internal_numeric_id = self.internal_numeric_id

        machine_count = self.machine_count

        name = self.name

        network = self.network

        network_cidr = self.network_cidr

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        volume_count = self.volume_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if internal_numeric_id is not UNSET:
            field_dict["internal_numeric_id"] = internal_numeric_id
        if machine_count is not UNSET:
            field_dict["machine_count"] = machine_count
        if name is not UNSET:
            field_dict["name"] = name
        if network is not UNSET:
            field_dict["network"] = network
        if network_cidr is not UNSET:
            field_dict["network_cidr"] = network_cidr
        if organization is not UNSET:
            field_dict["organization"] = organization
        if status is not UNSET:
            field_dict["status"] = status
        if volume_count is not UNSET:
            field_dict["volume_count"] = volume_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_organization_info import AppOrganizationInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        internal_numeric_id = d.pop("internal_numeric_id", UNSET)

        machine_count = d.pop("machine_count", UNSET)

        name = d.pop("name", UNSET)

        network = d.pop("network", UNSET)

        network_cidr = d.pop("network_cidr", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: AppOrganizationInfo | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = AppOrganizationInfo.from_dict(_organization)

        _status = d.pop("status", UNSET)
        status: AppStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppStatus(_status)

        volume_count = d.pop("volume_count", UNSET)

        app = cls(
            id=id,
            internal_numeric_id=internal_numeric_id,
            machine_count=machine_count,
            name=name,
            network=network,
            network_cidr=network_cidr,
            organization=organization,
            status=status,
            volume_count=volume_count,
        )

        app.additional_properties = d
        return app

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
