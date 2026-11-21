from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_postgres_users_response import ListPostgresUsersResponse
from ...models.postgres_error_response import PostgresErrorResponse
from ...types import Response


def _get_kwargs(
    postgres_cluster_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/postgres/{postgres_cluster_id}/users".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListPostgresUsersResponse | PostgresErrorResponse | None:
    if response.status_code == 200:
        response_200 = ListPostgresUsersResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostgresErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = PostgresErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = PostgresErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListPostgresUsersResponse | PostgresErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListPostgresUsersResponse | PostgresErrorResponse]:
    """List Users

     List all Postgres users within a specific cluster.

    Args:
        postgres_cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostgresUsersResponse | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ListPostgresUsersResponse | PostgresErrorResponse | None:
    """List Users

     List all Postgres users within a specific cluster.

    Args:
        postgres_cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostgresUsersResponse | PostgresErrorResponse
    """

    return sync_detailed(
        postgres_cluster_id=postgres_cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListPostgresUsersResponse | PostgresErrorResponse]:
    """List Users

     List all Postgres users within a specific cluster.

    Args:
        postgres_cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostgresUsersResponse | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ListPostgresUsersResponse | PostgresErrorResponse | None:
    """List Users

     List all Postgres users within a specific cluster.

    Args:
        postgres_cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostgresUsersResponse | PostgresErrorResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            client=client,
        )
    ).parsed
