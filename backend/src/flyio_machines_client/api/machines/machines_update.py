from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.machine import Machine
from ...models.update_machine_request import UpdateMachineRequest
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    body: UpdateMachineRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines/{machine_id}".format(
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
) -> ErrorResponse | Machine | None:
    if response.status_code == 200:
        response_200 = Machine.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | Machine]:
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
    body: UpdateMachineRequest,
) -> Response[ErrorResponse | Machine]:
    """Update Machine

     Update a Machine's configuration using the details provided in the request body.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Machine]
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
    body: UpdateMachineRequest,
) -> ErrorResponse | Machine | None:
    """Update Machine

     Update a Machine's configuration using the details provided in the request body.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Machine
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
    body: UpdateMachineRequest,
) -> Response[ErrorResponse | Machine]:
    """Update Machine

     Update a Machine's configuration using the details provided in the request body.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Machine]
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
    body: UpdateMachineRequest,
) -> ErrorResponse | Machine | None:
    """Update Machine

     Update a Machine's configuration using the details provided in the request body.

    Args:
        app_name (str):
        machine_id (str):
        body (UpdateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Machine
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            body=body,
        )
    ).parsed
