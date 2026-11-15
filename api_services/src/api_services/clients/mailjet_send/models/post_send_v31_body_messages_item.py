from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_send_v31_body_messages_item_track_clicks import (
    PostSendV31BodyMessagesItemTrackClicks,
)
from ..models.post_send_v31_body_messages_item_track_opens import (
    PostSendV31BodyMessagesItemTrackOpens,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_send_v31_body_messages_item_attachments_item import (
        PostSendV31BodyMessagesItemAttachmentsItem,
    )
    from ..models.post_send_v31_body_messages_item_bcc_item import (
        PostSendV31BodyMessagesItemBccItem,
    )
    from ..models.post_send_v31_body_messages_item_cc_item import (
        PostSendV31BodyMessagesItemCcItem,
    )
    from ..models.post_send_v31_body_messages_item_from import (
        PostSendV31BodyMessagesItemFrom,
    )
    from ..models.post_send_v31_body_messages_item_headers import (
        PostSendV31BodyMessagesItemHeaders,
    )
    from ..models.post_send_v31_body_messages_item_inlined_attachments_item import (
        PostSendV31BodyMessagesItemInlinedAttachmentsItem,
    )
    from ..models.post_send_v31_body_messages_item_reply_to import (
        PostSendV31BodyMessagesItemReplyTo,
    )
    from ..models.post_send_v31_body_messages_item_sender import (
        PostSendV31BodyMessagesItemSender,
    )
    from ..models.post_send_v31_body_messages_item_template_error_reporting import (
        PostSendV31BodyMessagesItemTemplateErrorReporting,
    )
    from ..models.post_send_v31_body_messages_item_to_item import (
        PostSendV31BodyMessagesItemToItem,
    )
    from ..models.post_send_v31_body_messages_item_variables import (
        PostSendV31BodyMessagesItemVariables,
    )


T = TypeVar("T", bound="PostSendV31BodyMessagesItem")


@_attrs_define
class PostSendV31BodyMessagesItem:
    """
    Attributes:
        from_ (PostSendV31BodyMessagesItemFrom): A JSON object containing 2 properties - `Email` and `Name`. Specifies
            the sender name and email address:

            1. When `Sender` is not specified, the email address will be used to send the message. In such cases, it must be
            a valid, activated sender for this account. See the `/sender` and `/metasender` resources for more info.

            2. When `Sender` is specified, the `Sender` email address will be used to send the message, while the `From`
            email address will be displayed in the recipient's inbox. In such cases, it is not necessary for the `From`
            address to be validated. When the `Sender` and `From` domains differ, the information will be displayed in the
            inbox as `From {from_email} via / sent on behalf of {sender_domain}`.

            > Note: If the `From` domain has a DMARC policy in effect (e.g. Yahoo, AOL), the message will not be delivered.
            Instead, it will either bounce or be considered as Spam.
        to (list[PostSendV31BodyMessagesItemToItem]): A JSON array of recipients. Each recipient object within the array
            may contain the name, but must always contain the recipient email.
        sender (PostSendV31BodyMessagesItemSender | Unset): A JSON object containing 2 properties - `Email` and `Name`.
            Specifies the sender name and email address. Used when you want to send emails on behalf of a different email
            address. Must be a valid, activated sender for this account. See the `/sender` and `/metasender` resources for
            more info. Only `Email` is a mandatory property within this object.

            The `Sender` email address will be used to send the message, while the `From` email address will be displayed in
            the recipient's inbox. In such cases, it is not necessary for the `From` address to be verified. However, the
            information will be displayed in the inbox as `From {from_email} via / sent on behalf of {sender_domain}`.

            > Note: This option is disabled by default and is no longer available for new setups. Existing Default Sender
            configurations continue to work, but Mailjet no longer enables this functionality on new requests.
        cc (list[PostSendV31BodyMessagesItemCcItem] | Unset): A JSON array of recipients who are supposed to receive a
            carbon copy (cc) of this message. Used together with `To` and `Bcc` (optional). Each recipient object within the
            array may contain the name, but must always contain the recipient email.
        bcc (list[PostSendV31BodyMessagesItemBccItem] | Unset): A JSON array recipients who are supposed to receive a
            blind carbon copy (bcc) of this message. Use this when you do not want your other recipients to see that you are
            sending a copy of the message to this email address. Used together with `To` and `Cc` (optional). Each recipient
            object within the array may contain the name, but must always contain the recipient email.
        reply_to (PostSendV31BodyMessagesItemReplyTo | Unset): An object containing the email address and name
            (optional), to which replies to this message will go.
        subject (str | Unset): The email subject line.
        text_part (str | Unset): Provides the Text part of the message. Mandatory, if the `HTMLPart` and `TemplateID`
            parameters are not specified.
        html_part (str | Unset): Provides the HTML part of the message. Mandatory, if the `TextPart` and `TemplateID`
            parameters are not specified.
        template_id (int | Unset): Unique numeric ID of the template to be used as email content. If the HTML/Text parts
            are specified, `TemplateID` will overwrite them. Equivalent to using the `X-MJ-TemplateID` header through SMTP.
        template_language (bool | Unset): When true, activates the template language processing. Equivalent to using the
            `X-MJ-TemplateLanguage` header through SMTP.

            Default value: `false`
        template_error_reporting (PostSendV31BodyMessagesItemTemplateErrorReporting | Unset): An object containing the
            email address and name of the recipient, to whom a carbon copy with the error message is sent to in case of
            sending issues. Can only be used when `TemplateLanguage=true`. Equivalent to using the `X-MJ-
            TemplateErrorReporting` header through SMTP.
        template_error_deliver (bool | Unset): When true, the message delivery will proceed if an error is discovered in
            the templating language. When false, the message delivery will be stopped. Can only be used when
            `TemplateLanguage=true`. Equivalent to using the `X-MJ-TemplateErrorDeliver` header through SMTP.

            Default value: `false`
        attachments (list[PostSendV31BodyMessagesItemAttachmentsItem] | Unset): A JSON array containing descriptions of
            the files attached to this message. The array contains the Filename, Content type and Base64 encoded content of
            the file. The total size of the API call payload - including all attachments, inline attachments and message
            content - should not exceed 15 MB.
        inlined_attachments (list[PostSendV31BodyMessagesItemInlinedAttachmentsItem] | Unset): A JSON array containing
            descriptions of the files attached to this message, that are available for inline use. Inline attachments can be
            visible directly in the body of the message, depending on the email client support. Insert the file into the
            HTML code of the email by using `cid:Filename`, or, if you have specified `ContentID`, by using `cid:ContentID`.
            The total size of the API call payload - including all attachments, inline attachments and message content -
            should not exceed 15 MB.
        priority (int | Unset): Indicates the processing priority inside your account (API Key) scheduling queue.
            Equivalent of using the `X-Mailjet-Prio` header through SMTP.

            There are two queues - low priority (`0`, `1`) and high priority (`2`, `3`):

            - `0` - low priority queue, processed first in, first out
            - `1` - goes before the low priority queue, processed last in, first out
            - `2` - high priority queue, processed first in, first out
            - `3` - goes before the high priority queue, processed last in, first out

            Send transactional messages with `2` and marketing messages with `0`. Codes `1` and `3` are intended for narrow
            cases where tight control of the email flow is necessary - `3` can block messages sent with `2`, so it is not
            advised for large volumes. Whether high or low priority, the processing speed is the same - only the order
            changes.

            [More information](https://documentation.mailjet.com/hc/en-us/articles/360043571894-Email-Priority-Management).

            Default value: `2`
        custom_campaign (str | Unset): Specifies a custom campaign name, to  which all messages with this property value
            will be assigned. If the campaign doesn't already exist it will be automatically created in the Mailjet system.
            API users are allowed to send multiple emails from the same campaign name to the same contacts. To block this
            feature, use the `DeduplicateCampaign` property. Equivalent of using `X-Mailjet-Campaign` header through SMTP.
        deduplicate_campaign (bool | Unset): Enables or disables the option to send messages from the same campaign to
            the same contact multiple times. Equivalent of using `X-Mailjet-DeduplicateCampaign` header through SMTP.

            When set to `true`, a contact that has already received a message carrying a particular `CustomCampaign` value
            will not receive another message from that same campaign. When `false`, the same contact can receive multiple
            messages from the same grouped campaign.

            Default value: `false`
        track_opens (PostSendV31BodyMessagesItemTrackOpens | Unset): Enable or disable open tracking on this message.
            This property will overwrite the preferences selected in the [Mailjet
            account](https://app.mailjet.com/account/settings). Equivalent of using `X-Mailjet-TrackOpen` header through
            SMTP.

            Allowed Values:
              - `account_default` = use the values specified in the [Mailjet
            account](https://app.mailjet.com/account/settings)
              - `disabled` = disable tracking for this message
              - `enabled` = enable tracking for this message
              - `anon` = record opens without linking them to the individual recipient

            This property is set per message object, so a single request can carry different values for different recipients
            - for example `enabled` for contacts who consented to tracking and `disabled` or `anon` for those who did not.
            Use `CustomCampaign` to keep those messages grouped under one campaign for reporting.

            Default value: `account_default`
        track_clicks (PostSendV31BodyMessagesItemTrackClicks | Unset): Enable or disable click tracking on this message.
            This property will overwrite the preferences selected in the [Mailjet
            account](https://app.mailjet.com/account/settings). Equivalent of using `X-Mailjet-TrackClick` header through
            SMTP.

            Allowed Values:
              - `account_default` = use the values specified in the [Mailjet
            account](https://app.mailjet.com/account/settings)
              - `disabled` = disable tracking for this message
              - `enabled` = enable tracking for this message
              - `anon` = record clicks without linking them to the individual recipient

            This property is set per message object, so a single request can carry different values for different recipients
            - for example `enabled` for contacts who consented to tracking and `disabled` or `anon` for those who did not.
            Use `CustomCampaign` to keep those messages grouped under one campaign for reporting.

            Default value: `account_default`
        custom_id (str | Unset): Select a user-defined custom ID.
        event_payload (str | Unset): Defines a payload attached to the message. The Parse API will return the values in
            the payload. Any standard format can be used - XML, JSON, CSV etc. Equivalent of using `X-MJ-EventPayload`
            header through SMTP.
        url_tags (str | Unset): URL tags to append every URL link in the message. The user needs to provide the query
            between the `?` and `#` characters in the URL. The URLTags value needs to be URL-encoded.
        headers (PostSendV31BodyMessagesItemHeaders | Unset): A JSON object containing additional email headers.
            Specified as `{header_name}:{header_value}` pairs.
        variables (PostSendV31BodyMessagesItemVariables | Unset): A JSON object containing variables used to modify the
            content of your email. Specified as `{var_name}:{var_value}` pairs. Enter the information in the template text /
            HTML part by using the `[[var:{var_name}]]` format. Equivalent of using `X-MJ-Vars` header through SMTP.
    """

    from_: PostSendV31BodyMessagesItemFrom
    to: list[PostSendV31BodyMessagesItemToItem]
    sender: PostSendV31BodyMessagesItemSender | Unset = UNSET
    cc: list[PostSendV31BodyMessagesItemCcItem] | Unset = UNSET
    bcc: list[PostSendV31BodyMessagesItemBccItem] | Unset = UNSET
    reply_to: PostSendV31BodyMessagesItemReplyTo | Unset = UNSET
    subject: str | Unset = UNSET
    text_part: str | Unset = UNSET
    html_part: str | Unset = UNSET
    template_id: int | Unset = UNSET
    template_language: bool | Unset = UNSET
    template_error_reporting: (
        PostSendV31BodyMessagesItemTemplateErrorReporting | Unset
    ) = UNSET
    template_error_deliver: bool | Unset = UNSET
    attachments: list[PostSendV31BodyMessagesItemAttachmentsItem] | Unset = UNSET
    inlined_attachments: (
        list[PostSendV31BodyMessagesItemInlinedAttachmentsItem] | Unset
    ) = UNSET
    priority: int | Unset = UNSET
    custom_campaign: str | Unset = UNSET
    deduplicate_campaign: bool | Unset = UNSET
    track_opens: PostSendV31BodyMessagesItemTrackOpens | Unset = UNSET
    track_clicks: PostSendV31BodyMessagesItemTrackClicks | Unset = UNSET
    custom_id: str | Unset = UNSET
    event_payload: str | Unset = UNSET
    url_tags: str | Unset = UNSET
    headers: PostSendV31BodyMessagesItemHeaders | Unset = UNSET
    variables: PostSendV31BodyMessagesItemVariables | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.to_dict()

        to = []
        for to_item_data in self.to:
            to_item = to_item_data.to_dict()
            to.append(to_item)

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

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

        reply_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_to, Unset):
            reply_to = self.reply_to.to_dict()

        subject = self.subject

        text_part = self.text_part

        html_part = self.html_part

        template_id = self.template_id

        template_language = self.template_language

        template_error_reporting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_error_reporting, Unset):
            template_error_reporting = self.template_error_reporting.to_dict()

        template_error_deliver = self.template_error_deliver

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        inlined_attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inlined_attachments, Unset):
            inlined_attachments = []
            for inlined_attachments_item_data in self.inlined_attachments:
                inlined_attachments_item = inlined_attachments_item_data.to_dict()
                inlined_attachments.append(inlined_attachments_item)

        priority = self.priority

        custom_campaign = self.custom_campaign

        deduplicate_campaign = self.deduplicate_campaign

        track_opens: str | Unset = UNSET
        if not isinstance(self.track_opens, Unset):
            track_opens = self.track_opens.value

        track_clicks: str | Unset = UNSET
        if not isinstance(self.track_clicks, Unset):
            track_clicks = self.track_clicks.value

        custom_id = self.custom_id

        event_payload = self.event_payload

        url_tags = self.url_tags

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "From": from_,
                "To": to,
            }
        )
        if sender is not UNSET:
            field_dict["Sender"] = sender
        if cc is not UNSET:
            field_dict["Cc"] = cc
        if bcc is not UNSET:
            field_dict["Bcc"] = bcc
        if reply_to is not UNSET:
            field_dict["ReplyTo"] = reply_to
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if text_part is not UNSET:
            field_dict["TextPart"] = text_part
        if html_part is not UNSET:
            field_dict["HTMLPart"] = html_part
        if template_id is not UNSET:
            field_dict["TemplateID"] = template_id
        if template_language is not UNSET:
            field_dict["TemplateLanguage"] = template_language
        if template_error_reporting is not UNSET:
            field_dict["TemplateErrorReporting"] = template_error_reporting
        if template_error_deliver is not UNSET:
            field_dict["TemplateErrorDeliver"] = template_error_deliver
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if inlined_attachments is not UNSET:
            field_dict["InlinedAttachments"] = inlined_attachments
        if priority is not UNSET:
            field_dict["Priority"] = priority
        if custom_campaign is not UNSET:
            field_dict["CustomCampaign"] = custom_campaign
        if deduplicate_campaign is not UNSET:
            field_dict["DeduplicateCampaign"] = deduplicate_campaign
        if track_opens is not UNSET:
            field_dict["TrackOpens"] = track_opens
        if track_clicks is not UNSET:
            field_dict["TrackClicks"] = track_clicks
        if custom_id is not UNSET:
            field_dict["CustomID"] = custom_id
        if event_payload is not UNSET:
            field_dict["EventPayload"] = event_payload
        if url_tags is not UNSET:
            field_dict["URLTags"] = url_tags
        if headers is not UNSET:
            field_dict["Headers"] = headers
        if variables is not UNSET:
            field_dict["Variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_send_v31_body_messages_item_attachments_item import (
            PostSendV31BodyMessagesItemAttachmentsItem,
        )
        from ..models.post_send_v31_body_messages_item_bcc_item import (
            PostSendV31BodyMessagesItemBccItem,
        )
        from ..models.post_send_v31_body_messages_item_cc_item import (
            PostSendV31BodyMessagesItemCcItem,
        )
        from ..models.post_send_v31_body_messages_item_from import (
            PostSendV31BodyMessagesItemFrom,
        )
        from ..models.post_send_v31_body_messages_item_headers import (
            PostSendV31BodyMessagesItemHeaders,
        )
        from ..models.post_send_v31_body_messages_item_inlined_attachments_item import (
            PostSendV31BodyMessagesItemInlinedAttachmentsItem,
        )
        from ..models.post_send_v31_body_messages_item_reply_to import (
            PostSendV31BodyMessagesItemReplyTo,
        )
        from ..models.post_send_v31_body_messages_item_sender import (
            PostSendV31BodyMessagesItemSender,
        )
        from ..models.post_send_v31_body_messages_item_template_error_reporting import (
            PostSendV31BodyMessagesItemTemplateErrorReporting,
        )
        from ..models.post_send_v31_body_messages_item_to_item import (
            PostSendV31BodyMessagesItemToItem,
        )
        from ..models.post_send_v31_body_messages_item_variables import (
            PostSendV31BodyMessagesItemVariables,
        )

        d = dict(src_dict)
        from_ = PostSendV31BodyMessagesItemFrom.from_dict(d.pop("From"))

        to = []
        _to = d.pop("To")
        for to_item_data in _to:
            to_item = PostSendV31BodyMessagesItemToItem.from_dict(to_item_data)

            to.append(to_item)

        _sender = d.pop("Sender", UNSET)
        sender: PostSendV31BodyMessagesItemSender | Unset
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = PostSendV31BodyMessagesItemSender.from_dict(_sender)

        _cc = d.pop("Cc", UNSET)
        cc: list[PostSendV31BodyMessagesItemCcItem] | Unset = UNSET
        if _cc is not UNSET:
            cc = []
            for cc_item_data in _cc:
                cc_item = PostSendV31BodyMessagesItemCcItem.from_dict(cc_item_data)

                cc.append(cc_item)

        _bcc = d.pop("Bcc", UNSET)
        bcc: list[PostSendV31BodyMessagesItemBccItem] | Unset = UNSET
        if _bcc is not UNSET:
            bcc = []
            for bcc_item_data in _bcc:
                bcc_item = PostSendV31BodyMessagesItemBccItem.from_dict(bcc_item_data)

                bcc.append(bcc_item)

        _reply_to = d.pop("ReplyTo", UNSET)
        reply_to: PostSendV31BodyMessagesItemReplyTo | Unset
        if isinstance(_reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = PostSendV31BodyMessagesItemReplyTo.from_dict(_reply_to)

        subject = d.pop("Subject", UNSET)

        text_part = d.pop("TextPart", UNSET)

        html_part = d.pop("HTMLPart", UNSET)

        template_id = d.pop("TemplateID", UNSET)

        template_language = d.pop("TemplateLanguage", UNSET)

        _template_error_reporting = d.pop("TemplateErrorReporting", UNSET)
        template_error_reporting: (
            PostSendV31BodyMessagesItemTemplateErrorReporting | Unset
        )
        if isinstance(_template_error_reporting, Unset):
            template_error_reporting = UNSET
        else:
            template_error_reporting = (
                PostSendV31BodyMessagesItemTemplateErrorReporting.from_dict(
                    _template_error_reporting
                )
            )

        template_error_deliver = d.pop("TemplateErrorDeliver", UNSET)

        _attachments = d.pop("Attachments", UNSET)
        attachments: list[PostSendV31BodyMessagesItemAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = PostSendV31BodyMessagesItemAttachmentsItem.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        _inlined_attachments = d.pop("InlinedAttachments", UNSET)
        inlined_attachments: (
            list[PostSendV31BodyMessagesItemInlinedAttachmentsItem] | Unset
        ) = UNSET
        if _inlined_attachments is not UNSET:
            inlined_attachments = []
            for inlined_attachments_item_data in _inlined_attachments:
                inlined_attachments_item = (
                    PostSendV31BodyMessagesItemInlinedAttachmentsItem.from_dict(
                        inlined_attachments_item_data
                    )
                )

                inlined_attachments.append(inlined_attachments_item)

        priority = d.pop("Priority", UNSET)

        custom_campaign = d.pop("CustomCampaign", UNSET)

        deduplicate_campaign = d.pop("DeduplicateCampaign", UNSET)

        _track_opens = d.pop("TrackOpens", UNSET)
        track_opens: PostSendV31BodyMessagesItemTrackOpens | Unset
        if isinstance(_track_opens, Unset):
            track_opens = UNSET
        else:
            track_opens = PostSendV31BodyMessagesItemTrackOpens(_track_opens)

        _track_clicks = d.pop("TrackClicks", UNSET)
        track_clicks: PostSendV31BodyMessagesItemTrackClicks | Unset
        if isinstance(_track_clicks, Unset):
            track_clicks = UNSET
        else:
            track_clicks = PostSendV31BodyMessagesItemTrackClicks(_track_clicks)

        custom_id = d.pop("CustomID", UNSET)

        event_payload = d.pop("EventPayload", UNSET)

        url_tags = d.pop("URLTags", UNSET)

        _headers = d.pop("Headers", UNSET)
        headers: PostSendV31BodyMessagesItemHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = PostSendV31BodyMessagesItemHeaders.from_dict(_headers)

        _variables = d.pop("Variables", UNSET)
        variables: PostSendV31BodyMessagesItemVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = PostSendV31BodyMessagesItemVariables.from_dict(_variables)

        post_send_v31_body_messages_item = cls(
            from_=from_,
            to=to,
            sender=sender,
            cc=cc,
            bcc=bcc,
            reply_to=reply_to,
            subject=subject,
            text_part=text_part,
            html_part=html_part,
            template_id=template_id,
            template_language=template_language,
            template_error_reporting=template_error_reporting,
            template_error_deliver=template_error_deliver,
            attachments=attachments,
            inlined_attachments=inlined_attachments,
            priority=priority,
            custom_campaign=custom_campaign,
            deduplicate_campaign=deduplicate_campaign,
            track_opens=track_opens,
            track_clicks=track_clicks,
            custom_id=custom_id,
            event_payload=event_payload,
            url_tags=url_tags,
            headers=headers,
            variables=variables,
        )

        post_send_v31_body_messages_item.additional_properties = d
        return post_send_v31_body_messages_item

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
