from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_secretkey_response import DeleteSecretkeyResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    secret_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_name}/secretkeys/{secret_name}".format(
            app_name=quote(str(app_name), safe=""),
            secret_name=quote(str(secret_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeleteSecretkeyResponse | None:
    if response.status_code == 200:
        response_200 = DeleteSecretkeyResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeleteSecretkeyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteSecretkeyResponse]:
    """Delete an app's secret key

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSecretkeyResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        secret_name=secret_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteSecretkeyResponse | None:
    """Delete an app's secret key

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSecretkeyResponse
    """

    return sync_detailed(
        app_name=app_name,
        secret_name=secret_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteSecretkeyResponse]:
    """Delete an app's secret key

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSecretkeyResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        secret_name=secret_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteSecretkeyResponse | None:
    """Delete an app's secret key

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSecretkeyResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            secret_name=secret_name,
            client=client,
        )
    ).parsed
