from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_postgres_cluster_request_pg_major_version import (
    CreatePostgresClusterRequestPgMajorVersion,
)
from ..models.create_postgres_cluster_request_plan import (
    CreatePostgresClusterRequestPlan,
)
from ..models.create_postgres_cluster_request_pool_mode import (
    CreatePostgresClusterRequestPoolMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePostgresClusterRequest")


@_attrs_define
class CreatePostgresClusterRequest:
    """
    Attributes:
        org_slug (str): Slug of the organization that will own the cluster, or "personal" for the caller's personal
            organization. Example: my-org.
        plan (CreatePostgresClusterRequestPlan): Plan slug selecting CPU, memory, and disk sizing. Matched case-
            insensitively. Example: basic.
        region (str): Fly region code where the cluster's primary runs. Example: iad.
        disk_size_gb (int | Unset): Disk size in gigabytes. Example: 10.
        name (str | Unset): Name for the cluster. A name is generated when omitted.
        pg_major_version (CreatePostgresClusterRequestPgMajorVersion | Unset): Postgres major version. Example: 17.
        pool_mode (CreatePostgresClusterRequestPoolMode | Unset): Connection pooler mode. Example: transaction.
        postgis_enabled (bool | Unset): Enable PostGIS support, required to later enable PostGIS extensions.
    """

    org_slug: str
    plan: CreatePostgresClusterRequestPlan
    region: str
    disk_size_gb: int | Unset = UNSET
    name: str | Unset = UNSET
    pg_major_version: CreatePostgresClusterRequestPgMajorVersion | Unset = UNSET
    pool_mode: CreatePostgresClusterRequestPoolMode | Unset = UNSET
    postgis_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_slug = self.org_slug

        plan = self.plan.value

        region = self.region

        disk_size_gb = self.disk_size_gb

        name = self.name

        pg_major_version: str | Unset = UNSET
        if not isinstance(self.pg_major_version, Unset):
            pg_major_version = self.pg_major_version.value

        pool_mode: str | Unset = UNSET
        if not isinstance(self.pool_mode, Unset):
            pool_mode = self.pool_mode.value

        postgis_enabled = self.postgis_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_slug": org_slug,
                "plan": plan,
                "region": region,
            }
        )
        if disk_size_gb is not UNSET:
            field_dict["disk_size_gb"] = disk_size_gb
        if name is not UNSET:
            field_dict["name"] = name
        if pg_major_version is not UNSET:
            field_dict["pg_major_version"] = pg_major_version
        if pool_mode is not UNSET:
            field_dict["pool_mode"] = pool_mode
        if postgis_enabled is not UNSET:
            field_dict["postgis_enabled"] = postgis_enabled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        org_slug = d.pop("org_slug")

        plan = CreatePostgresClusterRequestPlan(d.pop("plan"))

        region = d.pop("region")

        disk_size_gb = d.pop("disk_size_gb", UNSET)

        name = d.pop("name", UNSET)

        _pg_major_version = d.pop("pg_major_version", UNSET)
        pg_major_version: CreatePostgresClusterRequestPgMajorVersion | Unset
        if isinstance(_pg_major_version, Unset):
            pg_major_version = UNSET
        else:
            pg_major_version = CreatePostgresClusterRequestPgMajorVersion(
                _pg_major_version
            )

        _pool_mode = d.pop("pool_mode", UNSET)
        pool_mode: CreatePostgresClusterRequestPoolMode | Unset
        if isinstance(_pool_mode, Unset):
            pool_mode = UNSET
        else:
            pool_mode = CreatePostgresClusterRequestPoolMode(_pool_mode)

        postgis_enabled = d.pop("postgis_enabled", UNSET)

        create_postgres_cluster_request = cls(
            org_slug=org_slug,
            plan=plan,
            region=region,
            disk_size_gb=disk_size_gb,
            name=name,
            pg_major_version=pg_major_version,
            pool_mode=pool_mode,
            postgis_enabled=postgis_enabled,
        )

        create_postgres_cluster_request.additional_properties = d
        return create_postgres_cluster_request

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
