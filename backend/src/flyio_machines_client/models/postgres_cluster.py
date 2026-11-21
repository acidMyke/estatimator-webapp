from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postgres_cluster_cpu_kind import PostgresClusterCpuKind
from ..models.postgres_cluster_pg_major_version import PostgresClusterPgMajorVersion
from ..models.postgres_cluster_plan import PostgresClusterPlan
from ..models.postgres_cluster_status import PostgresClusterStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_ref import OrganizationRef
    from ..models.postgres_attached_app import PostgresAttachedApp
    from ..models.postgres_cluster_endpoints import PostgresClusterEndpoints


T = TypeVar("T", bound="PostgresCluster")


@_attrs_define
class PostgresCluster:
    """
    Attributes:
        attached_apps (list[PostgresAttachedApp] | Unset): Apps attached to the cluster.
        cpu_kind (PostgresClusterCpuKind | Unset): CPU class. Example: shared.
        cpus (int | Unset): vCPUs per node. Example: 2.
        created_at (datetime.datetime | Unset): RFC 3339 creation timestamp.
        disk_size_gb (int | Unset): Disk size in gigabytes, for one replica. Example: 10.
        endpoints (PostgresClusterEndpoints | Unset):
        id (str | Unset): Cluster ID.
        memory_mb (int | Unset): Memory per node in megabytes. Example: 1024.
        name (str | Unset): Cluster name.
        organization (OrganizationRef | Unset):
        pg_major_version (PostgresClusterPgMajorVersion | Unset): Postgres major version. Example: 17.
        plan (PostgresClusterPlan | Unset): Plan slug. Example: basic.
        postgis_enabled (bool | Unset): Whether PostGIS support is enabled.
        region (str | Unset): Fly region code. Example: iad.
        replicas (int | Unset): Number of replicas. Example: 1.
        status (PostgresClusterStatus | Unset): Current lifecycle status. Example: ready.
        storage_provisioned_bytes (int | None | Unset): Storage provisioned, summed across the cluster's volumes and
            measured hourly.
            Null until first measured. Example: 10737418240.
        storage_used_bytes (int | None | Unset): Storage used, summed across the cluster's volumes and measured hourly.
            Null
            until first measured. Example: 5368709120.
    """

    attached_apps: list[PostgresAttachedApp] | Unset = UNSET
    cpu_kind: PostgresClusterCpuKind | Unset = UNSET
    cpus: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    disk_size_gb: int | Unset = UNSET
    endpoints: PostgresClusterEndpoints | Unset = UNSET
    id: str | Unset = UNSET
    memory_mb: int | Unset = UNSET
    name: str | Unset = UNSET
    organization: OrganizationRef | Unset = UNSET
    pg_major_version: PostgresClusterPgMajorVersion | Unset = UNSET
    plan: PostgresClusterPlan | Unset = UNSET
    postgis_enabled: bool | Unset = UNSET
    region: str | Unset = UNSET
    replicas: int | Unset = UNSET
    status: PostgresClusterStatus | Unset = UNSET
    storage_provisioned_bytes: int | None | Unset = UNSET
    storage_used_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attached_apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attached_apps, Unset):
            attached_apps = []
            for attached_apps_item_data in self.attached_apps:
                attached_apps_item = attached_apps_item_data.to_dict()
                attached_apps.append(attached_apps_item)

        cpu_kind: str | Unset = UNSET
        if not isinstance(self.cpu_kind, Unset):
            cpu_kind = self.cpu_kind.value

        cpus = self.cpus

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        disk_size_gb = self.disk_size_gb

        endpoints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints.to_dict()

        id = self.id

        memory_mb = self.memory_mb

        name = self.name

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        pg_major_version: str | Unset = UNSET
        if not isinstance(self.pg_major_version, Unset):
            pg_major_version = self.pg_major_version.value

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        postgis_enabled = self.postgis_enabled

        region = self.region

        replicas = self.replicas

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_provisioned_bytes: int | None | Unset
        if isinstance(self.storage_provisioned_bytes, Unset):
            storage_provisioned_bytes = UNSET
        else:
            storage_provisioned_bytes = self.storage_provisioned_bytes

        storage_used_bytes: int | None | Unset
        if isinstance(self.storage_used_bytes, Unset):
            storage_used_bytes = UNSET
        else:
            storage_used_bytes = self.storage_used_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attached_apps is not UNSET:
            field_dict["attached_apps"] = attached_apps
        if cpu_kind is not UNSET:
            field_dict["cpu_kind"] = cpu_kind
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if disk_size_gb is not UNSET:
            field_dict["disk_size_gb"] = disk_size_gb
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if id is not UNSET:
            field_dict["id"] = id
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb
        if name is not UNSET:
            field_dict["name"] = name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if pg_major_version is not UNSET:
            field_dict["pg_major_version"] = pg_major_version
        if plan is not UNSET:
            field_dict["plan"] = plan
        if postgis_enabled is not UNSET:
            field_dict["postgis_enabled"] = postgis_enabled
        if region is not UNSET:
            field_dict["region"] = region
        if replicas is not UNSET:
            field_dict["replicas"] = replicas
        if status is not UNSET:
            field_dict["status"] = status
        if storage_provisioned_bytes is not UNSET:
            field_dict["storage_provisioned_bytes"] = storage_provisioned_bytes
        if storage_used_bytes is not UNSET:
            field_dict["storage_used_bytes"] = storage_used_bytes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.organization_ref import OrganizationRef
        from ..models.postgres_attached_app import PostgresAttachedApp
        from ..models.postgres_cluster_endpoints import PostgresClusterEndpoints

        d = dict(src_dict)
        _attached_apps = d.pop("attached_apps", UNSET)
        attached_apps: list[PostgresAttachedApp] | Unset = UNSET
        if _attached_apps is not UNSET:
            attached_apps = []
            for attached_apps_item_data in _attached_apps:
                attached_apps_item = PostgresAttachedApp.from_dict(
                    attached_apps_item_data
                )

                attached_apps.append(attached_apps_item)

        _cpu_kind = d.pop("cpu_kind", UNSET)
        cpu_kind: PostgresClusterCpuKind | Unset
        if isinstance(_cpu_kind, Unset):
            cpu_kind = UNSET
        else:
            cpu_kind = PostgresClusterCpuKind(_cpu_kind)

        cpus = d.pop("cpus", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        disk_size_gb = d.pop("disk_size_gb", UNSET)

        _endpoints = d.pop("endpoints", UNSET)
        endpoints: PostgresClusterEndpoints | Unset
        if isinstance(_endpoints, Unset):
            endpoints = UNSET
        else:
            endpoints = PostgresClusterEndpoints.from_dict(_endpoints)

        id = d.pop("id", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        name = d.pop("name", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: OrganizationRef | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = OrganizationRef.from_dict(_organization)

        _pg_major_version = d.pop("pg_major_version", UNSET)
        pg_major_version: PostgresClusterPgMajorVersion | Unset
        if isinstance(_pg_major_version, Unset):
            pg_major_version = UNSET
        else:
            pg_major_version = PostgresClusterPgMajorVersion(_pg_major_version)

        _plan = d.pop("plan", UNSET)
        plan: PostgresClusterPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = PostgresClusterPlan(_plan)

        postgis_enabled = d.pop("postgis_enabled", UNSET)

        region = d.pop("region", UNSET)

        replicas = d.pop("replicas", UNSET)

        _status = d.pop("status", UNSET)
        status: PostgresClusterStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostgresClusterStatus(_status)

        def _parse_storage_provisioned_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_provisioned_bytes = _parse_storage_provisioned_bytes(
            d.pop("storage_provisioned_bytes", UNSET)
        )

        def _parse_storage_used_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_used_bytes = _parse_storage_used_bytes(
            d.pop("storage_used_bytes", UNSET)
        )

        postgres_cluster = cls(
            attached_apps=attached_apps,
            cpu_kind=cpu_kind,
            cpus=cpus,
            created_at=created_at,
            disk_size_gb=disk_size_gb,
            endpoints=endpoints,
            id=id,
            memory_mb=memory_mb,
            name=name,
            organization=organization,
            pg_major_version=pg_major_version,
            plan=plan,
            postgis_enabled=postgis_enabled,
            region=region,
            replicas=replicas,
            status=status,
            storage_provisioned_bytes=storage_provisioned_bytes,
            storage_used_bytes=storage_used_bytes,
        )

        postgres_cluster.additional_properties = d
        return postgres_cluster

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
