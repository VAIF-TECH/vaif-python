# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .stream import (
    StreamResource,
    AsyncStreamResource,
    StreamResourceWithRawResponse,
    AsyncStreamResourceWithRawResponse,
    StreamResourceWithStreamingResponse,
    AsyncStreamResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.logs import project_retrieve_params
from ...._base_client import make_request_options
from ....types.logs.project_retrieve_response import ProjectRetrieveResponse

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def stream(self) -> StreamResource:
        return StreamResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ProjectResourceWithStreamingResponse(self)

    def retrieve(
        self,
        project_id: str,
        *,
        level: Literal["info", "warn", "error"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        List logs for a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/logs/project/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "level": level,
                        "limit": limit,
                    },
                    project_retrieve_params.ProjectRetrieveParams,
                ),
            ),
            cast_to=ProjectRetrieveResponse,
        )


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def stream(self) -> AsyncStreamResource:
        return AsyncStreamResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncProjectResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        project_id: str,
        *,
        level: Literal["info", "warn", "error"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        List logs for a project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/logs/project/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "level": level,
                        "limit": limit,
                    },
                    project_retrieve_params.ProjectRetrieveParams,
                ),
            ),
            cast_to=ProjectRetrieveResponse,
        )


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.retrieve = to_raw_response_wrapper(
            project.retrieve,
        )

    @cached_property
    def stream(self) -> StreamResourceWithRawResponse:
        return StreamResourceWithRawResponse(self._project.stream)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.retrieve = async_to_raw_response_wrapper(
            project.retrieve,
        )

    @cached_property
    def stream(self) -> AsyncStreamResourceWithRawResponse:
        return AsyncStreamResourceWithRawResponse(self._project.stream)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.retrieve = to_streamed_response_wrapper(
            project.retrieve,
        )

    @cached_property
    def stream(self) -> StreamResourceWithStreamingResponse:
        return StreamResourceWithStreamingResponse(self._project.stream)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.retrieve = async_to_streamed_response_wrapper(
            project.retrieve,
        )

    @cached_property
    def stream(self) -> AsyncStreamResourceWithStreamingResponse:
        return AsyncStreamResourceWithStreamingResponse(self._project.stream)
