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
from ...types.incidents.ack_ack_response import AckAckResponse

__all__ = ["AckResource", "AsyncAckResource"]


class AckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AckResourceWithStreamingResponse(self)

    def ack(
        self,
        incident_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AckAckResponse:
        """
        Acknowledge an incident

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not incident_id:
            raise ValueError(f"Expected a non-empty value for `incident_id` but received {incident_id!r}")
        return self._post(
            path_template("/incidents/{incident_id}/ack", incident_id=incident_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AckAckResponse,
        )


class AsyncAckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAckResourceWithStreamingResponse(self)

    async def ack(
        self,
        incident_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AckAckResponse:
        """
        Acknowledge an incident

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not incident_id:
            raise ValueError(f"Expected a non-empty value for `incident_id` but received {incident_id!r}")
        return await self._post(
            path_template("/incidents/{incident_id}/ack", incident_id=incident_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AckAckResponse,
        )


class AckResourceWithRawResponse:
    def __init__(self, ack: AckResource) -> None:
        self._ack = ack

        self.ack = to_raw_response_wrapper(
            ack.ack,
        )


class AsyncAckResourceWithRawResponse:
    def __init__(self, ack: AsyncAckResource) -> None:
        self._ack = ack

        self.ack = async_to_raw_response_wrapper(
            ack.ack,
        )


class AckResourceWithStreamingResponse:
    def __init__(self, ack: AckResource) -> None:
        self._ack = ack

        self.ack = to_streamed_response_wrapper(
            ack.ack,
        )


class AsyncAckResourceWithStreamingResponse:
    def __init__(self, ack: AsyncAckResource) -> None:
        self._ack = ack

        self.ack = async_to_streamed_response_wrapper(
            ack.ack,
        )
