from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_machine_service_autostop import FlyMachineServiceAutostop
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_port import FlyMachinePort
    from ..models.fly_machine_service_check import FlyMachineServiceCheck
    from ..models.fly_machine_service_concurrency import FlyMachineServiceConcurrency


T = TypeVar("T", bound="FlyMachineService")


@_attrs_define
class FlyMachineService:
    """
    Attributes:
        autostart (bool | Unset): Whether Fly Proxy starts stopped or suspended Machines when requests arrive. Defaults
            to true
        autostop (FlyMachineServiceAutostop | Unset): Accepts a string (new format) or a boolean (old format). For
            backward compatibility with older clients, the API continues to use booleans for "off" and "stop" in responses.
            * "off" or false - Do not autostop the Machine.
            * "stop" or true - Automatically stop the Machine.
            * "suspend" - Automatically suspend the Machine, falling back to a full stop if this is not possible.
        checks (list[FlyMachineServiceCheck] | Unset): An optional list of service checks
        concurrency (FlyMachineServiceConcurrency | Unset):
        force_instance_description (str | Unset): Currently has no effect
        force_instance_key (str | Unset): Currently has no effect
        internal_port (int | Unset): Port in the Machine that Fly Proxy forwards traffic to. Defaults to 8080
        min_machines_running (int | Unset): When autostop is on, the number of Machines Fly Proxy keeps running in the
            app's primary
            region (`PRIMARY_REGION` env var). Machines in other regions can all be stopped
        ports (list[FlyMachinePort] | Unset): Public ports that Fly Proxy accepts traffic on
        protocol (str | Unset): Protocol: tcp or udp. Defaults to tcp
    """

    autostart: bool | Unset = UNSET
    autostop: FlyMachineServiceAutostop | Unset = UNSET
    checks: list[FlyMachineServiceCheck] | Unset = UNSET
    concurrency: FlyMachineServiceConcurrency | Unset = UNSET
    force_instance_description: str | Unset = UNSET
    force_instance_key: str | Unset = UNSET
    internal_port: int | Unset = UNSET
    min_machines_running: int | Unset = UNSET
    ports: list[FlyMachinePort] | Unset = UNSET
    protocol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        autostart = self.autostart

        autostop: str | Unset = UNSET
        if not isinstance(self.autostop, Unset):
            autostop = self.autostop.value

        checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)

        concurrency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.concurrency, Unset):
            concurrency = self.concurrency.to_dict()

        force_instance_description = self.force_instance_description

        force_instance_key = self.force_instance_key

        internal_port = self.internal_port

        min_machines_running = self.min_machines_running

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autostart is not UNSET:
            field_dict["autostart"] = autostart
        if autostop is not UNSET:
            field_dict["autostop"] = autostop
        if checks is not UNSET:
            field_dict["checks"] = checks
        if concurrency is not UNSET:
            field_dict["concurrency"] = concurrency
        if force_instance_description is not UNSET:
            field_dict["force_instance_description"] = force_instance_description
        if force_instance_key is not UNSET:
            field_dict["force_instance_key"] = force_instance_key
        if internal_port is not UNSET:
            field_dict["internal_port"] = internal_port
        if min_machines_running is not UNSET:
            field_dict["min_machines_running"] = min_machines_running
        if ports is not UNSET:
            field_dict["ports"] = ports
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_port import FlyMachinePort
        from ..models.fly_machine_service_check import FlyMachineServiceCheck
        from ..models.fly_machine_service_concurrency import (
            FlyMachineServiceConcurrency,
        )

        d = dict(src_dict)
        autostart = d.pop("autostart", UNSET)

        _autostop = d.pop("autostop", UNSET)
        autostop: FlyMachineServiceAutostop | Unset
        if isinstance(_autostop, Unset):
            autostop = UNSET
        else:
            autostop = FlyMachineServiceAutostop(_autostop)

        _checks = d.pop("checks", UNSET)
        checks: list[FlyMachineServiceCheck] | Unset = UNSET
        if _checks is not UNSET:
            checks = []
            for checks_item_data in _checks:
                checks_item = FlyMachineServiceCheck.from_dict(checks_item_data)

                checks.append(checks_item)

        _concurrency = d.pop("concurrency", UNSET)
        concurrency: FlyMachineServiceConcurrency | Unset
        if isinstance(_concurrency, Unset):
            concurrency = UNSET
        else:
            concurrency = FlyMachineServiceConcurrency.from_dict(_concurrency)

        force_instance_description = d.pop("force_instance_description", UNSET)

        force_instance_key = d.pop("force_instance_key", UNSET)

        internal_port = d.pop("internal_port", UNSET)

        min_machines_running = d.pop("min_machines_running", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[FlyMachinePort] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = FlyMachinePort.from_dict(ports_item_data)

                ports.append(ports_item)

        protocol = d.pop("protocol", UNSET)

        fly_machine_service = cls(
            autostart=autostart,
            autostop=autostop,
            checks=checks,
            concurrency=concurrency,
            force_instance_description=force_instance_description,
            force_instance_key=force_instance_key,
            internal_port=internal_port,
            min_machines_running=min_machines_running,
            ports=ports,
            protocol=protocol,
        )

        fly_machine_service.additional_properties = d
        return fly_machine_service

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
