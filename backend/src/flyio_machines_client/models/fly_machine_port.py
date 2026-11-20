from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_http_options import FlyHTTPOptions
    from ..models.fly_proxy_proto_options import FlyProxyProtoOptions
    from ..models.fly_tls_options import FlyTLSOptions


T = TypeVar("T", bound="FlyMachinePort")


@_attrs_define
class FlyMachinePort:
    """
    Attributes:
        end_port (int | Unset): Last public port of a range
        force_https (bool | Unset): Redirect plain HTTP requests to HTTPS
        handlers (list[str] | Unset): How Fly Proxy handles connections before forwarding them: `tls` terminates TLS,
            `pg_tls`
            terminates PostgreSQL TLS, `http` handles HTTP, `proxy_proto` adds a PROXY protocol header.
            Without handlers, raw TCP is forwarded
        http_options (FlyHTTPOptions | Unset):
        port (int | Unset): Public port. Use either port, or start_port and end_port
        proxy_proto_options (FlyProxyProtoOptions | Unset):
        start_port (int | Unset): First public port of a range
        tls_options (FlyTLSOptions | Unset):
    """

    end_port: int | Unset = UNSET
    force_https: bool | Unset = UNSET
    handlers: list[str] | Unset = UNSET
    http_options: FlyHTTPOptions | Unset = UNSET
    port: int | Unset = UNSET
    proxy_proto_options: FlyProxyProtoOptions | Unset = UNSET
    start_port: int | Unset = UNSET
    tls_options: FlyTLSOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_port = self.end_port

        force_https = self.force_https

        handlers: list[str] | Unset = UNSET
        if not isinstance(self.handlers, Unset):
            handlers = self.handlers

        http_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http_options, Unset):
            http_options = self.http_options.to_dict()

        port = self.port

        proxy_proto_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proxy_proto_options, Unset):
            proxy_proto_options = self.proxy_proto_options.to_dict()

        start_port = self.start_port

        tls_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tls_options, Unset):
            tls_options = self.tls_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_port is not UNSET:
            field_dict["end_port"] = end_port
        if force_https is not UNSET:
            field_dict["force_https"] = force_https
        if handlers is not UNSET:
            field_dict["handlers"] = handlers
        if http_options is not UNSET:
            field_dict["http_options"] = http_options
        if port is not UNSET:
            field_dict["port"] = port
        if proxy_proto_options is not UNSET:
            field_dict["proxy_proto_options"] = proxy_proto_options
        if start_port is not UNSET:
            field_dict["start_port"] = start_port
        if tls_options is not UNSET:
            field_dict["tls_options"] = tls_options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_http_options import FlyHTTPOptions
        from ..models.fly_proxy_proto_options import FlyProxyProtoOptions
        from ..models.fly_tls_options import FlyTLSOptions

        d = dict(src_dict)
        end_port = d.pop("end_port", UNSET)

        force_https = d.pop("force_https", UNSET)

        handlers = cast(list[str], d.pop("handlers", UNSET))

        _http_options = d.pop("http_options", UNSET)
        http_options: FlyHTTPOptions | Unset
        if isinstance(_http_options, Unset):
            http_options = UNSET
        else:
            http_options = FlyHTTPOptions.from_dict(_http_options)

        port = d.pop("port", UNSET)

        _proxy_proto_options = d.pop("proxy_proto_options", UNSET)
        proxy_proto_options: FlyProxyProtoOptions | Unset
        if isinstance(_proxy_proto_options, Unset):
            proxy_proto_options = UNSET
        else:
            proxy_proto_options = FlyProxyProtoOptions.from_dict(_proxy_proto_options)

        start_port = d.pop("start_port", UNSET)

        _tls_options = d.pop("tls_options", UNSET)
        tls_options: FlyTLSOptions | Unset
        if isinstance(_tls_options, Unset):
            tls_options = UNSET
        else:
            tls_options = FlyTLSOptions.from_dict(_tls_options)

        fly_machine_port = cls(
            end_port=end_port,
            force_https=force_https,
            handlers=handlers,
            http_options=http_options,
            port=port,
            proxy_proto_options=proxy_proto_options,
            start_port=start_port,
            tls_options=tls_options,
        )

        fly_machine_port.additional_properties = d
        return fly_machine_port

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
