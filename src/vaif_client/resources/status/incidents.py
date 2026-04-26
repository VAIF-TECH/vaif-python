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

__all__ = ["IncidentsResource", "AsyncIncidentsResource"]


class IncidentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return IncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return IncidentsResourceWithStreamingResponse(self)

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
        """List recent public incidents"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/status/incidents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncIncidentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncIncidentsResourceWithStreamingResponse(self)

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
        """List recent public incidents"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/status/incidents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class IncidentsResourceWithRawResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

        self.list = to_raw_response_wrapper(
            incidents.list,
        )


class AsyncIncidentsResourceWithRawResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

        self.list = async_to_raw_response_wrapper(
            incidents.list,
        )


class IncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

        self.list = to_streamed_response_wrapper(
            incidents.list,
        )


class AsyncIncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

        self.list = async_to_streamed_response_wrapper(
            incidents.list,
        )
