# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["DiffResource", "AsyncDiffResource"]


class DiffResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiffResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DiffResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiffResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DiffResourceWithStreamingResponse(self)

    def retrieve(
        self,
        compare_version_id: str,
        *,
        version_id: str,
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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        if not compare_version_id:
            raise ValueError(f"Expected a non-empty value for `compare_version_id` but received {compare_version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/ai/copilot/version/{version_id}/diff/{compare_version_id}",
                version_id=version_id,
                compare_version_id=compare_version_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDiffResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiffResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiffResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiffResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDiffResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        compare_version_id: str,
        *,
        version_id: str,
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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        if not compare_version_id:
            raise ValueError(f"Expected a non-empty value for `compare_version_id` but received {compare_version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/ai/copilot/version/{version_id}/diff/{compare_version_id}",
                version_id=version_id,
                compare_version_id=compare_version_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DiffResourceWithRawResponse:
    def __init__(self, diff: DiffResource) -> None:
        self._diff = diff

        self.retrieve = to_raw_response_wrapper(
            diff.retrieve,
        )


class AsyncDiffResourceWithRawResponse:
    def __init__(self, diff: AsyncDiffResource) -> None:
        self._diff = diff

        self.retrieve = async_to_raw_response_wrapper(
            diff.retrieve,
        )


class DiffResourceWithStreamingResponse:
    def __init__(self, diff: DiffResource) -> None:
        self._diff = diff

        self.retrieve = to_streamed_response_wrapper(
            diff.retrieve,
        )


class AsyncDiffResourceWithStreamingResponse:
    def __init__(self, diff: AsyncDiffResource) -> None:
        self._diff = diff

        self.retrieve = async_to_streamed_response_wrapper(
            diff.retrieve,
        )
