from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecResponse")


@_attrs_define
class ExecResponse:
    """
    Attributes:
        exit_code (int | Unset): The command's exit code.
        exit_signal (int | Unset): The signal that terminated the command, or 0 if it exited normally.
        stderr (str | Unset): The command's standard error.
        stdout (str | Unset): The command's standard output.
    """

    exit_code: int | Unset = UNSET
    exit_signal: int | Unset = UNSET
    stderr: str | Unset = UNSET
    stdout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exit_code = self.exit_code

        exit_signal = self.exit_signal

        stderr = self.stderr

        stdout = self.stdout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if exit_signal is not UNSET:
            field_dict["exit_signal"] = exit_signal
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if stdout is not UNSET:
            field_dict["stdout"] = stdout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exit_code = d.pop("exit_code", UNSET)

        exit_signal = d.pop("exit_signal", UNSET)

        stderr = d.pop("stderr", UNSET)

        stdout = d.pop("stdout", UNSET)

        exec_response = cls(
            exit_code=exit_code,
            exit_signal=exit_signal,
            stderr=stderr,
            stdout=stdout,
        )

        exec_response.additional_properties = d
        return exec_response

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
