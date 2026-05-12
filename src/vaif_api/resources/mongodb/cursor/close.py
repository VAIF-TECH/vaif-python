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

__all__ = ["CloseResource", "AsyncCloseResource"]


class CloseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CloseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CloseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CloseResourceWithStreamingResponse(self)

    def close(
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
            path_template("/mongodb/{collection}/cursor/{cursor_id}/close", collection=collection, cursor_id=cursor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCloseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCloseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCloseResourceWithStreamingResponse(self)

    async def close(
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
            path_template("/mongodb/{collection}/cursor/{cursor_id}/close", collection=collection, cursor_id=cursor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CloseResourceWithRawResponse:
    def __init__(self, close: CloseResource) -> None:
        self._close = close

        self.close = to_raw_response_wrapper(
            close.close,
        )


class AsyncCloseResourceWithRawResponse:
    def __init__(self, close: AsyncCloseResource) -> None:
        self._close = close

        self.close = async_to_raw_response_wrapper(
            close.close,
        )


class CloseResourceWithStreamingResponse:
    def __init__(self, close: CloseResource) -> None:
        self._close = close

        self.close = to_streamed_response_wrapper(
            close.close,
        )


class AsyncCloseResourceWithStreamingResponse:
    def __init__(self, close: AsyncCloseResource) -> None:
        self._close = close

        self.close = async_to_streamed_response_wrapper(
            close.close,
        )
