from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fly_replay_cache_type import FlyReplayCacheType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyReplayCache")


@_attrs_define
class FlyReplayCache:
    """
    Attributes:
        allow_bypass (bool | Unset): Let clients skip the cache by sending the `fly-replay-cache-control: skip` header
        name (str | Unset): Name of the cookie or header to key the cache on
        path_prefix (str | Unset): Requests whose path starts with this prefix use the rule. May start with a hostname,
            e.g.
            `example.com/api/*`
        ttl_seconds (int | Unset): How long a cached replay is used, in seconds
        type_ (FlyReplayCacheType | Unset): Currently either "cookie" or "header"
    """

    allow_bypass: bool | Unset = UNSET
    name: str | Unset = UNSET
    path_prefix: str | Unset = UNSET
    ttl_seconds: int | Unset = UNSET
    type_: FlyReplayCacheType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_bypass = self.allow_bypass

        name = self.name

        path_prefix = self.path_prefix

        ttl_seconds = self.ttl_seconds

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_bypass is not UNSET:
            field_dict["allow_bypass"] = allow_bypass
        if name is not UNSET:
            field_dict["name"] = name
        if path_prefix is not UNSET:
            field_dict["path_prefix"] = path_prefix
        if ttl_seconds is not UNSET:
            field_dict["ttl_seconds"] = ttl_seconds
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allow_bypass = d.pop("allow_bypass", UNSET)

        name = d.pop("name", UNSET)

        path_prefix = d.pop("path_prefix", UNSET)

        ttl_seconds = d.pop("ttl_seconds", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FlyReplayCacheType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FlyReplayCacheType(_type_)

        fly_replay_cache = cls(
            allow_bypass=allow_bypass,
            name=name,
            path_prefix=path_prefix,
            ttl_seconds=ttl_seconds,
            type_=type_,
        )

        fly_replay_cache.additional_properties = d
        return fly_replay_cache

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
