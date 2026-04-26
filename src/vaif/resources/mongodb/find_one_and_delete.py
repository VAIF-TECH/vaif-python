# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
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

__all__ = ["FindOneAndDeleteResource", "AsyncFindOneAndDeleteResource"]


class FindOneAndDeleteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindOneAndDeleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return FindOneAndDeleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindOneAndDeleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return FindOneAndDeleteResourceWithStreamingResponse(self)

    def find_one_and_delete(
        self,
        collection: str,
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
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/mongodb/{collection}/findOneAndDelete", collection=collection),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFindOneAndDeleteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindOneAndDeleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindOneAndDeleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindOneAndDeleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncFindOneAndDeleteResourceWithStreamingResponse(self)

    async def find_one_and_delete(
        self,
        collection: str,
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
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/mongodb/{collection}/findOneAndDelete", collection=collection),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FindOneAndDeleteResourceWithRawResponse:
    def __init__(self, find_one_and_delete: FindOneAndDeleteResource) -> None:
        self._find_one_and_delete = find_one_and_delete

        self.find_one_and_delete = to_raw_response_wrapper(
            find_one_and_delete.find_one_and_delete,
        )


class AsyncFindOneAndDeleteResourceWithRawResponse:
    def __init__(self, find_one_and_delete: AsyncFindOneAndDeleteResource) -> None:
        self._find_one_and_delete = find_one_and_delete

        self.find_one_and_delete = async_to_raw_response_wrapper(
            find_one_and_delete.find_one_and_delete,
        )


class FindOneAndDeleteResourceWithStreamingResponse:
    def __init__(self, find_one_and_delete: FindOneAndDeleteResource) -> None:
        self._find_one_and_delete = find_one_and_delete

        self.find_one_and_delete = to_streamed_response_wrapper(
            find_one_and_delete.find_one_and_delete,
        )


class AsyncFindOneAndDeleteResourceWithStreamingResponse:
    def __init__(self, find_one_and_delete: AsyncFindOneAndDeleteResource) -> None:
        self._find_one_and_delete = find_one_and_delete

        self.find_one_and_delete = async_to_streamed_response_wrapper(
            find_one_and_delete.find_one_and_delete,
        )
