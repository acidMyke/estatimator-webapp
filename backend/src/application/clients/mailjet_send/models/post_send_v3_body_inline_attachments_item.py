from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSendV3BodyInlineAttachmentsItem")


@_attrs_define
class PostSendV3BodyInlineAttachmentsItem:
    """
    Attributes:
        filename (str): The full name of the file (including the file extension).
        content_type (str): Defines the type of content being sent out using a MIME type. See the [official MIME
            type](https://www.iana.org/assignments/media-types/media-types.xhtml) list for additional information.
        content (str): Base64 encoded content of the attached file.
    """

    filename: str
    content_type: str
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        content_type = self.content_type

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Filename": filename,
                "Content-type": content_type,
                "Content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        filename = d.pop("Filename")

        content_type = d.pop("Content-type")

        content = d.pop("Content")

        post_send_v3_body_inline_attachments_item = cls(
            filename=filename,
            content_type=content_type,
            content=content,
        )

        post_send_v3_body_inline_attachments_item.additional_properties = d
        return post_send_v3_body_inline_attachments_item

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
