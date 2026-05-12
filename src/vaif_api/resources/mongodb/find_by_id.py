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

__all__ = ["FindByIDResource", "AsyncFindByIDResource"]


class FindByIDResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindByIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return FindByIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindByIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return FindByIDResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/mongodb/{collection}/findById/{id}", collection=collection, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFindByIDResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindByIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindByIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindByIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncFindByIDResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/mongodb/{collection}/findById/{id}", collection=collection, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FindByIDResourceWithRawResponse:
    def __init__(self, find_by_id: FindByIDResource) -> None:
        self._find_by_id = find_by_id

        self.retrieve = to_raw_response_wrapper(
            find_by_id.retrieve,
        )


class AsyncFindByIDResourceWithRawResponse:
    def __init__(self, find_by_id: AsyncFindByIDResource) -> None:
        self._find_by_id = find_by_id

        self.retrieve = async_to_raw_response_wrapper(
            find_by_id.retrieve,
        )


class FindByIDResourceWithStreamingResponse:
    def __init__(self, find_by_id: FindByIDResource) -> None:
        self._find_by_id = find_by_id

        self.retrieve = to_streamed_response_wrapper(
            find_by_id.retrieve,
        )


class AsyncFindByIDResourceWithStreamingResponse:
    def __init__(self, find_by_id: AsyncFindByIDResource) -> None:
        self._find_by_id = find_by_id

        self.retrieve = async_to_streamed_response_wrapper(
            find_by_id.retrieve,
        )
