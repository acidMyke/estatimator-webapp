from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postgres_error_response import PostgresErrorResponse
from ...models.postgres_query_response import PostgresQueryResponse
from ...models.query_postgres_database_request import QueryPostgresDatabaseRequest
from ...types import Response


def _get_kwargs(
    postgres_cluster_id: str,
    database_name: str,
    *,
    body: QueryPostgresDatabaseRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/postgres/{postgres_cluster_id}/databases/{database_name}/query".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
            database_name=quote(str(database_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PostgresErrorResponse | PostgresQueryResponse | None:
    if response.status_code == 200:
        response_200 = PostgresQueryResponse.from_dict(response.json())

        return response_200

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

    if response.status_code == 500:
        response_500 = PostgresErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = PostgresErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[PostgresErrorResponse | PostgresQueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    postgres_cluster_id: str,
    database_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: QueryPostgresDatabaseRequest,
) -> Response[PostgresErrorResponse | PostgresQueryResponse]:
    """Query Database

     Run read-only SQL against a database and return the final result set. The SQL runs as
    pg_read_all_data inside a read-only transaction with a statement timeout, so it can read every table
    but cannot change data or schema. Results over 1000 rows are rejected rather than truncated; add a
    LIMIT. System databases cannot be queried. Requires only read access to the organization.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        body (QueryPostgresDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostgresErrorResponse | PostgresQueryResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        database_name=database_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_cluster_id: str,
    database_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: QueryPostgresDatabaseRequest,
) -> PostgresErrorResponse | PostgresQueryResponse | None:
    """Query Database

     Run read-only SQL against a database and return the final result set. The SQL runs as
    pg_read_all_data inside a read-only transaction with a statement timeout, so it can read every table
    but cannot change data or schema. Results over 1000 rows are rejected rather than truncated; add a
    LIMIT. System databases cannot be queried. Requires only read access to the organization.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        body (QueryPostgresDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostgresErrorResponse | PostgresQueryResponse
    """

    return sync_detailed(
        postgres_cluster_id=postgres_cluster_id,
        database_name=database_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    postgres_cluster_id: str,
    database_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: QueryPostgresDatabaseRequest,
) -> Response[PostgresErrorResponse | PostgresQueryResponse]:
    """Query Database

     Run read-only SQL against a database and return the final result set. The SQL runs as
    pg_read_all_data inside a read-only transaction with a statement timeout, so it can read every table
    but cannot change data or schema. Results over 1000 rows are rejected rather than truncated; add a
    LIMIT. System databases cannot be queried. Requires only read access to the organization.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        body (QueryPostgresDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostgresErrorResponse | PostgresQueryResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        database_name=database_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_cluster_id: str,
    database_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: QueryPostgresDatabaseRequest,
) -> PostgresErrorResponse | PostgresQueryResponse | None:
    """Query Database

     Run read-only SQL against a database and return the final result set. The SQL runs as
    pg_read_all_data inside a read-only transaction with a statement timeout, so it can read every table
    but cannot change data or schema. Results over 1000 rows are rejected rather than truncated; add a
    LIMIT. System databases cannot be queried. Requires only read access to the organization.

    Args:
        postgres_cluster_id (str):
        database_name (str):
        body (QueryPostgresDatabaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostgresErrorResponse | PostgresQueryResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            database_name=database_name,
            client=client,
            body=body,
        )
    ).parsed
