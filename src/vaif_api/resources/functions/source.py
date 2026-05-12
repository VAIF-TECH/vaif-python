# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.functions import source_source_params
from ...types.functions.source_source_response import SourceSourceResponse

__all__ = ["SourceResource", "AsyncSourceResource"]


class SourceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SourceResourceWithStreamingResponse(self)

    def source(
        self,
        function_id: str,
        *,
        source_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceSourceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._put(
            path_template("/functions/{function_id}/source", function_id=function_id),
            body=maybe_transform({"source_code": source_code}, source_source_params.SourceSourceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceSourceResponse,
        )


class AsyncSourceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSourceResourceWithStreamingResponse(self)

    async def source(
        self,
        function_id: str,
        *,
        source_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceSourceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._put(
            path_template("/functions/{function_id}/source", function_id=function_id),
            body=await async_maybe_transform({"source_code": source_code}, source_source_params.SourceSourceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceSourceResponse,
        )


class SourceResourceWithRawResponse:
    def __init__(self, source: SourceResource) -> None:
        self._source = source

        self.source = to_raw_response_wrapper(
            source.source,
        )


class AsyncSourceResourceWithRawResponse:
    def __init__(self, source: AsyncSourceResource) -> None:
        self._source = source

        self.source = async_to_raw_response_wrapper(
            source.source,
        )


class SourceResourceWithStreamingResponse:
    def __init__(self, source: SourceResource) -> None:
        self._source = source

        self.source = to_streamed_response_wrapper(
            source.source,
        )


class AsyncSourceResourceWithStreamingResponse:
    def __init__(self, source: AsyncSourceResource) -> None:
        self._source = source

        self.source = async_to_streamed_response_wrapper(
            source.source,
        )
