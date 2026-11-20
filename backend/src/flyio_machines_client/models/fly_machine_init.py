from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineInit")


@_attrs_define
class FlyMachineInit:
    """
    Attributes:
        cmd (list[str] | Unset): Replaces the image's CMD. It's appended to the entrypoint
        entrypoint (list[str] | Unset): Replaces the image's ENTRYPOINT
        exec_ (list[str] | Unset): Command to run instead of the image's ENTRYPOINT and CMD. Takes precedence over
            entrypoint
            and cmd
        kernel_args (list[str] | Unset): Currently has no effect. Use `guest.kernel_args` instead
        swap_size_mb (int | Unset): Size in MiB of a swap device to give the Machine. Machines with swap cannot be
            suspended
        tty (bool | Unset): Currently has no effect
    """

    cmd: list[str] | Unset = UNSET
    entrypoint: list[str] | Unset = UNSET
    exec_: list[str] | Unset = UNSET
    kernel_args: list[str] | Unset = UNSET
    swap_size_mb: int | Unset = UNSET
    tty: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmd: list[str] | Unset = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

        entrypoint: list[str] | Unset = UNSET
        if not isinstance(self.entrypoint, Unset):
            entrypoint = self.entrypoint

        exec_: list[str] | Unset = UNSET
        if not isinstance(self.exec_, Unset):
            exec_ = self.exec_

        kernel_args: list[str] | Unset = UNSET
        if not isinstance(self.kernel_args, Unset):
            kernel_args = self.kernel_args

        swap_size_mb = self.swap_size_mb

        tty = self.tty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if entrypoint is not UNSET:
            field_dict["entrypoint"] = entrypoint
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if kernel_args is not UNSET:
            field_dict["kernel_args"] = kernel_args
        if swap_size_mb is not UNSET:
            field_dict["swap_size_mb"] = swap_size_mb
        if tty is not UNSET:
            field_dict["tty"] = tty

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cmd = cast(list[str], d.pop("cmd", UNSET))

        entrypoint = cast(list[str], d.pop("entrypoint", UNSET))

        exec_ = cast(list[str], d.pop("exec", UNSET))

        kernel_args = cast(list[str], d.pop("kernel_args", UNSET))

        swap_size_mb = d.pop("swap_size_mb", UNSET)

        tty = d.pop("tty", UNSET)

        fly_machine_init = cls(
            cmd=cmd,
            entrypoint=entrypoint,
            exec_=exec_,
            kernel_args=kernel_args,
            swap_size_mb=swap_size_mb,
            tty=tty,
        )

        fly_machine_init.additional_properties = d
        return fly_machine_init

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
