from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.secret_keys import SecretKeys
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    *,
    min_version: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["min_version"] = min_version

    params["types"] = types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/secretkeys".format(
            app_name=quote(str(app_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> SecretKeys | None:
    if response.status_code == 200:
        response_200 = SecretKeys.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SecretKeys]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    min_version: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[SecretKeys]:
    """List secret keys belonging to an app

    Args:
        app_name (str):
        min_version (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretKeys]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        min_version=min_version,
        types=types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    min_version: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> SecretKeys | None:
    """List secret keys belonging to an app

    Args:
        app_name (str):
        min_version (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretKeys
    """

    return sync_detailed(
        app_name=app_name,
        client=client,
        min_version=min_version,
        types=types,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    min_version: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[SecretKeys]:
    """List secret keys belonging to an app

    Args:
        app_name (str):
        min_version (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretKeys]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        min_version=min_version,
        types=types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    min_version: str | Unset = UNSET,
    types: str | Unset = UNSET,
) -> SecretKeys | None:
    """List secret keys belonging to an app

    Args:
        app_name (str):
        min_version (str | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretKeys
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            client=client,
            min_version=min_version,
            types=types,
        )
    ).parsed
