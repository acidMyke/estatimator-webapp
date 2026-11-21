from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateValidationError")


@_attrs_define
class CertificateValidationError:
    """
    Attributes:
        code (str | Unset): Machine-readable error code.
        message (str | Unset): Human-readable description of the problem.
        remediation (str | Unset): How to fix the problem, if known.
        timestamp (str | Unset): When the problem was detected.
    """

    code: str | Unset = UNSET
    message: str | Unset = UNSET
    remediation: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        remediation = self.remediation

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if remediation is not UNSET:
            field_dict["remediation"] = remediation
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        remediation = d.pop("remediation", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        certificate_validation_error = cls(
            code=code,
            message=message,
            remediation=remediation,
            timestamp=timestamp,
        )

        certificate_validation_error.additional_properties = d
        return certificate_validation_error

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
