from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_stop_config_signal import FlyStopConfigSignal
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyStopConfig")


@_attrs_define
class FlyStopConfig:
    """
    Attributes:
        signal (FlyStopConfigSignal | Unset): Signal to send to the Machine's processes. Defaults to SIGINT
        timeout (str | Unset): How long to wait for the Machine to exit after sending the signal, before killing it. At
            most
            5 minutes (1 minute for spot Machines). Defaults to 5s (60s for spot Machines) Example: 10s.
    """

    signal: FlyStopConfigSignal | Unset = UNSET
    timeout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal: str | Unset = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal.value

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal is not UNSET:
            field_dict["signal"] = signal
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _signal = d.pop("signal", UNSET)
        signal: FlyStopConfigSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = FlyStopConfigSignal(_signal)

        timeout = d.pop("timeout", UNSET)

        fly_stop_config = cls(
            signal=signal,
            timeout=timeout,
        )

        fly_stop_config.additional_properties = d
        return fly_stop_config

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
