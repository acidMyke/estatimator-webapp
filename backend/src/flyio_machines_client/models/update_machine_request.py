from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_config import FlyMachineConfig


T = TypeVar("T", bound="UpdateMachineRequest")


@_attrs_define
class UpdateMachineRequest:
    """
    Attributes:
        config (FlyMachineConfig | Unset):
        current_version (str | Unset): Optional optimistic-concurrency guard: the Machine's `version`, as returned by
            create,
            get or a previous update. When set and it is no longer the Machine's current version,
            the update is rejected with 409 Conflict and nothing changes. Omit it to update
            unconditionally.
        lease_ttl (int | Unset): Ignored. Use the lease endpoints to lease an existing Machine.
        min_secrets_version (int | Unset): The minimum version of the app's secrets the Machine must run with. Set it to
            the `version`
            returned by the endpoints that set or delete app secrets, so that the Machine is guaranteed
            to see those changes. This field belongs at the top level of the request body, not in
            `config`. If omitted, the app's current secrets version is looked up for you.
        name (str | Unset): Ignored.
        region (str | Unset): Not used to place the Machine: an update never moves it to another region or host.
        skip_launch (bool | Unset): Apply the update without starting the Machine. It ends up `stopped`; start it with
            the
            Start Machine endpoint. Not allowed for spot Machines.
        skip_secrets (bool | Unset): Don't look up the app's current secrets version. The Machine still gets the app's
            secrets, but may not see recent changes to them. Takes precedence over
            `min_secrets_version`.
        skip_service_registration (bool | Unset): Ignored. Use the cordon and uncordon endpoints instead.
    """

    config: FlyMachineConfig | Unset = UNSET
    current_version: str | Unset = UNSET
    lease_ttl: int | Unset = UNSET
    min_secrets_version: int | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    skip_launch: bool | Unset = UNSET
    skip_secrets: bool | Unset = UNSET
    skip_service_registration: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        current_version = self.current_version

        lease_ttl = self.lease_ttl

        min_secrets_version = self.min_secrets_version

        name = self.name

        region = self.region

        skip_launch = self.skip_launch

        skip_secrets = self.skip_secrets

        skip_service_registration = self.skip_service_registration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if lease_ttl is not UNSET:
            field_dict["lease_ttl"] = lease_ttl
        if min_secrets_version is not UNSET:
            field_dict["min_secrets_version"] = min_secrets_version
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if skip_launch is not UNSET:
            field_dict["skip_launch"] = skip_launch
        if skip_secrets is not UNSET:
            field_dict["skip_secrets"] = skip_secrets
        if skip_service_registration is not UNSET:
            field_dict["skip_service_registration"] = skip_service_registration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_config import FlyMachineConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: FlyMachineConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = FlyMachineConfig.from_dict(_config)

        current_version = d.pop("current_version", UNSET)

        lease_ttl = d.pop("lease_ttl", UNSET)

        min_secrets_version = d.pop("min_secrets_version", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        skip_launch = d.pop("skip_launch", UNSET)

        skip_secrets = d.pop("skip_secrets", UNSET)

        skip_service_registration = d.pop("skip_service_registration", UNSET)

        update_machine_request = cls(
            config=config,
            current_version=current_version,
            lease_ttl=lease_ttl,
            min_secrets_version=min_secrets_version,
            name=name,
            region=region,
            skip_launch=skip_launch,
            skip_secrets=skip_secrets,
            skip_service_registration=skip_service_registration,
        )

        update_machine_request.additional_properties = d
        return update_machine_request

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
