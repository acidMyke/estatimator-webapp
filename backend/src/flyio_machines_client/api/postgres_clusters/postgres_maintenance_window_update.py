from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postgres_error_response import PostgresErrorResponse
from ...models.show_postgres_maintenance_window_response import (
    ShowPostgresMaintenanceWindowResponse,
)
from ...models.update_postgres_maintenance_window_request import (
    UpdatePostgresMaintenanceWindowRequest,
)
from ...types import Response


def _get_kwargs(
    postgres_cluster_id: str,
    *,
    body: UpdatePostgresMaintenanceWindowRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/postgres/{postgres_cluster_id}/maintenance_window".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse | None:
    if response.status_code == 200:
        response_200 = ShowPostgresMaintenanceWindowResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PostgresErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = PostgresErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = PostgresErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = PostgresErrorResponse.from_dict(response.json())

        return response_410

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
) -> Response[PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse]:
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
    body: UpdatePostgresMaintenanceWindowRequest,
) -> Response[PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse]:
    """Update Maintenance Window

     Update a cluster's weekly maintenance window. Give at least one of `day`, `start_hour` and
    `duration_hours`; omitted fields keep their current value. `start_hour` is in the cluster's
    timezone, which is derived from its region and cannot be changed. Changes are accepted only while
    the cluster is ready and no maintenance is running.

    Args:
        postgres_cluster_id (str):
        body (UpdatePostgresMaintenanceWindowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePostgresMaintenanceWindowRequest,
) -> PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse | None:
    """Update Maintenance Window

     Update a cluster's weekly maintenance window. Give at least one of `day`, `start_hour` and
    `duration_hours`; omitted fields keep their current value. `start_hour` is in the cluster's
    timezone, which is derived from its region and cannot be changed. Changes are accepted only while
    the cluster is ready and no maintenance is running.

    Args:
        postgres_cluster_id (str):
        body (UpdatePostgresMaintenanceWindowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse
    """

    return sync_detailed(
        postgres_cluster_id=postgres_cluster_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePostgresMaintenanceWindowRequest,
) -> Response[PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse]:
    """Update Maintenance Window

     Update a cluster's weekly maintenance window. Give at least one of `day`, `start_hour` and
    `duration_hours`; omitted fields keep their current value. `start_hour` is in the cluster's
    timezone, which is derived from its region and cannot be changed. Changes are accepted only while
    the cluster is ready and no maintenance is running.

    Args:
        postgres_cluster_id (str):
        body (UpdatePostgresMaintenanceWindowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePostgresMaintenanceWindowRequest,
) -> PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse | None:
    """Update Maintenance Window

     Update a cluster's weekly maintenance window. Give at least one of `day`, `start_hour` and
    `duration_hours`; omitted fields keep their current value. `start_hour` is in the cluster's
    timezone, which is derived from its region and cannot be changed. Changes are accepted only while
    the cluster is ready and no maintenance is running.

    Args:
        postgres_cluster_id (str):
        body (UpdatePostgresMaintenanceWindowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostgresErrorResponse | ShowPostgresMaintenanceWindowResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            client=client,
            body=body,
        )
    ).parsed
