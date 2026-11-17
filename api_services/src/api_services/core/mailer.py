from dataclasses import dataclass
from typing import cast

from api_services.clients.mailjet_send.api.send_emails import post_send_v31
from api_services.clients.mailjet_send.client import (
    AuthenticatedClient as MailjetClient,
)
from api_services.clients.mailjet_send.models.post_send_v31_body import PostSendV31Body
from api_services.clients.mailjet_send.models.post_send_v31_body_messages_item import (
    PostSendV31BodyMessagesItem,
)
from api_services.clients.mailjet_send.models.post_send_v31_body_messages_item_from import (
    PostSendV31BodyMessagesItemFrom,
)
from api_services.clients.mailjet_send.models.post_send_v31_body_messages_item_to_item import (
    PostSendV31BodyMessagesItemToItem,
)
from api_services.clients.mailjet_send.types import UNSET
from api_services.core.settings import settings

mailjet_client = cast(
    MailjetClient,
    MailjetClient(
        base_url="https://api.mailjet.com",
        auth_header_name="Basic",
        token=settings.mailjet_auth_token,
    )
    if settings.is_mailjet_configured
    else None,
)


@dataclass
class RawHtmlEmailPayload:
    to_email: str
    to_name: str | None
    subject: str
    html_content: str


async def send_email(payload: RawHtmlEmailPayload):
    if settings.is_mailjet_configured:
        await _send_via_mailjet_http(payload)
    else:
        await _send_via_mailpit_smtp(payload)


async def _send_via_mailjet_http(payload: RawHtmlEmailPayload):
    return post_send_v31.asyncio(
        client=mailjet_client,
        body=PostSendV31Body(
            messages=[
                PostSendV31BodyMessagesItem(
                    from_=PostSendV31BodyMessagesItemFrom(
                        email=settings.FROM_EMAIL, name=settings.FROM_NAME
                    ),
                    to=[
                        PostSendV31BodyMessagesItemToItem(
                            email=payload.to_email,
                            name=payload.to_name if payload.to_name else UNSET,
                        )
                    ],
                    subject=payload.subject,
                    html_part=payload.html_content,
                )
            ]
        ),
    )


async def _send_via_mailpit_smtp(payload: RawHtmlEmailPayload):
    raise NotImplementedError()
