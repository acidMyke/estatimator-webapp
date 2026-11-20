from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_postgres_slow_queries_response import (
    ListPostgresSlowQueriesResponse,
)
from ...models.postgres_error_response import PostgresErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    postgres_cluster_id: str,
    *,
    range_: int | Unset = 3600,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["range"] = range_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/postgres/{postgres_cluster_id}/queries/slow".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListPostgresSlowQueriesResponse | PostgresErrorResponse | None:
    if response.status_code == 200:
        response_200 = ListPostgresSlowQueriesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostgresErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = PostgresErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PostgresErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = PostgresErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListPostgresSlowQueriesResponse | PostgresErrorResponse]:
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
    range_: int | Unset = 3600,
) -> Response[ListPostgresSlowQueriesResponse | PostgresErrorResponse]:
    """List Slow Queries

     List the top 20 queries by cumulative total execution time, excluding the postgres database. Uses
    the latest available metrics within the lookback range; statistics are cumulative PostgreSQL
    counters, not deltas over that range. Returns full query text and execution times in seconds.

    Args:
        postgres_cluster_id (str):
        range_ (int | Unset):  Default: 3600.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostgresSlowQueriesResponse | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: int | Unset = 3600,
) -> ListPostgresSlowQueriesResponse | PostgresErrorResponse | None:
    """List Slow Queries

     List the top 20 queries by cumulative total execution time, excluding the postgres database. Uses
    the latest available metrics within the lookback range; statistics are cumulative PostgreSQL
    counters, not deltas over that range. Returns full query text and execution times in seconds.

    Args:
        postgres_cluster_id (str):
        range_ (int | Unset):  Default: 3600.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostgresSlowQueriesResponse | PostgresErrorResponse
    """

    return sync_detailed(
        postgres_cluster_id=postgres_cluster_id,
        client=client,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: int | Unset = 3600,
) -> Response[ListPostgresSlowQueriesResponse | PostgresErrorResponse]:
    """List Slow Queries

     List the top 20 queries by cumulative total execution time, excluding the postgres database. Uses
    the latest available metrics within the lookback range; statistics are cumulative PostgreSQL
    counters, not deltas over that range. Returns full query text and execution times in seconds.

    Args:
        postgres_cluster_id (str):
        range_ (int | Unset):  Default: 3600.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostgresSlowQueriesResponse | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: int | Unset = 3600,
) -> ListPostgresSlowQueriesResponse | PostgresErrorResponse | None:
    """List Slow Queries

     List the top 20 queries by cumulative total execution time, excluding the postgres database. Uses
    the latest available metrics within the lookback range; statistics are cumulative PostgreSQL
    counters, not deltas over that range. Returns full query text and execution times in seconds.

    Args:
        postgres_cluster_id (str):
        range_ (int | Unset):  Default: 3600.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostgresSlowQueriesResponse | PostgresErrorResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            client=client,
            range_=range_,
        )
    ).parsed
