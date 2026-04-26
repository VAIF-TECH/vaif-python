# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .event import (
    EventResource,
    AsyncEventResource,
    EventResourceWithRawResponse,
    AsyncEventResourceWithRawResponse,
    EventResourceWithStreamingResponse,
    AsyncEventResourceWithStreamingResponse,
)
from .retry import (
    RetryResource,
    AsyncRetryResource,
    RetryResourceWithRawResponse,
    AsyncRetryResourceWithRawResponse,
    RetryResourceWithStreamingResponse,
    AsyncRetryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .subscription import (
    SubscriptionResource,
    AsyncSubscriptionResource,
    SubscriptionResourceWithRawResponse,
    AsyncSubscriptionResourceWithRawResponse,
    SubscriptionResourceWithStreamingResponse,
    AsyncSubscriptionResourceWithStreamingResponse,
)

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    @cached_property
    def event(self) -> EventResource:
        return EventResource(self._client)

    @cached_property
    def retry(self) -> RetryResource:
        return RetryResource(self._client)

    @cached_property
    def subscription(self) -> SubscriptionResource:
        return SubscriptionResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)


class AsyncDeliveriesResource(AsyncAPIResource):
    @cached_property
    def event(self) -> AsyncEventResource:
        return AsyncEventResource(self._client)

    @cached_property
    def retry(self) -> AsyncRetryResource:
        return AsyncRetryResource(self._client)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        return AsyncSubscriptionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

    @cached_property
    def event(self) -> EventResourceWithRawResponse:
        return EventResourceWithRawResponse(self._deliveries.event)

    @cached_property
    def retry(self) -> RetryResourceWithRawResponse:
        return RetryResourceWithRawResponse(self._deliveries.retry)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithRawResponse:
        return SubscriptionResourceWithRawResponse(self._deliveries.subscription)


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

    @cached_property
    def event(self) -> AsyncEventResourceWithRawResponse:
        return AsyncEventResourceWithRawResponse(self._deliveries.event)

    @cached_property
    def retry(self) -> AsyncRetryResourceWithRawResponse:
        return AsyncRetryResourceWithRawResponse(self._deliveries.retry)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithRawResponse:
        return AsyncSubscriptionResourceWithRawResponse(self._deliveries.subscription)


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

    @cached_property
    def event(self) -> EventResourceWithStreamingResponse:
        return EventResourceWithStreamingResponse(self._deliveries.event)

    @cached_property
    def retry(self) -> RetryResourceWithStreamingResponse:
        return RetryResourceWithStreamingResponse(self._deliveries.retry)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithStreamingResponse:
        return SubscriptionResourceWithStreamingResponse(self._deliveries.subscription)


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

    @cached_property
    def event(self) -> AsyncEventResourceWithStreamingResponse:
        return AsyncEventResourceWithStreamingResponse(self._deliveries.event)

    @cached_property
    def retry(self) -> AsyncRetryResourceWithStreamingResponse:
        return AsyncRetryResourceWithStreamingResponse(self._deliveries.retry)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        return AsyncSubscriptionResourceWithStreamingResponse(self._deliveries.subscription)
