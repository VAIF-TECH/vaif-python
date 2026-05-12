# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.auth.cli.authorize_create_response import AuthorizeCreateResponse

__all__ = ["AuthorizeResource", "AsyncAuthorizeResource"]


class AuthorizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AuthorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AuthorizeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthorizeCreateResponse:
        """Request a CLI auth session code — returns a code and browser URL for approval"""
        return self._post(
            "/auth/cli/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizeCreateResponse,
        )


class AsyncAuthorizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAuthorizeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthorizeCreateResponse:
        """Request a CLI auth session code — returns a code and browser URL for approval"""
        return await self._post(
            "/auth/cli/authorize",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizeCreateResponse,
        )


class AuthorizeResourceWithRawResponse:
    def __init__(self, authorize: AuthorizeResource) -> None:
        self._authorize = authorize

        self.create = to_raw_response_wrapper(
            authorize.create,
        )


class AsyncAuthorizeResourceWithRawResponse:
    def __init__(self, authorize: AsyncAuthorizeResource) -> None:
        self._authorize = authorize

        self.create = async_to_raw_response_wrapper(
            authorize.create,
        )


class AuthorizeResourceWithStreamingResponse:
    def __init__(self, authorize: AuthorizeResource) -> None:
        self._authorize = authorize

        self.create = to_streamed_response_wrapper(
            authorize.create,
        )


class AsyncAuthorizeResourceWithStreamingResponse:
    def __init__(self, authorize: AsyncAuthorizeResource) -> None:
        self._authorize = authorize

        self.create = async_to_streamed_response_wrapper(
            authorize.create,
        )
