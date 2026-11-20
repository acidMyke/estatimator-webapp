from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_secret import AppSecret


T = TypeVar("T", bound="AppSecretsUpdateResp")


@_attrs_define
class AppSecretsUpdateResp:
    """
    Attributes:
        Version (int | Unset): Same value as `version`.

            Deprecated: use `version`.
        secrets (list[AppSecret] | Unset): The secrets from the request, with their new values and digests; deleted
            secrets only
            have a name.
        version (int | Unset): The app's secrets version after this change. Pass it as `min_secrets_version` when
            creating or
            updating Machines so that they are guaranteed to see the change.
    """

    Version: int | Unset = UNSET
    secrets: list[AppSecret] | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        Version = self.Version

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if Version is not UNSET:
            field_dict["Version"] = Version
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_secret import AppSecret

        d = dict(src_dict)
        Version = d.pop("Version", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[AppSecret] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = AppSecret.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        version = d.pop("version", UNSET)

        app_secrets_update_resp = cls(
            Version=Version,
            secrets=secrets,
            version=version,
        )

        app_secrets_update_resp.additional_properties = d
        return app_secrets_update_resp

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
