from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extend_volume_request import ExtendVolumeRequest
from ...models.extend_volume_response import ExtendVolumeResponse
from ...types import Response


def _get_kwargs(
    app_name: str,
    volume_id: str,
    *,
    body: ExtendVolumeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/apps/{app_name}/volumes/{volume_id}/extend".format(
            app_name=quote(str(app_name), safe=""),
            volume_id=quote(str(volume_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ExtendVolumeResponse | None:
    if response.status_code == 200:
        response_200 = ExtendVolumeResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ExtendVolumeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtendVolumeRequest,
) -> Response[ExtendVolumeResponse]:
    """Extend Volume

     Extend a volume's size within an app using the details provided in the request body.

    Args:
        app_name (str):
        volume_id (str):
        body (ExtendVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtendVolumeResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        volume_id=volume_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtendVolumeRequest,
) -> ExtendVolumeResponse | None:
    """Extend Volume

     Extend a volume's size within an app using the details provided in the request body.

    Args:
        app_name (str):
        volume_id (str):
        body (ExtendVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtendVolumeResponse
    """

    return sync_detailed(
        app_name=app_name,
        volume_id=volume_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtendVolumeRequest,
) -> Response[ExtendVolumeResponse]:
    """Extend Volume

     Extend a volume's size within an app using the details provided in the request body.

    Args:
        app_name (str):
        volume_id (str):
        body (ExtendVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtendVolumeResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        volume_id=volume_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    volume_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtendVolumeRequest,
) -> ExtendVolumeResponse | None:
    """Extend Volume

     Extend a volume's size within an app using the details provided in the request body.

    Args:
        app_name (str):
        volume_id (str):
        body (ExtendVolumeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtendVolumeResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            volume_id=volume_id,
            client=client,
            body=body,
        )
    ).parsed
