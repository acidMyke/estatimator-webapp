from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyMachineMetrics")


@_attrs_define
class FlyMachineMetrics:
    """
    Attributes:
        https (bool | Unset): Scrape over HTTPS instead of HTTP
        path (str | Unset): HTTP path to scrape. Defaults to `/`
        port (int | Unset): Port in the Machine to scrape metrics from
    """

    https: bool | Unset = UNSET
    path: str | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        https = self.https

        path = self.path

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if https is not UNSET:
            field_dict["https"] = https
        if path is not UNSET:
            field_dict["path"] = path
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        https = d.pop("https", UNSET)

        path = d.pop("path", UNSET)

        port = d.pop("port", UNSET)

        fly_machine_metrics = cls(
            https=https,
            path=path,
            port=port,
        )

        fly_machine_metrics.additional_properties = d
        return fly_machine_metrics

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
