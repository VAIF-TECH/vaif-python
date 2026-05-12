# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["PollStatusResource", "AsyncPollStatusResource"]


class PollStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PollStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return PollStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PollStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return PollStatusResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/infrastructure/poll-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPollStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPollStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPollStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPollStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncPollStatusResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/infrastructure/poll-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PollStatusResourceWithRawResponse:
    def __init__(self, poll_status: PollStatusResource) -> None:
        self._poll_status = poll_status

        self.create = to_raw_response_wrapper(
            poll_status.create,
        )


class AsyncPollStatusResourceWithRawResponse:
    def __init__(self, poll_status: AsyncPollStatusResource) -> None:
        self._poll_status = poll_status

        self.create = async_to_raw_response_wrapper(
            poll_status.create,
        )


class PollStatusResourceWithStreamingResponse:
    def __init__(self, poll_status: PollStatusResource) -> None:
        self._poll_status = poll_status

        self.create = to_streamed_response_wrapper(
            poll_status.create,
        )


class AsyncPollStatusResourceWithStreamingResponse:
    def __init__(self, poll_status: AsyncPollStatusResource) -> None:
        self._poll_status = poll_status

        self.create = async_to_streamed_response_wrapper(
            poll_status.create,
        )
