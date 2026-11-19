from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateSummary")


@_attrs_define
class CertificateSummary:
    """
    Attributes:
        acme_alpn_configured (bool | Unset): Whether the hostname points at the app, allowing TLS-ALPN-01 validation.
        acme_dns_configured (bool | Unset): Whether the `_acme-challenge` CNAME record is set up, allowing DNS-01
            validation.
        acme_http_configured (bool | Unset): Whether the hostname points at the app, allowing HTTP-01 validation.
        acme_requested (bool | Unset): Whether Fly.io-issued (ACME) certificates were requested for the hostname.
        configured (bool | Unset): Whether ownership of the hostname has been verified by any of the methods above.
        created_at (str | Unset): When the hostname was added to the app.
        dns_provider (str | Unset): DNS provider detected for the hostname, if known.
        has_custom_certificate (bool | Unset): Whether a custom certificate was uploaded for the hostname.
        has_fly_certificate (bool | Unset): Whether Fly.io has issued certificates for the hostname.
        hostname (str | Unset): The hostname the certificate is for. May start with `*.` for a wildcard certificate.
        ownership_txt_configured (bool | Unset): Whether the `_fly-ownership` TXT record is set up.
        status (str | Unset): Human-readable status: `Ready`, `Awaiting certificates`, `Awaiting configuration`, or a
            hint about what is misconfigured.
        updated_at (str | Unset): When the hostname's certificate configuration last changed.
    """

    acme_alpn_configured: bool | Unset = UNSET
    acme_dns_configured: bool | Unset = UNSET
    acme_http_configured: bool | Unset = UNSET
    acme_requested: bool | Unset = UNSET
    configured: bool | Unset = UNSET
    created_at: str | Unset = UNSET
    dns_provider: str | Unset = UNSET
    has_custom_certificate: bool | Unset = UNSET
    has_fly_certificate: bool | Unset = UNSET
    hostname: str | Unset = UNSET
    ownership_txt_configured: bool | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acme_alpn_configured = self.acme_alpn_configured

        acme_dns_configured = self.acme_dns_configured

        acme_http_configured = self.acme_http_configured

        acme_requested = self.acme_requested

        configured = self.configured

        created_at = self.created_at

        dns_provider = self.dns_provider

        has_custom_certificate = self.has_custom_certificate

        has_fly_certificate = self.has_fly_certificate

        hostname = self.hostname

        ownership_txt_configured = self.ownership_txt_configured

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acme_alpn_configured is not UNSET:
            field_dict["acme_alpn_configured"] = acme_alpn_configured
        if acme_dns_configured is not UNSET:
            field_dict["acme_dns_configured"] = acme_dns_configured
        if acme_http_configured is not UNSET:
            field_dict["acme_http_configured"] = acme_http_configured
        if acme_requested is not UNSET:
            field_dict["acme_requested"] = acme_requested
        if configured is not UNSET:
            field_dict["configured"] = configured
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if dns_provider is not UNSET:
            field_dict["dns_provider"] = dns_provider
        if has_custom_certificate is not UNSET:
            field_dict["has_custom_certificate"] = has_custom_certificate
        if has_fly_certificate is not UNSET:
            field_dict["has_fly_certificate"] = has_fly_certificate
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ownership_txt_configured is not UNSET:
            field_dict["ownership_txt_configured"] = ownership_txt_configured
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        acme_alpn_configured = d.pop("acme_alpn_configured", UNSET)

        acme_dns_configured = d.pop("acme_dns_configured", UNSET)

        acme_http_configured = d.pop("acme_http_configured", UNSET)

        acme_requested = d.pop("acme_requested", UNSET)

        configured = d.pop("configured", UNSET)

        created_at = d.pop("created_at", UNSET)

        dns_provider = d.pop("dns_provider", UNSET)

        has_custom_certificate = d.pop("has_custom_certificate", UNSET)

        has_fly_certificate = d.pop("has_fly_certificate", UNSET)

        hostname = d.pop("hostname", UNSET)

        ownership_txt_configured = d.pop("ownership_txt_configured", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        certificate_summary = cls(
            acme_alpn_configured=acme_alpn_configured,
            acme_dns_configured=acme_dns_configured,
            acme_http_configured=acme_http_configured,
            acme_requested=acme_requested,
            configured=configured,
            created_at=created_at,
            dns_provider=dns_provider,
            has_custom_certificate=has_custom_certificate,
            has_fly_certificate=has_fly_certificate,
            hostname=hostname,
            ownership_txt_configured=ownership_txt_configured,
            status=status,
            updated_at=updated_at,
        )

        certificate_summary.additional_properties = d
        return certificate_summary

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
