from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_app_secret_response import DeleteAppSecretResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    secret_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_name}/secrets/{secret_name}".format(
            app_name=quote(str(app_name), safe=""),
            secret_name=quote(str(secret_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeleteAppSecretResponse | None:
    if response.status_code == 200:
        response_200 = DeleteAppSecretResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeleteAppSecretResponse]:
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
) -> Response[DeleteAppSecretResponse]:
    """Delete an app secret

     Running Machines don't pick up the change on their own: create or update Machines with
    `min_secrets_version` set to the returned `version` for them to see it.

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAppSecretResponse]
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
) -> DeleteAppSecretResponse | None:
    """Delete an app secret

     Running Machines don't pick up the change on their own: create or update Machines with
    `min_secrets_version` set to the returned `version` for them to see it.

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAppSecretResponse
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
) -> Response[DeleteAppSecretResponse]:
    """Delete an app secret

     Running Machines don't pick up the change on their own: create or update Machines with
    `min_secrets_version` set to the returned `version` for them to see it.

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAppSecretResponse]
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
) -> DeleteAppSecretResponse | None:
    """Delete an app secret

     Running Machines don't pick up the change on their own: create or update Machines with
    `min_secrets_version` set to the returned `version` for them to see it.

    Args:
        app_name (str):
        secret_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAppSecretResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            secret_name=secret_name,
            client=client,
        )
    ).parsed
