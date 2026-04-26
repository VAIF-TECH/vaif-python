# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.ai.copilot import rate_create_params
from ....types.ai.copilot.rate_create_response import RateCreateResponse

__all__ = ["RateResource", "AsyncRateResource"]


class RateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RateResourceWithStreamingResponse(self)

    def create(
        self,
        message_id: str,
        *,
        rating: int,
        approved: bool | Omit = omit,
        feedback: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/ai/copilot/rate/{message_id}", message_id=message_id),
            body=maybe_transform(
                {
                    "rating": rating,
                    "approved": approved,
                    "feedback": feedback,
                },
                rate_create_params.RateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCreateResponse,
        )


class AsyncRateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRateResourceWithStreamingResponse(self)

    async def create(
        self,
        message_id: str,
        *,
        rating: int,
        approved: bool | Omit = omit,
        feedback: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RateCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/ai/copilot/rate/{message_id}", message_id=message_id),
            body=await async_maybe_transform(
                {
                    "rating": rating,
                    "approved": approved,
                    "feedback": feedback,
                },
                rate_create_params.RateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCreateResponse,
        )


class RateResourceWithRawResponse:
    def __init__(self, rate: RateResource) -> None:
        self._rate = rate

        self.create = to_raw_response_wrapper(
            rate.create,
        )


class AsyncRateResourceWithRawResponse:
    def __init__(self, rate: AsyncRateResource) -> None:
        self._rate = rate

        self.create = async_to_raw_response_wrapper(
            rate.create,
        )


class RateResourceWithStreamingResponse:
    def __init__(self, rate: RateResource) -> None:
        self._rate = rate

        self.create = to_streamed_response_wrapper(
            rate.create,
        )


class AsyncRateResourceWithStreamingResponse:
    def __init__(self, rate: AsyncRateResource) -> None:
        self._rate = rate

        self.create = async_to_streamed_response_wrapper(
            rate.create,
        )
