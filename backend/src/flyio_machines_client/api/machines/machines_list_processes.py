from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.machines_list_processes_order import MachinesListProcessesOrder
from ...models.machines_list_processes_sort_by import MachinesListProcessesSortBy
from ...models.process_stat import ProcessStat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    sort_by: MachinesListProcessesSortBy | Unset = UNSET,
    order: MachinesListProcessesOrder | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/ps".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | list[ProcessStat] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProcessStat.from_dict(response_200_item_data)

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
) -> Response[ErrorResponse | list[ProcessStat]]:
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
    sort_by: MachinesListProcessesSortBy | Unset = UNSET,
    order: MachinesListProcessesOrder | Unset = UNSET,
) -> Response[ErrorResponse | list[ProcessStat]]:
    """List Processes

     List all processes running on a specific Machine within an app, with optional sorting parameters.
    The Machine must be started.

    Args:
        app_name (str):
        machine_id (str):
        sort_by (MachinesListProcessesSortBy | Unset):
        order (MachinesListProcessesOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[ProcessStat]]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        sort_by=sort_by,
        order=order,
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
    sort_by: MachinesListProcessesSortBy | Unset = UNSET,
    order: MachinesListProcessesOrder | Unset = UNSET,
) -> ErrorResponse | list[ProcessStat] | None:
    """List Processes

     List all processes running on a specific Machine within an app, with optional sorting parameters.
    The Machine must be started.

    Args:
        app_name (str):
        machine_id (str):
        sort_by (MachinesListProcessesSortBy | Unset):
        order (MachinesListProcessesOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[ProcessStat]
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        sort_by=sort_by,
        order=order,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: MachinesListProcessesSortBy | Unset = UNSET,
    order: MachinesListProcessesOrder | Unset = UNSET,
) -> Response[ErrorResponse | list[ProcessStat]]:
    """List Processes

     List all processes running on a specific Machine within an app, with optional sorting parameters.
    The Machine must be started.

    Args:
        app_name (str):
        machine_id (str):
        sort_by (MachinesListProcessesSortBy | Unset):
        order (MachinesListProcessesOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[ProcessStat]]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        sort_by=sort_by,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_by: MachinesListProcessesSortBy | Unset = UNSET,
    order: MachinesListProcessesOrder | Unset = UNSET,
) -> ErrorResponse | list[ProcessStat] | None:
    """List Processes

     List all processes running on a specific Machine within an app, with optional sorting parameters.
    The Machine must be started.

    Args:
        app_name (str):
        machine_id (str):
        sort_by (MachinesListProcessesSortBy | Unset):
        order (MachinesListProcessesOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[ProcessStat]
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            sort_by=sort_by,
            order=order,
        )
    ).parsed
