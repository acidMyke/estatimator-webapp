from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_http_header import FlyMachineHTTPHeader


T = TypeVar("T", bound="FlyMachineServiceCheck")


@_attrs_define
class FlyMachineServiceCheck:
    """
    Attributes:
        grace_period (str | Unset): The time to wait after a VM starts before checking its health Example: 1s.
        headers (list[FlyMachineHTTPHeader] | Unset): For http checks, headers to send with the request
        interval (str | Unset): The time between connectivity checks Example: 15s.
        method (str | Unset): For http checks, the HTTP method to use to when making the request
        path (str | Unset): For http checks, the path to send the request to
        port (int | Unset): The port to connect to. Defaults to the service's internal_port
        protocol (str | Unset): For http checks, whether to use http or https
        timeout (str | Unset): The maximum time a connection can take before being reported as failing its health check
            Example: 2s.
        tls_server_name (str | Unset): If the protocol is https, the hostname to use for TLS certificate validation
        tls_skip_verify (bool | Unset): For http checks with https protocol, whether or not to verify the TLS
            certificate
        type_ (str | Unset): tcp or http
    """

    grace_period: str | Unset = UNSET
    headers: list[FlyMachineHTTPHeader] | Unset = UNSET
    interval: str | Unset = UNSET
    method: str | Unset = UNSET
    path: str | Unset = UNSET
    port: int | Unset = UNSET
    protocol: str | Unset = UNSET
    timeout: str | Unset = UNSET
    tls_server_name: str | Unset = UNSET
    tls_skip_verify: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grace_period = self.grace_period

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        interval = self.interval

        method = self.method

        path = self.path

        port = self.port

        protocol = self.protocol

        timeout = self.timeout

        tls_server_name = self.tls_server_name

        tls_skip_verify = self.tls_skip_verify

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grace_period is not UNSET:
            field_dict["grace_period"] = grace_period
        if headers is not UNSET:
            field_dict["headers"] = headers
        if interval is not UNSET:
            field_dict["interval"] = interval
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if tls_server_name is not UNSET:
            field_dict["tls_server_name"] = tls_server_name
        if tls_skip_verify is not UNSET:
            field_dict["tls_skip_verify"] = tls_skip_verify
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_http_header import FlyMachineHTTPHeader

        d = dict(src_dict)
        grace_period = d.pop("grace_period", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: list[FlyMachineHTTPHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = FlyMachineHTTPHeader.from_dict(headers_item_data)

                headers.append(headers_item)

        interval = d.pop("interval", UNSET)

        method = d.pop("method", UNSET)

        path = d.pop("path", UNSET)

        port = d.pop("port", UNSET)

        protocol = d.pop("protocol", UNSET)

        timeout = d.pop("timeout", UNSET)

        tls_server_name = d.pop("tls_server_name", UNSET)

        tls_skip_verify = d.pop("tls_skip_verify", UNSET)

        type_ = d.pop("type", UNSET)

        fly_machine_service_check = cls(
            grace_period=grace_period,
            headers=headers,
            interval=interval,
            method=method,
            path=path,
            port=port,
            protocol=protocol,
            timeout=timeout,
            tls_server_name=tls_server_name,
            tls_skip_verify=tls_skip_verify,
            type_=type_,
        )

        fly_machine_service_check.additional_properties = d
        return fly_machine_service_check

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
