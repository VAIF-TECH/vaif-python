# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.integrations.deliveries.retry_retry_response import RetryRetryResponse

__all__ = ["RetryResource", "AsyncRetryResource"]


class RetryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RetryResourceWithStreamingResponse(self)

    def retry(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetryRetryResponse:
        """
        Retry a failed webhook delivery

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._post(
            path_template("/integrations/deliveries/{delivery_id}/retry", delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetryRetryResponse,
        )


class AsyncRetryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRetryResourceWithStreamingResponse(self)

    async def retry(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetryRetryResponse:
        """
        Retry a failed webhook delivery

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._post(
            path_template("/integrations/deliveries/{delivery_id}/retry", delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetryRetryResponse,
        )


class RetryResourceWithRawResponse:
    def __init__(self, retry: RetryResource) -> None:
        self._retry = retry

        self.retry = to_raw_response_wrapper(
            retry.retry,
        )


class AsyncRetryResourceWithRawResponse:
    def __init__(self, retry: AsyncRetryResource) -> None:
        self._retry = retry

        self.retry = async_to_raw_response_wrapper(
            retry.retry,
        )


class RetryResourceWithStreamingResponse:
    def __init__(self, retry: RetryResource) -> None:
        self._retry = retry

        self.retry = to_streamed_response_wrapper(
            retry.retry,
        )


class AsyncRetryResourceWithStreamingResponse:
    def __init__(self, retry: AsyncRetryResource) -> None:
        self._retry = retry

        self.retry = async_to_streamed_response_wrapper(
            retry.retry,
        )
