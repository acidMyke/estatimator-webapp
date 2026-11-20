from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.ok_response import OkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    force: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_name}/machines/{machine_id}".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | OkResponse | None:
    if response.status_code == 200:
        response_200 = OkResponse.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | OkResponse]:
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
    force: bool | Unset = UNSET,
) -> Response[ErrorResponse | OkResponse]:
    """Destroy Machine

     Delete a specific Machine within an app by Machine ID.

    Only a Machine in the `stopped`, `suspended`, `failed`, `pending` or `archived` state can be
    deleted. Deleting a Machine in any other state, such as `started`, fails with `412 Precondition
    Failed` unless you set `force=true`, which kills the Machine first. Deleting a Machine that is
    already `destroying` or `destroyed` succeeds without doing anything.

    If someone else holds a lease on the Machine, the request fails with `409 Conflict`. Pass the lease
    nonce in the `fly-machine-lease-nonce` header to delete a Machine you hold the lease on.

    Args:
        app_name (str):
        machine_id (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        force=force,
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
    force: bool | Unset = UNSET,
) -> ErrorResponse | OkResponse | None:
    """Destroy Machine

     Delete a specific Machine within an app by Machine ID.

    Only a Machine in the `stopped`, `suspended`, `failed`, `pending` or `archived` state can be
    deleted. Deleting a Machine in any other state, such as `started`, fails with `412 Precondition
    Failed` unless you set `force=true`, which kills the Machine first. Deleting a Machine that is
    already `destroying` or `destroyed` succeeds without doing anything.

    If someone else holds a lease on the Machine, the request fails with `409 Conflict`. Pass the lease
    nonce in the `fly-machine-lease-nonce` header to delete a Machine you hold the lease on.

    Args:
        app_name (str):
        machine_id (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OkResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        force=force,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> Response[ErrorResponse | OkResponse]:
    """Destroy Machine

     Delete a specific Machine within an app by Machine ID.

    Only a Machine in the `stopped`, `suspended`, `failed`, `pending` or `archived` state can be
    deleted. Deleting a Machine in any other state, such as `started`, fails with `412 Precondition
    Failed` unless you set `force=true`, which kills the Machine first. Deleting a Machine that is
    already `destroying` or `destroyed` succeeds without doing anything.

    If someone else holds a lease on the Machine, the request fails with `409 Conflict`. Pass the lease
    nonce in the `fly-machine-lease-nonce` header to delete a Machine you hold the lease on.

    Args:
        app_name (str):
        machine_id (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    force: bool | Unset = UNSET,
) -> ErrorResponse | OkResponse | None:
    """Destroy Machine

     Delete a specific Machine within an app by Machine ID.

    Only a Machine in the `stopped`, `suspended`, `failed`, `pending` or `archived` state can be
    deleted. Deleting a Machine in any other state, such as `started`, fails with `412 Precondition
    Failed` unless you set `force=true`, which kills the Machine first. Deleting a Machine that is
    already `destroying` or `destroyed` succeeds without doing anything.

    If someone else holds a lease on the Machine, the request fails with `409 Conflict`. Pass the lease
    nonce in the `fly-machine-lease-nonce` header to delete a Machine you hold the lease on.

    Args:
        app_name (str):
        machine_id (str):
        force (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OkResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            force=force,
        )
    ).parsed
