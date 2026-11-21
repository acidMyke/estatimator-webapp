from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resset_action import RessetAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlyioAccess")


@_attrs_define
class FlyioAccess:
    """
    Attributes:
        action (RessetAction | Unset):
        app_feature (str | Unset):
        appid (int | Unset):
        cluster (str | Unset):
        command (list[str] | Unset):
        feature (str | Unset):
        machine (str | Unset):
        machine_feature (str | Unset):
        mutation (str | Unset):
        orgid (int | Unset):
        source_app (str | Unset):
        source_machine (str | Unset):
        source_organization (str | Unset):
        storage_object (str | Unset):
        volume (str | Unset):
    """

    action: RessetAction | Unset = UNSET
    app_feature: str | Unset = UNSET
    appid: int | Unset = UNSET
    cluster: str | Unset = UNSET
    command: list[str] | Unset = UNSET
    feature: str | Unset = UNSET
    machine: str | Unset = UNSET
    machine_feature: str | Unset = UNSET
    mutation: str | Unset = UNSET
    orgid: int | Unset = UNSET
    source_app: str | Unset = UNSET
    source_machine: str | Unset = UNSET
    source_organization: str | Unset = UNSET
    storage_object: str | Unset = UNSET
    volume: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: int | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        app_feature = self.app_feature

        appid = self.appid

        cluster = self.cluster

        command: list[str] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command

        feature = self.feature

        machine = self.machine

        machine_feature = self.machine_feature

        mutation = self.mutation

        orgid = self.orgid

        source_app = self.source_app

        source_machine = self.source_machine

        source_organization = self.source_organization

        storage_object = self.storage_object

        volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if app_feature is not UNSET:
            field_dict["app_feature"] = app_feature
        if appid is not UNSET:
            field_dict["appid"] = appid
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if command is not UNSET:
            field_dict["command"] = command
        if feature is not UNSET:
            field_dict["feature"] = feature
        if machine is not UNSET:
            field_dict["machine"] = machine
        if machine_feature is not UNSET:
            field_dict["machine_feature"] = machine_feature
        if mutation is not UNSET:
            field_dict["mutation"] = mutation
        if orgid is not UNSET:
            field_dict["orgid"] = orgid
        if source_app is not UNSET:
            field_dict["sourceApp"] = source_app
        if source_machine is not UNSET:
            field_dict["sourceMachine"] = source_machine
        if source_organization is not UNSET:
            field_dict["sourceOrganization"] = source_organization
        if storage_object is not UNSET:
            field_dict["storage_object"] = storage_object
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: RessetAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = RessetAction(_action)

        app_feature = d.pop("app_feature", UNSET)

        appid = d.pop("appid", UNSET)

        cluster = d.pop("cluster", UNSET)

        command = cast(list[str], d.pop("command", UNSET))

        feature = d.pop("feature", UNSET)

        machine = d.pop("machine", UNSET)

        machine_feature = d.pop("machine_feature", UNSET)

        mutation = d.pop("mutation", UNSET)

        orgid = d.pop("orgid", UNSET)

        source_app = d.pop("sourceApp", UNSET)

        source_machine = d.pop("sourceMachine", UNSET)

        source_organization = d.pop("sourceOrganization", UNSET)

        storage_object = d.pop("storage_object", UNSET)

        volume = d.pop("volume", UNSET)

        flyio_access = cls(
            action=action,
            app_feature=app_feature,
            appid=appid,
            cluster=cluster,
            command=command,
            feature=feature,
            machine=machine,
            machine_feature=machine_feature,
            mutation=mutation,
            orgid=orgid,
            source_app=source_app,
            source_machine=source_machine,
            source_organization=source_organization,
            storage_object=storage_object,
            volume=volume,
        )

        flyio_access.additional_properties = d
        return flyio_access

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
