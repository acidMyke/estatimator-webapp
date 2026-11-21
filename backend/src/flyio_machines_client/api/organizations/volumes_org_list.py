from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.org_volumes_response import OrgVolumesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_slug: str,
    *,
    include_deleted: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_deleted"] = include_deleted

    params["region"] = region

    params["state"] = state

    params["summary"] = summary

    params["updated_after"] = updated_after

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/orgs/{org_slug}/volumes".format(
            org_slug=quote(str(org_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> OrgVolumesResponse | None:
    if response.status_code == 200:
        response_200 = OrgVolumesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[OrgVolumesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_slug: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[OrgVolumesResponse]:
    """List All Volumes

     List all volumes for an organization with optional filters and cursor-based pagination.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        updated_after (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgVolumesResponse]
    """

    kwargs = _get_kwargs(
        org_slug=org_slug,
        include_deleted=include_deleted,
        region=region,
        state=state,
        summary=summary,
        updated_after=updated_after,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_slug: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> OrgVolumesResponse | None:
    """List All Volumes

     List all volumes for an organization with optional filters and cursor-based pagination.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        updated_after (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgVolumesResponse
    """

    return sync_detailed(
        org_slug=org_slug,
        client=client,
        include_deleted=include_deleted,
        region=region,
        state=state,
        summary=summary,
        updated_after=updated_after,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    org_slug: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[OrgVolumesResponse]:
    """List All Volumes

     List all volumes for an organization with optional filters and cursor-based pagination.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        updated_after (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgVolumesResponse]
    """

    kwargs = _get_kwargs(
        org_slug=org_slug,
        include_deleted=include_deleted,
        region=region,
        state=state,
        summary=summary,
        updated_after=updated_after,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_slug: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = UNSET,
    region: str | Unset = UNSET,
    state: str | Unset = UNSET,
    summary: bool | Unset = UNSET,
    updated_after: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> OrgVolumesResponse | None:
    """List All Volumes

     List all volumes for an organization with optional filters and cursor-based pagination.

    Args:
        org_slug (str):
        include_deleted (bool | Unset):
        region (str | Unset):
        state (str | Unset):
        summary (bool | Unset):
        updated_after (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgVolumesResponse
    """

    return (
        await asyncio_detailed(
            org_slug=org_slug,
            client=client,
            include_deleted=include_deleted,
            region=region,
            state=state,
            summary=summary,
            updated_after=updated_after,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
