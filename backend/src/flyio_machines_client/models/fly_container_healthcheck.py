from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_container_healthcheck_kind import FlyContainerHealthcheckKind
from ..models.fly_unhealthy_policy import FlyUnhealthyPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_exec_healthcheck import FlyExecHealthcheck
    from ..models.fly_http_healthcheck import FlyHTTPHealthcheck
    from ..models.fly_tcp_healthcheck import FlyTCPHealthcheck


T = TypeVar("T", bound="FlyContainerHealthcheck")


@_attrs_define
class FlyContainerHealthcheck:
    """
    Attributes:
        exec_ (FlyExecHealthcheck | Unset):
        failure_threshold (int | Unset): The number of times the check must fail before considering the container
            unhealthy.
        grace_period (int | Unset): The time in seconds to wait after a container starts before checking its health.
        http (FlyHTTPHealthcheck | Unset):
        interval (int | Unset): The time in seconds between executing the defined check.
        kind (FlyContainerHealthcheckKind | Unset):
        name (str | Unset): The name of the check. Must be unique within the container.
        success_threshold (int | Unset): The number of times the check must succeeed before considering the container
            healthy.
        tcp (FlyTCPHealthcheck | Unset):
        timeout (int | Unset): The time in seconds to wait for the check to complete.
        unhealthy (FlyUnhealthyPolicy | Unset):
    """

    exec_: FlyExecHealthcheck | Unset = UNSET
    failure_threshold: int | Unset = UNSET
    grace_period: int | Unset = UNSET
    http: FlyHTTPHealthcheck | Unset = UNSET
    interval: int | Unset = UNSET
    kind: FlyContainerHealthcheckKind | Unset = UNSET
    name: str | Unset = UNSET
    success_threshold: int | Unset = UNSET
    tcp: FlyTCPHealthcheck | Unset = UNSET
    timeout: int | Unset = UNSET
    unhealthy: FlyUnhealthyPolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exec_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exec_, Unset):
            exec_ = self.exec_.to_dict()

        failure_threshold = self.failure_threshold

        grace_period = self.grace_period

        http: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http, Unset):
            http = self.http.to_dict()

        interval = self.interval

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        success_threshold = self.success_threshold

        tcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp, Unset):
            tcp = self.tcp.to_dict()

        timeout = self.timeout

        unhealthy: str | Unset = UNSET
        if not isinstance(self.unhealthy, Unset):
            unhealthy = self.unhealthy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if failure_threshold is not UNSET:
            field_dict["failure_threshold"] = failure_threshold
        if grace_period is not UNSET:
            field_dict["grace_period"] = grace_period
        if http is not UNSET:
            field_dict["http"] = http
        if interval is not UNSET:
            field_dict["interval"] = interval
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if success_threshold is not UNSET:
            field_dict["success_threshold"] = success_threshold
        if tcp is not UNSET:
            field_dict["tcp"] = tcp
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if unhealthy is not UNSET:
            field_dict["unhealthy"] = unhealthy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_exec_healthcheck import FlyExecHealthcheck
        from ..models.fly_http_healthcheck import FlyHTTPHealthcheck
        from ..models.fly_tcp_healthcheck import FlyTCPHealthcheck

        d = dict(src_dict)
        _exec_ = d.pop("exec", UNSET)
        exec_: FlyExecHealthcheck | Unset
        if isinstance(_exec_, Unset):
            exec_ = UNSET
        else:
            exec_ = FlyExecHealthcheck.from_dict(_exec_)

        failure_threshold = d.pop("failure_threshold", UNSET)

        grace_period = d.pop("grace_period", UNSET)

        _http = d.pop("http", UNSET)
        http: FlyHTTPHealthcheck | Unset
        if isinstance(_http, Unset):
            http = UNSET
        else:
            http = FlyHTTPHealthcheck.from_dict(_http)

        interval = d.pop("interval", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: FlyContainerHealthcheckKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = FlyContainerHealthcheckKind(_kind)

        name = d.pop("name", UNSET)

        success_threshold = d.pop("success_threshold", UNSET)

        _tcp = d.pop("tcp", UNSET)
        tcp: FlyTCPHealthcheck | Unset
        if isinstance(_tcp, Unset):
            tcp = UNSET
        else:
            tcp = FlyTCPHealthcheck.from_dict(_tcp)

        timeout = d.pop("timeout", UNSET)

        _unhealthy = d.pop("unhealthy", UNSET)
        unhealthy: FlyUnhealthyPolicy | Unset
        if isinstance(_unhealthy, Unset):
            unhealthy = UNSET
        else:
            unhealthy = FlyUnhealthyPolicy(_unhealthy)

        fly_container_healthcheck = cls(
            exec_=exec_,
            failure_threshold=failure_threshold,
            grace_period=grace_period,
            http=http,
            interval=interval,
            kind=kind,
            name=name,
            success_threshold=success_threshold,
            tcp=tcp,
            timeout=timeout,
            unhealthy=unhealthy,
        )

        fly_container_healthcheck.additional_properties = d
        return fly_container_healthcheck

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
