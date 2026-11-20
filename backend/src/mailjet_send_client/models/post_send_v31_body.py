from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_send_v31_body_globals import PostSendV31BodyGlobals
    from ..models.post_send_v31_body_messages_item import PostSendV31BodyMessagesItem


T = TypeVar("T", bound="PostSendV31Body")


@_attrs_define
class PostSendV31Body:
    """
    Attributes:
        messages (list[PostSendV31BodyMessagesItem]): A JSON array containing message objects.
        sandbox_mode (bool | Unset): When true, the API call will be run in Sandbox mode. This will disable the delivery
            of the message, but the API will still perform all necessary validations. You will still receive success or
            error messages related to the processing of the message. If the message is processed successfully, you will
            receive the standard response payload but without the Message ID and UUID.

            Default value: `false`
        advance_error_handling (bool | Unset): When true, enables additional error checks relating to the Send API v3.1
            payload. Keep in mind that For a list of all error checks enabled by this, please see the [Send API
            errors](/docs/email-api/send-api-v31/send-api-errors) section in the Email API Guides.
        globals_ (PostSendV31BodyGlobals | Unset): An object containing properties that will be applied to all message
            objects (). Use this whenever you have property values that are the same across multiple messages in the
            payload.

            In `Globals` you can specify any of the message properties __except `To`__.

            If the properties are specified in both `Globals` and in a message object:

              - String, integer and boolean properties will be overwritten by the message properties of the same name.
              - Object type properties (`From`, `Sender`, `ReplyTo`, `TemplateErrorReporting`, `Headers`, `Variables`) will
            be merged with the message property, overwriting any concurrent property.
              - Array type properties (`Cc`, `Bcc`, `Attachments`, `InlineAttachments`) will be appended.

            For more information and examples click [here](/docs/email-api/send-api-v31/set-global-payload-properties).
    """

    messages: list[PostSendV31BodyMessagesItem]
    sandbox_mode: bool | Unset = UNSET
    advance_error_handling: bool | Unset = UNSET
    globals_: PostSendV31BodyGlobals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        sandbox_mode = self.sandbox_mode

        advance_error_handling = self.advance_error_handling

        globals_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.globals_, Unset):
            globals_ = self.globals_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Messages": messages,
            }
        )
        if sandbox_mode is not UNSET:
            field_dict["SandboxMode"] = sandbox_mode
        if advance_error_handling is not UNSET:
            field_dict["AdvanceErrorHandling"] = advance_error_handling
        if globals_ is not UNSET:
            field_dict["Globals"] = globals_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_send_v31_body_globals import PostSendV31BodyGlobals
        from ..models.post_send_v31_body_messages_item import (
            PostSendV31BodyMessagesItem,
        )

        d = dict(src_dict)
        messages = []
        _messages = d.pop("Messages")
        for messages_item_data in _messages:
            messages_item = PostSendV31BodyMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        sandbox_mode = d.pop("SandboxMode", UNSET)

        advance_error_handling = d.pop("AdvanceErrorHandling", UNSET)

        _globals_ = d.pop("Globals", UNSET)
        globals_: PostSendV31BodyGlobals | Unset
        if isinstance(_globals_, Unset):
            globals_ = UNSET
        else:
            globals_ = PostSendV31BodyGlobals.from_dict(_globals_)

        post_send_v31_body = cls(
            messages=messages,
            sandbox_mode=sandbox_mode,
            advance_error_handling=advance_error_handling,
            globals_=globals_,
        )

        post_send_v31_body.additional_properties = d
        return post_send_v31_body

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
