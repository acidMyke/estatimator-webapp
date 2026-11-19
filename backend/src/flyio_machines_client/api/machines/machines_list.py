from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.machine import Machine
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    *,
    include_deleted: bool | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    metadata_key: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_deleted"] = include_deleted

    params["include_leases"] = include_leases

    params["region"] = region

    params["state"] = state

    params["summary"] = summary

    params["metadata.{key}"] = metadata_key

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/machines".format(
            app_name=quote(str(app_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | list[Machine] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Machine.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | list[Machine]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    metadata_key: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorResponse | list[Machine]]:
    """List Machines

     List all Machines associated with a specific app, with optional filters for including deleted
    Machines and filtering by region.

    Args:
        app_name (str):
        include_deleted (bool | Unset):
        include_leases (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        metadata_key (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[Machine]]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        include_deleted=include_deleted,
        include_leases=include_leases,
        region=region,
        state=state,
        summary=summary,
        metadata_key=metadata_key,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    metadata_key: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorResponse | list[Machine] | None:
    """List Machines

     List all Machines associated with a specific app, with optional filters for including deleted
    Machines and filtering by region.

    Args:
        app_name (str):
        include_deleted (bool | Unset):
        include_leases (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        metadata_key (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[Machine]
    """

    return sync_detailed(
        app_name=app_name,
        client=client,
        include_deleted=include_deleted,
        include_leases=include_leases,
        region=region,
        state=state,
        summary=summary,
        metadata_key=metadata_key,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    metadata_key: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorResponse | list[Machine]]:
    """List Machines

     List all Machines associated with a specific app, with optional filters for including deleted
    Machines and filtering by region.

    Args:
        app_name (str):
        include_deleted (bool | Unset):
        include_leases (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        metadata_key (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[Machine]]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        include_deleted=include_deleted,
        include_leases=include_leases,
        region=region,
        state=state,
        summary=summary,
        metadata_key=metadata_key,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    metadata_key: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorResponse | list[Machine] | None:
    """List Machines

     List all Machines associated with a specific app, with optional filters for including deleted
    Machines and filtering by region.

    Args:
        app_name (str):
        include_deleted (bool | Unset):
        include_leases (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        metadata_key (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[Machine]
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            client=client,
            include_deleted=include_deleted,
            include_leases=include_leases,
            region=region,
            state=state,
            summary=summary,
            metadata_key=metadata_key,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
