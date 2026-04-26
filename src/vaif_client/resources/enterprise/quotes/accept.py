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

__all__ = ["AcceptResource", "AsyncAcceptResource"]


class AcceptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AcceptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AcceptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AcceptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AcceptResourceWithStreamingResponse(self)

    def accept(
        self,
        quote_id: str,
        *,
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
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/enterprise/quotes/{quote_id}/accept", quote_id=quote_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAcceptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAcceptResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAcceptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAcceptResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAcceptResourceWithStreamingResponse(self)

    async def accept(
        self,
        quote_id: str,
        *,
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
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/enterprise/quotes/{quote_id}/accept", quote_id=quote_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AcceptResourceWithRawResponse:
    def __init__(self, accept: AcceptResource) -> None:
        self._accept = accept

        self.accept = to_raw_response_wrapper(
            accept.accept,
        )


class AsyncAcceptResourceWithRawResponse:
    def __init__(self, accept: AsyncAcceptResource) -> None:
        self._accept = accept

        self.accept = async_to_raw_response_wrapper(
            accept.accept,
        )


class AcceptResourceWithStreamingResponse:
    def __init__(self, accept: AcceptResource) -> None:
        self._accept = accept

        self.accept = to_streamed_response_wrapper(
            accept.accept,
        )


class AsyncAcceptResourceWithStreamingResponse:
    def __init__(self, accept: AsyncAcceptResource) -> None:
        self._accept = accept

        self.accept = async_to_streamed_response_wrapper(
            accept.accept,
        )
