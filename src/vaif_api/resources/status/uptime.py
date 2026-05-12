# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.status.uptime_retrieve_response import UptimeRetrieveResponse

__all__ = ["UptimeResource", "AsyncUptimeResource"]


class UptimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UptimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return UptimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UptimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return UptimeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        component_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UptimeRetrieveResponse:
        """
        Get uptime history for a component

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_id:
            raise ValueError(f"Expected a non-empty value for `component_id` but received {component_id!r}")
        return self._get(
            path_template("/status/uptime/{component_id}", component_id=component_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UptimeRetrieveResponse,
        )


class AsyncUptimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUptimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUptimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUptimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncUptimeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        component_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UptimeRetrieveResponse:
        """
        Get uptime history for a component

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not component_id:
            raise ValueError(f"Expected a non-empty value for `component_id` but received {component_id!r}")
        return await self._get(
            path_template("/status/uptime/{component_id}", component_id=component_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UptimeRetrieveResponse,
        )


class UptimeResourceWithRawResponse:
    def __init__(self, uptime: UptimeResource) -> None:
        self._uptime = uptime

        self.retrieve = to_raw_response_wrapper(
            uptime.retrieve,
        )


class AsyncUptimeResourceWithRawResponse:
    def __init__(self, uptime: AsyncUptimeResource) -> None:
        self._uptime = uptime

        self.retrieve = async_to_raw_response_wrapper(
            uptime.retrieve,
        )


class UptimeResourceWithStreamingResponse:
    def __init__(self, uptime: UptimeResource) -> None:
        self._uptime = uptime

        self.retrieve = to_streamed_response_wrapper(
            uptime.retrieve,
        )


class AsyncUptimeResourceWithStreamingResponse:
    def __init__(self, uptime: AsyncUptimeResource) -> None:
        self._uptime = uptime

        self.retrieve = async_to_streamed_response_wrapper(
            uptime.retrieve,
        )
