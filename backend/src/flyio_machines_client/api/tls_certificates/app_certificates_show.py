from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate_detail import CertificateDetail
from ...types import Response


def _get_kwargs(
    app_name: str,
    hostname: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_name}/certificates/{hostname}".format(
            app_name=quote(str(app_name), safe=""),
            hostname=quote(str(hostname), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CertificateDetail | None:
    if response.status_code == 200:
        response_200 = CertificateDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CertificateDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_name: str,
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CertificateDetail]:
    """Get certificate details

    Args:
        app_name (str):
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertificateDetail]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        hostname=hostname,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_name: str,
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> CertificateDetail | None:
    """Get certificate details

    Args:
        app_name (str):
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertificateDetail
    """

    return sync_detailed(
        app_name=app_name,
        hostname=hostname,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_name: str,
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CertificateDetail]:
    """Get certificate details

    Args:
        app_name (str):
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertificateDetail]
    """

    kwargs = _get_kwargs(
        app_name=app_name,
        hostname=hostname,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_name: str,
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> CertificateDetail | None:
    """Get certificate details

    Args:
        app_name (str):
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertificateDetail
    """

    return (
        await asyncio_detailed(
            app_name=app_name,
            hostname=hostname,
            client=client,
        )
    ).parsed
