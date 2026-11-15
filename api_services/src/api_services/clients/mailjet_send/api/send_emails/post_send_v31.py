from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_send_v31_body import PostSendV31Body
from ...models.post_send_v31_response_201 import PostSendV31Response201
from ...types import Response


def _get_kwargs(
    *,
    body: PostSendV31Body,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3.1/send",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | PostSendV31Response201 | None:
    if response.status_code == 201:
        response_201 = PostSendV31Response201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | PostSendV31Response201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSendV31Body,
) -> Response[Any | PostSendV31Response201]:
    """Send an email message via Send API v3.1

     Send API v3.1 is built mainly for reliability, providing very detailed information in case of
    sending errors. This results in a lower sending limit, however - Send API v3.1 allows you to send up
    to 50 messages in a single API call, as opposed to v3, where the limit is 100 messages per call.

    Additionally, Send API v3.1 includes a Sandbox mode. When enabled, the API will perform all the
    required validations and return success or error messages, but the message will not be sent.

    Args:
        body (PostSendV31Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSendV31Response201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostSendV31Body,
) -> Any | PostSendV31Response201 | None:
    """Send an email message via Send API v3.1

     Send API v3.1 is built mainly for reliability, providing very detailed information in case of
    sending errors. This results in a lower sending limit, however - Send API v3.1 allows you to send up
    to 50 messages in a single API call, as opposed to v3, where the limit is 100 messages per call.

    Additionally, Send API v3.1 includes a Sandbox mode. When enabled, the API will perform all the
    required validations and return success or error messages, but the message will not be sent.

    Args:
        body (PostSendV31Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSendV31Response201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSendV31Body,
) -> Response[Any | PostSendV31Response201]:
    """Send an email message via Send API v3.1

     Send API v3.1 is built mainly for reliability, providing very detailed information in case of
    sending errors. This results in a lower sending limit, however - Send API v3.1 allows you to send up
    to 50 messages in a single API call, as opposed to v3, where the limit is 100 messages per call.

    Additionally, Send API v3.1 includes a Sandbox mode. When enabled, the API will perform all the
    required validations and return success or error messages, but the message will not be sent.

    Args:
        body (PostSendV31Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSendV31Response201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostSendV31Body,
) -> Any | PostSendV31Response201 | None:
    """Send an email message via Send API v3.1

     Send API v3.1 is built mainly for reliability, providing very detailed information in case of
    sending errors. This results in a lower sending limit, however - Send API v3.1 allows you to send up
    to 50 messages in a single API call, as opposed to v3, where the limit is 100 messages per call.

    Additionally, Send API v3.1 includes a Sandbox mode. When enabled, the API will perform all the
    required validations and return success or error messages, but the message will not be sent.

    Args:
        body (PostSendV31Body):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSendV31Response201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
