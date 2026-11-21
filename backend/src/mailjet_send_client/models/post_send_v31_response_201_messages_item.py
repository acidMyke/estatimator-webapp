from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_send_v31_response_201_messages_item_bcc_item import (
        PostSendV31Response201MessagesItemBccItem,
    )
    from ..models.post_send_v31_response_201_messages_item_cc_item import (
        PostSendV31Response201MessagesItemCcItem,
    )
    from ..models.post_send_v31_response_201_messages_item_errors_item import (
        PostSendV31Response201MessagesItemErrorsItem,
    )
    from ..models.post_send_v31_response_201_messages_item_to_item import (
        PostSendV31Response201MessagesItemToItem,
    )


T = TypeVar("T", bound="PostSendV31Response201MessagesItem")


@_attrs_define
class PostSendV31Response201MessagesItem:
    """
    Attributes:
        status (str | Unset): Indicates the sending status of the message.

            Possible values:

            - `success`
            - `error`
        errors (list[PostSendV31Response201MessagesItemErrorsItem] | Unset): A JSON array containing information about
            any errors with the processing of this message. Will be displayed only if processing errors occur. Each error
            will generate a separate error object with the below properties.
        custom_id (str | Unset): A user-defined custom ID.
        to (list[PostSendV31Response201MessagesItemToItem] | Unset): A JSON array containing information about the
            messages sent to recipients in To.
        cc (list[PostSendV31Response201MessagesItemCcItem] | Unset): A JSON array containing information about the
            messages sent to recipients in Cc.
        bcc (list[PostSendV31Response201MessagesItemBccItem] | Unset): A JSON array containing information about the
            messages sent to recipients in Bcc.
    """

    status: str | Unset = UNSET
    errors: list[PostSendV31Response201MessagesItemErrorsItem] | Unset = UNSET
    custom_id: str | Unset = UNSET
    to: list[PostSendV31Response201MessagesItemToItem] | Unset = UNSET
    cc: list[PostSendV31Response201MessagesItemCcItem] | Unset = UNSET
    bcc: list[PostSendV31Response201MessagesItemBccItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        custom_id = self.custom_id

        to: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = []
            for to_item_data in self.to:
                to_item = to_item_data.to_dict()
                to.append(to_item)

        cc: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cc, Unset):
            cc = []
            for cc_item_data in self.cc:
                cc_item = cc_item_data.to_dict()
                cc.append(cc_item)

        bcc: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bcc, Unset):
            bcc = []
            for bcc_item_data in self.bcc:
                bcc_item = bcc_item_data.to_dict()
                bcc.append(bcc_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["Status"] = status
        if errors is not UNSET:
            field_dict["Errors"] = errors
        if custom_id is not UNSET:
            field_dict["CustomID"] = custom_id
        if to is not UNSET:
            field_dict["To"] = to
        if cc is not UNSET:
            field_dict["Cc"] = cc
        if bcc is not UNSET:
            field_dict["Bcc"] = bcc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_send_v31_response_201_messages_item_bcc_item import (
            PostSendV31Response201MessagesItemBccItem,
        )
        from ..models.post_send_v31_response_201_messages_item_cc_item import (
            PostSendV31Response201MessagesItemCcItem,
        )
        from ..models.post_send_v31_response_201_messages_item_errors_item import (
            PostSendV31Response201MessagesItemErrorsItem,
        )
        from ..models.post_send_v31_response_201_messages_item_to_item import (
            PostSendV31Response201MessagesItemToItem,
        )

        d = dict(src_dict)
        status = d.pop("Status", UNSET)

        _errors = d.pop("Errors", UNSET)
        errors: list[PostSendV31Response201MessagesItemErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = PostSendV31Response201MessagesItemErrorsItem.from_dict(
                    errors_item_data
                )

                errors.append(errors_item)

        custom_id = d.pop("CustomID", UNSET)

        _to = d.pop("To", UNSET)
        to: list[PostSendV31Response201MessagesItemToItem] | Unset = UNSET
        if _to is not UNSET:
            to = []
            for to_item_data in _to:
                to_item = PostSendV31Response201MessagesItemToItem.from_dict(
                    to_item_data
                )

                to.append(to_item)

        _cc = d.pop("Cc", UNSET)
        cc: list[PostSendV31Response201MessagesItemCcItem] | Unset = UNSET
        if _cc is not UNSET:
            cc = []
            for cc_item_data in _cc:
                cc_item = PostSendV31Response201MessagesItemCcItem.from_dict(
                    cc_item_data
                )

                cc.append(cc_item)

        _bcc = d.pop("Bcc", UNSET)
        bcc: list[PostSendV31Response201MessagesItemBccItem] | Unset = UNSET
        if _bcc is not UNSET:
            bcc = []
            for bcc_item_data in _bcc:
                bcc_item = PostSendV31Response201MessagesItemBccItem.from_dict(
                    bcc_item_data
                )

                bcc.append(bcc_item)

        post_send_v31_response_201_messages_item = cls(
            status=status,
            errors=errors,
            custom_id=custom_id,
            to=to,
            cc=cc,
            bcc=bcc,
        )

        post_send_v31_response_201_messages_item.additional_properties = d
        return post_send_v31_response_201_messages_item

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
