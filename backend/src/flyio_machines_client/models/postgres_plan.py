from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postgres_plan_cpu_kind import PostgresPlanCpuKind
from ..models.postgres_plan_plan import PostgresPlanPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresPlan")


@_attrs_define
class PostgresPlan:
    """
    Attributes:
        cpu_kind (PostgresPlanCpuKind | Unset): CPU class. Example: shared.
        cpus (int | Unset): vCPUs per node. Example: 2.
        memory_mb (int | Unset): Memory per node in megabytes. Example: 1024.
        monthly_price_usd (int | Unset): Base monthly price in US dollars. Example: 38.
        plan (PostgresPlanPlan | Unset): Plan slug. Pass it as `plan` when creating or forking a cluster. Example:
            basic.
    """

    cpu_kind: PostgresPlanCpuKind | Unset = UNSET
    cpus: int | Unset = UNSET
    memory_mb: int | Unset = UNSET
    monthly_price_usd: int | Unset = UNSET
    plan: PostgresPlanPlan | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_kind: str | Unset = UNSET
        if not isinstance(self.cpu_kind, Unset):
            cpu_kind = self.cpu_kind.value

        cpus = self.cpus

        memory_mb = self.memory_mb

        monthly_price_usd = self.monthly_price_usd

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_kind is not UNSET:
            field_dict["cpu_kind"] = cpu_kind
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb
        if monthly_price_usd is not UNSET:
            field_dict["monthly_price_usd"] = monthly_price_usd
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _cpu_kind = d.pop("cpu_kind", UNSET)
        cpu_kind: PostgresPlanCpuKind | Unset
        if isinstance(_cpu_kind, Unset):
            cpu_kind = UNSET
        else:
            cpu_kind = PostgresPlanCpuKind(_cpu_kind)

        cpus = d.pop("cpus", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        monthly_price_usd = d.pop("monthly_price_usd", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: PostgresPlanPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = PostgresPlanPlan(_plan)

        postgres_plan = cls(
            cpu_kind=cpu_kind,
            cpus=cpus,
            memory_mb=memory_mb,
            monthly_price_usd=monthly_price_usd,
            plan=plan,
        )

        postgres_plan.additional_properties = d
        return postgres_plan

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
