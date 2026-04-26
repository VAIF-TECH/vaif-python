# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .rss import (
    RssResource,
    AsyncRssResource,
    RssResourceWithRawResponse,
    AsyncRssResourceWithRawResponse,
    RssResourceWithStreamingResponse,
    AsyncRssResourceWithStreamingResponse,
)
from .atom import (
    AtomResource,
    AsyncAtomResource,
    AtomResourceWithRawResponse,
    AsyncAtomResourceWithRawResponse,
    AtomResourceWithStreamingResponse,
    AsyncAtomResourceWithStreamingResponse,
)
from .uptime import (
    UptimeResource,
    AsyncUptimeResource,
    UptimeResourceWithRawResponse,
    AsyncUptimeResourceWithRawResponse,
    UptimeResourceWithStreamingResponse,
    AsyncUptimeResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from .incidents import (
    IncidentsResource,
    AsyncIncidentsResource,
    IncidentsResourceWithRawResponse,
    AsyncIncidentsResourceWithRawResponse,
    IncidentsResourceWithStreamingResponse,
    AsyncIncidentsResourceWithStreamingResponse,
)
from .subscribe import (
    SubscribeResource,
    AsyncSubscribeResource,
    SubscribeResourceWithRawResponse,
    AsyncSubscribeResourceWithRawResponse,
    SubscribeResourceWithStreamingResponse,
    AsyncSubscribeResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .unsubscribe import (
    UnsubscribeResource,
    AsyncUnsubscribeResource,
    UnsubscribeResourceWithRawResponse,
    AsyncUnsubscribeResourceWithRawResponse,
    UnsubscribeResourceWithStreamingResponse,
    AsyncUnsubscribeResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .subscribers.subscribers import (
    SubscribersResource,
    AsyncSubscribersResource,
    SubscribersResourceWithRawResponse,
    AsyncSubscribersResourceWithRawResponse,
    SubscribersResourceWithStreamingResponse,
    AsyncSubscribersResourceWithStreamingResponse,
)

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    @cached_property
    def atom(self) -> AtomResource:
        return AtomResource(self._client)

    @cached_property
    def incidents(self) -> IncidentsResource:
        return IncidentsResource(self._client)

    @cached_property
    def rss(self) -> RssResource:
        return RssResource(self._client)

    @cached_property
    def subscribe(self) -> SubscribeResource:
        return SubscribeResource(self._client)

    @cached_property
    def subscribers(self) -> SubscribersResource:
        return SubscribersResource(self._client)

    @cached_property
    def unsubscribe(self) -> UnsubscribeResource:
        return UnsubscribeResource(self._client)

    @cached_property
    def uptime(self) -> UptimeResource:
        return UptimeResource(self._client)

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get platform status"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncStatusResource(AsyncAPIResource):
    @cached_property
    def atom(self) -> AsyncAtomResource:
        return AsyncAtomResource(self._client)

    @cached_property
    def incidents(self) -> AsyncIncidentsResource:
        return AsyncIncidentsResource(self._client)

    @cached_property
    def rss(self) -> AsyncRssResource:
        return AsyncRssResource(self._client)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResource:
        return AsyncSubscribeResource(self._client)

    @cached_property
    def subscribers(self) -> AsyncSubscribersResource:
        return AsyncSubscribersResource(self._client)

    @cached_property
    def unsubscribe(self) -> AsyncUnsubscribeResource:
        return AsyncUnsubscribeResource(self._client)

    @cached_property
    def uptime(self) -> AsyncUptimeResource:
        return AsyncUptimeResource(self._client)

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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get platform status"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class StatusResourceWithRawResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.list = to_raw_response_wrapper(
            status.list,
        )

    @cached_property
    def atom(self) -> AtomResourceWithRawResponse:
        return AtomResourceWithRawResponse(self._status.atom)

    @cached_property
    def incidents(self) -> IncidentsResourceWithRawResponse:
        return IncidentsResourceWithRawResponse(self._status.incidents)

    @cached_property
    def rss(self) -> RssResourceWithRawResponse:
        return RssResourceWithRawResponse(self._status.rss)

    @cached_property
    def subscribe(self) -> SubscribeResourceWithRawResponse:
        return SubscribeResourceWithRawResponse(self._status.subscribe)

    @cached_property
    def subscribers(self) -> SubscribersResourceWithRawResponse:
        return SubscribersResourceWithRawResponse(self._status.subscribers)

    @cached_property
    def unsubscribe(self) -> UnsubscribeResourceWithRawResponse:
        return UnsubscribeResourceWithRawResponse(self._status.unsubscribe)

    @cached_property
    def uptime(self) -> UptimeResourceWithRawResponse:
        return UptimeResourceWithRawResponse(self._status.uptime)


class AsyncStatusResourceWithRawResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.list = async_to_raw_response_wrapper(
            status.list,
        )

    @cached_property
    def atom(self) -> AsyncAtomResourceWithRawResponse:
        return AsyncAtomResourceWithRawResponse(self._status.atom)

    @cached_property
    def incidents(self) -> AsyncIncidentsResourceWithRawResponse:
        return AsyncIncidentsResourceWithRawResponse(self._status.incidents)

    @cached_property
    def rss(self) -> AsyncRssResourceWithRawResponse:
        return AsyncRssResourceWithRawResponse(self._status.rss)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResourceWithRawResponse:
        return AsyncSubscribeResourceWithRawResponse(self._status.subscribe)

    @cached_property
    def subscribers(self) -> AsyncSubscribersResourceWithRawResponse:
        return AsyncSubscribersResourceWithRawResponse(self._status.subscribers)

    @cached_property
    def unsubscribe(self) -> AsyncUnsubscribeResourceWithRawResponse:
        return AsyncUnsubscribeResourceWithRawResponse(self._status.unsubscribe)

    @cached_property
    def uptime(self) -> AsyncUptimeResourceWithRawResponse:
        return AsyncUptimeResourceWithRawResponse(self._status.uptime)


class StatusResourceWithStreamingResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.list = to_streamed_response_wrapper(
            status.list,
        )

    @cached_property
    def atom(self) -> AtomResourceWithStreamingResponse:
        return AtomResourceWithStreamingResponse(self._status.atom)

    @cached_property
    def incidents(self) -> IncidentsResourceWithStreamingResponse:
        return IncidentsResourceWithStreamingResponse(self._status.incidents)

    @cached_property
    def rss(self) -> RssResourceWithStreamingResponse:
        return RssResourceWithStreamingResponse(self._status.rss)

    @cached_property
    def subscribe(self) -> SubscribeResourceWithStreamingResponse:
        return SubscribeResourceWithStreamingResponse(self._status.subscribe)

    @cached_property
    def subscribers(self) -> SubscribersResourceWithStreamingResponse:
        return SubscribersResourceWithStreamingResponse(self._status.subscribers)

    @cached_property
    def unsubscribe(self) -> UnsubscribeResourceWithStreamingResponse:
        return UnsubscribeResourceWithStreamingResponse(self._status.unsubscribe)

    @cached_property
    def uptime(self) -> UptimeResourceWithStreamingResponse:
        return UptimeResourceWithStreamingResponse(self._status.uptime)


class AsyncStatusResourceWithStreamingResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.list = async_to_streamed_response_wrapper(
            status.list,
        )

    @cached_property
    def atom(self) -> AsyncAtomResourceWithStreamingResponse:
        return AsyncAtomResourceWithStreamingResponse(self._status.atom)

    @cached_property
    def incidents(self) -> AsyncIncidentsResourceWithStreamingResponse:
        return AsyncIncidentsResourceWithStreamingResponse(self._status.incidents)

    @cached_property
    def rss(self) -> AsyncRssResourceWithStreamingResponse:
        return AsyncRssResourceWithStreamingResponse(self._status.rss)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResourceWithStreamingResponse:
        return AsyncSubscribeResourceWithStreamingResponse(self._status.subscribe)

    @cached_property
    def subscribers(self) -> AsyncSubscribersResourceWithStreamingResponse:
        return AsyncSubscribersResourceWithStreamingResponse(self._status.subscribers)

    @cached_property
    def unsubscribe(self) -> AsyncUnsubscribeResourceWithStreamingResponse:
        return AsyncUnsubscribeResourceWithStreamingResponse(self._status.unsubscribe)

    @cached_property
    def uptime(self) -> AsyncUptimeResourceWithStreamingResponse:
        return AsyncUptimeResourceWithStreamingResponse(self._status.uptime)
