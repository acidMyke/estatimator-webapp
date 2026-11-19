from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_machine import OrgMachine


T = TypeVar("T", bound="OrgMachinesResponse")


@_attrs_define
class OrgMachinesResponse:
    """
    Attributes:
        error_regions (list[str] | Unset): Regions that could not be queried. Their Machines are missing from the
            response.
        last_machine_id (str | Unset): ID of the last Machine on this page.
        last_updated_at (str | Unset): `updated_at` of the last Machine on this page.
        machines (list[OrgMachine] | Unset): The Machines on this page.
        next_cursor (str | Unset): Pagination cursor for the next page. Absent when no more Machines remain. Cursors
            expire
            30 minutes after the first page was requested.
    """

    error_regions: list[str] | Unset = UNSET
    last_machine_id: str | Unset = UNSET
    last_updated_at: str | Unset = UNSET
    machines: list[OrgMachine] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_regions: list[str] | Unset = UNSET
        if not isinstance(self.error_regions, Unset):
            error_regions = self.error_regions

        last_machine_id = self.last_machine_id

        last_updated_at = self.last_updated_at

        machines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.machines, Unset):
            machines = []
            for machines_item_data in self.machines:
                machines_item = machines_item_data.to_dict()
                machines.append(machines_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_regions is not UNSET:
            field_dict["error_regions"] = error_regions
        if last_machine_id is not UNSET:
            field_dict["last_machine_id"] = last_machine_id
        if last_updated_at is not UNSET:
            field_dict["last_updated_at"] = last_updated_at
        if machines is not UNSET:
            field_dict["machines"] = machines
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.org_machine import OrgMachine

        d = dict(src_dict)
        error_regions = cast(list[str], d.pop("error_regions", UNSET))

        last_machine_id = d.pop("last_machine_id", UNSET)

        last_updated_at = d.pop("last_updated_at", UNSET)

        _machines = d.pop("machines", UNSET)
        machines: list[OrgMachine] | Unset = UNSET
        if _machines is not UNSET:
            machines = []
            for machines_item_data in _machines:
                machines_item = OrgMachine.from_dict(machines_item_data)

                machines.append(machines_item)

        next_cursor = d.pop("next_cursor", UNSET)

        org_machines_response = cls(
            error_regions=error_regions,
            last_machine_id=last_machine_id,
            last_updated_at=last_updated_at,
            machines=machines,
            next_cursor=next_cursor,
        )

        org_machines_response.additional_properties = d
        return org_machines_response

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
