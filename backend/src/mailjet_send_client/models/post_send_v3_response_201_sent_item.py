from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSendV3Response201SentItem")


@_attrs_define
class PostSendV3Response201SentItem:
    """
    Attributes:
        email (str | Unset): The email address for the recipient of this message.
        message_id (int | Unset): Unique numeric ID of this message.
        message_uuid (str | Unset): A 128-bit universally unique identifier (UUID) for this message.
    """

    email: str | Unset = UNSET
    message_id: int | Unset = UNSET
    message_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        message_id = self.message_id

        message_uuid = self.message_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["Email"] = email
        if message_id is not UNSET:
            field_dict["MessageID"] = message_id
        if message_uuid is not UNSET:
            field_dict["MessageUUID"] = message_uuid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("Email", UNSET)

        message_id = d.pop("MessageID", UNSET)

        message_uuid = d.pop("MessageUUID", UNSET)

        post_send_v3_response_201_sent_item = cls(
            email=email,
            message_id=message_id,
            message_uuid=message_uuid,
        )

        post_send_v3_response_201_sent_item.additional_properties = d
        return post_send_v3_response_201_sent_item

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
