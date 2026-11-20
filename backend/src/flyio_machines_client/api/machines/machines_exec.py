from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.exec_response import ExecResponse
from ...models.machine_exec_request import MachineExecRequest
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    body: MachineExecRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/exec".format(
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
) -> ErrorResponse | ExecResponse | None:
    if response.status_code == 200:
        response_200 = ExecResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 412:
        response_412 = ErrorResponse.from_dict(response.json())

        return response_412

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ExecResponse]:
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
    body: MachineExecRequest,
) -> Response[ErrorResponse | ExecResponse]:
    """Execute Command

     Execute a command on a specific Machine and return a JSON response containing
    stdout, stderr, exit_code, and exit_signal.

    A completed command returns HTTP 200, including when the command exits
    unsuccessfully.

    HTTP 412 is returned when the Machine is not running. On Machines without
    containers, it can also indicate an error before or during command execution.
    For example, the executable may be missing or lack execute permission. The
    `error` field describes the failure.

    HTTP 413 responses include a `status` field identifying the size limit that was
    exceeded:

    * `exec_request_too_large`: the Machine rejected the exec request as too large.
      The error message is `exec request rejected: payload too large`. The limit
      applies to the encoded request sent to the Machine, which can differ in size
      from the public API request.
    * `exec_output_too_large`: the command ran, but its output could not be returned
      because it exceeded the maximum allowed response size after JSON encoding.

    Args:
        app_name (str):
        machine_id (str):
        body (MachineExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExecResponse]
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
    body: MachineExecRequest,
) -> ErrorResponse | ExecResponse | None:
    """Execute Command

     Execute a command on a specific Machine and return a JSON response containing
    stdout, stderr, exit_code, and exit_signal.

    A completed command returns HTTP 200, including when the command exits
    unsuccessfully.

    HTTP 412 is returned when the Machine is not running. On Machines without
    containers, it can also indicate an error before or during command execution.
    For example, the executable may be missing or lack execute permission. The
    `error` field describes the failure.

    HTTP 413 responses include a `status` field identifying the size limit that was
    exceeded:

    * `exec_request_too_large`: the Machine rejected the exec request as too large.
      The error message is `exec request rejected: payload too large`. The limit
      applies to the encoded request sent to the Machine, which can differ in size
      from the public API request.
    * `exec_output_too_large`: the command ran, but its output could not be returned
      because it exceeded the maximum allowed response size after JSON encoding.

    Args:
        app_name (str):
        machine_id (str):
        body (MachineExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExecResponse
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
    body: MachineExecRequest,
) -> Response[ErrorResponse | ExecResponse]:
    """Execute Command

     Execute a command on a specific Machine and return a JSON response containing
    stdout, stderr, exit_code, and exit_signal.

    A completed command returns HTTP 200, including when the command exits
    unsuccessfully.

    HTTP 412 is returned when the Machine is not running. On Machines without
    containers, it can also indicate an error before or during command execution.
    For example, the executable may be missing or lack execute permission. The
    `error` field describes the failure.

    HTTP 413 responses include a `status` field identifying the size limit that was
    exceeded:

    * `exec_request_too_large`: the Machine rejected the exec request as too large.
      The error message is `exec request rejected: payload too large`. The limit
      applies to the encoded request sent to the Machine, which can differ in size
      from the public API request.
    * `exec_output_too_large`: the command ran, but its output could not be returned
      because it exceeded the maximum allowed response size after JSON encoding.

    Args:
        app_name (str):
        machine_id (str):
        body (MachineExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExecResponse]
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
    body: MachineExecRequest,
) -> ErrorResponse | ExecResponse | None:
    """Execute Command

     Execute a command on a specific Machine and return a JSON response containing
    stdout, stderr, exit_code, and exit_signal.

    A completed command returns HTTP 200, including when the command exits
    unsuccessfully.

    HTTP 412 is returned when the Machine is not running. On Machines without
    containers, it can also indicate an error before or during command execution.
    For example, the executable may be missing or lack execute permission. The
    `error` field describes the failure.

    HTTP 413 responses include a `status` field identifying the size limit that was
    exceeded:

    * `exec_request_too_large`: the Machine rejected the exec request as too large.
      The error message is `exec request rejected: payload too large`. The limit
      applies to the encoded request sent to the Machine, which can differ in size
      from the public API request.
    * `exec_output_too_large`: the command ran, but its output could not be returned
      because it exceeded the maximum allowed response size after JSON encoding.

    Args:
        app_name (str):
        machine_id (str):
        body (MachineExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExecResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            body=body,
        )
    ).parsed
