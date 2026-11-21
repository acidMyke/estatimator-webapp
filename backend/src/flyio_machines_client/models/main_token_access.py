from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resset_action import RessetAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="MainTokenAccess")


@_attrs_define
class MainTokenAccess:
    """
    Attributes:
        action (RessetAction | Unset):
        app_feature (str | Unset): AppFeature is a named set of functionality associated with the app. If
            this is specified, the AppName field must be set.
              - images: images in the fly.io registry
        app_name (str | Unset): AppName is the name of the app being accessed.
        command (list[str] | Unset): Command is the command being executed on a machine. If this is specified,
            the Machine must be set.
        machine_feature (str | Unset): MachineFeature is a named set of functionality associated with the
            machine. If this is specified, the Machine field must be set.
              - metadata: machine metadata service
              - oidc: OIDC tokens
              - kmstoken: Petsem tokens for KMS access
        machine_id (str | Unset): MachineID is the ID of the machine being accessed (e.g. 7811701f564258).
        mutation (str | Unset): Mutation is the GraphQL mutation being performed.
        org_feature (str | Unset): OrgFeature is a named set of functionality associated with the
            organization. If this is specified, the OrgSlug field must be set.
              - wg: WireGuard peers
              - builder: remote builders
              - addon: addons
              - membership: organization membership
              - billing: billing
              - litefs-cloud: LiteFS Cloud
              - authentication: authentication settings
        org_slug (str | Unset): OrgSlug is the slug of the organization being accessed.
        source_machine (str | Unset): SourceMachine is the machine ID of the actor attempting access.
        storage_object (str | Unset): StorageObject is the storage object being accessed. If this is specified,
            the OrgSlug must be set.
        volume_id (str | Unset): VolumeID is the encoded ID of the volume being accessed (e.g.
            vol_r1p6pln1k9m9j7zr).
    """

    action: RessetAction | Unset = UNSET
    app_feature: str | Unset = UNSET
    app_name: str | Unset = UNSET
    command: list[str] | Unset = UNSET
    machine_feature: str | Unset = UNSET
    machine_id: str | Unset = UNSET
    mutation: str | Unset = UNSET
    org_feature: str | Unset = UNSET
    org_slug: str | Unset = UNSET
    source_machine: str | Unset = UNSET
    storage_object: str | Unset = UNSET
    volume_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: int | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        app_feature = self.app_feature

        app_name = self.app_name

        command: list[str] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command

        machine_feature = self.machine_feature

        machine_id = self.machine_id

        mutation = self.mutation

        org_feature = self.org_feature

        org_slug = self.org_slug

        source_machine = self.source_machine

        storage_object = self.storage_object

        volume_id = self.volume_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if app_feature is not UNSET:
            field_dict["app_feature"] = app_feature
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if command is not UNSET:
            field_dict["command"] = command
        if machine_feature is not UNSET:
            field_dict["machine_feature"] = machine_feature
        if machine_id is not UNSET:
            field_dict["machine_id"] = machine_id
        if mutation is not UNSET:
            field_dict["mutation"] = mutation
        if org_feature is not UNSET:
            field_dict["org_feature"] = org_feature
        if org_slug is not UNSET:
            field_dict["org_slug"] = org_slug
        if source_machine is not UNSET:
            field_dict["source_machine"] = source_machine
        if storage_object is not UNSET:
            field_dict["storage_object"] = storage_object
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id

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

        app_name = d.pop("app_name", UNSET)

        command = cast(list[str], d.pop("command", UNSET))

        machine_feature = d.pop("machine_feature", UNSET)

        machine_id = d.pop("machine_id", UNSET)

        mutation = d.pop("mutation", UNSET)

        org_feature = d.pop("org_feature", UNSET)

        org_slug = d.pop("org_slug", UNSET)

        source_machine = d.pop("source_machine", UNSET)

        storage_object = d.pop("storage_object", UNSET)

        volume_id = d.pop("volume_id", UNSET)

        main_token_access = cls(
            action=action,
            app_feature=app_feature,
            app_name=app_name,
            command=command,
            machine_feature=machine_feature,
            machine_id=machine_id,
            mutation=mutation,
            org_feature=org_feature,
            org_slug=org_slug,
            source_machine=source_machine,
            storage_object=storage_object,
            volume_id=volume_id,
        )

        main_token_access.additional_properties = d
        return main_token_access

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
