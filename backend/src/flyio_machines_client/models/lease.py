from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Lease")


@_attrs_define
class Lease:
    """
    Attributes:
        description (str | Unset): Description or reason for the lease.
        expires_at (int | Unset): When the lease expires, in Unix seconds.
        nonce (str | Unset): Unique ID generated for the lease. Pass it in the `fly-machine-lease-nonce` header to
            act on the leased Machine, refresh the lease, or release it.
        owner (str | Unset): Email address of the user who acquired the lease.
        version (str | Unset): ID of the Machine's version at the time of the request.
    """

    description: str | Unset = UNSET
    expires_at: int | Unset = UNSET
    nonce: str | Unset = UNSET
    owner: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        expires_at = self.expires_at

        nonce = self.nonce

        owner = self.owner

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if owner is not UNSET:
            field_dict["owner"] = owner
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        nonce = d.pop("nonce", UNSET)

        owner = d.pop("owner", UNSET)

        version = d.pop("version", UNSET)

        lease = cls(
            description=description,
            expires_at=expires_at,
            nonce=nonce,
            owner=owner,
            version=version,
        )

        lease.additional_properties = d
        return lease

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
