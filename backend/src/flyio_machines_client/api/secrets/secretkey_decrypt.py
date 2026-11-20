from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decrypt_secretkey_request import DecryptSecretkeyRequest
from ...models.decrypt_secretkey_response import DecryptSecretkeyResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    secret_name: str,
    *,
    body: DecryptSecretkeyRequest,
    min_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["min_version"] = min_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_name}/secretkeys/{secret_name}/decrypt".format(
            app_name=quote(str(app_name), safe=""),
            secret_name=quote(str(secret_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DecryptSecretkeyResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DecryptSecretkeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DecryptSecretkeyResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DecryptSecretkeyRequest,
    min_version: str | Unset = UNSET,
) -> Response[DecryptSecretkeyResponse | ErrorResponse]:
    """Decrypt with a secret key

     The request must come from a Machine of the app; otherwise it fails with 403.

    Args:
        app_name (str):
        secret_name (str):
        min_version (str | Unset):
        body (DecryptSecretkeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptSecretkeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        secret_name=secret_name,
        body=body,
        min_version=min_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DecryptSecretkeyRequest,
    min_version: str | Unset = UNSET,
) -> DecryptSecretkeyResponse | ErrorResponse | None:
    """Decrypt with a secret key

     The request must come from a Machine of the app; otherwise it fails with 403.

    Args:
        app_name (str):
        secret_name (str):
        min_version (str | Unset):
        body (DecryptSecretkeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptSecretkeyResponse | ErrorResponse
    """

    return sync_detailed(
        app_name=app_name,
        secret_name=secret_name,
        client=client,
        body=body,
        min_version=min_version,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DecryptSecretkeyRequest,
    min_version: str | Unset = UNSET,
) -> Response[DecryptSecretkeyResponse | ErrorResponse]:
    """Decrypt with a secret key

     The request must come from a Machine of the app; otherwise it fails with 403.

    Args:
        app_name (str):
        secret_name (str):
        min_version (str | Unset):
        body (DecryptSecretkeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DecryptSecretkeyResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        secret_name=secret_name,
        body=body,
        min_version=min_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: DecryptSecretkeyRequest,
    min_version: str | Unset = UNSET,
) -> DecryptSecretkeyResponse | ErrorResponse | None:
    """Decrypt with a secret key

     The request must come from a Machine of the app; otherwise it fails with 403.

    Args:
        app_name (str):
        secret_name (str):
        min_version (str | Unset):
        body (DecryptSecretkeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DecryptSecretkeyResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            secret_name=secret_name,
            client=client,
            body=body,
            min_version=min_version,
        )
    ).parsed
