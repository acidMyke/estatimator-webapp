from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_send_v31_response_201_messages_item import (
        PostSendV31Response201MessagesItem,
    )


T = TypeVar("T", bound="PostSendV31Response201")


@_attrs_define
class PostSendV31Response201:
    """
    Attributes:
        messages (list[PostSendV31Response201MessagesItem] | Unset): A JSON array containing message objects.
    """

    messages: list[PostSendV31Response201MessagesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["Messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_send_v31_response_201_messages_item import (
            PostSendV31Response201MessagesItem,
        )

        d = dict(src_dict)
        _messages = d.pop("Messages", UNSET)
        messages: list[PostSendV31Response201MessagesItem] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = PostSendV31Response201MessagesItem.from_dict(
                    messages_item_data
                )

                messages.append(messages_item)

        post_send_v31_response_201 = cls(
            messages=messages,
        )

        post_send_v31_response_201.additional_properties = d
        return post_send_v31_response_201

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
