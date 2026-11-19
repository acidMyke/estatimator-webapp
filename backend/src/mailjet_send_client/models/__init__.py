"""Contains all the data models used in inputs/outputs"""

from .post_send_v3_body import PostSendV3Body
from .post_send_v3_body_attachments_item import PostSendV3BodyAttachmentsItem
from .post_send_v3_body_headers import PostSendV3BodyHeaders
from .post_send_v3_body_inline_attachments_item import (
    PostSendV3BodyInlineAttachmentsItem,
)
from .post_send_v3_body_recipients_item import PostSendV3BodyRecipientsItem
from .post_send_v3_body_vars import PostSendV3BodyVars
from .post_send_v3_response_201 import PostSendV3Response201
from .post_send_v3_response_201_sent_item import PostSendV3Response201SentItem
from .post_send_v31_body import PostSendV31Body
from .post_send_v31_body_globals import PostSendV31BodyGlobals
from .post_send_v31_body_messages_item import PostSendV31BodyMessagesItem
from .post_send_v31_body_messages_item_attachments_item import (
    PostSendV31BodyMessagesItemAttachmentsItem,
)
from .post_send_v31_body_messages_item_bcc_item import (
    PostSendV31BodyMessagesItemBccItem,
)
from .post_send_v31_body_messages_item_cc_item import PostSendV31BodyMessagesItemCcItem
from .post_send_v31_body_messages_item_from import PostSendV31BodyMessagesItemFrom
from .post_send_v31_body_messages_item_headers import PostSendV31BodyMessagesItemHeaders
from .post_send_v31_body_messages_item_inlined_attachments_item import (
    PostSendV31BodyMessagesItemInlinedAttachmentsItem,
)
from .post_send_v31_body_messages_item_reply_to import (
    PostSendV31BodyMessagesItemReplyTo,
)
from .post_send_v31_body_messages_item_sender import PostSendV31BodyMessagesItemSender
from .post_send_v31_body_messages_item_template_error_reporting import (
    PostSendV31BodyMessagesItemTemplateErrorReporting,
)
from .post_send_v31_body_messages_item_to_item import PostSendV31BodyMessagesItemToItem
from .post_send_v31_body_messages_item_track_clicks import (
    PostSendV31BodyMessagesItemTrackClicks,
)
from .post_send_v31_body_messages_item_track_opens import (
    PostSendV31BodyMessagesItemTrackOpens,
)
from .post_send_v31_body_messages_item_variables import (
    PostSendV31BodyMessagesItemVariables,
)
from .post_send_v31_response_201 import PostSendV31Response201
from .post_send_v31_response_201_messages_item import PostSendV31Response201MessagesItem
from .post_send_v31_response_201_messages_item_bcc_item import (
    PostSendV31Response201MessagesItemBccItem,
)
from .post_send_v31_response_201_messages_item_cc_item import (
    PostSendV31Response201MessagesItemCcItem,
)
from .post_send_v31_response_201_messages_item_errors_item import (
    PostSendV31Response201MessagesItemErrorsItem,
)
from .post_send_v31_response_201_messages_item_errors_item_error_related_to import (
    PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo,
)
from .post_send_v31_response_201_messages_item_to_item import (
    PostSendV31Response201MessagesItemToItem,
)

__all__ = (
    "PostSendV3Body",
    "PostSendV3BodyAttachmentsItem",
    "PostSendV3BodyHeaders",
    "PostSendV3BodyInlineAttachmentsItem",
    "PostSendV3BodyRecipientsItem",
    "PostSendV3BodyVars",
    "PostSendV3Response201",
    "PostSendV3Response201SentItem",
    "PostSendV31Body",
    "PostSendV31BodyGlobals",
    "PostSendV31BodyMessagesItem",
    "PostSendV31BodyMessagesItemAttachmentsItem",
    "PostSendV31BodyMessagesItemBccItem",
    "PostSendV31BodyMessagesItemCcItem",
    "PostSendV31BodyMessagesItemFrom",
    "PostSendV31BodyMessagesItemHeaders",
    "PostSendV31BodyMessagesItemInlinedAttachmentsItem",
    "PostSendV31BodyMessagesItemReplyTo",
    "PostSendV31BodyMessagesItemSender",
    "PostSendV31BodyMessagesItemTemplateErrorReporting",
    "PostSendV31BodyMessagesItemToItem",
    "PostSendV31BodyMessagesItemTrackClicks",
    "PostSendV31BodyMessagesItemTrackOpens",
    "PostSendV31BodyMessagesItemVariables",
    "PostSendV31Response201",
    "PostSendV31Response201MessagesItem",
    "PostSendV31Response201MessagesItemBccItem",
    "PostSendV31Response201MessagesItemCcItem",
    "PostSendV31Response201MessagesItemErrorsItem",
    "PostSendV31Response201MessagesItemErrorsItemErrorRelatedTo",
    "PostSendV31Response201MessagesItemToItem",
)
