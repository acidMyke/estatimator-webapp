from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postgres_cluster_summary_plan import PostgresClusterSummaryPlan
from ..models.postgres_cluster_summary_status import PostgresClusterSummaryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgres_attached_app import PostgresAttachedApp


T = TypeVar("T", bound="PostgresClusterSummary")


@_attrs_define
class PostgresClusterSummary:
    """
    Attributes:
        attached_apps (list[PostgresAttachedApp] | Unset): Apps attached to the cluster.
        created_at (datetime.datetime | Unset): RFC 3339 creation timestamp.
        deleted_at (str | Unset): RFC 3339 deletion timestamp; present for deleted clusters.
        id (str | Unset): Cluster ID.
        name (str | Unset): Cluster name.
        plan (PostgresClusterSummaryPlan | Unset): Plan slug. Example: basic.
        region (str | Unset): Fly region code. Example: iad.
        status (PostgresClusterSummaryStatus | Unset): Current lifecycle status. Example: ready.
    """

    attached_apps: list[PostgresAttachedApp] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    deleted_at: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    plan: PostgresClusterSummaryPlan | Unset = UNSET
    region: str | Unset = UNSET
    status: PostgresClusterSummaryStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attached_apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attached_apps, Unset):
            attached_apps = []
            for attached_apps_item_data in self.attached_apps:
                attached_apps_item = attached_apps_item_data.to_dict()
                attached_apps.append(attached_apps_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at = self.deleted_at

        id = self.id

        name = self.name

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        region = self.region

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attached_apps is not UNSET:
            field_dict["attached_apps"] = attached_apps
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if plan is not UNSET:
            field_dict["plan"] = plan
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.postgres_attached_app import PostgresAttachedApp

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

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        deleted_at = d.pop("deleted_at", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: PostgresClusterSummaryPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = PostgresClusterSummaryPlan(_plan)

        region = d.pop("region", UNSET)

        _status = d.pop("status", UNSET)
        status: PostgresClusterSummaryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostgresClusterSummaryStatus(_status)

        postgres_cluster_summary = cls(
            attached_apps=attached_apps,
            created_at=created_at,
            deleted_at=deleted_at,
            id=id,
            name=name,
            plan=plan,
            region=region,
            status=status,
        )

        postgres_cluster_summary.additional_properties = d
        return postgres_cluster_summary

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
