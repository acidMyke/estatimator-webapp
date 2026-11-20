from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_get_placements_request import MainGetPlacementsRequest
from ...models.main_get_placements_response import MainGetPlacementsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: MainGetPlacementsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/platform/placements",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> MainGetPlacementsResponse | None:
    if response.status_code == 200:
        response_200 = MainGetPlacementsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[MainGetPlacementsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MainGetPlacementsRequest,
) -> Response[MainGetPlacementsResponse]:
    """Get Placements

     Simulates placing the specified number of machines into regions, depending on available capacity and
    limits.

    Args:
        body (MainGetPlacementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainGetPlacementsResponse]
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
    body: MainGetPlacementsRequest,
) -> MainGetPlacementsResponse | None:
    """Get Placements

     Simulates placing the specified number of machines into regions, depending on available capacity and
    limits.

    Args:
        body (MainGetPlacementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainGetPlacementsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MainGetPlacementsRequest,
) -> Response[MainGetPlacementsResponse]:
    """Get Placements

     Simulates placing the specified number of machines into regions, depending on available capacity and
    limits.

    Args:
        body (MainGetPlacementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainGetPlacementsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MainGetPlacementsRequest,
) -> MainGetPlacementsResponse | None:
    """Get Placements

     Simulates placing the specified number of machines into regions, depending on available capacity and
    limits.

    Args:
        body (MainGetPlacementsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainGetPlacementsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
