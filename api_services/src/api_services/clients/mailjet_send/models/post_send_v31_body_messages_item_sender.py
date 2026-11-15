from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSendV31BodyMessagesItemSender")


@_attrs_define
class PostSendV31BodyMessagesItemSender:
    """A JSON object containing 2 properties - `Email` and `Name`. Specifies the sender name and email address. Used when
    you want to send emails on behalf of a different email address. Must be a valid, activated sender for this account.
    See the `/sender` and `/metasender` resources for more info. Only `Email` is a mandatory property within this
    object.

    The `Sender` email address will be used to send the message, while the `From` email address will be displayed in the
    recipient's inbox. In such cases, it is not necessary for the `From` address to be verified. However, the
    information will be displayed in the inbox as `From {from_email} via / sent on behalf of {sender_domain}`.

    > Note: This option is disabled by default and is no longer available for new setups. Existing Default Sender
    configurations continue to work, but Mailjet no longer enables this functionality on new requests.

        Attributes:
            email (str): The email address used to send the message.
            name (str | Unset): User-selected name for the `Sender` email address.
    """

    email: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Email": email,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("Email")

        name = d.pop("Name", UNSET)

        post_send_v31_body_messages_item_sender = cls(
            email=email,
            name=name,
        )

        post_send_v31_body_messages_item_sender.additional_properties = d
        return post_send_v31_body_messages_item_sender

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
