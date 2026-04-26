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

__all__ = ["CheckNameResource", "AsyncCheckNameResource"]


class CheckNameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CheckNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CheckNameResourceWithStreamingResponse(self)

    def list(
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
        return self._get(
            "/orgs/check-name",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCheckNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCheckNameResourceWithStreamingResponse(self)

    async def list(
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
        return await self._get(
            "/orgs/check-name",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CheckNameResourceWithRawResponse:
    def __init__(self, check_name: CheckNameResource) -> None:
        self._check_name = check_name

        self.list = to_raw_response_wrapper(
            check_name.list,
        )


class AsyncCheckNameResourceWithRawResponse:
    def __init__(self, check_name: AsyncCheckNameResource) -> None:
        self._check_name = check_name

        self.list = async_to_raw_response_wrapper(
            check_name.list,
        )


class CheckNameResourceWithStreamingResponse:
    def __init__(self, check_name: CheckNameResource) -> None:
        self._check_name = check_name

        self.list = to_streamed_response_wrapper(
            check_name.list,
        )


class AsyncCheckNameResourceWithStreamingResponse:
    def __init__(self, check_name: AsyncCheckNameResource) -> None:
        self._check_name = check_name

        self.list = async_to_streamed_response_wrapper(
            check_name.list,
        )
