from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgres_extension_installed_type_0 import (
        PostgresExtensionInstalledType0,
    )


T = TypeVar("T", bound="PostgresExtension")


@_attrs_define
class PostgresExtension:
    """
    Attributes:
        default_version (str | Unset): Default version installed when enabled.
        description (str | Unset): Human-readable description.
        installed (None | PostgresExtensionInstalledType0 | Unset): Installation details, or null when the extension is
            not installed.
        name (str | Unset): Extension name. Example: citext.
        system (bool | Unset): Whether this is a system extension that cannot be disabled.
    """

    default_version: str | Unset = UNSET
    description: str | Unset = UNSET
    installed: None | PostgresExtensionInstalledType0 | Unset = UNSET
    name: str | Unset = UNSET
    system: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.postgres_extension_installed_type_0 import (
            PostgresExtensionInstalledType0,
        )

        default_version = self.default_version

        description = self.description

        installed: dict[str, Any] | None | Unset
        if isinstance(self.installed, Unset):
            installed = UNSET
        elif isinstance(self.installed, PostgresExtensionInstalledType0):
            installed = self.installed.to_dict()
        else:
            installed = self.installed

        name = self.name

        system = self.system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_version is not UNSET:
            field_dict["default_version"] = default_version
        if description is not UNSET:
            field_dict["description"] = description
        if installed is not UNSET:
            field_dict["installed"] = installed
        if name is not UNSET:
            field_dict["name"] = name
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.postgres_extension_installed_type_0 import (
            PostgresExtensionInstalledType0,
        )

        d = dict(src_dict)
        default_version = d.pop("default_version", UNSET)

        description = d.pop("description", UNSET)

        def _parse_installed(
            data: object,
        ) -> None | PostgresExtensionInstalledType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installed_type_0 = PostgresExtensionInstalledType0.from_dict(data)

                return installed_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(None | PostgresExtensionInstalledType0 | Unset, data)

        installed = _parse_installed(d.pop("installed", UNSET))

        name = d.pop("name", UNSET)

        system = d.pop("system", UNSET)

        postgres_extension = cls(
            default_version=default_version,
            description=description,
            installed=installed,
            name=name,
            system=system,
        )

        postgres_extension.additional_properties = d
        return postgres_extension

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
