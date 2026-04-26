# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["DeleteBatchResource", "AsyncDeleteBatchResource"]


class DeleteBatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeleteBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DeleteBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeleteBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DeleteBatchResourceWithStreamingResponse(self)

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
            "/storage/files/delete-batch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDeleteBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeleteBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeleteBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeleteBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDeleteBatchResourceWithStreamingResponse(self)

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
            "/storage/files/delete-batch",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DeleteBatchResourceWithRawResponse:
    def __init__(self, delete_batch: DeleteBatchResource) -> None:
        self._delete_batch = delete_batch

        self.create = to_raw_response_wrapper(
            delete_batch.create,
        )


class AsyncDeleteBatchResourceWithRawResponse:
    def __init__(self, delete_batch: AsyncDeleteBatchResource) -> None:
        self._delete_batch = delete_batch

        self.create = async_to_raw_response_wrapper(
            delete_batch.create,
        )


class DeleteBatchResourceWithStreamingResponse:
    def __init__(self, delete_batch: DeleteBatchResource) -> None:
        self._delete_batch = delete_batch

        self.create = to_streamed_response_wrapper(
            delete_batch.create,
        )


class AsyncDeleteBatchResourceWithStreamingResponse:
    def __init__(self, delete_batch: AsyncDeleteBatchResource) -> None:
        self._delete_batch = delete_batch

        self.create = async_to_streamed_response_wrapper(
            delete_batch.create,
        )
