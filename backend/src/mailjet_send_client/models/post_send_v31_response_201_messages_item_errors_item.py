from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_send_v31_response_201_messages_item_errors_item_error_related_to import (
        PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo,
    )


T = TypeVar("T", bound="PostSendV31Response201MessagesItemErrorsItem")


@_attrs_define
class PostSendV31Response201MessagesItemErrorsItem:
    """
    Attributes:
        error_identifier (str | Unset): A 128-bit universally unique identifier (UUID) for this error.
        error_code (str | Unset): An internal Mailjet error code for this error. See [Send API Errors](/docs/email-
            api/send-api-v31/send-api-errors) for more information.
        status_code (int | Unset): The error status code. See [Send API Errors](/docs/email-api/send-api-v31/send-api-
            errors) for more information.
        error_message (str | Unset): An error message informing the user what the issue is.
        error_related_to (PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo | Unset): Indicates which part of
            the payload this error is related to.
    """

    error_identifier: str | Unset = UNSET
    error_code: str | Unset = UNSET
    status_code: int | Unset = UNSET
    error_message: str | Unset = UNSET
    error_related_to: (
        PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_identifier = self.error_identifier

        error_code = self.error_code

        status_code = self.status_code

        error_message = self.error_message

        error_related_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_related_to, Unset):
            error_related_to = self.error_related_to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_identifier is not UNSET:
            field_dict["ErrorIdentifier"] = error_identifier
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code
        if status_code is not UNSET:
            field_dict["StatusCode"] = status_code
        if error_message is not UNSET:
            field_dict["ErrorMessage"] = error_message
        if error_related_to is not UNSET:
            field_dict["ErrorRelatedTo"] = error_related_to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_send_v31_response_201_messages_item_errors_item_error_related_to import (
            PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo,
        )

        d = dict(src_dict)
        error_identifier = d.pop("ErrorIdentifier", UNSET)

        error_code = d.pop("ErrorCode", UNSET)

        status_code = d.pop("StatusCode", UNSET)

        error_message = d.pop("ErrorMessage", UNSET)

        _error_related_to = d.pop("ErrorRelatedTo", UNSET)
        error_related_to: (
            PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo | Unset
        )
        if isinstance(_error_related_to, Unset):
            error_related_to = UNSET
        else:
            error_related_to = (
                PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo.from_dict(
                    _error_related_to
                )
            )

        post_send_v31_response_201_messages_item_errors_item = cls(
            error_identifier=error_identifier,
            error_code=error_code,
            status_code=status_code,
            error_message=error_message,
            error_related_to=error_related_to,
        )

        post_send_v31_response_201_messages_item_errors_item.additional_properties = d
        return post_send_v31_response_201_messages_item_errors_item

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
