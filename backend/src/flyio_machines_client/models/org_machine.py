from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_overview_config import MachineOverviewConfig


T = TypeVar("T", bound="OrgMachine")


@_attrs_define
class OrgMachine:
    """
    Attributes:
        app_name (str | Unset): Name of the app the Machine belongs to.
        config (MachineOverviewConfig | Unset):
        created_at (str | Unset): When the Machine was created.
        id (str | Unset): Unique ID of the Machine.
        name (str | Unset): Name of the Machine.
        private_ip (str | Unset): The Machine's address on the organization's private (6PN) IPv6 network.
        region (str | Unset): Code of the region the Machine runs in.
        state (str | Unset): Current state of the Machine; see the `state` field of Machine.
        updated_at (str | Unset): When Fly.io last recorded a change to the Machine.
        version (str | Unset): ID of the Machine's current version.
    """

    app_name: str | Unset = UNSET
    config: MachineOverviewConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    private_ip: str | Unset = UNSET
    region: str | Unset = UNSET
    state: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        created_at = self.created_at

        id = self.id

        name = self.name

        private_ip = self.private_ip

        region = self.region

        state = self.state

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if config is not UNSET:
            field_dict["config"] = config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if private_ip is not UNSET:
            field_dict["private_ip"] = private_ip
        if region is not UNSET:
            field_dict["region"] = region
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.machine_overview_config import MachineOverviewConfig

        d = dict(src_dict)
        app_name = d.pop("app_name", UNSET)

        _config = d.pop("config", UNSET)
        config: MachineOverviewConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = MachineOverviewConfig.from_dict(_config)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        private_ip = d.pop("private_ip", UNSET)

        region = d.pop("region", UNSET)

        state = d.pop("state", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        org_machine = cls(
            app_name=app_name,
            config=config,
            created_at=created_at,
            id=id,
            name=name,
            private_ip=private_ip,
            region=region,
            state=state,
            updated_at=updated_at,
            version=version,
        )

        org_machine.additional_properties = d
        return org_machine

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
