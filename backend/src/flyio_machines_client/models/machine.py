from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.machine_host_status import MachineHostStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_status import CheckStatus
    from ..models.fly_machine_config import FlyMachineConfig
    from ..models.image_ref import ImageRef
    from ..models.machine_event import MachineEvent
    from ..models.stripped_lease import StrippedLease


T = TypeVar("T", bound="Machine")


@_attrs_define
class Machine:
    """
    Attributes:
        checks (list[CheckStatus] | Unset): Status of each health check: the Machine's top-level `checks` and its
            services'
            checks.
        config (FlyMachineConfig | Unset):
        cordoned (bool | Unset): Whether the Machine is cordoned, meaning Fly Proxy does not route requests to it. See
            the Cordon Machine endpoint.
        created_at (str | Unset): When the Machine was created.
        events (list[MachineEvent] | Unset): Up to 5 of the most recent events of the current Machine version, newest
            first. Use
            the List Events endpoint for more.
        host_features (list[str] | Unset): Features of the Machine's host, for comparison with
            `config.guest.required_host_features`.
            Only returned when the request sets the `fly-include-host-features: true` header.
        host_status (MachineHostStatus | Unset): Whether Fly.io could reach the Machine's host: `ok` if it could,
            `unreachable` if it
            could not, in which case the response is built from last known state. `unknown` if the
            host's status was not reported.
        id (str | Unset): Unique ID of the Machine.
        image_ref (ImageRef | Unset):
        incomplete_config (FlyMachineConfig | Unset):
        instance_id (str | Unset): Same value as `version`.

            Deprecated: use `version`.
        lease (StrippedLease | Unset):
        name (str | Unset): Name of the Machine. Generated when not provided at creation. Names are not required
            to be unique.
        nonce (str | Unset): Nonce of the lease acquired on the Machine at creation. Only returned when creating a
            Machine with `lease_ttl` set. Pass it in the `fly-machine-lease-nonce` header to act on
            the Machine while the lease is held.
        private_ip (str | Unset): The Machine's address on the organization's private (6PN) IPv6 network.
        region (str | Unset): Code of the region the Machine runs in, such as `iad`.
        state (str | Unset): Current state of the Machine, taken from the status of its most recent event. One of
            `created`, `starting`, `started`, `stopping`, `stopped`, `suspending`, `suspended`,
            `replacing`, `replaced`, `destroying`, `destroyed`, `failed`, `migrating`, `migrated`,
            `archived`, or `pending`. See https://fly.io/docs/machines/machine-states/.
        updated_at (str | Unset): Time of the Machine's most recent event, truncated to whole seconds. The zero time
            (0001-01-01T00:00:00Z) if the host could not be reached. With `summary=true`, the time
            Fly.io last recorded a change to the Machine.
        version (str | Unset): Unique ID of this version of the Machine. Every update creates a new version. Pass it
            as `current_version` when updating the Machine to reject the update if the Machine has
            changed since this version.
    """

    checks: list[CheckStatus] | Unset = UNSET
    config: FlyMachineConfig | Unset = UNSET
    cordoned: bool | Unset = UNSET
    created_at: str | Unset = UNSET
    events: list[MachineEvent] | Unset = UNSET
    host_features: list[str] | Unset = UNSET
    host_status: MachineHostStatus | Unset = UNSET
    id: str | Unset = UNSET
    image_ref: ImageRef | Unset = UNSET
    incomplete_config: FlyMachineConfig | Unset = UNSET
    instance_id: str | Unset = UNSET
    lease: StrippedLease | Unset = UNSET
    name: str | Unset = UNSET
    nonce: str | Unset = UNSET
    private_ip: str | Unset = UNSET
    region: str | Unset = UNSET
    state: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        cordoned = self.cordoned

        created_at = self.created_at

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        host_features: list[str] | Unset = UNSET
        if not isinstance(self.host_features, Unset):
            host_features = self.host_features

        host_status: str | Unset = UNSET
        if not isinstance(self.host_status, Unset):
            host_status = self.host_status.value

        id = self.id

        image_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_ref, Unset):
            image_ref = self.image_ref.to_dict()

        incomplete_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incomplete_config, Unset):
            incomplete_config = self.incomplete_config.to_dict()

        instance_id = self.instance_id

        lease: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lease, Unset):
            lease = self.lease.to_dict()

        name = self.name

        nonce = self.nonce

        private_ip = self.private_ip

        region = self.region

        state = self.state

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checks is not UNSET:
            field_dict["checks"] = checks
        if config is not UNSET:
            field_dict["config"] = config
        if cordoned is not UNSET:
            field_dict["cordoned"] = cordoned
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if events is not UNSET:
            field_dict["events"] = events
        if host_features is not UNSET:
            field_dict["host_features"] = host_features
        if host_status is not UNSET:
            field_dict["host_status"] = host_status
        if id is not UNSET:
            field_dict["id"] = id
        if image_ref is not UNSET:
            field_dict["image_ref"] = image_ref
        if incomplete_config is not UNSET:
            field_dict["incomplete_config"] = incomplete_config
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if lease is not UNSET:
            field_dict["lease"] = lease
        if name is not UNSET:
            field_dict["name"] = name
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
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
        from ..models.check_status import CheckStatus
        from ..models.fly_machine_config import FlyMachineConfig
        from ..models.image_ref import ImageRef
        from ..models.machine_event import MachineEvent
        from ..models.stripped_lease import StrippedLease

        d = dict(src_dict)
        _checks = d.pop("checks", UNSET)
        checks: list[CheckStatus] | Unset = UNSET
        if _checks is not UNSET:
            checks = []
            for checks_item_data in _checks:
                checks_item = CheckStatus.from_dict(checks_item_data)

                checks.append(checks_item)

        _config = d.pop("config", UNSET)
        config: FlyMachineConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = FlyMachineConfig.from_dict(_config)

        cordoned = d.pop("cordoned", UNSET)

        created_at = d.pop("created_at", UNSET)

        _events = d.pop("events", UNSET)
        events: list[MachineEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = MachineEvent.from_dict(events_item_data)

                events.append(events_item)

        host_features = cast(list[str], d.pop("host_features", UNSET))

        _host_status = d.pop("host_status", UNSET)
        host_status: MachineHostStatus | Unset
        if isinstance(_host_status, Unset):
            host_status = UNSET
        else:
            host_status = MachineHostStatus(_host_status)

        id = d.pop("id", UNSET)

        _image_ref = d.pop("image_ref", UNSET)
        image_ref: ImageRef | Unset
        if isinstance(_image_ref, Unset):
            image_ref = UNSET
        else:
            image_ref = ImageRef.from_dict(_image_ref)

        _incomplete_config = d.pop("incomplete_config", UNSET)
        incomplete_config: FlyMachineConfig | Unset
        if isinstance(_incomplete_config, Unset):
            incomplete_config = UNSET
        else:
            incomplete_config = FlyMachineConfig.from_dict(_incomplete_config)

        instance_id = d.pop("instance_id", UNSET)

        _lease = d.pop("lease", UNSET)
        lease: StrippedLease | Unset
        if isinstance(_lease, Unset):
            lease = UNSET
        else:
            lease = StrippedLease.from_dict(_lease)

        name = d.pop("name", UNSET)

        nonce = d.pop("nonce", UNSET)

        private_ip = d.pop("private_ip", UNSET)

        region = d.pop("region", UNSET)

        state = d.pop("state", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        machine = cls(
            checks=checks,
            config=config,
            cordoned=cordoned,
            created_at=created_at,
            events=events,
            host_features=host_features,
            host_status=host_status,
            id=id,
            image_ref=image_ref,
            incomplete_config=incomplete_config,
            instance_id=instance_id,
            lease=lease,
            name=name,
            nonce=nonce,
            private_ip=private_ip,
            region=region,
            state=state,
            updated_at=updated_at,
            version=version,
        )

        machine.additional_properties = d
        return machine

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
