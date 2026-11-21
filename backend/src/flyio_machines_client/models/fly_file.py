from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyFile")


@_attrs_define
class FlyFile:
    """A file that will be written to the Machine. One of RawValue or SecretName must be set.

    Attributes:
        guest_path (str | Unset): GuestPath is the path on the machine where the file will be written and must be an
            absolute path.
            For example: /full/path/to/file.json
        image_config (str | Unset): The name of an image to use the OCI image config as the file contents.
        mode (int | Unset): Mode bits used to set permissions on this file as accepted by chmod(2).
        raw_value (str | Unset): The base64 encoded string of the file contents.
        secret_name (str | Unset): The name of the secret that contains the base64 encoded file contents.
    """

    guest_path: str | Unset = UNSET
    image_config: str | Unset = UNSET
    mode: int | Unset = UNSET
    raw_value: str | Unset = UNSET
    secret_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guest_path = self.guest_path

        image_config = self.image_config

        mode = self.mode

        raw_value = self.raw_value

        secret_name = self.secret_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guest_path is not UNSET:
            field_dict["guest_path"] = guest_path
        if image_config is not UNSET:
            field_dict["image_config"] = image_config
        if mode is not UNSET:
            field_dict["mode"] = mode
        if raw_value is not UNSET:
            field_dict["raw_value"] = raw_value
        if secret_name is not UNSET:
            field_dict["secret_name"] = secret_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        guest_path = d.pop("guest_path", UNSET)

        image_config = d.pop("image_config", UNSET)

        mode = d.pop("mode", UNSET)

        raw_value = d.pop("raw_value", UNSET)

        secret_name = d.pop("secret_name", UNSET)

        fly_file = cls(
            guest_path=guest_path,
            image_config=image_config,
            mode=mode,
            raw_value=raw_value,
            secret_name=secret_name,
        )

        fly_file.additional_properties = d
        return fly_file

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
