from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_send_v3_body_attachments_item import (
        PostSendV3BodyAttachmentsItem,
    )
    from ..models.post_send_v3_body_headers import PostSendV3BodyHeaders
    from ..models.post_send_v3_body_inline_attachments_item import (
        PostSendV3BodyInlineAttachmentsItem,
    )
    from ..models.post_send_v3_body_recipients_item import PostSendV3BodyRecipientsItem
    from ..models.post_send_v3_body_vars import PostSendV3BodyVars


T = TypeVar("T", bound="PostSendV3Body")


@_attrs_define
class PostSendV3Body:
    """
    Attributes:
        from_email (str | Unset): Specifies the sender email address:

            1. When `Sender` is not specified, the email address will be used to send the message. In such cases, it must be
            a valid, activated sender for this account. See the `/sender` and `/metasender` resources for more info.

            2. When `Sender` is specified as `True`, your default sender email address will be used to send the message
            instead, while the `FromEmail` will be displayed in the recipient's inbox. In such cases, it is not necessary
            for the `FromEmail` to be validated. When the default sender and `FromEmail` domains differ, the information
            will be displayed in the inbox as `From {FromEmail} via / sent on behalf of {default_sender_domain}`.

            > Note: If the `FromEmail` domain has a DMARC policy in effect (e.g. Yahoo, AOL), the message will not be
            delivered. Instead, it will either bounce or be considered as Spam.
        from_name (str | Unset): Sender name that will be displayed in the recipient's mailbox.
        sender (bool | Unset): When true, default sender email address will be used to send the message, while the
            `FromEmail` will be displayed in the recipient's inbox. In such cases, it is not necessary for the `FromEmail`
            to be verified. However, the information will be displayed in the inbox as `From {from_email} via / sent on
            behalf of {sender_domain}`.

            Default value: `false`

            > Note: This option is disabled by default and is no longer available for new setups. Existing Default Sender
            configurations continue to work, but Mailjet no longer enables this functionality on new requests.
        recipients (list[PostSendV3BodyRecipientsItem] | Unset): A JSON array containing the list of recipients. Must
            include at least an `Email` property in each element. Required, unless `To` is specified. Cannot be used
            together with `Cc` and `Bcc`.
        to (str | Unset): The email address (and name, optionally) of the recipients. Interchangeable with `Recipients`.
            Acceptable formats are  `john@example.com` or `<john@example.com>` or `"John Doe" <john@example.com>`. Can
            include multiple contacts, which should  be separated by commas. Can be used together with `Cc` and `Bcc`.
        cc (str | Unset): The email address (and name, optionally) of a recipient who is supposed to receive a carbon
            copy (cc) of this message. Used together with `To` and `Bcc` (optional). Acceptable formats are
            `john@example.com` or `<john@example.com>` or `"John Doe" <john@example.com>`. Can include multiple contacts,
            which should  be separated by commas.
        bcc (str | Unset): The email address (and name, optionally) of a recipient who is supposed to receive a blind
            carbon copy (bcc) of this message. Use this when you do not want your other recipients to see that you are
            sending a copy of the message to this email address. Used together with `To` and `Cc` (optional). Acceptable
            formats are  `john@example.com` or `<john@example.com>` or `"John Doe" <john@example.com>`. Can include multiple
            contacts, which should  be separated by commas.
        subject (str | Unset): The email subject line.
        text_part (str | Unset): Provides the Text part of the message. Mandatory, if the `Html-part` parameter is not
            specified.
        html_part (str | Unset): Provides the HTML part of the message. Mandatory, if the `Text-part` parameter is not
            specified.
        mj_template_id (int | Unset): The Template ID or Name to use as this email content. If the HTML/Text parts are
            specified, `Mj-TemplateID` will overwrite them. Equivalent to using the `X-MJ-TemplateID` header through SMTP.
        mj_template_language (bool | Unset): When true, activates the template language processing. Equivalent to using
            the `X-MJ-TemplateLanguage` header through SMTP.

            Default value: `false`
        mj_template_error_reporting (str | Unset): An email address, where a carbon copy with the error message is sent
            to in case of sending issues. Can only be used when `Mj-TemplateLanguage=true`. Equivalent to using the `X-MJ-
            TemplateErrorReporting` header through SMTP.
        mj_template_error_deliver (str | Unset): Defines if the message will be delivered if an error is discovered in
            the templating language. Can only be used when `Mj-TemplateLanguage=true`. Equivalent to using the `X-MJ-
            TemplateErrorDeliver` header through SMTP.

            Possible values:

            - `deliver`
            - `0`

            Default value: `0`
        attachments (list[PostSendV3BodyAttachmentsItem] | Unset): A JSON object containing descriptions of the files
            attached to this message. Contains the Filename, Content type and Base64 encoded content of the file. The total
            size of the API call payload - including all attachments, inline attachments and message content - should not
            exceed 15 MB.
        inline_attachments (list[PostSendV3BodyInlineAttachmentsItem] | Unset): A JSON object containing descriptions of
            the files attached to this message, that are available for inline use. Inline attachments can be visible
            directly in the body of the message, depending on the email client support. Insert the file into the HTML code
            of the email by using `cid:Filename`. The total size of the API call payload - including all attachments, inline
            attachments and message content - should not exceed 15 MB.
        mj_prio (int | Unset): Indicates the processing priority inside your account (API Key) scheduling queue.
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
        mj_campaign (str | Unset): Specifies a custom campaign name, to  which all messages with this property value
            will be assigned. If the campaign doesn't already exist it will be automatically created in the Mailjet system.
            API users are allowed to send multiple emails from the same campaign name to the same contacts. To block this
            feature, use the `Mj-deduplicatecampaign` property. Equivalent of using `X-Mailjet-Campaign` header through
            SMTP.
        mj_deduplicatecampaign (int | Unset): Enables or disables the option to send messages from the same campaign to
            the same contact multiple times. Equivalent of using `X-Mailjet-DeduplicateCampaign` header through SMTP.

            When set to `1`, a contact that has already received a message carrying a particular `Mj-campaign` value will
            not receive another message from that same campaign. When `0`, the same contact can receive multiple messages
            from the same grouped campaign.

            Possible values:

            - `0`
            - `1`

            Default value: `0`
        mj_trackopen (int | Unset): Enable or disable open tracking on this message. This property will overwrite the
            preferences selected in the [Mailjet account](https://app.mailjet.com/account/settings). Equivalent of using
            `X-Mailjet-TrackOpen` header through SMTP.

            Allowed Values:

            - `0` = use the values specified in the [Mailjet account](https://app.mailjet.com/account/settings)
            - `1` = disable tracking for this message
            - `2` = enable tracking for this message
            - `3` = anonymous tracking - opens are recorded without linking them to the individual recipient

            This property is set per message object, so a single request can carry different values for different
            recipients. Use `Mj-campaign` to keep those messages grouped under one campaign for reporting.

            Default value: `0`
        mj_trackclick (int | Unset): Enable or disable click tracking on this message. This property will overwrite the
            preferences selected in the [Mailjet account](https://app.mailjet.com/account/settings). Equivalent of using
            `X-Mailjet-TrackClick` header through SMTP.

            Allowed Values:

            - `0` = use the values specified in the [Mailjet account](https://app.mailjet.com/account/settings)
            - `1` = disable tracking for this message
            - `2` = enable tracking for this message
            - `3` = anonymous tracking - clicks are recorded without linking them to the individual recipient

            This property is set per message object, so a single request can carry different values for different
            recipients. Use `Mj-campaign` to keep those messages grouped under one campaign for reporting.

            Default value: `0`
        mj_custom_id (str | Unset): Select a user-defined custom ID.
        mj_event_payload (str | Unset): Defines a payload attached to the message. The Parse API will return the values
            in the payload. Any standard format can be used - XML, JSON, CSV etc. Equivalent of using `X-MJ-EventPayload`
            header through SMTP.
        headers (PostSendV3BodyHeaders | Unset): A JSON object containing additional email headers. Specified as
            `{header_name}:{header_value}` pairs.
        vars_ (PostSendV3BodyVars | Unset): A JSON object containing variables used to modify the content of your email.
            Specified as `{var_name}:{var_value}` pairs. Enter the information in the template text / HTML part by using the
            `[[var:{var_name}]]` format. Equivalent of using `X-MJ-Vars` header through SMTP.
    """

    from_email: str | Unset = UNSET
    from_name: str | Unset = UNSET
    sender: bool | Unset = UNSET
    recipients: list[PostSendV3BodyRecipientsItem] | Unset = UNSET
    to: str | Unset = UNSET
    cc: str | Unset = UNSET
    bcc: str | Unset = UNSET
    subject: str | Unset = UNSET
    text_part: str | Unset = UNSET
    html_part: str | Unset = UNSET
    mj_template_id: int | Unset = UNSET
    mj_template_language: bool | Unset = UNSET
    mj_template_error_reporting: str | Unset = UNSET
    mj_template_error_deliver: str | Unset = UNSET
    attachments: list[PostSendV3BodyAttachmentsItem] | Unset = UNSET
    inline_attachments: list[PostSendV3BodyInlineAttachmentsItem] | Unset = UNSET
    mj_prio: int | Unset = UNSET
    mj_campaign: str | Unset = UNSET
    mj_deduplicatecampaign: int | Unset = UNSET
    mj_trackopen: int | Unset = UNSET
    mj_trackclick: int | Unset = UNSET
    mj_custom_id: str | Unset = UNSET
    mj_event_payload: str | Unset = UNSET
    headers: PostSendV3BodyHeaders | Unset = UNSET
    vars_: PostSendV3BodyVars | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_email = self.from_email

        from_name = self.from_name

        sender = self.sender

        recipients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        to = self.to

        cc = self.cc

        bcc = self.bcc

        subject = self.subject

        text_part = self.text_part

        html_part = self.html_part

        mj_template_id = self.mj_template_id

        mj_template_language = self.mj_template_language

        mj_template_error_reporting = self.mj_template_error_reporting

        mj_template_error_deliver = self.mj_template_error_deliver

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        inline_attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inline_attachments, Unset):
            inline_attachments = []
            for inline_attachments_item_data in self.inline_attachments:
                inline_attachments_item = inline_attachments_item_data.to_dict()
                inline_attachments.append(inline_attachments_item)

        mj_prio = self.mj_prio

        mj_campaign = self.mj_campaign

        mj_deduplicatecampaign = self.mj_deduplicatecampaign

        mj_trackopen = self.mj_trackopen

        mj_trackclick = self.mj_trackclick

        mj_custom_id = self.mj_custom_id

        mj_event_payload = self.mj_event_payload

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        vars_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vars_, Unset):
            vars_ = self.vars_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_email is not UNSET:
            field_dict["FromEmail"] = from_email
        if from_name is not UNSET:
            field_dict["FromName"] = from_name
        if sender is not UNSET:
            field_dict["Sender"] = sender
        if recipients is not UNSET:
            field_dict["Recipients"] = recipients
        if to is not UNSET:
            field_dict["To"] = to
        if cc is not UNSET:
            field_dict["Cc"] = cc
        if bcc is not UNSET:
            field_dict["Bcc"] = bcc
        if subject is not UNSET:
            field_dict["Subject"] = subject
        if text_part is not UNSET:
            field_dict["Text-part"] = text_part
        if html_part is not UNSET:
            field_dict["Html-part"] = html_part
        if mj_template_id is not UNSET:
            field_dict["Mj-TemplateID"] = mj_template_id
        if mj_template_language is not UNSET:
            field_dict["Mj-TemplateLanguage"] = mj_template_language
        if mj_template_error_reporting is not UNSET:
            field_dict["Mj-TemplateErrorReporting"] = mj_template_error_reporting
        if mj_template_error_deliver is not UNSET:
            field_dict["Mj-TemplateErrorDeliver"] = mj_template_error_deliver
        if attachments is not UNSET:
            field_dict["Attachments"] = attachments
        if inline_attachments is not UNSET:
            field_dict["Inline_attachments"] = inline_attachments
        if mj_prio is not UNSET:
            field_dict["Mj-prio"] = mj_prio
        if mj_campaign is not UNSET:
            field_dict["Mj-campaign"] = mj_campaign
        if mj_deduplicatecampaign is not UNSET:
            field_dict["Mj-deduplicatecampaign"] = mj_deduplicatecampaign
        if mj_trackopen is not UNSET:
            field_dict["Mj-trackopen"] = mj_trackopen
        if mj_trackclick is not UNSET:
            field_dict["Mj-trackclick"] = mj_trackclick
        if mj_custom_id is not UNSET:
            field_dict["Mj-CustomID"] = mj_custom_id
        if mj_event_payload is not UNSET:
            field_dict["Mj-EventPayload"] = mj_event_payload
        if headers is not UNSET:
            field_dict["Headers"] = headers
        if vars_ is not UNSET:
            field_dict["Vars"] = vars_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_send_v3_body_attachments_item import (
            PostSendV3BodyAttachmentsItem,
        )
        from ..models.post_send_v3_body_headers import PostSendV3BodyHeaders
        from ..models.post_send_v3_body_inline_attachments_item import (
            PostSendV3BodyInlineAttachmentsItem,
        )
        from ..models.post_send_v3_body_recipients_item import (
            PostSendV3BodyRecipientsItem,
        )
        from ..models.post_send_v3_body_vars import PostSendV3BodyVars

        d = dict(src_dict)
        from_email = d.pop("FromEmail", UNSET)

        from_name = d.pop("FromName", UNSET)

        sender = d.pop("Sender", UNSET)

        _recipients = d.pop("Recipients", UNSET)
        recipients: list[PostSendV3BodyRecipientsItem] | Unset = UNSET
        if _recipients is not UNSET:
            recipients = []
            for recipients_item_data in _recipients:
                recipients_item = PostSendV3BodyRecipientsItem.from_dict(
                    recipients_item_data
                )

                recipients.append(recipients_item)

        to = d.pop("To", UNSET)

        cc = d.pop("Cc", UNSET)

        bcc = d.pop("Bcc", UNSET)

        subject = d.pop("Subject", UNSET)

        text_part = d.pop("Text-part", UNSET)

        html_part = d.pop("Html-part", UNSET)

        mj_template_id = d.pop("Mj-TemplateID", UNSET)

        mj_template_language = d.pop("Mj-TemplateLanguage", UNSET)

        mj_template_error_reporting = d.pop("Mj-TemplateErrorReporting", UNSET)

        mj_template_error_deliver = d.pop("Mj-TemplateErrorDeliver", UNSET)

        _attachments = d.pop("Attachments", UNSET)
        attachments: list[PostSendV3BodyAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = PostSendV3BodyAttachmentsItem.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        _inline_attachments = d.pop("Inline_attachments", UNSET)
        inline_attachments: list[PostSendV3BodyInlineAttachmentsItem] | Unset = UNSET
        if _inline_attachments is not UNSET:
            inline_attachments = []
            for inline_attachments_item_data in _inline_attachments:
                inline_attachments_item = PostSendV3BodyInlineAttachmentsItem.from_dict(
                    inline_attachments_item_data
                )

                inline_attachments.append(inline_attachments_item)

        mj_prio = d.pop("Mj-prio", UNSET)

        mj_campaign = d.pop("Mj-campaign", UNSET)

        mj_deduplicatecampaign = d.pop("Mj-deduplicatecampaign", UNSET)

        mj_trackopen = d.pop("Mj-trackopen", UNSET)

        mj_trackclick = d.pop("Mj-trackclick", UNSET)

        mj_custom_id = d.pop("Mj-CustomID", UNSET)

        mj_event_payload = d.pop("Mj-EventPayload", UNSET)

        _headers = d.pop("Headers", UNSET)
        headers: PostSendV3BodyHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = PostSendV3BodyHeaders.from_dict(_headers)

        _vars_ = d.pop("Vars", UNSET)
        vars_: PostSendV3BodyVars | Unset
        if isinstance(_vars_, Unset):
            vars_ = UNSET
        else:
            vars_ = PostSendV3BodyVars.from_dict(_vars_)

        post_send_v3_body = cls(
            from_email=from_email,
            from_name=from_name,
            sender=sender,
            recipients=recipients,
            to=to,
            cc=cc,
            bcc=bcc,
            subject=subject,
            text_part=text_part,
            html_part=html_part,
            mj_template_id=mj_template_id,
            mj_template_language=mj_template_language,
            mj_template_error_reporting=mj_template_error_reporting,
            mj_template_error_deliver=mj_template_error_deliver,
            attachments=attachments,
            inline_attachments=inline_attachments,
            mj_prio=mj_prio,
            mj_campaign=mj_campaign,
            mj_deduplicatecampaign=mj_deduplicatecampaign,
            mj_trackopen=mj_trackopen,
            mj_trackclick=mj_trackclick,
            mj_custom_id=mj_custom_id,
            mj_event_payload=mj_event_payload,
            headers=headers,
            vars_=vars_,
        )

        post_send_v3_body.additional_properties = d
        return post_send_v3_body

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
