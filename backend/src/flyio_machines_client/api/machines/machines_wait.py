from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.machines_wait_state import MachinesWaitState
from ...models.wait_machine_response import WaitMachineResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    version: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    from_event_id: str | Unset = UNSET,
    timeout: int | Unset = UNSET,
    state: MachinesWaitState | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params["instance_id"] = instance_id

    params["from_event_id"] = from_event_id

    params["timeout"] = timeout

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/wait".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | WaitMachineResponse | None:
    if response.status_code == 200:
        response_200 = WaitMachineResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | WaitMachineResponse]:
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
    version: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    from_event_id: str | Unset = UNSET,
    timeout: int | Unset = UNSET,
    state: MachinesWaitState | Unset = UNSET,
) -> Response[ErrorResponse | WaitMachineResponse]:
    """Wait for State

     Wait for a Machine to reach a specific state. Specify the desired state with the state parameter.
    See the [Machine states table](https://fly.io/docs/machines/working-with-machines/#machine-states)
    for a list of possible states. The default for this parameter is `started`.

    This request will block for up to 60 seconds. Set a shorter timeout with the timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        instance_id (str | Unset):
        from_event_id (str | Unset):
        timeout (int | Unset):
        state (MachinesWaitState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WaitMachineResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        version=version,
        instance_id=instance_id,
        from_event_id=from_event_id,
        timeout=timeout,
        state=state,
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
    version: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    from_event_id: str | Unset = UNSET,
    timeout: int | Unset = UNSET,
    state: MachinesWaitState | Unset = UNSET,
) -> ErrorResponse | WaitMachineResponse | None:
    """Wait for State

     Wait for a Machine to reach a specific state. Specify the desired state with the state parameter.
    See the [Machine states table](https://fly.io/docs/machines/working-with-machines/#machine-states)
    for a list of possible states. The default for this parameter is `started`.

    This request will block for up to 60 seconds. Set a shorter timeout with the timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        instance_id (str | Unset):
        from_event_id (str | Unset):
        timeout (int | Unset):
        state (MachinesWaitState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WaitMachineResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        version=version,
        instance_id=instance_id,
        from_event_id=from_event_id,
        timeout=timeout,
        state=state,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    from_event_id: str | Unset = UNSET,
    timeout: int | Unset = UNSET,
    state: MachinesWaitState | Unset = UNSET,
) -> Response[ErrorResponse | WaitMachineResponse]:
    """Wait for State

     Wait for a Machine to reach a specific state. Specify the desired state with the state parameter.
    See the [Machine states table](https://fly.io/docs/machines/working-with-machines/#machine-states)
    for a list of possible states. The default for this parameter is `started`.

    This request will block for up to 60 seconds. Set a shorter timeout with the timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        instance_id (str | Unset):
        from_event_id (str | Unset):
        timeout (int | Unset):
        state (MachinesWaitState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WaitMachineResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        version=version,
        instance_id=instance_id,
        from_event_id=from_event_id,
        timeout=timeout,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    instance_id: str | Unset = UNSET,
    from_event_id: str | Unset = UNSET,
    timeout: int | Unset = UNSET,
    state: MachinesWaitState | Unset = UNSET,
) -> ErrorResponse | WaitMachineResponse | None:
    """Wait for State

     Wait for a Machine to reach a specific state. Specify the desired state with the state parameter.
    See the [Machine states table](https://fly.io/docs/machines/working-with-machines/#machine-states)
    for a list of possible states. The default for this parameter is `started`.

    This request will block for up to 60 seconds. Set a shorter timeout with the timeout parameter.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        instance_id (str | Unset):
        from_event_id (str | Unset):
        timeout (int | Unset):
        state (MachinesWaitState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WaitMachineResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            version=version,
            instance_id=instance_id,
            from_event_id=from_event_id,
            timeout=timeout,
            state=state,
        )
    ).parsed
