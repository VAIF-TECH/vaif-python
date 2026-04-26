# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .check import (
    CheckResource,
    AsyncCheckResource,
    CheckResourceWithRawResponse,
    AsyncCheckResourceWithRawResponse,
    CheckResourceWithStreamingResponse,
    AsyncCheckResourceWithStreamingResponse,
)
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

__all__ = ["HealthResource", "AsyncHealthResource"]


class HealthResource(SyncAPIResource):
    @cached_property
    def check(self) -> CheckResource:
        return CheckResource(self._client)

    @cached_property
    def with_raw_response(self) -> HealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return HealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return HealthResourceWithStreamingResponse(self)

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
            "/regions/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHealthResource(AsyncAPIResource):
    @cached_property
    def check(self) -> AsyncCheckResource:
        return AsyncCheckResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncHealthResourceWithStreamingResponse(self)

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
            "/regions/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HealthResourceWithRawResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.list = to_raw_response_wrapper(
            health.list,
        )

    @cached_property
    def check(self) -> CheckResourceWithRawResponse:
        return CheckResourceWithRawResponse(self._health.check)


class AsyncHealthResourceWithRawResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.list = async_to_raw_response_wrapper(
            health.list,
        )

    @cached_property
    def check(self) -> AsyncCheckResourceWithRawResponse:
        return AsyncCheckResourceWithRawResponse(self._health.check)


class HealthResourceWithStreamingResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.list = to_streamed_response_wrapper(
            health.list,
        )

    @cached_property
    def check(self) -> CheckResourceWithStreamingResponse:
        return CheckResourceWithStreamingResponse(self._health.check)


class AsyncHealthResourceWithStreamingResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.list = async_to_streamed_response_wrapper(
            health.list,
        )

    @cached_property
    def check(self) -> AsyncCheckResourceWithStreamingResponse:
        return AsyncCheckResourceWithStreamingResponse(self._health.check)
