from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyStatic")


@_attrs_define
class FlyStatic:
    """
    Attributes:
        guest_path (str): The path inside the Machine, or inside tigris_bucket when set, where the files to serve are
            located
        url_prefix (str): The URL prefix under which the files are served
        index_document (str | Unset): The document served for requests to the URL prefix or any of its subfolders. Only
            works with tigris_bucket
        tigris_bucket (str | Unset): An existing Tigris bucket belonging to the app to read the files from, instead of
            the Machine's
            filesystem. The files are still served through the Machine
    """

    guest_path: str
    url_prefix: str
    index_document: str | Unset = UNSET
    tigris_bucket: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_path = self.guest_path

        url_prefix = self.url_prefix

        index_document = self.index_document

        tigris_bucket = self.tigris_bucket

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "guest_path": guest_path,
                "url_prefix": url_prefix,
            }
        )
        if index_document is not UNSET:
            field_dict["index_document"] = index_document
        if tigris_bucket is not UNSET:
            field_dict["tigris_bucket"] = tigris_bucket

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        guest_path = d.pop("guest_path")

        url_prefix = d.pop("url_prefix")

        index_document = d.pop("index_document", UNSET)

        tigris_bucket = d.pop("tigris_bucket", UNSET)

        fly_static = cls(
            guest_path=guest_path,
            url_prefix=url_prefix,
            index_document=index_document,
            tigris_bucket=tigris_bucket,
        )

        fly_static.additional_properties = d
        return fly_static

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
