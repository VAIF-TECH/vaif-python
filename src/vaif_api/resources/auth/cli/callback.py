# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.auth.cli import callback_create_params
from ....types.auth.cli.callback_create_response import CallbackCreateResponse

__all__ = ["CallbackResource", "AsyncCallbackResource"]


class CallbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CallbackResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallbackCreateResponse:
        """
        Approve a pending CLI auth session from the web app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/cli/callback",
            body=maybe_transform({"code": code}, callback_create_params.CallbackCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackCreateResponse,
        )


class AsyncCallbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCallbackResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallbackCreateResponse:
        """
        Approve a pending CLI auth session from the web app

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/cli/callback",
            body=await async_maybe_transform({"code": code}, callback_create_params.CallbackCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackCreateResponse,
        )


class CallbackResourceWithRawResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.create = to_raw_response_wrapper(
            callback.create,
        )


class AsyncCallbackResourceWithRawResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.create = async_to_raw_response_wrapper(
            callback.create,
        )


class CallbackResourceWithStreamingResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.create = to_streamed_response_wrapper(
            callback.create,
        )


class AsyncCallbackResourceWithStreamingResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.create = async_to_streamed_response_wrapper(
            callback.create,
        )
