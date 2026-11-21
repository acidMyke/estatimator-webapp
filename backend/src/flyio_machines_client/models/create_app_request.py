from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAppRequest")


@_attrs_define
class CreateAppRequest:
    """
    Attributes:
        enable_subdomains (bool | Unset): Request a wildcard TLS certificate for *.svc.<app-name>.fly.dev. Defaults to
            false. Certificate provisioning is asynchronous; this does not create services or configure their routing.
        idempotency_key (str | Unset): When set, makes a retry of this exact request safe: a
            second create with the same key and the same name (or no name) returns
            the app the first request created, instead of erroring on a false name
            conflict or creating a duplicate. A second create with the same key
            but a *different* name is rejected outright; it won't silently
            hand back the first app.
        name (str | Unset): Globally unique name for the app. Required.
        network (str | Unset): Name of the organization's private network to attach the app to. Creates the network if
            it does not exist. Omit, use an empty string, or use "default" to select the organization's default network.
        org_slug (str | Unset): Slug of the organization that will own the app, or "personal" for your personal
            organization. Required.
    """

    enable_subdomains: bool | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    name: str | Unset = UNSET
    network: str | Unset = UNSET
    org_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_subdomains = self.enable_subdomains

        idempotency_key = self.idempotency_key

        name = self.name

        network = self.network

        org_slug = self.org_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_subdomains is not UNSET:
            field_dict["enable_subdomains"] = enable_subdomains
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if name is not UNSET:
            field_dict["name"] = name
        if network is not UNSET:
            field_dict["network"] = network
        if org_slug is not UNSET:
            field_dict["org_slug"] = org_slug

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable_subdomains = d.pop("enable_subdomains", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        name = d.pop("name", UNSET)

        network = d.pop("network", UNSET)

        org_slug = d.pop("org_slug", UNSET)

        create_app_request = cls(
            enable_subdomains=enable_subdomains,
            idempotency_key=idempotency_key,
            name=name,
            network=network,
            org_slug=org_slug,
        )

        create_app_request.additional_properties = d
        return create_app_request

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
