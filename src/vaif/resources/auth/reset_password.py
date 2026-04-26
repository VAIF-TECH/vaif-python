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
from ...types.auth import reset_password_create_params
from ..._base_client import make_request_options
from ...types.auth.reset_password_create_response import ResetPasswordCreateResponse

__all__ = ["ResetPasswordResource", "AsyncResetPasswordResource"]


class ResetPasswordResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResetPasswordResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ResetPasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResetPasswordResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ResetPasswordResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        token: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResetPasswordCreateResponse:
        """
        Submit a new password using a reset token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/reset-password",
            body=maybe_transform(
                {
                    "token": token,
                    "password": password,
                },
                reset_password_create_params.ResetPasswordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetPasswordCreateResponse,
        )


class AsyncResetPasswordResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResetPasswordResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResetPasswordResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResetPasswordResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncResetPasswordResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        token: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResetPasswordCreateResponse:
        """
        Submit a new password using a reset token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/reset-password",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "password": password,
                },
                reset_password_create_params.ResetPasswordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetPasswordCreateResponse,
        )


class ResetPasswordResourceWithRawResponse:
    def __init__(self, reset_password: ResetPasswordResource) -> None:
        self._reset_password = reset_password

        self.create = to_raw_response_wrapper(
            reset_password.create,
        )


class AsyncResetPasswordResourceWithRawResponse:
    def __init__(self, reset_password: AsyncResetPasswordResource) -> None:
        self._reset_password = reset_password

        self.create = async_to_raw_response_wrapper(
            reset_password.create,
        )


class ResetPasswordResourceWithStreamingResponse:
    def __init__(self, reset_password: ResetPasswordResource) -> None:
        self._reset_password = reset_password

        self.create = to_streamed_response_wrapper(
            reset_password.create,
        )


class AsyncResetPasswordResourceWithStreamingResponse:
    def __init__(self, reset_password: AsyncResetPasswordResource) -> None:
        self._reset_password = reset_password

        self.create = async_to_streamed_response_wrapper(
            reset_password.create,
        )
