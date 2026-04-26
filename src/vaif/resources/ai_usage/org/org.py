# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .recent import (
    RecentResource,
    AsyncRecentResource,
    RecentResourceWithRawResponse,
    AsyncRecentResourceWithRawResponse,
    RecentResourceWithStreamingResponse,
    AsyncRecentResourceWithStreamingResponse,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from .rollups import (
    RollupsResource,
    AsyncRollupsResource,
    RollupsResourceWithRawResponse,
    AsyncRollupsResourceWithRawResponse,
    RollupsResourceWithStreamingResponse,
    AsyncRollupsResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from .breakdown import (
    BreakdownResource,
    AsyncBreakdownResource,
    BreakdownResourceWithRawResponse,
    AsyncBreakdownResourceWithRawResponse,
    BreakdownResourceWithStreamingResponse,
    AsyncBreakdownResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .exhaustion_events import (
    ExhaustionEventsResource,
    AsyncExhaustionEventsResource,
    ExhaustionEventsResourceWithRawResponse,
    AsyncExhaustionEventsResourceWithRawResponse,
    ExhaustionEventsResourceWithStreamingResponse,
    AsyncExhaustionEventsResourceWithStreamingResponse,
)

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def breakdown(self) -> BreakdownResource:
        return BreakdownResource(self._client)

    @cached_property
    def exhaustion_events(self) -> ExhaustionEventsResource:
        return ExhaustionEventsResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def recent(self) -> RecentResource:
        return RecentResource(self._client)

    @cached_property
    def rollups(self) -> RollupsResource:
        return RollupsResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def breakdown(self) -> AsyncBreakdownResource:
        return AsyncBreakdownResource(self._client)

    @cached_property
    def exhaustion_events(self) -> AsyncExhaustionEventsResource:
        return AsyncExhaustionEventsResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def recent(self) -> AsyncRecentResource:
        return AsyncRecentResource(self._client)

    @cached_property
    def rollups(self) -> AsyncRollupsResource:
        return AsyncRollupsResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def breakdown(self) -> BreakdownResourceWithRawResponse:
        return BreakdownResourceWithRawResponse(self._org.breakdown)

    @cached_property
    def exhaustion_events(self) -> ExhaustionEventsResourceWithRawResponse:
        return ExhaustionEventsResourceWithRawResponse(self._org.exhaustion_events)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._org.history)

    @cached_property
    def recent(self) -> RecentResourceWithRawResponse:
        return RecentResourceWithRawResponse(self._org.recent)

    @cached_property
    def rollups(self) -> RollupsResourceWithRawResponse:
        return RollupsResourceWithRawResponse(self._org.rollups)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._org.summary)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def breakdown(self) -> AsyncBreakdownResourceWithRawResponse:
        return AsyncBreakdownResourceWithRawResponse(self._org.breakdown)

    @cached_property
    def exhaustion_events(self) -> AsyncExhaustionEventsResourceWithRawResponse:
        return AsyncExhaustionEventsResourceWithRawResponse(self._org.exhaustion_events)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._org.history)

    @cached_property
    def recent(self) -> AsyncRecentResourceWithRawResponse:
        return AsyncRecentResourceWithRawResponse(self._org.recent)

    @cached_property
    def rollups(self) -> AsyncRollupsResourceWithRawResponse:
        return AsyncRollupsResourceWithRawResponse(self._org.rollups)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._org.summary)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def breakdown(self) -> BreakdownResourceWithStreamingResponse:
        return BreakdownResourceWithStreamingResponse(self._org.breakdown)

    @cached_property
    def exhaustion_events(self) -> ExhaustionEventsResourceWithStreamingResponse:
        return ExhaustionEventsResourceWithStreamingResponse(self._org.exhaustion_events)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._org.history)

    @cached_property
    def recent(self) -> RecentResourceWithStreamingResponse:
        return RecentResourceWithStreamingResponse(self._org.recent)

    @cached_property
    def rollups(self) -> RollupsResourceWithStreamingResponse:
        return RollupsResourceWithStreamingResponse(self._org.rollups)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._org.summary)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def breakdown(self) -> AsyncBreakdownResourceWithStreamingResponse:
        return AsyncBreakdownResourceWithStreamingResponse(self._org.breakdown)

    @cached_property
    def exhaustion_events(self) -> AsyncExhaustionEventsResourceWithStreamingResponse:
        return AsyncExhaustionEventsResourceWithStreamingResponse(self._org.exhaustion_events)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._org.history)

    @cached_property
    def recent(self) -> AsyncRecentResourceWithStreamingResponse:
        return AsyncRecentResourceWithStreamingResponse(self._org.recent)

    @cached_property
    def rollups(self) -> AsyncRollupsResourceWithStreamingResponse:
        return AsyncRollupsResourceWithStreamingResponse(self._org.rollups)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._org.summary)
