from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_env_from import FlyEnvFrom
    from ..models.fly_machine_process_env import FlyMachineProcessEnv
    from ..models.fly_machine_secret import FlyMachineSecret


T = TypeVar("T", bound="FlyMachineProcess")


@_attrs_define
class FlyMachineProcess:
    """
    Attributes:
        cmd (list[str] | Unset): Replaces the image's CMD for this process. It's appended to the entrypoint
        entrypoint (list[str] | Unset): Replaces the image's ENTRYPOINT for this process
        env (FlyMachineProcessEnv | Unset): Environment variables for this process, in addition to the Machine's `env`
        env_from (list[FlyEnvFrom] | Unset): EnvFrom can be provided to set environment variables from machine fields.
        exec_ (list[str] | Unset): Command to run instead of the image's ENTRYPOINT and CMD. Takes precedence over
            entrypoint
            and cmd
        ignore_app_secrets (bool | Unset): IgnoreAppSecrets can be set to true to ignore the secrets for the App the
            Machine belongs to
            and only use the secrets provided at the process level. The default/legacy behavior is to use
            the secrets provided at the App level.
        secrets (list[FlyMachineSecret] | Unset): Secrets can be provided at the process level to explicitly indicate
            which secrets should be
            used for the process. If not provided, the secrets provided at the machine level will be used.
        user (str | Unset): User to run the process as, instead of the image's USER
    """

    cmd: list[str] | Unset = UNSET
    entrypoint: list[str] | Unset = UNSET
    env: FlyMachineProcessEnv | Unset = UNSET
    env_from: list[FlyEnvFrom] | Unset = UNSET
    exec_: list[str] | Unset = UNSET
    ignore_app_secrets: bool | Unset = UNSET
    secrets: list[FlyMachineSecret] | Unset = UNSET
    user: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmd: list[str] | Unset = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

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

        ignore_app_secrets = self.ignore_app_secrets

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if entrypoint is not UNSET:
            field_dict["entrypoint"] = entrypoint
        if env is not UNSET:
            field_dict["env"] = env
        if env_from is not UNSET:
            field_dict["env_from"] = env_from
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if ignore_app_secrets is not UNSET:
            field_dict["ignore_app_secrets"] = ignore_app_secrets
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_env_from import FlyEnvFrom
        from ..models.fly_machine_process_env import FlyMachineProcessEnv
        from ..models.fly_machine_secret import FlyMachineSecret

        d = dict(src_dict)
        cmd = cast(list[str], d.pop("cmd", UNSET))

        entrypoint = cast(list[str], d.pop("entrypoint", UNSET))

        _env = d.pop("env", UNSET)
        env: FlyMachineProcessEnv | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = FlyMachineProcessEnv.from_dict(_env)

        _env_from = d.pop("env_from", UNSET)
        env_from: list[FlyEnvFrom] | Unset = UNSET
        if _env_from is not UNSET:
            env_from = []
            for env_from_item_data in _env_from:
                env_from_item = FlyEnvFrom.from_dict(env_from_item_data)

                env_from.append(env_from_item)

        exec_ = cast(list[str], d.pop("exec", UNSET))

        ignore_app_secrets = d.pop("ignore_app_secrets", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[FlyMachineSecret] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = FlyMachineSecret.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        user = d.pop("user", UNSET)

        fly_machine_process = cls(
            cmd=cmd,
            entrypoint=entrypoint,
            env=env,
            env_from=env_from,
            exec_=exec_,
            ignore_app_secrets=ignore_app_secrets,
            secrets=secrets,
            user=user,
        )

        fly_machine_process.additional_properties = d
        return fly_machine_process

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
