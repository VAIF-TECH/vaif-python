# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .count import (
    CountResource,
    AsyncCountResource,
    CountResourceWithRawResponse,
    AsyncCountResourceWithRawResponse,
    CountResourceWithStreamingResponse,
    AsyncCountResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SubscribersResource", "AsyncSubscribersResource"]


class SubscribersResource(SyncAPIResource):
    @cached_property
    def count(self) -> CountResource:
        return CountResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubscribersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SubscribersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscribersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SubscribersResourceWithStreamingResponse(self)


class AsyncSubscribersResource(AsyncAPIResource):
    @cached_property
    def count(self) -> AsyncCountResource:
        return AsyncCountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubscribersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscribersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscribersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSubscribersResourceWithStreamingResponse(self)


class SubscribersResourceWithRawResponse:
    def __init__(self, subscribers: SubscribersResource) -> None:
        self._subscribers = subscribers

    @cached_property
    def count(self) -> CountResourceWithRawResponse:
        return CountResourceWithRawResponse(self._subscribers.count)


class AsyncSubscribersResourceWithRawResponse:
    def __init__(self, subscribers: AsyncSubscribersResource) -> None:
        self._subscribers = subscribers

    @cached_property
    def count(self) -> AsyncCountResourceWithRawResponse:
        return AsyncCountResourceWithRawResponse(self._subscribers.count)


class SubscribersResourceWithStreamingResponse:
    def __init__(self, subscribers: SubscribersResource) -> None:
        self._subscribers = subscribers

    @cached_property
    def count(self) -> CountResourceWithStreamingResponse:
        return CountResourceWithStreamingResponse(self._subscribers.count)


class AsyncSubscribersResourceWithStreamingResponse:
    def __init__(self, subscribers: AsyncSubscribersResource) -> None:
        self._subscribers = subscribers

    @cached_property
    def count(self) -> AsyncCountResourceWithStreamingResponse:
        return AsyncCountResourceWithStreamingResponse(self._subscribers.count)
