# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .all import (
    AllResource,
    AsyncAllResource,
    AllResourceWithRawResponse,
    AsyncAllResourceWithRawResponse,
    AllResourceWithStreamingResponse,
    AsyncAllResourceWithStreamingResponse,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
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
from .health.health import (
    HealthResource,
    AsyncHealthResource,
    HealthResourceWithRawResponse,
    AsyncHealthResourceWithRawResponse,
    HealthResourceWithStreamingResponse,
    AsyncHealthResourceWithStreamingResponse,
)
from ..._base_client import make_request_options

__all__ = ["RegionsResource", "AsyncRegionsResource"]


class RegionsResource(SyncAPIResource):
    @cached_property
    def all(self) -> AllResource:
        return AllResource(self._client)

    @cached_property
    def health(self) -> HealthResource:
        return HealthResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RegionsResourceWithStreamingResponse(self)

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
            "/regions/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        key: str,
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
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/regions/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        key: str,
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
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/regions/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
            "/regions/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRegionsResource(AsyncAPIResource):
    @cached_property
    def all(self) -> AsyncAllResource:
        return AsyncAllResource(self._client)

    @cached_property
    def health(self) -> AsyncHealthResource:
        return AsyncHealthResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRegionsResourceWithStreamingResponse(self)

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
            "/regions/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        key: str,
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
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/regions/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        key: str,
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
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/regions/{key}", key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
            "/regions/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RegionsResourceWithRawResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.create = to_raw_response_wrapper(
            regions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            regions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            regions.update,
        )
        self.list = to_raw_response_wrapper(
            regions.list,
        )

    @cached_property
    def all(self) -> AllResourceWithRawResponse:
        return AllResourceWithRawResponse(self._regions.all)

    @cached_property
    def health(self) -> HealthResourceWithRawResponse:
        return HealthResourceWithRawResponse(self._regions.health)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._regions.metrics)


class AsyncRegionsResourceWithRawResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.create = async_to_raw_response_wrapper(
            regions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            regions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            regions.update,
        )
        self.list = async_to_raw_response_wrapper(
            regions.list,
        )

    @cached_property
    def all(self) -> AsyncAllResourceWithRawResponse:
        return AsyncAllResourceWithRawResponse(self._regions.all)

    @cached_property
    def health(self) -> AsyncHealthResourceWithRawResponse:
        return AsyncHealthResourceWithRawResponse(self._regions.health)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._regions.metrics)


class RegionsResourceWithStreamingResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.create = to_streamed_response_wrapper(
            regions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            regions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            regions.update,
        )
        self.list = to_streamed_response_wrapper(
            regions.list,
        )

    @cached_property
    def all(self) -> AllResourceWithStreamingResponse:
        return AllResourceWithStreamingResponse(self._regions.all)

    @cached_property
    def health(self) -> HealthResourceWithStreamingResponse:
        return HealthResourceWithStreamingResponse(self._regions.health)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._regions.metrics)


class AsyncRegionsResourceWithStreamingResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.create = async_to_streamed_response_wrapper(
            regions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            regions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            regions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            regions.list,
        )

    @cached_property
    def all(self) -> AsyncAllResourceWithStreamingResponse:
        return AsyncAllResourceWithStreamingResponse(self._regions.all)

    @cached_property
    def health(self) -> AsyncHealthResourceWithStreamingResponse:
        return AsyncHealthResourceWithStreamingResponse(self._regions.health)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._regions.metrics)
