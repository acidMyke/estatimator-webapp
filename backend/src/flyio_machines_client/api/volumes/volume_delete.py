from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.volume import Volume
from ...types import Response


def _get_kwargs(
    app_name: str,
    volume_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_name}/volumes/{volume_id}".format(
            app_name=quote(str(app_name), safe=""),
            volume_id=quote(str(volume_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Volume | None:
    if response.status_code == 200:
        response_200 = Volume.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Volume]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Volume]:
    """Destroy Volume

     Delete a specific volume within an app by volume ID.

    Args:
        app_name (str):
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Volume]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        volume_id=volume_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Volume | None:
    """Destroy Volume

     Delete a specific volume within an app by volume ID.

    Args:
        app_name (str):
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Volume
    """

    return sync_detailed(
        app_name=app_name,
        volume_id=volume_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Volume]:
    """Destroy Volume

     Delete a specific volume within an app by volume ID.

    Args:
        app_name (str):
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Volume]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        volume_id=volume_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Volume | None:
    """Destroy Volume

     Delete a specific volume within an app by volume ID.

    Args:
        app_name (str):
        volume_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Volume
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            volume_id=volume_id,
            client=client,
        )
    ).parsed
