from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_container_healthcheck_scheme import FlyContainerHealthcheckScheme
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_machine_http_header import FlyMachineHTTPHeader


T = TypeVar("T", bound="FlyHTTPHealthcheck")


@_attrs_define
class FlyHTTPHealthcheck:
    """
    Attributes:
        headers (list[FlyMachineHTTPHeader] | Unset): Additional headers to send with the request
        method (str | Unset): The HTTP method to use to when making the request
        path (str | Unset): The path to send the request to
        port (int | Unset): The port to connect to, often the same as internal_port
        scheme (FlyContainerHealthcheckScheme | Unset):
        tls_server_name (str | Unset): If the protocol is https, the hostname to use for TLS certificate validation
        tls_skip_verify (bool | Unset): If the protocol is https, whether or not to verify the TLS certificate
    """

    headers: list[FlyMachineHTTPHeader] | Unset = UNSET
    method: str | Unset = UNSET
    path: str | Unset = UNSET
    port: int | Unset = UNSET
    scheme: FlyContainerHealthcheckScheme | Unset = UNSET
    tls_server_name: str | Unset = UNSET
    tls_skip_verify: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        method = self.method

        path = self.path

        port = self.port

        scheme: str | Unset = UNSET
        if not isinstance(self.scheme, Unset):
            scheme = self.scheme.value

        tls_server_name = self.tls_server_name

        tls_skip_verify = self.tls_skip_verify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if port is not UNSET:
            field_dict["port"] = port
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if tls_server_name is not UNSET:
            field_dict["tls_server_name"] = tls_server_name
        if tls_skip_verify is not UNSET:
            field_dict["tls_skip_verify"] = tls_skip_verify

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_machine_http_header import FlyMachineHTTPHeader

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: list[FlyMachineHTTPHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = FlyMachineHTTPHeader.from_dict(headers_item_data)

                headers.append(headers_item)

        method = d.pop("method", UNSET)

        path = d.pop("path", UNSET)

        port = d.pop("port", UNSET)

        _scheme = d.pop("scheme", UNSET)
        scheme: FlyContainerHealthcheckScheme | Unset
        if isinstance(_scheme, Unset):
            scheme = UNSET
        else:
            scheme = FlyContainerHealthcheckScheme(_scheme)

        tls_server_name = d.pop("tls_server_name", UNSET)

        tls_skip_verify = d.pop("tls_skip_verify", UNSET)

        fly_http_healthcheck = cls(
            headers=headers,
            method=method,
            path=path,
            port=port,
            scheme=scheme,
            tls_server_name=tls_server_name,
            tls_skip_verify=tls_skip_verify,
        )

        fly_http_healthcheck.additional_properties = d
        return fly_http_healthcheck

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
