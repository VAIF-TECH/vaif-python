# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .project.project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)

__all__ = ["QuickstartResource", "AsyncQuickstartResource"]


class QuickstartResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> QuickstartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return QuickstartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuickstartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return QuickstartResourceWithStreamingResponse(self)


class AsyncQuickstartResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQuickstartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuickstartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuickstartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncQuickstartResourceWithStreamingResponse(self)


class QuickstartResourceWithRawResponse:
    def __init__(self, quickstart: QuickstartResource) -> None:
        self._quickstart = quickstart

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._quickstart.project)


class AsyncQuickstartResourceWithRawResponse:
    def __init__(self, quickstart: AsyncQuickstartResource) -> None:
        self._quickstart = quickstart

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._quickstart.project)


class QuickstartResourceWithStreamingResponse:
    def __init__(self, quickstart: QuickstartResource) -> None:
        self._quickstart = quickstart

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._quickstart.project)


class AsyncQuickstartResourceWithStreamingResponse:
    def __init__(self, quickstart: AsyncQuickstartResource) -> None:
        self._quickstart = quickstart

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._quickstart.project)
