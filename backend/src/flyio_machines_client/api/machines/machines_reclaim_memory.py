from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.main_reclaim_memory_request import MainReclaimMemoryRequest
from ...models.main_reclaim_memory_response import MainReclaimMemoryResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    body: MainReclaimMemoryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/memory/reclaim".format(
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
) -> ErrorResponse | MainReclaimMemoryResponse | None:
    if response.status_code == 200:
        response_200 = MainReclaimMemoryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

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
) -> Response[ErrorResponse | MainReclaimMemoryResponse]:
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
    body: MainReclaimMemoryRequest,
) -> Response[ErrorResponse | MainReclaimMemoryResponse]:
    """Reclaim Machine Memory

     Return unused memory of a started Firecracker Machine to the host. The memory balloon is inflated by
    `amount_mb` for a few seconds and then deflated again, so the Machine's memory limit does not
    change.
    + Fails with 409 while the Machine has a lease, even when the lease nonce is passed.

    Args:
        app_name (str):
        machine_id (str):
        body (MainReclaimMemoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MainReclaimMemoryResponse]
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
    body: MainReclaimMemoryRequest,
) -> ErrorResponse | MainReclaimMemoryResponse | None:
    """Reclaim Machine Memory

     Return unused memory of a started Firecracker Machine to the host. The memory balloon is inflated by
    `amount_mb` for a few seconds and then deflated again, so the Machine's memory limit does not
    change.
    + Fails with 409 while the Machine has a lease, even when the lease nonce is passed.

    Args:
        app_name (str):
        machine_id (str):
        body (MainReclaimMemoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MainReclaimMemoryResponse
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
    body: MainReclaimMemoryRequest,
) -> Response[ErrorResponse | MainReclaimMemoryResponse]:
    """Reclaim Machine Memory

     Return unused memory of a started Firecracker Machine to the host. The memory balloon is inflated by
    `amount_mb` for a few seconds and then deflated again, so the Machine's memory limit does not
    change.
    + Fails with 409 while the Machine has a lease, even when the lease nonce is passed.

    Args:
        app_name (str):
        machine_id (str):
        body (MainReclaimMemoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MainReclaimMemoryResponse]
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
    body: MainReclaimMemoryRequest,
) -> ErrorResponse | MainReclaimMemoryResponse | None:
    """Reclaim Machine Memory

     Return unused memory of a started Firecracker Machine to the host. The memory balloon is inflated by
    `amount_mb` for a few seconds and then deflated again, so the Machine's memory limit does not
    change.
    + Fails with 409 while the Machine has a lease, even when the lease nonce is passed.

    Args:
        app_name (str):
        machine_id (str):
        body (MainReclaimMemoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MainReclaimMemoryResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            body=body,
        )
    ).parsed
