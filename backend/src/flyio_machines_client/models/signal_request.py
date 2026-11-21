from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.signal_request_signal import SignalRequestSignal
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalRequest")


@_attrs_define
class SignalRequest:
    """
    Attributes:
        signal (SignalRequestSignal | Unset): Signal to send to the Machine's main process.
    """

    signal: SignalRequestSignal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal: str | Unset = UNSET
        if not isinstance(self.signal, Unset):
            signal = self.signal.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _signal = d.pop("signal", UNSET)
        signal: SignalRequestSignal | Unset
        if isinstance(_signal, Unset):
            signal = UNSET
        else:
            signal = SignalRequestSignal(_signal)

        signal_request = cls(
            signal=signal,
        )

        signal_request.additional_properties = d
        return signal_request

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
