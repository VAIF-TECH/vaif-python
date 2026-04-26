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
from ...types.status.unsubscribe_retrieve_response import UnsubscribeRetrieveResponse

__all__ = ["UnsubscribeResource", "AsyncUnsubscribeResource"]


class UnsubscribeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnsubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return UnsubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnsubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return UnsubscribeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnsubscribeRetrieveResponse:
        """
        Unsubscribe from status updates

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._get(
            path_template("/status/unsubscribe/{token}", token=token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeRetrieveResponse,
        )


class AsyncUnsubscribeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnsubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUnsubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnsubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncUnsubscribeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnsubscribeRetrieveResponse:
        """
        Unsubscribe from status updates

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._get(
            path_template("/status/unsubscribe/{token}", token=token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeRetrieveResponse,
        )


class UnsubscribeResourceWithRawResponse:
    def __init__(self, unsubscribe: UnsubscribeResource) -> None:
        self._unsubscribe = unsubscribe

        self.retrieve = to_raw_response_wrapper(
            unsubscribe.retrieve,
        )


class AsyncUnsubscribeResourceWithRawResponse:
    def __init__(self, unsubscribe: AsyncUnsubscribeResource) -> None:
        self._unsubscribe = unsubscribe

        self.retrieve = async_to_raw_response_wrapper(
            unsubscribe.retrieve,
        )


class UnsubscribeResourceWithStreamingResponse:
    def __init__(self, unsubscribe: UnsubscribeResource) -> None:
        self._unsubscribe = unsubscribe

        self.retrieve = to_streamed_response_wrapper(
            unsubscribe.retrieve,
        )


class AsyncUnsubscribeResourceWithStreamingResponse:
    def __init__(self, unsubscribe: AsyncUnsubscribeResource) -> None:
        self._unsubscribe = unsubscribe

        self.retrieve = async_to_streamed_response_wrapper(
            unsubscribe.retrieve,
        )
