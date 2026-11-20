from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_oidc_token_request import CreateOIDCTokenRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateOIDCTokenRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tokens/oidc",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.text)

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOIDCTokenRequest | Unset = UNSET,
) -> Response[ErrorResponse | str]:
    """Request an OIDC token

     Request an Open ID Connect token for your machine. Customize the audience claim with the `aud`
    parameter. This returns a JWT token. Learn more about [using OpenID
    Connect](https://docs.fly.io/security/openid-connect) on Fly.io.

    Args:
        body (CreateOIDCTokenRequest | Unset): Optional parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
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
    client: AuthenticatedClient | Client,
    body: CreateOIDCTokenRequest | Unset = UNSET,
) -> ErrorResponse | str | None:
    """Request an OIDC token

     Request an Open ID Connect token for your machine. Customize the audience claim with the `aud`
    parameter. This returns a JWT token. Learn more about [using OpenID
    Connect](https://docs.fly.io/security/openid-connect) on Fly.io.

    Args:
        body (CreateOIDCTokenRequest | Unset): Optional parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOIDCTokenRequest | Unset = UNSET,
) -> Response[ErrorResponse | str]:
    """Request an OIDC token

     Request an Open ID Connect token for your machine. Customize the audience claim with the `aud`
    parameter. This returns a JWT token. Learn more about [using OpenID
    Connect](https://docs.fly.io/security/openid-connect) on Fly.io.

    Args:
        body (CreateOIDCTokenRequest | Unset): Optional parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOIDCTokenRequest | Unset = UNSET,
) -> ErrorResponse | str | None:
    """Request an OIDC token

     Request an Open ID Connect token for your machine. Customize the audience claim with the `aud`
    parameter. This returns a JWT token. Learn more about [using OpenID
    Connect](https://docs.fly.io/security/openid-connect) on Fly.io.

    Args:
        body (CreateOIDCTokenRequest | Unset): Optional parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
