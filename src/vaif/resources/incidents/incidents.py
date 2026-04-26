# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ack import (
    AckResource,
    AsyncAckResource,
    AckResourceWithRawResponse,
    AsyncAckResourceWithRawResponse,
    AckResourceWithStreamingResponse,
    AsyncAckResourceWithStreamingResponse,
)
from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from .resolve import (
    ResolveResource,
    AsyncResolveResource,
    ResolveResourceWithRawResponse,
    AsyncResolveResourceWithRawResponse,
    ResolveResourceWithStreamingResponse,
    AsyncResolveResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IncidentsResource", "AsyncIncidentsResource"]


class IncidentsResource(SyncAPIResource):
    @cached_property
    def ack(self) -> AckResource:
        return AckResource(self._client)

    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def resolve(self) -> ResolveResource:
        return ResolveResource(self._client)

    @cached_property
    def with_raw_response(self) -> IncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return IncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return IncidentsResourceWithStreamingResponse(self)


class AsyncIncidentsResource(AsyncAPIResource):
    @cached_property
    def ack(self) -> AsyncAckResource:
        return AsyncAckResource(self._client)

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def resolve(self) -> AsyncResolveResource:
        return AsyncResolveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncIncidentsResourceWithStreamingResponse(self)


class IncidentsResourceWithRawResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

    @cached_property
    def ack(self) -> AckResourceWithRawResponse:
        return AckResourceWithRawResponse(self._incidents.ack)

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._incidents.bulk)

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._incidents.project)

    @cached_property
    def resolve(self) -> ResolveResourceWithRawResponse:
        return ResolveResourceWithRawResponse(self._incidents.resolve)


class AsyncIncidentsResourceWithRawResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

    @cached_property
    def ack(self) -> AsyncAckResourceWithRawResponse:
        return AsyncAckResourceWithRawResponse(self._incidents.ack)

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._incidents.bulk)

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._incidents.project)

    @cached_property
    def resolve(self) -> AsyncResolveResourceWithRawResponse:
        return AsyncResolveResourceWithRawResponse(self._incidents.resolve)


class IncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

    @cached_property
    def ack(self) -> AckResourceWithStreamingResponse:
        return AckResourceWithStreamingResponse(self._incidents.ack)

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._incidents.bulk)

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._incidents.project)

    @cached_property
    def resolve(self) -> ResolveResourceWithStreamingResponse:
        return ResolveResourceWithStreamingResponse(self._incidents.resolve)


class AsyncIncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

    @cached_property
    def ack(self) -> AsyncAckResourceWithStreamingResponse:
        return AsyncAckResourceWithStreamingResponse(self._incidents.ack)

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._incidents.bulk)

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._incidents.project)

    @cached_property
    def resolve(self) -> AsyncResolveResourceWithStreamingResponse:
        return AsyncResolveResourceWithStreamingResponse(self._incidents.resolve)
