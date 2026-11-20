from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestorePostgresClusterRequest")


@_attrs_define
class RestorePostgresClusterRequest:
    """
    Attributes:
        backup_id (str | Unset): Backup label to restore from, as returned by the backups list. Mutually exclusive with
            pitr_time.
        name (str | Unset): Name for the restored cluster. Defaults to a generated name derived from the source cluster
            and backup/point in time when omitted or blank.
        pitr_time (str | Unset): Point in time to restore to, as an RFC3339 timestamp with an explicit offset from UTC
            (e.g. Z or +02:00). Normalized to UTC and must fall within the cluster's PITR recovery window. Mutually
            exclusive with backup_id.
    """

    backup_id: str | Unset = UNSET
    name: str | Unset = UNSET
    pitr_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_id = self.backup_id

        name = self.name

        pitr_time = self.pitr_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_id is not UNSET:
            field_dict["backup_id"] = backup_id
        if name is not UNSET:
            field_dict["name"] = name
        if pitr_time is not UNSET:
            field_dict["pitr_time"] = pitr_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backup_id = d.pop("backup_id", UNSET)

        name = d.pop("name", UNSET)

        pitr_time = d.pop("pitr_time", UNSET)

        restore_postgres_cluster_request = cls(
            backup_id=backup_id,
            name=name,
            pitr_time=pitr_time,
        )

        restore_postgres_cluster_request.additional_properties = d
        return restore_postgres_cluster_request

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
