from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.metadata_value_response import MetadataValueResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
    key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/metadata/{key}".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | MetadataValueResponse | None:
    if response.status_code == 200:
        response_200 = MetadataValueResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | MetadataValueResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    machine_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | MetadataValueResponse]:
    """Get Metadata Value

     Get the value of a specific metadata key

    Args:
        app_name (str):
        machine_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MetadataValueResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    machine_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | MetadataValueResponse | None:
    """Get Metadata Value

     Get the value of a specific metadata key

    Args:
        app_name (str):
        machine_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MetadataValueResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | MetadataValueResponse]:
    """Get Metadata Value

     Get the value of a specific metadata key

    Args:
        app_name (str):
        machine_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MetadataValueResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | MetadataValueResponse | None:
    """Get Metadata Value

     Get the value of a specific metadata key

    Args:
        app_name (str):
        machine_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MetadataValueResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            key=key,
            client=client,
        )
    ).parsed
