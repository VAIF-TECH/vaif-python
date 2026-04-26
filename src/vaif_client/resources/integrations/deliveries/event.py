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
from ....types.integrations.deliveries.event_retrieve_response import EventRetrieveResponse

__all__ = ["EventResource", "AsyncEventResource"]


class EventResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return EventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return EventResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventRetrieveResponse:
        """
        List deliveries for an event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/integrations/deliveries/event/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventRetrieveResponse,
        )


class AsyncEventResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncEventResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventRetrieveResponse:
        """
        List deliveries for an event

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/integrations/deliveries/event/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventRetrieveResponse,
        )


class EventResourceWithRawResponse:
    def __init__(self, event: EventResource) -> None:
        self._event = event

        self.retrieve = to_raw_response_wrapper(
            event.retrieve,
        )


class AsyncEventResourceWithRawResponse:
    def __init__(self, event: AsyncEventResource) -> None:
        self._event = event

        self.retrieve = async_to_raw_response_wrapper(
            event.retrieve,
        )


class EventResourceWithStreamingResponse:
    def __init__(self, event: EventResource) -> None:
        self._event = event

        self.retrieve = to_streamed_response_wrapper(
            event.retrieve,
        )


class AsyncEventResourceWithStreamingResponse:
    def __init__(self, event: AsyncEventResource) -> None:
        self._event = event

        self.retrieve = async_to_streamed_response_wrapper(
            event.retrieve,
        )
