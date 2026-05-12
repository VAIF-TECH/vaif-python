# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
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

__all__ = ["NextResource", "AsyncNextResource"]


class NextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return NextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return NextResourceWithStreamingResponse(self)

    def next(
        self,
        cursor_id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not cursor_id:
            raise ValueError(f"Expected a non-empty value for `cursor_id` but received {cursor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/mongodb/{collection}/cursor/{cursor_id}/next", collection=collection, cursor_id=cursor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncNextResourceWithStreamingResponse(self)

    async def next(
        self,
        cursor_id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not cursor_id:
            raise ValueError(f"Expected a non-empty value for `cursor_id` but received {cursor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/mongodb/{collection}/cursor/{cursor_id}/next", collection=collection, cursor_id=cursor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NextResourceWithRawResponse:
    def __init__(self, next: NextResource) -> None:
        self._next = next

        self.next = to_raw_response_wrapper(
            next.next,
        )


class AsyncNextResourceWithRawResponse:
    def __init__(self, next: AsyncNextResource) -> None:
        self._next = next

        self.next = async_to_raw_response_wrapper(
            next.next,
        )


class NextResourceWithStreamingResponse:
    def __init__(self, next: NextResource) -> None:
        self._next = next

        self.next = to_streamed_response_wrapper(
            next.next,
        )


class AsyncNextResourceWithStreamingResponse:
    def __init__(self, next: AsyncNextResource) -> None:
        self._next = next

        self.next = async_to_streamed_response_wrapper(
            next.next,
        )
