from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.main_status_code import MainStatusCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_details import ErrorResponseDetails


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        details (ErrorResponseDetails | Unset): Deprecated: details about some errors. Do not rely on its contents.
        error (str | Unset): Human-readable description of the error. Its wording may change; use `status` to tell
            errors apart.
        status (MainStatusCode | Unset):
    """

    details: ErrorResponseDetails | Unset = UNSET
    error: str | Unset = UNSET
    status: MainStatusCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        error = self.error

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if error is not UNSET:
            field_dict["error"] = error
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_response_details import ErrorResponseDetails

        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: ErrorResponseDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorResponseDetails.from_dict(_details)

        error = d.pop("error", UNSET)

        _status = d.pop("status", UNSET)
        status: MainStatusCode | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MainStatusCode(_status)

        error_response = cls(
            details=details,
            error=error,
            status=status,
        )

        error_response.additional_properties = d
        return error_response

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
