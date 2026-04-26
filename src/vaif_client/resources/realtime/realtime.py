# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .install import (
    InstallResource,
    AsyncInstallResource,
    InstallResourceWithRawResponse,
    AsyncInstallResourceWithRawResponse,
    InstallResourceWithStreamingResponse,
    AsyncInstallResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .enable_all import (
    EnableAllResource,
    AsyncEnableAllResource,
    EnableAllResourceWithRawResponse,
    AsyncEnableAllResourceWithRawResponse,
    EnableAllResourceWithStreamingResponse,
    AsyncEnableAllResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .stats.stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .events.events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .status.status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from .connections.connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["RealtimeResource", "AsyncRealtimeResource"]


class RealtimeResource(SyncAPIResource):
    @cached_property
    def connections(self) -> ConnectionsResource:
        return ConnectionsResource(self._client)

    @cached_property
    def enable_all(self) -> EnableAllResource:
        return EnableAllResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def install(self) -> InstallResource:
        return InstallResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RealtimeResourceWithStreamingResponse(self)


class AsyncRealtimeResource(AsyncAPIResource):
    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        return AsyncConnectionsResource(self._client)

    @cached_property
    def enable_all(self) -> AsyncEnableAllResource:
        return AsyncEnableAllResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def install(self) -> AsyncInstallResource:
        return AsyncInstallResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRealtimeResourceWithStreamingResponse(self)


class RealtimeResourceWithRawResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self._realtime.connections)

    @cached_property
    def enable_all(self) -> EnableAllResourceWithRawResponse:
        return EnableAllResourceWithRawResponse(self._realtime.enable_all)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._realtime.events)

    @cached_property
    def install(self) -> InstallResourceWithRawResponse:
        return InstallResourceWithRawResponse(self._realtime.install)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._realtime.stats)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._realtime.status)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._realtime.subscriptions)


class AsyncRealtimeResourceWithRawResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self._realtime.connections)

    @cached_property
    def enable_all(self) -> AsyncEnableAllResourceWithRawResponse:
        return AsyncEnableAllResourceWithRawResponse(self._realtime.enable_all)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._realtime.events)

    @cached_property
    def install(self) -> AsyncInstallResourceWithRawResponse:
        return AsyncInstallResourceWithRawResponse(self._realtime.install)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._realtime.stats)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._realtime.status)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._realtime.subscriptions)


class RealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self._realtime.connections)

    @cached_property
    def enable_all(self) -> EnableAllResourceWithStreamingResponse:
        return EnableAllResourceWithStreamingResponse(self._realtime.enable_all)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._realtime.events)

    @cached_property
    def install(self) -> InstallResourceWithStreamingResponse:
        return InstallResourceWithStreamingResponse(self._realtime.install)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._realtime.stats)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._realtime.status)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._realtime.subscriptions)


class AsyncRealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self._realtime.connections)

    @cached_property
    def enable_all(self) -> AsyncEnableAllResourceWithStreamingResponse:
        return AsyncEnableAllResourceWithStreamingResponse(self._realtime.enable_all)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._realtime.events)

    @cached_property
    def install(self) -> AsyncInstallResourceWithStreamingResponse:
        return AsyncInstallResourceWithStreamingResponse(self._realtime.install)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._realtime.stats)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._realtime.status)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._realtime.subscriptions)
