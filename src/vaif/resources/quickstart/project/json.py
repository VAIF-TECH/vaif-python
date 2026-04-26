# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.quickstart.project.json_get_json_response import JsonGetJsonResponse

__all__ = ["JsonResource", "AsyncJsonResource"]


class JsonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return JsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return JsonResourceWithStreamingResponse(self)

    def get_json(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JsonGetJsonResponse:
        """
        Get quickstart JSON data for a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/quickstart/project/{project_id}/json", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JsonGetJsonResponse,
        )


class AsyncJsonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncJsonResourceWithStreamingResponse(self)

    async def get_json(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JsonGetJsonResponse:
        """
        Get quickstart JSON data for a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/quickstart/project/{project_id}/json", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JsonGetJsonResponse,
        )


class JsonResourceWithRawResponse:
    def __init__(self, json: JsonResource) -> None:
        self._json = json

        self.get_json = to_raw_response_wrapper(
            json.get_json,
        )


class AsyncJsonResourceWithRawResponse:
    def __init__(self, json: AsyncJsonResource) -> None:
        self._json = json

        self.get_json = async_to_raw_response_wrapper(
            json.get_json,
        )


class JsonResourceWithStreamingResponse:
    def __init__(self, json: JsonResource) -> None:
        self._json = json

        self.get_json = to_streamed_response_wrapper(
            json.get_json,
        )


class AsyncJsonResourceWithStreamingResponse:
    def __init__(self, json: AsyncJsonResource) -> None:
        self._json = json

        self.get_json = async_to_streamed_response_wrapper(
            json.get_json,
        )
