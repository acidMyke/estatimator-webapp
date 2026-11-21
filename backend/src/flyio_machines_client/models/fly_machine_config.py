from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_container_config import FlyContainerConfig
    from ..models.fly_dns_config import FlyDNSConfig
    from ..models.fly_file import FlyFile
    from ..models.fly_machine_cache_drive import FlyMachineCacheDrive
    from ..models.fly_machine_config_checks import FlyMachineConfigChecks
    from ..models.fly_machine_config_env import FlyMachineConfigEnv
    from ..models.fly_machine_config_metadata import FlyMachineConfigMetadata
    from ..models.fly_machine_guest import FlyMachineGuest
    from ..models.fly_machine_init import FlyMachineInit
    from ..models.fly_machine_metrics import FlyMachineMetrics
    from ..models.fly_machine_mount import FlyMachineMount
    from ..models.fly_machine_process import FlyMachineProcess
    from ..models.fly_machine_restart import FlyMachineRestart
    from ..models.fly_machine_rootfs import FlyMachineRootfs
    from ..models.fly_machine_service import FlyMachineService
    from ..models.fly_machine_spot import FlyMachineSpot
    from ..models.fly_static import FlyStatic
    from ..models.fly_stop_config import FlyStopConfig


T = TypeVar("T", bound="FlyMachineConfig")


@_attrs_define
class FlyMachineConfig:
    """
    Attributes:
        auto_destroy (bool | Unset): Optional boolean telling the Machine to destroy itself once it’s complete (default
            false)
        cache_disk (FlyMachineCacheDrive | Unset):
        checks (FlyMachineConfigChecks | Unset): An optional object that defines one or more named top-level checks. The
            key for each check is the check name.
        containers (list[FlyContainerConfig] | Unset): Containers are a list of containers that will run in the machine,
            each from its own image.
        disable_machine_autostart (bool | Unset): Deprecated: use Service.Autostart instead
        dns (FlyDNSConfig | Unset):
        env (FlyMachineConfigEnv | Unset): An object filled with key/value pairs to be set as environment variables
        files (list[FlyFile] | Unset): Files to write into the Machine, from either a raw value or an app secret
        guest (FlyMachineGuest | Unset):
        image (str | Unset): The docker image to run
        init (FlyMachineInit | Unset):
        metadata (FlyMachineConfigMetadata | Unset): Key/value pairs of Machine metadata. Fly.io uses metadata
            internally for routing, process groups, and clusters
        metrics (FlyMachineMetrics | Unset):
        mounts (list[FlyMachineMount] | Unset): Persistent volumes to mount in the Machine. A Machine can mount at most
            one volume, which must be on
            the same host. The mounted volume cannot be changed by updating the Machine
        processes (list[FlyMachineProcess] | Unset): Multiple processes to run within this one Machine, all from the
            Machine's image. Unrelated to the
            process groups in fly.toml, which run on separate Machines. To run processes from different
            images, use containers instead
        restart (FlyMachineRestart | Unset): The Machine restart policy defines whether and how flyd restarts a Machine
            after its main process exits. See https://fly.io/docs/machines/guides-examples/machine-restart-policy/.
        rootfs (FlyMachineRootfs | Unset):
        schedule (str | Unset): Run the Machine at an interval: one of hourly, daily, weekly or monthly. The interval
            starts when
            the Machine is created
        services (list[FlyMachineService] | Unset): Network services that Fly Proxy routes traffic to
        size (str | Unset): Deprecated: use Guest instead
        spot (FlyMachineSpot | Unset):
        standbys (list[str] | Unset): Standbys enable a machine to be a standby for another. In the event of a hardware
            failure,
            the standby machine will be started.
        statics (list[FlyStatic] | Unset): Static files to serve under a URL prefix. Fly Proxy routes matching requests
            to a file server
            inside the Machine, bypassing your application's own process; the Machine must be running. The
            files are read either from a path inside the Machine or from a Tigris bucket that belongs to the
            app; no bucket is created for you
        stop_config (FlyStopConfig | Unset):
    """

    auto_destroy: bool | Unset = UNSET
    cache_disk: FlyMachineCacheDrive | Unset = UNSET
    checks: FlyMachineConfigChecks | Unset = UNSET
    containers: list[FlyContainerConfig] | Unset = UNSET
    disable_machine_autostart: bool | Unset = UNSET
    dns: FlyDNSConfig | Unset = UNSET
    env: FlyMachineConfigEnv | Unset = UNSET
    files: list[FlyFile] | Unset = UNSET
    guest: FlyMachineGuest | Unset = UNSET
    image: str | Unset = UNSET
    init: FlyMachineInit | Unset = UNSET
    metadata: FlyMachineConfigMetadata | Unset = UNSET
    metrics: FlyMachineMetrics | Unset = UNSET
    mounts: list[FlyMachineMount] | Unset = UNSET
    processes: list[FlyMachineProcess] | Unset = UNSET
    restart: FlyMachineRestart | Unset = UNSET
    rootfs: FlyMachineRootfs | Unset = UNSET
    schedule: str | Unset = UNSET
    services: list[FlyMachineService] | Unset = UNSET
    size: str | Unset = UNSET
    spot: FlyMachineSpot | Unset = UNSET
    standbys: list[str] | Unset = UNSET
    statics: list[FlyStatic] | Unset = UNSET
    stop_config: FlyStopConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_destroy = self.auto_destroy

        cache_disk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_disk, Unset):
            cache_disk = self.cache_disk.to_dict()

        checks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks.to_dict()

        containers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.containers, Unset):
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()
                containers.append(containers_item)

        disable_machine_autostart = self.disable_machine_autostart

        dns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        guest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guest, Unset):
            guest = self.guest.to_dict()

        image = self.image

        init: dict[str, Any] | Unset = UNSET
        if not isinstance(self.init, Unset):
            init = self.init.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        mounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)

        processes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.processes, Unset):
            processes = []
            for processes_item_data in self.processes:
                processes_item = processes_item_data.to_dict()
                processes.append(processes_item)

        restart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        rootfs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rootfs, Unset):
            rootfs = self.rootfs.to_dict()

        schedule = self.schedule

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        size = self.size

        spot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spot, Unset):
            spot = self.spot.to_dict()

        standbys: list[str] | Unset = UNSET
        if not isinstance(self.standbys, Unset):
            standbys = self.standbys

        statics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statics, Unset):
            statics = []
            for statics_item_data in self.statics:
                statics_item = statics_item_data.to_dict()
                statics.append(statics_item)

        stop_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_config, Unset):
            stop_config = self.stop_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_destroy is not UNSET:
            field_dict["auto_destroy"] = auto_destroy
        if cache_disk is not UNSET:
            field_dict["cache_disk"] = cache_disk
        if checks is not UNSET:
            field_dict["checks"] = checks
        if containers is not UNSET:
            field_dict["containers"] = containers
        if disable_machine_autostart is not UNSET:
            field_dict["disable_machine_autostart"] = disable_machine_autostart
        if dns is not UNSET:
            field_dict["dns"] = dns
        if env is not UNSET:
            field_dict["env"] = env
        if files is not UNSET:
            field_dict["files"] = files
        if guest is not UNSET:
            field_dict["guest"] = guest
        if image is not UNSET:
            field_dict["image"] = image
        if init is not UNSET:
            field_dict["init"] = init
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if processes is not UNSET:
            field_dict["processes"] = processes
        if restart is not UNSET:
            field_dict["restart"] = restart
        if rootfs is not UNSET:
            field_dict["rootfs"] = rootfs
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if services is not UNSET:
            field_dict["services"] = services
        if size is not UNSET:
            field_dict["size"] = size
        if spot is not UNSET:
            field_dict["spot"] = spot
        if standbys is not UNSET:
            field_dict["standbys"] = standbys
        if statics is not UNSET:
            field_dict["statics"] = statics
        if stop_config is not UNSET:
            field_dict["stop_config"] = stop_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_container_config import FlyContainerConfig
        from ..models.fly_dns_config import FlyDNSConfig
        from ..models.fly_file import FlyFile
        from ..models.fly_machine_cache_drive import FlyMachineCacheDrive
        from ..models.fly_machine_config_checks import FlyMachineConfigChecks
        from ..models.fly_machine_config_env import FlyMachineConfigEnv
        from ..models.fly_machine_config_metadata import FlyMachineConfigMetadata
        from ..models.fly_machine_guest import FlyMachineGuest
        from ..models.fly_machine_init import FlyMachineInit
        from ..models.fly_machine_metrics import FlyMachineMetrics
        from ..models.fly_machine_mount import FlyMachineMount
        from ..models.fly_machine_process import FlyMachineProcess
        from ..models.fly_machine_restart import FlyMachineRestart
        from ..models.fly_machine_rootfs import FlyMachineRootfs
        from ..models.fly_machine_service import FlyMachineService
        from ..models.fly_machine_spot import FlyMachineSpot
        from ..models.fly_static import FlyStatic
        from ..models.fly_stop_config import FlyStopConfig

        d = dict(src_dict)
        auto_destroy = d.pop("auto_destroy", UNSET)

        _cache_disk = d.pop("cache_disk", UNSET)
        cache_disk: FlyMachineCacheDrive | Unset
        if isinstance(_cache_disk, Unset):
            cache_disk = UNSET
        else:
            cache_disk = FlyMachineCacheDrive.from_dict(_cache_disk)

        _checks = d.pop("checks", UNSET)
        checks: FlyMachineConfigChecks | Unset
        if isinstance(_checks, Unset):
            checks = UNSET
        else:
            checks = FlyMachineConfigChecks.from_dict(_checks)

        _containers = d.pop("containers", UNSET)
        containers: list[FlyContainerConfig] | Unset = UNSET
        if _containers is not UNSET:
            containers = []
            for containers_item_data in _containers:
                containers_item = FlyContainerConfig.from_dict(containers_item_data)

                containers.append(containers_item)

        disable_machine_autostart = d.pop("disable_machine_autostart", UNSET)

        _dns = d.pop("dns", UNSET)
        dns: FlyDNSConfig | Unset
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = FlyDNSConfig.from_dict(_dns)

        _env = d.pop("env", UNSET)
        env: FlyMachineConfigEnv | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = FlyMachineConfigEnv.from_dict(_env)

        _files = d.pop("files", UNSET)
        files: list[FlyFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FlyFile.from_dict(files_item_data)

                files.append(files_item)

        _guest = d.pop("guest", UNSET)
        guest: FlyMachineGuest | Unset
        if isinstance(_guest, Unset):
            guest = UNSET
        else:
            guest = FlyMachineGuest.from_dict(_guest)

        image = d.pop("image", UNSET)

        _init = d.pop("init", UNSET)
        init: FlyMachineInit | Unset
        if isinstance(_init, Unset):
            init = UNSET
        else:
            init = FlyMachineInit.from_dict(_init)

        _metadata = d.pop("metadata", UNSET)
        metadata: FlyMachineConfigMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FlyMachineConfigMetadata.from_dict(_metadata)

        _metrics = d.pop("metrics", UNSET)
        metrics: FlyMachineMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = FlyMachineMetrics.from_dict(_metrics)

        _mounts = d.pop("mounts", UNSET)
        mounts: list[FlyMachineMount] | Unset = UNSET
        if _mounts is not UNSET:
            mounts = []
            for mounts_item_data in _mounts:
                mounts_item = FlyMachineMount.from_dict(mounts_item_data)

                mounts.append(mounts_item)

        _processes = d.pop("processes", UNSET)
        processes: list[FlyMachineProcess] | Unset = UNSET
        if _processes is not UNSET:
            processes = []
            for processes_item_data in _processes:
                processes_item = FlyMachineProcess.from_dict(processes_item_data)

                processes.append(processes_item)

        _restart = d.pop("restart", UNSET)
        restart: FlyMachineRestart | Unset
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = FlyMachineRestart.from_dict(_restart)

        _rootfs = d.pop("rootfs", UNSET)
        rootfs: FlyMachineRootfs | Unset
        if isinstance(_rootfs, Unset):
            rootfs = UNSET
        else:
            rootfs = FlyMachineRootfs.from_dict(_rootfs)

        schedule = d.pop("schedule", UNSET)

        _services = d.pop("services", UNSET)
        services: list[FlyMachineService] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = FlyMachineService.from_dict(services_item_data)

                services.append(services_item)

        size = d.pop("size", UNSET)

        _spot = d.pop("spot", UNSET)
        spot: FlyMachineSpot | Unset
        if isinstance(_spot, Unset):
            spot = UNSET
        else:
            spot = FlyMachineSpot.from_dict(_spot)

        standbys = cast(list[str], d.pop("standbys", UNSET))

        _statics = d.pop("statics", UNSET)
        statics: list[FlyStatic] | Unset = UNSET
        if _statics is not UNSET:
            statics = []
            for statics_item_data in _statics:
                statics_item = FlyStatic.from_dict(statics_item_data)

                statics.append(statics_item)

        _stop_config = d.pop("stop_config", UNSET)
        stop_config: FlyStopConfig | Unset
        if isinstance(_stop_config, Unset):
            stop_config = UNSET
        else:
            stop_config = FlyStopConfig.from_dict(_stop_config)

        fly_machine_config = cls(
            auto_destroy=auto_destroy,
            cache_disk=cache_disk,
            checks=checks,
            containers=containers,
            disable_machine_autostart=disable_machine_autostart,
            dns=dns,
            env=env,
            files=files,
            guest=guest,
            image=image,
            init=init,
            metadata=metadata,
            metrics=metrics,
            mounts=mounts,
            processes=processes,
            restart=restart,
            rootfs=rootfs,
            schedule=schedule,
            services=services,
            size=size,
            spot=spot,
            standbys=standbys,
            statics=statics,
            stop_config=stop_config,
        )

        fly_machine_config.additional_properties = d
        return fly_machine_config

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
