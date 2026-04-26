# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

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
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

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
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._project.events)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._project.stats)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._project.events)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._project.stats)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._project.events)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._project.stats)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._project.events)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._project.stats)
