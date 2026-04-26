# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.auth.refresh_create_response import RefreshCreateResponse

__all__ = ["RefreshResource", "AsyncRefreshResource"]


class RefreshResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefreshResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RefreshResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefreshResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RefreshResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RefreshCreateResponse:
        """Rotate the refresh token and issue a new access token"""
        return self._post(
            "/auth/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefreshCreateResponse,
        )


class AsyncRefreshResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefreshResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRefreshResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefreshResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRefreshResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RefreshCreateResponse:
        """Rotate the refresh token and issue a new access token"""
        return await self._post(
            "/auth/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RefreshCreateResponse,
        )


class RefreshResourceWithRawResponse:
    def __init__(self, refresh: RefreshResource) -> None:
        self._refresh = refresh

        self.create = to_raw_response_wrapper(
            refresh.create,
        )


class AsyncRefreshResourceWithRawResponse:
    def __init__(self, refresh: AsyncRefreshResource) -> None:
        self._refresh = refresh

        self.create = async_to_raw_response_wrapper(
            refresh.create,
        )


class RefreshResourceWithStreamingResponse:
    def __init__(self, refresh: RefreshResource) -> None:
        self._refresh = refresh

        self.create = to_streamed_response_wrapper(
            refresh.create,
        )


class AsyncRefreshResourceWithStreamingResponse:
    def __init__(self, refresh: AsyncRefreshResource) -> None:
        self._refresh = refresh

        self.create = async_to_streamed_response_wrapper(
            refresh.create,
        )
