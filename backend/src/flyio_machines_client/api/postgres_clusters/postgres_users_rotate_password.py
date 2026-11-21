from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postgres_error_response import PostgresErrorResponse
from ...models.rotate_postgres_password_request import RotatePostgresPasswordRequest
from ...models.rotate_postgres_password_response import RotatePostgresPasswordResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    postgres_cluster_id: str,
    username: str,
    *,
    body: RotatePostgresPasswordRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/postgres/{postgres_cluster_id}/users/{username}/rotate_password".format(
            postgres_cluster_id=quote(str(postgres_cluster_id), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PostgresErrorResponse | RotatePostgresPasswordResponse | None:
    if response.status_code == 200:
        response_200 = RotatePostgresPasswordResponse.from_dict(response.json())

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

    if response.status_code == 410:
        response_410 = PostgresErrorResponse.from_dict(response.json())

        return response_410

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
) -> Response[PostgresErrorResponse | RotatePostgresPasswordResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    postgres_cluster_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: RotatePostgresPasswordRequest | Unset = UNSET,
) -> Response[PostgresErrorResponse | RotatePostgresPasswordResponse]:
    """Rotate User Password

     Rotate a specific Postgres user's password within a cluster, optionally terminating the user's
    existing sessions.

    Args:
        postgres_cluster_id (str):
        username (str):
        body (RotatePostgresPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostgresErrorResponse | RotatePostgresPasswordResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    postgres_cluster_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: RotatePostgresPasswordRequest | Unset = UNSET,
) -> PostgresErrorResponse | RotatePostgresPasswordResponse | None:
    """Rotate User Password

     Rotate a specific Postgres user's password within a cluster, optionally terminating the user's
    existing sessions.

    Args:
        postgres_cluster_id (str):
        username (str):
        body (RotatePostgresPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostgresErrorResponse | RotatePostgresPasswordResponse
    """

    return sync_detailed(
        postgres_cluster_id=postgres_cluster_id,
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    postgres_cluster_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: RotatePostgresPasswordRequest | Unset = UNSET,
) -> Response[PostgresErrorResponse | RotatePostgresPasswordResponse]:
    """Rotate User Password

     Rotate a specific Postgres user's password within a cluster, optionally terminating the user's
    existing sessions.

    Args:
        postgres_cluster_id (str):
        username (str):
        body (RotatePostgresPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostgresErrorResponse | RotatePostgresPasswordResponse]
    """

    kwargs = _get_kwargs(
        postgres_cluster_id=postgres_cluster_id,
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    postgres_cluster_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: RotatePostgresPasswordRequest | Unset = UNSET,
) -> PostgresErrorResponse | RotatePostgresPasswordResponse | None:
    """Rotate User Password

     Rotate a specific Postgres user's password within a cluster, optionally terminating the user's
    existing sessions.

    Args:
        postgres_cluster_id (str):
        username (str):
        body (RotatePostgresPasswordRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostgresErrorResponse | RotatePostgresPasswordResponse
    """

    return (
        await asyncio_detailed(
            postgres_cluster_id=postgres_cluster_id,
            username=username,
            client=client,
            body=body,
        )
    ).parsed
