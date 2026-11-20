from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_postgres_attachment_request import CreatePostgresAttachmentRequest
from ...models.create_postgres_attachment_response import (
    CreatePostgresAttachmentResponse,
)
from ...models.postgres_error_response import PostgresErrorResponse
from ...types import Response


def _get_kwargs(
    postgres_cluster_id: str,
    *,
    body: CreatePostgresAttachmentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/postgres/{postgres_cluster_id}/attachments".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreatePostgresAttachmentResponse | PostgresErrorResponse | None:
    if response.status_code == 200:
        response_200 = CreatePostgresAttachmentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CreatePostgresAttachmentResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = PostgresErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = PostgresErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 410:
        response_410 = PostgresErrorResponse.from_dict(response.json())

        return response_410

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreatePostgresAttachmentResponse | PostgresErrorResponse]:
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
    body: CreatePostgresAttachmentRequest,
) -> Response[CreatePostgresAttachmentResponse | PostgresErrorResponse]:
    """Attach Cluster to App

     Record an attachment between a cluster and a Fly app. This endpoint records the relationship but
    does not set DATABASE_URL or other app secrets; configure the connection string separately. The
    attachment is created if it does not already exist.

    Args:
        postgres_cluster_id (str):
        body (CreatePostgresAttachmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePostgresAttachmentResponse | PostgresErrorResponse]
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
    body: CreatePostgresAttachmentRequest,
) -> CreatePostgresAttachmentResponse | PostgresErrorResponse | None:
    """Attach Cluster to App

     Record an attachment between a cluster and a Fly app. This endpoint records the relationship but
    does not set DATABASE_URL or other app secrets; configure the connection string separately. The
    attachment is created if it does not already exist.

    Args:
        postgres_cluster_id (str):
        body (CreatePostgresAttachmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePostgresAttachmentResponse | PostgresErrorResponse
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
    body: CreatePostgresAttachmentRequest,
) -> Response[CreatePostgresAttachmentResponse | PostgresErrorResponse]:
    """Attach Cluster to App

     Record an attachment between a cluster and a Fly app. This endpoint records the relationship but
    does not set DATABASE_URL or other app secrets; configure the connection string separately. The
    attachment is created if it does not already exist.

    Args:
        postgres_cluster_id (str):
        body (CreatePostgresAttachmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePostgresAttachmentResponse | PostgresErrorResponse]
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
    body: CreatePostgresAttachmentRequest,
) -> CreatePostgresAttachmentResponse | PostgresErrorResponse | None:
    """Attach Cluster to App

     Record an attachment between a cluster and a Fly app. This endpoint records the relationship but
    does not set DATABASE_URL or other app secrets; configure the connection string separately. The
    attachment is created if it does not already exist.

    Args:
        postgres_cluster_id (str):
        body (CreatePostgresAttachmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePostgresAttachmentResponse | PostgresErrorResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            client=client,
            body=body,
        )
    ).parsed
