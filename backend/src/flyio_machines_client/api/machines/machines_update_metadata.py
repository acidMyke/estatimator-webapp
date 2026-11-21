from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_metadata_request import UpdateMetadataRequest
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    body: UpdateMetadataRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/metadata".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMetadataRequest,
) -> Response[Any | ErrorResponse]:
    """Update Metadata (set/remove multiple keys)

     Update multiple metadata keys at once. Keys that are not in the request are left untouched. Null
    values and empty strings remove keys.
    + If `machine_version` is provided and no longer matches the current machine version, returns 412
    Precondition Failed.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMetadataRequest,
) -> Any | ErrorResponse | None:
    """Update Metadata (set/remove multiple keys)

     Update multiple metadata keys at once. Keys that are not in the request are left untouched. Null
    values and empty strings remove keys.
    + If `machine_version` is provided and no longer matches the current machine version, returns 412
    Precondition Failed.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMetadataRequest,
) -> Response[Any | ErrorResponse]:
    """Update Metadata (set/remove multiple keys)

     Update multiple metadata keys at once. Keys that are not in the request are left untouched. Null
    values and empty strings remove keys.
    + If `machine_version` is provided and no longer matches the current machine version, returns 412
    Precondition Failed.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateMetadataRequest,
) -> Any | ErrorResponse | None:
    """Update Metadata (set/remove multiple keys)

     Update multiple metadata keys at once. Keys that are not in the request are left untouched. Null
    values and empty strings remove keys.
    + If `machine_version` is provided and no longer matches the current machine version, returns 412
    Precondition Failed.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            body=body,
        )
    ).parsed
