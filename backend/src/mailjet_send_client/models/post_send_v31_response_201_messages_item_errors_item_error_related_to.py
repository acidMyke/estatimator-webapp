from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo")


@_attrs_define
class PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo:
    """Indicates which part of the payload this error is related to."""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        post_send_v31_response_201_messages_item_errors_item_error_related_to = cls()

        post_send_v31_response_201_messages_item_errors_item_error_related_to.additional_properties = d
        return post_send_v31_response_201_messages_item_errors_item_error_related_to

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
