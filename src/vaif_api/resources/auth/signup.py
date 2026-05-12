# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.auth import signup_create_params
from ..._base_client import make_request_options
from ...types.auth.signup_create_response import SignupCreateResponse

__all__ = ["SignupResource", "AsyncSignupResource"]


class SignupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SignupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SignupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SignupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SignupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        password: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignupCreateResponse:
        """
        Register a new user account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/signup",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "name": name,
                },
                signup_create_params.SignupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignupCreateResponse,
        )


class AsyncSignupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSignupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSignupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSignupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSignupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        password: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignupCreateResponse:
        """
        Register a new user account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/signup",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "name": name,
                },
                signup_create_params.SignupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignupCreateResponse,
        )


class SignupResourceWithRawResponse:
    def __init__(self, signup: SignupResource) -> None:
        self._signup = signup

        self.create = to_raw_response_wrapper(
            signup.create,
        )


class AsyncSignupResourceWithRawResponse:
    def __init__(self, signup: AsyncSignupResource) -> None:
        self._signup = signup

        self.create = async_to_raw_response_wrapper(
            signup.create,
        )


class SignupResourceWithStreamingResponse:
    def __init__(self, signup: SignupResource) -> None:
        self._signup = signup

        self.create = to_streamed_response_wrapper(
            signup.create,
        )


class AsyncSignupResourceWithStreamingResponse:
    def __init__(self, signup: AsyncSignupResource) -> None:
        self._signup = signup

        self.create = async_to_streamed_response_wrapper(
            signup.create,
        )
