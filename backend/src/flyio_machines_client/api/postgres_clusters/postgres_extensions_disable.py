from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postgres_error_response import PostgresErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    postgres_cluster_id: str,
    database_name: str,
    extension_name: str,
    *,
    force: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/postgres/{postgres_cluster_id}/databases/{database_name}/extensions/{extension_name}".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
            database_name=quote(str(database_name), safe=""),
            extension_name=quote(str(extension_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | PostgresErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = PostgresErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostgresErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = PostgresErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PostgresErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = PostgresErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | PostgresErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    postgres_cluster_id: str,
    database_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Response[Any | PostgresErrorResponse]:
    """Disable Extension

     Disable a specific Postgres extension within a database, optionally dropping objects that depend on
    it. System extensions cannot be disabled.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        extension_name (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        database_name=database_name,
        extension_name=extension_name,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_cluster_id: str,
    database_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Any | PostgresErrorResponse | None:
    """Disable Extension

     Disable a specific Postgres extension within a database, optionally dropping objects that depend on
    it. System extensions cannot be disabled.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        extension_name (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostgresErrorResponse
    """

    return sync_detailed(
        postgres_cluster_id=postgres_cluster_id,
        database_name=database_name,
        extension_name=extension_name,
        client=client,
        force=force,
    ).parsed


async def asyncio_detailed(
    postgres_cluster_id: str,
    database_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Response[Any | PostgresErrorResponse]:
    """Disable Extension

     Disable a specific Postgres extension within a database, optionally dropping objects that depend on
    it. System extensions cannot be disabled.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        extension_name (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        database_name=database_name,
        extension_name=extension_name,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_cluster_id: str,
    database_name: str,
    extension_name: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Any | PostgresErrorResponse | None:
    """Disable Extension

     Disable a specific Postgres extension within a database, optionally dropping objects that depend on
    it. System extensions cannot be disabled.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        extension_name (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostgresErrorResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            database_name=database_name,
            extension_name=extension_name,
            client=client,
            force=force,
        )
    ).parsed
