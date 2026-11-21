from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_ip_request import AssignIPRequest
from ...models.assign_ip_response import AssignIPResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    *,
    body: AssignIPRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/ip_assignments".format(
            app_name=quote(str(app_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AssignIPResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AssignIPResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AssignIPResponse | ErrorResponse]:
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
    body: AssignIPRequest,
) -> Response[AssignIPResponse | ErrorResponse]:
    """Assign new IP address to app

    Args:
        app_name (str):
        body (AssignIPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignIPResponse | ErrorResponse]
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
    body: AssignIPRequest,
) -> AssignIPResponse | ErrorResponse | None:
    """Assign new IP address to app

    Args:
        app_name (str):
        body (AssignIPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignIPResponse | ErrorResponse
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
    body: AssignIPRequest,
) -> Response[AssignIPResponse | ErrorResponse]:
    """Assign new IP address to app

    Args:
        app_name (str):
        body (AssignIPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignIPResponse | ErrorResponse]
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
    body: AssignIPRequest,
) -> AssignIPResponse | ErrorResponse | None:
    """Assign new IP address to app

    Args:
        app_name (str):
        body (AssignIPRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignIPResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            client=client,
            body=body,
        )
    ).parsed
