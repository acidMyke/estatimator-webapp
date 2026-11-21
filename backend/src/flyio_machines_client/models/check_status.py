from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_status_status import CheckStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckStatus")


@_attrs_define
class CheckStatus:
    """
    Attributes:
        name (str | Unset): Name of the check: the key of a top-level check in `config.checks`, or
            `servicecheck-<index>-<type>-<internal_port>` for a check defined in a service.
        output (str | Unset): Output of the most recent check run, such as an error message.
        status (CheckStatusStatus | Unset): Result of the check: `passing`, `warning`, or `critical`.
        updated_at (str | Unset): When the check's status was last updated.
    """

    name: str | Unset = UNSET
    output: str | Unset = UNSET
    status: CheckStatusStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        output = self.output

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if output is not UNSET:
            field_dict["output"] = output
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        output = d.pop("output", UNSET)

        _status = d.pop("status", UNSET)
        status: CheckStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CheckStatusStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        check_status = cls(
            name=name,
            output=output,
            status=status,
            updated_at=updated_at,
        )

        check_status.additional_properties = d
        return check_status

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
