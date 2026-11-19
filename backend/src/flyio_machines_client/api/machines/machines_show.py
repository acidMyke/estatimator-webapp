from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.machine import Machine
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    version: str | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["version"] = version

    params["include_leases"] = include_leases

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/machines/{machine_id}".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Machine | None:
    if response.status_code == 200:
        response_200 = Machine.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Machine]:
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
    include_leases: bool | Unset = UNSET,
) -> Response[Machine]:
    """Get Machine

     Get details of a specific Machine within an app by the Machine ID.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        include_leases (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Machine]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        version=version,
        include_leases=include_leases,
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
    include_leases: bool | Unset = UNSET,
) -> Machine | None:
    """Get Machine

     Get details of a specific Machine within an app by the Machine ID.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        include_leases (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Machine
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        version=version,
        include_leases=include_leases,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
) -> Response[Machine]:
    """Get Machine

     Get details of a specific Machine within an app by the Machine ID.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        include_leases (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Machine]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        version=version,
        include_leases=include_leases,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: str | Unset = UNSET,
    include_leases: bool | Unset = UNSET,
) -> Machine | None:
    """Get Machine

     Get details of a specific Machine within an app by the Machine ID.

    Args:
        app_name (str):
        machine_id (str):
        version (str | Unset):
        include_leases (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Machine
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            version=version,
            include_leases=include_leases,
        )
    ).parsed
