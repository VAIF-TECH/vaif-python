# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ...types.projects import region_region_params
from ...types.projects.region_region_response import RegionRegionResponse

__all__ = ["RegionResource", "AsyncRegionResource"]


class RegionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RegionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RegionResourceWithStreamingResponse(self)

    def get_region(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/region", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def region(
        self,
        project_id: str,
        *,
        region_key: str,
        tenancy_type: Literal["shared", "dedicated_db", "dedicated_stack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegionRegionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/region", project_id=project_id),
            body=maybe_transform(
                {
                    "region_key": region_key,
                    "tenancy_type": tenancy_type,
                },
                region_region_params.RegionRegionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionRegionResponse,
        )


class AsyncRegionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRegionResourceWithStreamingResponse(self)

    async def get_region(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/region", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def region(
        self,
        project_id: str,
        *,
        region_key: str,
        tenancy_type: Literal["shared", "dedicated_db", "dedicated_stack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegionRegionResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/region", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "region_key": region_key,
                    "tenancy_type": tenancy_type,
                },
                region_region_params.RegionRegionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionRegionResponse,
        )


class RegionResourceWithRawResponse:
    def __init__(self, region: RegionResource) -> None:
        self._region = region

        self.get_region = to_raw_response_wrapper(
            region.get_region,
        )
        self.region = to_raw_response_wrapper(
            region.region,
        )


class AsyncRegionResourceWithRawResponse:
    def __init__(self, region: AsyncRegionResource) -> None:
        self._region = region

        self.get_region = async_to_raw_response_wrapper(
            region.get_region,
        )
        self.region = async_to_raw_response_wrapper(
            region.region,
        )


class RegionResourceWithStreamingResponse:
    def __init__(self, region: RegionResource) -> None:
        self._region = region

        self.get_region = to_streamed_response_wrapper(
            region.get_region,
        )
        self.region = to_streamed_response_wrapper(
            region.region,
        )


class AsyncRegionResourceWithStreamingResponse:
    def __init__(self, region: AsyncRegionResource) -> None:
        self._region = region

        self.get_region = async_to_streamed_response_wrapper(
            region.get_region,
        )
        self.region = async_to_streamed_response_wrapper(
            region.region,
        )
