from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_certificates_response import ListCertificatesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_name: str,
    *,
    filter_: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/certificates".format(
            app_name=quote(str(app_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListCertificatesResponse | None:
    if response.status_code == 200:
        response_200 = ListCertificatesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListCertificatesResponse]:
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
    filter_: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListCertificatesResponse]:
    """List certificates for app

    Args:
        app_name (str):
        filter_ (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCertificatesResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        filter_=filter_,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListCertificatesResponse | None:
    """List certificates for app

    Args:
        app_name (str):
        filter_ (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCertificatesResponse
    """

    return sync_detailed(
        app_name=app_name,
        client=client,
        filter_=filter_,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ListCertificatesResponse]:
    """List certificates for app

    Args:
        app_name (str):
        filter_ (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCertificatesResponse]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        filter_=filter_,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ListCertificatesResponse | None:
    """List certificates for app

    Args:
        app_name (str):
        filter_ (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCertificatesResponse
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            client=client,
            filter_=filter_,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
