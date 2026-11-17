from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSendV31BodyGlobals")


@_attrs_define
class PostSendV31BodyGlobals:
    """An object containing properties that will be applied to all message objects (). Use this whenever you have property
    values that are the same across multiple messages in the payload.

    In `Globals` you can specify any of the message properties __except `To`__.

    If the properties are specified in both `Globals` and in a message object:

      - String, integer and boolean properties will be overwritten by the message properties of the same name.
      - Object type properties (`From`, `Sender`, `ReplyTo`, `TemplateErrorReporting`, `Headers`, `Variables`) will be
    merged with the message property, overwriting any concurrent property.
      - Array type properties (`Cc`, `Bcc`, `Attachments`, `InlineAttachments`) will be appended.

    For more information and examples click [here](/docs/email-api/send-api-v31/set-global-payload-properties).

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        post_send_v31_body_globals = cls()

        post_send_v31_body_globals.additional_properties = d
        return post_send_v31_body_globals

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
