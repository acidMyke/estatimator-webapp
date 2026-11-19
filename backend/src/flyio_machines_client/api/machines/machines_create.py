from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_machine_request import CreateMachineRequest
from ...models.machine import Machine
from ...types import Response


def _get_kwargs(
    app_name: str,
    *,
    body: CreateMachineRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines".format(
            app_name=quote(str(app_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateMachineRequest,
) -> Response[Machine]:
    """Create Machine

     Create a Machine within a specific app using the details provided in the request body.

    **Important**: This request can fail, and you’re responsible for handling that failure. If you ask
    for a large Machine, or a Machine in a region we happen to be at capacity for, you might need to
    retry the request, or to fall back to another region. If you’re working directly with the Machines
    API, you’re taking some responsibility for your own orchestration!

    Args:
        app_name (str):
        body (CreateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Machine]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateMachineRequest,
) -> Machine | None:
    """Create Machine

     Create a Machine within a specific app using the details provided in the request body.

    **Important**: This request can fail, and you’re responsible for handling that failure. If you ask
    for a large Machine, or a Machine in a region we happen to be at capacity for, you might need to
    retry the request, or to fall back to another region. If you’re working directly with the Machines
    API, you’re taking some responsibility for your own orchestration!

    Args:
        app_name (str):
        body (CreateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Machine
    """

    return sync_detailed(
        app_name=app_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateMachineRequest,
) -> Response[Machine]:
    """Create Machine

     Create a Machine within a specific app using the details provided in the request body.

    **Important**: This request can fail, and you’re responsible for handling that failure. If you ask
    for a large Machine, or a Machine in a region we happen to be at capacity for, you might need to
    retry the request, or to fall back to another region. If you’re working directly with the Machines
    API, you’re taking some responsibility for your own orchestration!

    Args:
        app_name (str):
        body (CreateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Machine]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateMachineRequest,
) -> Machine | None:
    """Create Machine

     Create a Machine within a specific app using the details provided in the request body.

    **Important**: This request can fail, and you’re responsible for handling that failure. If you ask
    for a large Machine, or a Machine in a region we happen to be at capacity for, you might need to
    retry the request, or to fall back to another region. If you’re working directly with the Machines
    API, you’re taking some responsibility for your own orchestration!

    Args:
        app_name (str):
        body (CreateMachineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Machine
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            client=client,
            body=body,
        )
    ).parsed
