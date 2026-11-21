from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lease_response_status import LeaseResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lease import Lease


T = TypeVar("T", bound="LeaseResponse")


@_attrs_define
class LeaseResponse:
    """
    Attributes:
        data (Lease | Unset):
        status (LeaseResponseStatus | Unset): Always `success`.
    """

    data: Lease | Unset = UNSET
    status: LeaseResponseStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lease import Lease

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Lease | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Lease.from_dict(_data)

        _status = d.pop("status", UNSET)
        status: LeaseResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LeaseResponseStatus(_status)

        lease_response = cls(
            data=data,
            status=status,
        )

        lease_response.additional_properties = d
        return lease_response

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
