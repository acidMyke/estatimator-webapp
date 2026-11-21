from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fly_http_response_options_headers_additional_property import (
        FlyHTTPResponseOptionsHeadersAdditionalProperty,
    )


T = TypeVar("T", bound="FlyHTTPResponseOptionsHeaders")


@_attrs_define
class FlyHTTPResponseOptionsHeaders:
    """Response headers to set. A string sets the header, a list of strings sets it to multiple
    values, and false removes it

    """

    additional_properties: dict[
        str, FlyHTTPResponseOptionsHeadersAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fly_http_response_options_headers_additional_property import (
            FlyHTTPResponseOptionsHeadersAdditionalProperty,
        )

        d = dict(src_dict)
        fly_http_response_options_headers = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                FlyHTTPResponseOptionsHeadersAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        fly_http_response_options_headers.additional_properties = additional_properties
        return fly_http_response_options_headers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FlyHTTPResponseOptionsHeadersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: FlyHTTPResponseOptionsHeadersAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
