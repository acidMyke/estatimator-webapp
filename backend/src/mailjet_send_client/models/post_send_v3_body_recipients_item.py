from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSendV3BodyRecipientsItem")


@_attrs_define
class PostSendV3BodyRecipientsItem:
    """
    Attributes:
        email (str): The email address of the recipient.
        name (str | Unset): The name of the recipient. Will be displayed next to the email in the recipient's mailbox.
        vars_ (str | Unset): Variables used in the message content for this recipient. Specified as a JSON array of
            `var_name:var_value`. Inserted in the text and/or HTML part of the message as `[[var: var_value]]`.
    """

    email: str
    name: str | Unset = UNSET
    vars_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        vars_ = self.vars_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Email": email,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name
        if vars_ is not UNSET:
            field_dict["Vars"] = vars_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("Email")

        name = d.pop("Name", UNSET)

        vars_ = d.pop("Vars", UNSET)

        post_send_v3_body_recipients_item = cls(
            email=email,
            name=name,
            vars_=vars_,
        )

        post_send_v3_body_recipients_item.additional_properties = d
        return post_send_v3_body_recipients_item

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
