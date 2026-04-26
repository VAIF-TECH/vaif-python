# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .quickstart import (
    QuickstartResource,
    AsyncQuickstartResource,
    QuickstartResourceWithRawResponse,
    AsyncQuickstartResourceWithRawResponse,
    QuickstartResourceWithStreamingResponse,
    AsyncQuickstartResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def quickstart(self) -> QuickstartResource:
        return QuickstartResource(self._client)

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


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def quickstart(self) -> AsyncQuickstartResource:
        return AsyncQuickstartResource(self._client)

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


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def quickstart(self) -> QuickstartResourceWithRawResponse:
        return QuickstartResourceWithRawResponse(self._project.quickstart)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def quickstart(self) -> AsyncQuickstartResourceWithRawResponse:
        return AsyncQuickstartResourceWithRawResponse(self._project.quickstart)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def quickstart(self) -> QuickstartResourceWithStreamingResponse:
        return QuickstartResourceWithStreamingResponse(self._project.quickstart)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def quickstart(self) -> AsyncQuickstartResourceWithStreamingResponse:
        return AsyncQuickstartResourceWithStreamingResponse(self._project.quickstart)
