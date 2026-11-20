from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ok_response import OkResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    machine_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/machines/{machine_id}/suspend".format(
            app_name=quote(str(app_name), safe=""),
            machine_id=quote(str(machine_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> OkResponse | None:
    if response.status_code == 200:
        response_200 = OkResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[OkResponse]:
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
) -> Response[OkResponse]:
    """Suspend Machine

     Suspend a specific Machine within an app. The next start operation will attempt (but is not
    guaranteed) to resume the Machine from a snapshot taken at suspension time, rather than performing a
    cold boot.

    Args:
        app_name (str):
        machine_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
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
) -> OkResponse | None:
    """Suspend Machine

     Suspend a specific Machine within an app. The next start operation will attempt (but is not
    guaranteed) to resume the Machine from a snapshot taken at suspension time, rather than performing a
    cold boot.

    Args:
        app_name (str):
        machine_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OkResponse
    """

    return sync_detailed(
        app_name=app_name,
        machine_id=machine_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OkResponse]:
    """Suspend Machine

     Suspend a specific Machine within an app. The next start operation will attempt (but is not
    guaranteed) to resume the Machine from a snapshot taken at suspension time, rather than performing a
    cold boot.

    Args:
        app_name (str):
        machine_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OkResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        machine_id=machine_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    machine_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OkResponse | None:
    """Suspend Machine

     Suspend a specific Machine within an app. The next start operation will attempt (but is not
    guaranteed) to resume the Machine from a snapshot taken at suspension time, rather than performing a
    cold boot.

    Args:
        app_name (str):
        machine_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OkResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            machine_id=machine_id,
            client=client,
        )
    ).parsed
