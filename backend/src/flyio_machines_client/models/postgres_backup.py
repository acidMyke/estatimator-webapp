from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.postgres_backup_type import PostgresBackupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresBackup")


@_attrs_define
class PostgresBackup:
    """
    Attributes:
        finished_at (str | Unset): RFC 3339 stop timestamp.
        id (str | Unset): Backup ID.
        size_bytes (int | Unset): Backup size in bytes.
        started_at (str | Unset): RFC 3339 start timestamp.
        status (str | Unset): Backup status. Example: completed.
        type_ (PostgresBackupType | Unset): Backup type.
    """

    finished_at: str | Unset = UNSET
    id: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    started_at: str | Unset = UNSET
    status: str | Unset = UNSET
    type_: PostgresBackupType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finished_at = self.finished_at

        id = self.id

        size_bytes = self.size_bytes

        started_at = self.started_at

        status = self.status

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        finished_at = d.pop("finished_at", UNSET)

        id = d.pop("id", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        started_at = d.pop("started_at", UNSET)

        status = d.pop("status", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PostgresBackupType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostgresBackupType(_type_)

        postgres_backup = cls(
            finished_at=finished_at,
            id=id,
            size_bytes=size_bytes,
            started_at=started_at,
            status=status,
            type_=type_,
        )

        postgres_backup.additional_properties = d
        return postgres_backup

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
