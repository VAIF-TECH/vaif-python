# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .revoke import (
    RevokeResource,
    AsyncRevokeResource,
    RevokeResourceWithRawResponse,
    AsyncRevokeResourceWithRawResponse,
    RevokeResourceWithStreamingResponse,
    AsyncRevokeResourceWithStreamingResponse,
)
from .rotate import (
    RotateResource,
    AsyncRotateResource,
    RotateResourceWithRawResponse,
    AsyncRotateResourceWithRawResponse,
    RotateResourceWithStreamingResponse,
    AsyncRotateResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.projects import api_key_update_params, api_key_api_keys_params
from ....types.projects.api_key_update_response import APIKeyUpdateResponse
from ....types.projects.api_key_api_keys_response import APIKeyAPIKeysResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def revoke(self) -> RevokeResource:
        return RevokeResource(self._client)

    @cached_property
    def rotate(self) -> RotateResource:
        return RotateResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def update(
        self,
        key_id: str,
        *,
        project_id: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        name: str | Omit = omit,
        scopes: List[Literal["crud", "realtime", "functions", "storage", "mongodb"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._patch(
            path_template("/projects/{project_id}/api-keys/{key_id}", project_id=project_id, key_id=key_id),
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "name": name,
                    "scopes": scopes,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyUpdateResponse,
        )

    def api_keys(
        self,
        project_id: str,
        *,
        env_id: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        scopes: List[Literal["crud", "realtime", "functions", "storage"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyAPIKeysResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/api-keys", project_id=project_id),
            body=maybe_transform(
                {
                    "env_id": env_id,
                    "expires_at": expires_at,
                    "name": name,
                    "scopes": scopes,
                },
                api_key_api_keys_params.APIKeyAPIKeysParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyAPIKeysResponse,
        )

    def get_api_keys(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/api-keys", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def revoke(self) -> AsyncRevokeResource:
        return AsyncRevokeResource(self._client)

    @cached_property
    def rotate(self) -> AsyncRotateResource:
        return AsyncRotateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def update(
        self,
        key_id: str,
        *,
        project_id: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        name: str | Omit = omit,
        scopes: List[Literal["crud", "realtime", "functions", "storage", "mongodb"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._patch(
            path_template("/projects/{project_id}/api-keys/{key_id}", project_id=project_id, key_id=key_id),
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "name": name,
                    "scopes": scopes,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyUpdateResponse,
        )

    async def api_keys(
        self,
        project_id: str,
        *,
        env_id: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        scopes: List[Literal["crud", "realtime", "functions", "storage"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyAPIKeysResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/api-keys", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "env_id": env_id,
                    "expires_at": expires_at,
                    "name": name,
                    "scopes": scopes,
                },
                api_key_api_keys_params.APIKeyAPIKeysParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyAPIKeysResponse,
        )

    async def get_api_keys(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/api-keys", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.update = to_raw_response_wrapper(
            api_keys.update,
        )
        self.api_keys = to_raw_response_wrapper(
            api_keys.api_keys,
        )
        self.get_api_keys = to_raw_response_wrapper(
            api_keys.get_api_keys,
        )

    @cached_property
    def revoke(self) -> RevokeResourceWithRawResponse:
        return RevokeResourceWithRawResponse(self._api_keys.revoke)

    @cached_property
    def rotate(self) -> RotateResourceWithRawResponse:
        return RotateResourceWithRawResponse(self._api_keys.rotate)


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.update = async_to_raw_response_wrapper(
            api_keys.update,
        )
        self.api_keys = async_to_raw_response_wrapper(
            api_keys.api_keys,
        )
        self.get_api_keys = async_to_raw_response_wrapper(
            api_keys.get_api_keys,
        )

    @cached_property
    def revoke(self) -> AsyncRevokeResourceWithRawResponse:
        return AsyncRevokeResourceWithRawResponse(self._api_keys.revoke)

    @cached_property
    def rotate(self) -> AsyncRotateResourceWithRawResponse:
        return AsyncRotateResourceWithRawResponse(self._api_keys.rotate)


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.update = to_streamed_response_wrapper(
            api_keys.update,
        )
        self.api_keys = to_streamed_response_wrapper(
            api_keys.api_keys,
        )
        self.get_api_keys = to_streamed_response_wrapper(
            api_keys.get_api_keys,
        )

    @cached_property
    def revoke(self) -> RevokeResourceWithStreamingResponse:
        return RevokeResourceWithStreamingResponse(self._api_keys.revoke)

    @cached_property
    def rotate(self) -> RotateResourceWithStreamingResponse:
        return RotateResourceWithStreamingResponse(self._api_keys.rotate)


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.update = async_to_streamed_response_wrapper(
            api_keys.update,
        )
        self.api_keys = async_to_streamed_response_wrapper(
            api_keys.api_keys,
        )
        self.get_api_keys = async_to_streamed_response_wrapper(
            api_keys.get_api_keys,
        )

    @cached_property
    def revoke(self) -> AsyncRevokeResourceWithStreamingResponse:
        return AsyncRevokeResourceWithStreamingResponse(self._api_keys.revoke)

    @cached_property
    def rotate(self) -> AsyncRotateResourceWithStreamingResponse:
        return AsyncRotateResourceWithStreamingResponse(self._api_keys.rotate)
