from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_lease_request import CreateLeaseRequest
from ...models.lease_error_response import LeaseErrorResponse
from ...models.lease_response import LeaseResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    machine_id: str,
    *,
    body: CreateLeaseRequest,
    ttl: int | Unset = UNSET,
    fly_machine_lease_nonce: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(fly_machine_lease_nonce, Unset):
        headers["fly-machine-lease-nonce"] = fly_machine_lease_nonce

    params: dict[str, Any] = {}

    params["ttl"] = ttl

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/lease".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> LeaseErrorResponse | LeaseResponse | None:
    if response.status_code == 201:
        response_201 = LeaseResponse.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        response_403 = LeaseErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = LeaseErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[LeaseErrorResponse | LeaseResponse]:
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
    body: CreateLeaseRequest,
    ttl: int | Unset = UNSET,
    fly_machine_lease_nonce: str | Unset = UNSET,
) -> Response[LeaseErrorResponse | LeaseResponse]:
    """Create Lease

     Create a lease for a specific Machine within an app using the details provided in the request body.
    Machine leases can be used to obtain an exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        ttl (int | Unset):
        fly_machine_lease_nonce (str | Unset):
        body (CreateLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LeaseErrorResponse | LeaseResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        body=body,
        ttl=ttl,
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
    body: CreateLeaseRequest,
    ttl: int | Unset = UNSET,
    fly_machine_lease_nonce: str | Unset = UNSET,
) -> LeaseErrorResponse | LeaseResponse | None:
    """Create Lease

     Create a lease for a specific Machine within an app using the details provided in the request body.
    Machine leases can be used to obtain an exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        ttl (int | Unset):
        fly_machine_lease_nonce (str | Unset):
        body (CreateLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LeaseErrorResponse | LeaseResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
        body=body,
        ttl=ttl,
        fly_machine_lease_nonce=fly_machine_lease_nonce,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateLeaseRequest,
    ttl: int | Unset = UNSET,
    fly_machine_lease_nonce: str | Unset = UNSET,
) -> Response[LeaseErrorResponse | LeaseResponse]:
    """Create Lease

     Create a lease for a specific Machine within an app using the details provided in the request body.
    Machine leases can be used to obtain an exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        ttl (int | Unset):
        fly_machine_lease_nonce (str | Unset):
        body (CreateLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LeaseErrorResponse | LeaseResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
        body=body,
        ttl=ttl,
        fly_machine_lease_nonce=fly_machine_lease_nonce,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateLeaseRequest,
    ttl: int | Unset = UNSET,
    fly_machine_lease_nonce: str | Unset = UNSET,
) -> LeaseErrorResponse | LeaseResponse | None:
    """Create Lease

     Create a lease for a specific Machine within an app using the details provided in the request body.
    Machine leases can be used to obtain an exclusive lock on modifying a Machine.

    Args:
        app_name (str):
        machine_id (str):
        ttl (int | Unset):
        fly_machine_lease_nonce (str | Unset):
        body (CreateLeaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LeaseErrorResponse | LeaseResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
            body=body,
            ttl=ttl,
            fly_machine_lease_nonce=fly_machine_lease_nonce,
        )
    ).parsed
