from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_postgres_clusters_response import ListPostgresClustersResponse
from ...models.postgres_error_response import PostgresErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_slug: str,
    include_deleted: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["org_slug"] = org_slug

    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/postgres",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListPostgresClustersResponse | PostgresErrorResponse | None:
    if response.status_code == 200:
        response_200 = ListPostgresClustersResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListPostgresClustersResponse | PostgresErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_slug: str,
    include_deleted: bool | Unset = UNSET,
) -> Response[ListPostgresClustersResponse | PostgresErrorResponse]:
    """List Postgres Clusters

     List Managed Postgres clusters for an organization.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostgresClustersResponse | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        org_slug=org_slug,
        include_deleted=include_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_slug: str,
    include_deleted: bool | Unset = UNSET,
) -> ListPostgresClustersResponse | PostgresErrorResponse | None:
    """List Postgres Clusters

     List Managed Postgres clusters for an organization.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostgresClustersResponse | PostgresErrorResponse
    """

    return sync_detailed(
        client=client,
        org_slug=org_slug,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_slug: str,
    include_deleted: bool | Unset = UNSET,
) -> Response[ListPostgresClustersResponse | PostgresErrorResponse]:
    """List Postgres Clusters

     List Managed Postgres clusters for an organization.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostgresClustersResponse | PostgresErrorResponse]
    """

    kwargs = _get_kwargs(
        org_slug=org_slug,
        include_deleted=include_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_slug: str,
    include_deleted: bool | Unset = UNSET,
) -> ListPostgresClustersResponse | PostgresErrorResponse | None:
    """List Postgres Clusters

     List Managed Postgres clusters for an organization.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostgresClustersResponse | PostgresErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_slug=org_slug,
            include_deleted=include_deleted,
        )
    ).parsed
