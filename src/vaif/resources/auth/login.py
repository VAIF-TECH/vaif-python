# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import login_create_params
from ..._base_client import make_request_options
from ...types.auth.login_create_response import LoginCreateResponse

__all__ = ["LoginResource", "AsyncLoginResource"]


class LoginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return LoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return LoginResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginCreateResponse:
        """
        Authenticate with email and password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/login",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                login_create_params.LoginCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginCreateResponse,
        )


class AsyncLoginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncLoginResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginCreateResponse:
        """
        Authenticate with email and password

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/login",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                login_create_params.LoginCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginCreateResponse,
        )


class LoginResourceWithRawResponse:
    def __init__(self, login: LoginResource) -> None:
        self._login = login

        self.create = to_raw_response_wrapper(
            login.create,
        )


class AsyncLoginResourceWithRawResponse:
    def __init__(self, login: AsyncLoginResource) -> None:
        self._login = login

        self.create = async_to_raw_response_wrapper(
            login.create,
        )


class LoginResourceWithStreamingResponse:
    def __init__(self, login: LoginResource) -> None:
        self._login = login

        self.create = to_streamed_response_wrapper(
            login.create,
        )


class AsyncLoginResourceWithStreamingResponse:
    def __init__(self, login: AsyncLoginResource) -> None:
        self._login = login

        self.create = async_to_streamed_response_wrapper(
            login.create,
        )
