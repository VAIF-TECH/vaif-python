# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sizes import (
    SizesResource,
    AsyncSizesResource,
    SizesResourceWithRawResponse,
    AsyncSizesResourceWithRawResponse,
    SizesResourceWithStreamingResponse,
    AsyncSizesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .poll_status import (
    PollStatusResource,
    AsyncPollStatusResource,
    PollStatusResourceWithRawResponse,
    AsyncPollStatusResourceWithRawResponse,
    PollStatusResourceWithStreamingResponse,
    AsyncPollStatusResourceWithStreamingResponse,
)

__all__ = ["InfrastructureResource", "AsyncInfrastructureResource"]


class InfrastructureResource(SyncAPIResource):
    @cached_property
    def poll_status(self) -> PollStatusResource:
        return PollStatusResource(self._client)

    @cached_property
    def sizes(self) -> SizesResource:
        return SizesResource(self._client)

    @cached_property
    def with_raw_response(self) -> InfrastructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return InfrastructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfrastructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return InfrastructureResourceWithStreamingResponse(self)


class AsyncInfrastructureResource(AsyncAPIResource):
    @cached_property
    def poll_status(self) -> AsyncPollStatusResource:
        return AsyncPollStatusResource(self._client)

    @cached_property
    def sizes(self) -> AsyncSizesResource:
        return AsyncSizesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInfrastructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfrastructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfrastructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncInfrastructureResourceWithStreamingResponse(self)


class InfrastructureResourceWithRawResponse:
    def __init__(self, infrastructure: InfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def poll_status(self) -> PollStatusResourceWithRawResponse:
        return PollStatusResourceWithRawResponse(self._infrastructure.poll_status)

    @cached_property
    def sizes(self) -> SizesResourceWithRawResponse:
        return SizesResourceWithRawResponse(self._infrastructure.sizes)


class AsyncInfrastructureResourceWithRawResponse:
    def __init__(self, infrastructure: AsyncInfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def poll_status(self) -> AsyncPollStatusResourceWithRawResponse:
        return AsyncPollStatusResourceWithRawResponse(self._infrastructure.poll_status)

    @cached_property
    def sizes(self) -> AsyncSizesResourceWithRawResponse:
        return AsyncSizesResourceWithRawResponse(self._infrastructure.sizes)


class InfrastructureResourceWithStreamingResponse:
    def __init__(self, infrastructure: InfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def poll_status(self) -> PollStatusResourceWithStreamingResponse:
        return PollStatusResourceWithStreamingResponse(self._infrastructure.poll_status)

    @cached_property
    def sizes(self) -> SizesResourceWithStreamingResponse:
        return SizesResourceWithStreamingResponse(self._infrastructure.sizes)


class AsyncInfrastructureResourceWithStreamingResponse:
    def __init__(self, infrastructure: AsyncInfrastructureResource) -> None:
        self._infrastructure = infrastructure

    @cached_property
    def poll_status(self) -> AsyncPollStatusResourceWithStreamingResponse:
        return AsyncPollStatusResourceWithStreamingResponse(self._infrastructure.poll_status)

    @cached_property
    def sizes(self) -> AsyncSizesResourceWithStreamingResponse:
        return AsyncSizesResourceWithStreamingResponse(self._infrastructure.sizes)
