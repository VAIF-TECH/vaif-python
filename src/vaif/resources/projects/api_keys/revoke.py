# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["RevokeResource", "AsyncRevokeResource"]


class RevokeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevokeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RevokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevokeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RevokeResourceWithStreamingResponse(self)

    def revoke(
        self,
        key_id: str,
        *,
        project_id: str,
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
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/api-keys/{key_id}/revoke", project_id=project_id, key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRevokeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevokeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevokeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevokeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRevokeResourceWithStreamingResponse(self)

    async def revoke(
        self,
        key_id: str,
        *,
        project_id: str,
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
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/api-keys/{key_id}/revoke", project_id=project_id, key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RevokeResourceWithRawResponse:
    def __init__(self, revoke: RevokeResource) -> None:
        self._revoke = revoke

        self.revoke = to_raw_response_wrapper(
            revoke.revoke,
        )


class AsyncRevokeResourceWithRawResponse:
    def __init__(self, revoke: AsyncRevokeResource) -> None:
        self._revoke = revoke

        self.revoke = async_to_raw_response_wrapper(
            revoke.revoke,
        )


class RevokeResourceWithStreamingResponse:
    def __init__(self, revoke: RevokeResource) -> None:
        self._revoke = revoke

        self.revoke = to_streamed_response_wrapper(
            revoke.revoke,
        )


class AsyncRevokeResourceWithStreamingResponse:
    def __init__(self, revoke: AsyncRevokeResource) -> None:
        self._revoke = revoke

        self.revoke = async_to_streamed_response_wrapper(
            revoke.revoke,
        )
