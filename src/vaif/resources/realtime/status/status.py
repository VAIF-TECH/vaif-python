# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> StatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return StatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return StatusResourceWithStreamingResponse(self)


class AsyncStatusResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncStatusResourceWithStreamingResponse(self)


class StatusResourceWithRawResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._status.project)


class AsyncStatusResourceWithRawResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._status.project)


class StatusResourceWithStreamingResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._status.project)


class AsyncStatusResourceWithStreamingResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._status.project)
