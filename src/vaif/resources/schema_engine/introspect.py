# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.schema_engine.introspect_retrieve_response import IntrospectRetrieveResponse

__all__ = ["IntrospectResource", "AsyncIntrospectResource"]


class IntrospectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntrospectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return IntrospectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntrospectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return IntrospectResourceWithStreamingResponse(self)

    def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntrospectRetrieveResponse:
        """
        Introspect current database schema for a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/schema-engine/introspect/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrospectRetrieveResponse,
        )


class AsyncIntrospectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntrospectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntrospectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntrospectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncIntrospectResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntrospectRetrieveResponse:
        """
        Introspect current database schema for a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/schema-engine/introspect/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrospectRetrieveResponse,
        )


class IntrospectResourceWithRawResponse:
    def __init__(self, introspect: IntrospectResource) -> None:
        self._introspect = introspect

        self.retrieve = to_raw_response_wrapper(
            introspect.retrieve,
        )


class AsyncIntrospectResourceWithRawResponse:
    def __init__(self, introspect: AsyncIntrospectResource) -> None:
        self._introspect = introspect

        self.retrieve = async_to_raw_response_wrapper(
            introspect.retrieve,
        )


class IntrospectResourceWithStreamingResponse:
    def __init__(self, introspect: IntrospectResource) -> None:
        self._introspect = introspect

        self.retrieve = to_streamed_response_wrapper(
            introspect.retrieve,
        )


class AsyncIntrospectResourceWithStreamingResponse:
    def __init__(self, introspect: AsyncIntrospectResource) -> None:
        self._introspect = introspect

        self.retrieve = async_to_streamed_response_wrapper(
            introspect.retrieve,
        )
