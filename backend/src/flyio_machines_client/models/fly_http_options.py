from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fly_http_response_options import FlyHTTPResponseOptions
    from ..models.fly_replay_cache import FlyReplayCache


T = TypeVar("T", bound="FlyHTTPOptions")


@_attrs_define
class FlyHTTPOptions:
    """
    Attributes:
        compress (bool | Unset): Compress response bodies. Defaults to true
        h2_backend (bool | Unset): Use HTTP/2 to talk to the Machine
        headers_read_timeout (int | Unset): Seconds Fly Proxy waits for a client to send request headers. Defaults to 5
        idle_timeout (int | Unset): Seconds a client connection can be idle between requests before it's closed.
            Defaults to 300
        replay_cache (list[FlyReplayCache] | Unset): Cache `fly-replay` responses from the Machine: once a client is
            replayed, its further
            requests are replayed directly, keyed on a cookie or header, without asking the Machine again
        response (FlyHTTPResponseOptions | Unset):
    """

    compress: bool | Unset = UNSET
    h2_backend: bool | Unset = UNSET
    headers_read_timeout: int | Unset = UNSET
    idle_timeout: int | Unset = UNSET
    replay_cache: list[FlyReplayCache] | Unset = UNSET
    response: FlyHTTPResponseOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compress = self.compress

        h2_backend = self.h2_backend

        headers_read_timeout = self.headers_read_timeout

        idle_timeout = self.idle_timeout

        replay_cache: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replay_cache, Unset):
            replay_cache = []
            for replay_cache_item_data in self.replay_cache:
                replay_cache_item = replay_cache_item_data.to_dict()
                replay_cache.append(replay_cache_item)

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compress is not UNSET:
            field_dict["compress"] = compress
        if h2_backend is not UNSET:
            field_dict["h2_backend"] = h2_backend
        if headers_read_timeout is not UNSET:
            field_dict["headers_read_timeout"] = headers_read_timeout
        if idle_timeout is not UNSET:
            field_dict["idle_timeout"] = idle_timeout
        if replay_cache is not UNSET:
            field_dict["replay_cache"] = replay_cache
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_http_response_options import FlyHTTPResponseOptions
        from ..models.fly_replay_cache import FlyReplayCache

        d = dict(src_dict)
        compress = d.pop("compress", UNSET)

        h2_backend = d.pop("h2_backend", UNSET)

        headers_read_timeout = d.pop("headers_read_timeout", UNSET)

        idle_timeout = d.pop("idle_timeout", UNSET)

        _replay_cache = d.pop("replay_cache", UNSET)
        replay_cache: list[FlyReplayCache] | Unset = UNSET
        if _replay_cache is not UNSET:
            replay_cache = []
            for replay_cache_item_data in _replay_cache:
                replay_cache_item = FlyReplayCache.from_dict(replay_cache_item_data)

                replay_cache.append(replay_cache_item)

        _response = d.pop("response", UNSET)
        response: FlyHTTPResponseOptions | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = FlyHTTPResponseOptions.from_dict(_response)

        fly_http_options = cls(
            compress=compress,
            h2_backend=h2_backend,
            headers_read_timeout=headers_read_timeout,
            idle_timeout=idle_timeout,
            replay_cache=replay_cache,
            response=response,
        )

        fly_http_options.additional_properties = d
        return fly_http_options

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
