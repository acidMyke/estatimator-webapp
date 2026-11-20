from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_container_config_env import FlyContainerConfigEnv
    from ..models.fly_container_dependency import FlyContainerDependency
    from ..models.fly_container_healthcheck import FlyContainerHealthcheck
    from ..models.fly_env_from import FlyEnvFrom
    from ..models.fly_file import FlyFile
    from ..models.fly_machine_restart import FlyMachineRestart
    from ..models.fly_machine_secret import FlyMachineSecret
    from ..models.fly_stop_config import FlyStopConfig


T = TypeVar("T", bound="FlyContainerConfig")


@_attrs_define
class FlyContainerConfig:
    """
    Attributes:
        cmd (list[str] | Unset): CmdOverride is used to override the default command of the image.
        depends_on (list[FlyContainerDependency] | Unset): DependsOn can be used to define dependencies between
            containers. The container will only be
            started after all of its dependent conditions have been satisfied.
        entrypoint (list[str] | Unset): EntrypointOverride is used to override the default entrypoint of the image.
        env (FlyContainerConfigEnv | Unset): ExtraEnv is used to add additional environment variables to the container.
        env_from (list[FlyEnvFrom] | Unset): EnvFrom can be provided to set environment variables from machine fields.
        exec_ (list[str] | Unset): Image Config overrides - these fields are used to override the image configuration.
            If not provided, the image configuration will be used.
            ExecOverride is used to override the default command of the image.
        files (list[FlyFile] | Unset): Files are files that will be written to the container file system.
        healthchecks (list[FlyContainerHealthcheck] | Unset): Healthchecks determine the health of your containers.
            Healthchecks can use HTTP, TCP or an Exec command.
        image (str | Unset): Image is the docker image to run.
        name (str | Unset): Name is used to identify the container in the machine.
        restart (FlyMachineRestart | Unset): The Machine restart policy defines whether and how flyd restarts a Machine
            after its main process exits. See https://fly.io/docs/machines/guides-examples/machine-restart-policy/.
        secrets (list[FlyMachineSecret] | Unset): Secrets can be provided at the process level to explicitly indicate
            which secrets should be
            used for the process. If not provided, the secrets provided at the machine level will be used.
        stop (FlyStopConfig | Unset):
        user (str | Unset): UserOverride is used to override the default user of the image.
    """

    cmd: list[str] | Unset = UNSET
    depends_on: list[FlyContainerDependency] | Unset = UNSET
    entrypoint: list[str] | Unset = UNSET
    env: FlyContainerConfigEnv | Unset = UNSET
    env_from: list[FlyEnvFrom] | Unset = UNSET
    exec_: list[str] | Unset = UNSET
    files: list[FlyFile] | Unset = UNSET
    healthchecks: list[FlyContainerHealthcheck] | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    restart: FlyMachineRestart | Unset = UNSET
    secrets: list[FlyMachineSecret] | Unset = UNSET
    stop: FlyStopConfig | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmd: list[str] | Unset = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

        depends_on: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = []
            for depends_on_item_data in self.depends_on:
                depends_on_item = depends_on_item_data.to_dict()
                depends_on.append(depends_on_item)

        entrypoint: list[str] | Unset = UNSET
        if not isinstance(self.entrypoint, Unset):
            entrypoint = self.entrypoint

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        env_from: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.env_from, Unset):
            env_from = []
            for env_from_item_data in self.env_from:
                env_from_item = env_from_item_data.to_dict()
                env_from.append(env_from_item)

        exec_: list[str] | Unset = UNSET
        if not isinstance(self.exec_, Unset):
            exec_ = self.exec_

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        healthchecks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.healthchecks, Unset):
            healthchecks = []
            for healthchecks_item_data in self.healthchecks:
                healthchecks_item = healthchecks_item_data.to_dict()
                healthchecks.append(healthchecks_item)

        image = self.image

        name = self.name

        restart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        stop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop.to_dict()

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if depends_on is not UNSET:
            field_dict["depends_on"] = depends_on
        if entrypoint is not UNSET:
            field_dict["entrypoint"] = entrypoint
        if env is not UNSET:
            field_dict["env"] = env
        if env_from is not UNSET:
            field_dict["env_from"] = env_from
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if files is not UNSET:
            field_dict["files"] = files
        if healthchecks is not UNSET:
            field_dict["healthchecks"] = healthchecks
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if restart is not UNSET:
            field_dict["restart"] = restart
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if stop is not UNSET:
            field_dict["stop"] = stop
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_container_config_env import FlyContainerConfigEnv
        from ..models.fly_container_dependency import FlyContainerDependency
        from ..models.fly_container_healthcheck import FlyContainerHealthcheck
        from ..models.fly_env_from import FlyEnvFrom
        from ..models.fly_file import FlyFile
        from ..models.fly_machine_restart import FlyMachineRestart
        from ..models.fly_machine_secret import FlyMachineSecret
        from ..models.fly_stop_config import FlyStopConfig

        d = dict(src_dict)
        cmd = cast(list[str], d.pop("cmd", UNSET))

        _depends_on = d.pop("depends_on", UNSET)
        depends_on: list[FlyContainerDependency] | Unset = UNSET
        if _depends_on is not UNSET:
            depends_on = []
            for depends_on_item_data in _depends_on:
                depends_on_item = FlyContainerDependency.from_dict(depends_on_item_data)

                depends_on.append(depends_on_item)

        entrypoint = cast(list[str], d.pop("entrypoint", UNSET))

        _env = d.pop("env", UNSET)
        env: FlyContainerConfigEnv | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = FlyContainerConfigEnv.from_dict(_env)

        _env_from = d.pop("env_from", UNSET)
        env_from: list[FlyEnvFrom] | Unset = UNSET
        if _env_from is not UNSET:
            env_from = []
            for env_from_item_data in _env_from:
                env_from_item = FlyEnvFrom.from_dict(env_from_item_data)

                env_from.append(env_from_item)

        exec_ = cast(list[str], d.pop("exec", UNSET))

        _files = d.pop("files", UNSET)
        files: list[FlyFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FlyFile.from_dict(files_item_data)

                files.append(files_item)

        _healthchecks = d.pop("healthchecks", UNSET)
        healthchecks: list[FlyContainerHealthcheck] | Unset = UNSET
        if _healthchecks is not UNSET:
            healthchecks = []
            for healthchecks_item_data in _healthchecks:
                healthchecks_item = FlyContainerHealthcheck.from_dict(
                    healthchecks_item_data
                )

                healthchecks.append(healthchecks_item)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        _restart = d.pop("restart", UNSET)
        restart: FlyMachineRestart | Unset
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = FlyMachineRestart.from_dict(_restart)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[FlyMachineSecret] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = FlyMachineSecret.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        _stop = d.pop("stop", UNSET)
        stop: FlyStopConfig | Unset
        if isinstance(_stop, Unset):
            stop = UNSET
        else:
            stop = FlyStopConfig.from_dict(_stop)

        user = d.pop("user", UNSET)

        fly_container_config = cls(
            cmd=cmd,
            depends_on=depends_on,
            entrypoint=entrypoint,
            env=env,
            env_from=env_from,
            exec_=exec_,
            files=files,
            healthchecks=healthchecks,
            image=image,
            name=name,
            restart=restart,
            secrets=secrets,
            stop=stop,
            user=user,
        )

        fly_container_config.additional_properties = d
        return fly_container_config

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
