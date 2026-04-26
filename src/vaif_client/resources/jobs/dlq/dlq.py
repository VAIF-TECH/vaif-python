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

__all__ = ["DlqResource", "AsyncDlqResource"]


class DlqResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> DlqResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DlqResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DlqResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DlqResourceWithStreamingResponse(self)


class AsyncDlqResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDlqResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDlqResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDlqResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDlqResourceWithStreamingResponse(self)


class DlqResourceWithRawResponse:
    def __init__(self, dlq: DlqResource) -> None:
        self._dlq = dlq

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._dlq.project)


class AsyncDlqResourceWithRawResponse:
    def __init__(self, dlq: AsyncDlqResource) -> None:
        self._dlq = dlq

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._dlq.project)


class DlqResourceWithStreamingResponse:
    def __init__(self, dlq: DlqResource) -> None:
        self._dlq = dlq

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._dlq.project)


class AsyncDlqResourceWithStreamingResponse:
    def __init__(self, dlq: AsyncDlqResource) -> None:
        self._dlq = dlq

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._dlq.project)
