from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSendV31BodyMessagesItemTemplateErrorReporting")


@_attrs_define
class PostSendV31BodyMessagesItemTemplateErrorReporting:
    """An object containing the email address and name of the recipient, to whom a carbon copy with the error message is
    sent to in case of sending issues. Can only be used when `TemplateLanguage=true`. Equivalent to using the `X-MJ-
    TemplateErrorReporting` header through SMTP.

        Attributes:
            email (str): The email address, to which the carbon copy of the email with the error message will be sent.
            name (str | Unset): The name of the recipient, to whom the carbon copy of the email with the error message will
                be sent.
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

        post_send_v31_body_messages_item_template_error_reporting = cls(
            email=email,
            name=name,
        )

        post_send_v31_body_messages_item_template_error_reporting.additional_properties = d
        return post_send_v31_body_messages_item_template_error_reporting

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
