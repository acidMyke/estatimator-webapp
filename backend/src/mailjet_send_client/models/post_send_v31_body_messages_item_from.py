from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSendV31BodyMessagesItemFrom")


@_attrs_define
class PostSendV31BodyMessagesItemFrom:
    """A JSON object containing 2 properties - `Email` and `Name`. Specifies the sender name and email address:

    1. When `Sender` is not specified, the email address will be used to send the message. In such cases, it must be a
    valid, activated sender for this account. See the `/sender` and `/metasender` resources for more info.

    2. When `Sender` is specified, the `Sender` email address will be used to send the message, while the `From` email
    address will be displayed in the recipient's inbox. In such cases, it is not necessary for the `From` address to be
    validated. When the `Sender` and `From` domains differ, the information will be displayed in the inbox as `From
    {from_email} via / sent on behalf of {sender_domain}`.

    > Note: If the `From` domain has a DMARC policy in effect (e.g. Yahoo, AOL), the message will not be delivered.
    Instead, it will either bounce or be considered as Spam.

        Attributes:
            email (str): The `From` email address.
            name (str | Unset): The name of the sender. Will be displayed next to the sender email in the recipient's
                mailbox.
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

        post_send_v31_body_messages_item_from = cls(
            email=email,
            name=name,
        )

        post_send_v31_body_messages_item_from.additional_properties = d
        return post_send_v31_body_messages_item_from

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
