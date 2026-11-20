from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lease_error_response import LeaseErrorResponse
from ...models.lease_ok_response import LeaseOkResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    fly_machine_lease_nonce: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["fly-machine-lease-nonce"] = fly_machine_lease_nonce

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/lease".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> LeaseErrorResponse | LeaseOkResponse | None:
    if response.status_code == 200:
        response_200 = LeaseOkResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = LeaseErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LeaseErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[LeaseErrorResponse | LeaseOkResponse]:
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
    fly_machine_lease_nonce: str,
) -> Response[LeaseErrorResponse | LeaseOkResponse]:
    """Release Lease

     Release the lease of a specific Machine within an app. Machine leases can be used to obtain an
    exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        fly_machine_lease_nonce (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LeaseErrorResponse | LeaseOkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        fly_machine_lease_nonce=fly_machine_lease_nonce,
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
    fly_machine_lease_nonce: str,
) -> LeaseErrorResponse | LeaseOkResponse | None:
    """Release Lease

     Release the lease of a specific Machine within an app. Machine leases can be used to obtain an
    exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        fly_machine_lease_nonce (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LeaseErrorResponse | LeaseOkResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        fly_machine_lease_nonce=fly_machine_lease_nonce,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    fly_machine_lease_nonce: str,
) -> Response[LeaseErrorResponse | LeaseOkResponse]:
    """Release Lease

     Release the lease of a specific Machine within an app. Machine leases can be used to obtain an
    exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        fly_machine_lease_nonce (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LeaseErrorResponse | LeaseOkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        fly_machine_lease_nonce=fly_machine_lease_nonce,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    fly_machine_lease_nonce: str,
) -> LeaseErrorResponse | LeaseOkResponse | None:
    """Release Lease

     Release the lease of a specific Machine within an app. Machine leases can be used to obtain an
    exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        fly_machine_lease_nonce (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LeaseErrorResponse | LeaseOkResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            fly_machine_lease_nonce=fly_machine_lease_nonce,
        )
    ).parsed
