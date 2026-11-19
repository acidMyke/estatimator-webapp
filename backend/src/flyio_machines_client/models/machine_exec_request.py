from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineExecRequest")


@_attrs_define
class MachineExecRequest:
    """
    Attributes:
        cmd (str | Unset): Command line to run, split into arguments like a shell would. Takes precedence over
            `command`.

            Deprecated: use `command`.
        command (list[str] | Unset): Command to run, as the program followed by its arguments. It is run directly, not
            by a
            shell.
        container (str | Unset): Name of the container to run the command in, for Machines with containers.
        machine (bool | Unset): Run the command in the Machine's own namespace instead of in a container. Mutually
            exclusive with `container`.
        stdin (str | Unset): Data to write to the command's standard input.
        timeout (int | Unset): How long to let the command run, in seconds. Defaults to 10; at most 600.
    """

    cmd: str | Unset = UNSET
    command: list[str] | Unset = UNSET
    container: str | Unset = UNSET
    machine: bool | Unset = UNSET
    stdin: str | Unset = UNSET
    timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmd = self.cmd

        command: list[str] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command

        container = self.container

        machine = self.machine

        stdin = self.stdin

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if command is not UNSET:
            field_dict["command"] = command
        if container is not UNSET:
            field_dict["container"] = container
        if machine is not UNSET:
            field_dict["machine"] = machine
        if stdin is not UNSET:
            field_dict["stdin"] = stdin
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cmd = d.pop("cmd", UNSET)

        command = cast(list[str], d.pop("command", UNSET))

        container = d.pop("container", UNSET)

        machine = d.pop("machine", UNSET)

        stdin = d.pop("stdin", UNSET)

        timeout = d.pop("timeout", UNSET)

        machine_exec_request = cls(
            cmd=cmd,
            command=command,
            container=container,
            machine=machine,
            stdin=stdin,
            timeout=timeout,
        )

        machine_exec_request.additional_properties = d
        return machine_exec_request

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
