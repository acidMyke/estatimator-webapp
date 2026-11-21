from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_entry import CertificateEntry
    from ..models.certificate_validation import CertificateValidation
    from ..models.certificate_validation_error import CertificateValidationError
    from ..models.dns_requirements import DNSRequirements


T = TypeVar("T", bound="DestroyCustomCertificateResponse")


@_attrs_define
class DestroyCustomCertificateResponse:
    """
    Attributes:
        acme_requested (bool | Unset): Whether Fly.io-issued (ACME) certificates were requested for the hostname.
        certificates (list[CertificateEntry] | Unset): The hostname's certificates: at most one custom entry and one
            Fly.io entry.
        configured (bool | Unset): Whether ownership of the hostname has been verified.
        dns_provider (str | Unset): DNS provider detected for the hostname, if known.
        dns_requirements (DNSRequirements | Unset):
        hostname (str | Unset): The hostname the certificate is for. May start with `*.` for a wildcard certificate.
        rate_limited_until (str | Unset): If Let's Encrypt is rate-limiting certificate requests for the hostname, when
            that ends.
        status (str | Unset): Human-readable status: `Ready`, `Awaiting certificates`, `Awaiting configuration`, or a
            hint about what is misconfigured.
        validation (CertificateValidation | Unset):
        validation_errors (list[CertificateValidationError] | Unset): Problems found by the most recent validation.
        warning (str | Unset): Set when no ACME certificates are configured for the hostname either, so it no longer has
            any certificate.
    """

    acme_requested: bool | Unset = UNSET
    certificates: list[CertificateEntry] | Unset = UNSET
    configured: bool | Unset = UNSET
    dns_provider: str | Unset = UNSET
    dns_requirements: DNSRequirements | Unset = UNSET
    hostname: str | Unset = UNSET
    rate_limited_until: str | Unset = UNSET
    status: str | Unset = UNSET
    validation: CertificateValidation | Unset = UNSET
    validation_errors: list[CertificateValidationError] | Unset = UNSET
    warning: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acme_requested = self.acme_requested

        certificates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()
                certificates.append(certificates_item)

        configured = self.configured

        dns_provider = self.dns_provider

        dns_requirements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns_requirements, Unset):
            dns_requirements = self.dns_requirements.to_dict()

        hostname = self.hostname

        rate_limited_until = self.rate_limited_until

        status = self.status

        validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        validation_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = []
            for validation_errors_item_data in self.validation_errors:
                validation_errors_item = validation_errors_item_data.to_dict()
                validation_errors.append(validation_errors_item)

        warning = self.warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acme_requested is not UNSET:
            field_dict["acme_requested"] = acme_requested
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if configured is not UNSET:
            field_dict["configured"] = configured
        if dns_provider is not UNSET:
            field_dict["dns_provider"] = dns_provider
        if dns_requirements is not UNSET:
            field_dict["dns_requirements"] = dns_requirements
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if rate_limited_until is not UNSET:
            field_dict["rate_limited_until"] = rate_limited_until
        if status is not UNSET:
            field_dict["status"] = status
        if validation is not UNSET:
            field_dict["validation"] = validation
        if validation_errors is not UNSET:
            field_dict["validation_errors"] = validation_errors
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.certificate_entry import CertificateEntry
        from ..models.certificate_validation import CertificateValidation
        from ..models.certificate_validation_error import CertificateValidationError
        from ..models.dns_requirements import DNSRequirements

        d = dict(src_dict)
        acme_requested = d.pop("acme_requested", UNSET)

        _certificates = d.pop("certificates", UNSET)
        certificates: list[CertificateEntry] | Unset = UNSET
        if _certificates is not UNSET:
            certificates = []
            for certificates_item_data in _certificates:
                certificates_item = CertificateEntry.from_dict(certificates_item_data)

                certificates.append(certificates_item)

        configured = d.pop("configured", UNSET)

        dns_provider = d.pop("dns_provider", UNSET)

        _dns_requirements = d.pop("dns_requirements", UNSET)
        dns_requirements: DNSRequirements | Unset
        if isinstance(_dns_requirements, Unset):
            dns_requirements = UNSET
        else:
            dns_requirements = DNSRequirements.from_dict(_dns_requirements)

        hostname = d.pop("hostname", UNSET)

        rate_limited_until = d.pop("rate_limited_until", UNSET)

        status = d.pop("status", UNSET)

        _validation = d.pop("validation", UNSET)
        validation: CertificateValidation | Unset
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = CertificateValidation.from_dict(_validation)

        _validation_errors = d.pop("validation_errors", UNSET)
        validation_errors: list[CertificateValidationError] | Unset = UNSET
        if _validation_errors is not UNSET:
            validation_errors = []
            for validation_errors_item_data in _validation_errors:
                validation_errors_item = CertificateValidationError.from_dict(
                    validation_errors_item_data
                )

                validation_errors.append(validation_errors_item)

        warning = d.pop("warning", UNSET)

        destroy_custom_certificate_response = cls(
            acme_requested=acme_requested,
            certificates=certificates,
            configured=configured,
            dns_provider=dns_provider,
            dns_requirements=dns_requirements,
            hostname=hostname,
            rate_limited_until=rate_limited_until,
            status=status,
            validation=validation,
            validation_errors=validation_errors,
            warning=warning,
        )

        destroy_custom_certificate_response.additional_properties = d
        return destroy_custom_certificate_response

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
