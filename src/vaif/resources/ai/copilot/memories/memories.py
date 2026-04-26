# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .promote import (
    PromoteResource,
    AsyncPromoteResource,
    PromoteResourceWithRawResponse,
    AsyncPromoteResourceWithRawResponse,
    PromoteResourceWithStreamingResponse,
    AsyncPromoteResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    @cached_property
    def promote(self) -> PromoteResource:
        return PromoteResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)


class AsyncMemoriesResource(AsyncAPIResource):
    @cached_property
    def promote(self) -> AsyncPromoteResource:
        return AsyncPromoteResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

    @cached_property
    def promote(self) -> PromoteResourceWithRawResponse:
        return PromoteResourceWithRawResponse(self._memories.promote)


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

    @cached_property
    def promote(self) -> AsyncPromoteResourceWithRawResponse:
        return AsyncPromoteResourceWithRawResponse(self._memories.promote)


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

    @cached_property
    def promote(self) -> PromoteResourceWithStreamingResponse:
        return PromoteResourceWithStreamingResponse(self._memories.promote)


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

    @cached_property
    def promote(self) -> AsyncPromoteResourceWithStreamingResponse:
        return AsyncPromoteResourceWithStreamingResponse(self._memories.promote)
