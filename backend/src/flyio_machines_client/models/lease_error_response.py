from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lease_error_response_status import LeaseErrorResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaseErrorResponse")


@_attrs_define
class LeaseErrorResponse:
    """
    Attributes:
        message (str | Unset): What went wrong.
        status (LeaseErrorResponseStatus | Unset): Always `error`.
    """

    message: str | Unset = UNSET
    status: LeaseErrorResponseStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _status = d.pop("status", UNSET)
        status: LeaseErrorResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LeaseErrorResponseStatus(_status)

        lease_error_response = cls(
            message=message,
            status=status,
        )

        lease_error_response.additional_properties = d
        return lease_error_response

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
