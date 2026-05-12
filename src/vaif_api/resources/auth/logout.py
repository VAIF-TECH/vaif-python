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
from ...types.auth.logout_create_response import LogoutCreateResponse

__all__ = ["LogoutResource", "AsyncLogoutResource"]


class LogoutResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return LogoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return LogoutResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoutCreateResponse:
        """Invalidate the current session and clear the refresh token cookie"""
        return self._post(
            "/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoutCreateResponse,
        )


class AsyncLogoutResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncLogoutResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoutCreateResponse:
        """Invalidate the current session and clear the refresh token cookie"""
        return await self._post(
            "/auth/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoutCreateResponse,
        )


class LogoutResourceWithRawResponse:
    def __init__(self, logout: LogoutResource) -> None:
        self._logout = logout

        self.create = to_raw_response_wrapper(
            logout.create,
        )


class AsyncLogoutResourceWithRawResponse:
    def __init__(self, logout: AsyncLogoutResource) -> None:
        self._logout = logout

        self.create = async_to_raw_response_wrapper(
            logout.create,
        )


class LogoutResourceWithStreamingResponse:
    def __init__(self, logout: LogoutResource) -> None:
        self._logout = logout

        self.create = to_streamed_response_wrapper(
            logout.create,
        )


class AsyncLogoutResourceWithStreamingResponse:
    def __init__(self, logout: AsyncLogoutResource) -> None:
        self._logout = logout

        self.create = async_to_streamed_response_wrapper(
            logout.create,
        )
