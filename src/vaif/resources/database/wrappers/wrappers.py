# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .available import (
    AvailableResource,
    AsyncAvailableResource,
    AvailableResourceWithRawResponse,
    AsyncAvailableResourceWithRawResponse,
    AvailableResourceWithStreamingResponse,
    AsyncAvailableResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .project.project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)

__all__ = ["WrappersResource", "AsyncWrappersResource"]


class WrappersResource(SyncAPIResource):
    @cached_property
    def available(self) -> AvailableResource:
        return AvailableResource(self._client)

    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> WrappersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return WrappersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WrappersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return WrappersResourceWithStreamingResponse(self)


class AsyncWrappersResource(AsyncAPIResource):
    @cached_property
    def available(self) -> AsyncAvailableResource:
        return AsyncAvailableResource(self._client)

    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWrappersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWrappersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWrappersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncWrappersResourceWithStreamingResponse(self)


class WrappersResourceWithRawResponse:
    def __init__(self, wrappers: WrappersResource) -> None:
        self._wrappers = wrappers

    @cached_property
    def available(self) -> AvailableResourceWithRawResponse:
        return AvailableResourceWithRawResponse(self._wrappers.available)

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._wrappers.project)


class AsyncWrappersResourceWithRawResponse:
    def __init__(self, wrappers: AsyncWrappersResource) -> None:
        self._wrappers = wrappers

    @cached_property
    def available(self) -> AsyncAvailableResourceWithRawResponse:
        return AsyncAvailableResourceWithRawResponse(self._wrappers.available)

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._wrappers.project)


class WrappersResourceWithStreamingResponse:
    def __init__(self, wrappers: WrappersResource) -> None:
        self._wrappers = wrappers

    @cached_property
    def available(self) -> AvailableResourceWithStreamingResponse:
        return AvailableResourceWithStreamingResponse(self._wrappers.available)

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._wrappers.project)


class AsyncWrappersResourceWithStreamingResponse:
    def __init__(self, wrappers: AsyncWrappersResource) -> None:
        self._wrappers = wrappers

    @cached_property
    def available(self) -> AsyncAvailableResourceWithStreamingResponse:
        return AsyncAvailableResourceWithStreamingResponse(self._wrappers.available)

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._wrappers.project)
