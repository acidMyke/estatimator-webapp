from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app import App


T = TypeVar("T", bound="ListAppsResponse")


@_attrs_define
class ListAppsResponse:
    """
    Attributes:
        apps (list[App] | Unset): The apps on this page, or all apps if `limit` was not provided.
        next_cursor (str | Unset): Pagination cursor for the next page. Absent when no more apps remain.
            Cursors expire 30 minutes after the first page was requested.
        total_apps (int | Unset): The number of matching apps across all pages. With an organization-wide
            token, it is counted when the first page is requested and not updated
            afterwards, so it excludes apps created later and includes apps deleted
            while paginating. With an app-scoped token, such as a deploy token, it is
            recounted on each page and includes only the apps the token can read.
            Either way, it may differ slightly from the number of apps returned.
    """

    apps: list[App] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    total_apps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        next_cursor = self.next_cursor

        total_apps = self.total_apps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if total_apps is not UNSET:
            field_dict["total_apps"] = total_apps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app import App

        d = dict(src_dict)
        _apps = d.pop("apps", UNSET)
        apps: list[App] | Unset = UNSET
        if _apps is not UNSET:
            apps = []
            for apps_item_data in _apps:
                apps_item = App.from_dict(apps_item_data)

                apps.append(apps_item)

        next_cursor = d.pop("next_cursor", UNSET)

        total_apps = d.pop("total_apps", UNSET)

        list_apps_response = cls(
            apps=apps,
            next_cursor=next_cursor,
            total_apps=total_apps,
        )

        list_apps_response.additional_properties = d
        return list_apps_response

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
