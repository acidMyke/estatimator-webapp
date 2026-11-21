from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSendV31BodyMessagesItemVariables")


@_attrs_define
class PostSendV31BodyMessagesItemVariables:
    """A JSON object containing variables used to modify the content of your email. Specified as `{var_name}:{var_value}`
    pairs. Enter the information in the template text / HTML part by using the `[[var:{var_name}]]` format. Equivalent
    of using `X-MJ-Vars` header through SMTP.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        post_send_v31_body_messages_item_variables = cls()

        post_send_v31_body_messages_item_variables.additional_properties = d
        return post_send_v31_body_messages_item_variables

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
