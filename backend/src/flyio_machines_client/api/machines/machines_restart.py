from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.machines_restart_signal import MachinesRestartSignal
from ...models.ok_response import OkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    timeout: str | Unset = UNSET,
    signal: MachinesRestartSignal | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["timeout"] = timeout

    json_signal: str | Unset = UNSET
    if not isinstance(signal, Unset):
        json_signal = signal.value

    params["signal"] = json_signal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/restart".format(
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

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
    timeout: str | Unset = UNSET,
    signal: MachinesRestartSignal | Unset = UNSET,
) -> Response[ErrorResponse | OkResponse]:
    """Restart Machine

     Restart a specific Machine within an app, with an optional timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        timeout (str | Unset):
        signal (MachinesRestartSignal | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        timeout=timeout,
        signal=signal,
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
    timeout: str | Unset = UNSET,
    signal: MachinesRestartSignal | Unset = UNSET,
) -> ErrorResponse | OkResponse | None:
    """Restart Machine

     Restart a specific Machine within an app, with an optional timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        timeout (str | Unset):
        signal (MachinesRestartSignal | Unset):

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
        timeout=timeout,
        signal=signal,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    timeout: str | Unset = UNSET,
    signal: MachinesRestartSignal | Unset = UNSET,
) -> Response[ErrorResponse | OkResponse]:
    """Restart Machine

     Restart a specific Machine within an app, with an optional timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        timeout (str | Unset):
        signal (MachinesRestartSignal | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        timeout=timeout,
        signal=signal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    timeout: str | Unset = UNSET,
    signal: MachinesRestartSignal | Unset = UNSET,
) -> ErrorResponse | OkResponse | None:
    """Restart Machine

     Restart a specific Machine within an app, with an optional timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        timeout (str | Unset):
        signal (MachinesRestartSignal | Unset):

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
            timeout=timeout,
            signal=signal,
        )
    ).parsed
