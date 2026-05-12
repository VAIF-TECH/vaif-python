# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .abort import (
    AbortResource,
    AsyncAbortResource,
    AbortResourceWithRawResponse,
    AsyncAbortResourceWithRawResponse,
    AbortResourceWithStreamingResponse,
    AsyncAbortResourceWithStreamingResponse,
)
from .create import (
    CreateResource,
    AsyncCreateResource,
    CreateResourceWithRawResponse,
    AsyncCreateResourceWithRawResponse,
    CreateResourceWithStreamingResponse,
    AsyncCreateResourceWithStreamingResponse,
)
from .complete import (
    CompleteResource,
    AsyncCompleteResource,
    CompleteResourceWithRawResponse,
    AsyncCompleteResourceWithRawResponse,
    CompleteResourceWithStreamingResponse,
    AsyncCompleteResourceWithStreamingResponse,
)
from .part_url import (
    PartURLResource,
    AsyncPartURLResource,
    PartURLResourceWithRawResponse,
    AsyncPartURLResourceWithRawResponse,
    PartURLResourceWithStreamingResponse,
    AsyncPartURLResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MultipartResource", "AsyncMultipartResource"]


class MultipartResource(SyncAPIResource):
    @cached_property
    def abort(self) -> AbortResource:
        return AbortResource(self._client)

    @cached_property
    def complete(self) -> CompleteResource:
        return CompleteResource(self._client)

    @cached_property
    def create(self) -> CreateResource:
        return CreateResource(self._client)

    @cached_property
    def part_url(self) -> PartURLResource:
        return PartURLResource(self._client)

    @cached_property
    def with_raw_response(self) -> MultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return MultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return MultipartResourceWithStreamingResponse(self)


class AsyncMultipartResource(AsyncAPIResource):
    @cached_property
    def abort(self) -> AsyncAbortResource:
        return AsyncAbortResource(self._client)

    @cached_property
    def complete(self) -> AsyncCompleteResource:
        return AsyncCompleteResource(self._client)

    @cached_property
    def create(self) -> AsyncCreateResource:
        return AsyncCreateResource(self._client)

    @cached_property
    def part_url(self) -> AsyncPartURLResource:
        return AsyncPartURLResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMultipartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMultipartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultipartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncMultipartResourceWithStreamingResponse(self)


class MultipartResourceWithRawResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

    @cached_property
    def abort(self) -> AbortResourceWithRawResponse:
        return AbortResourceWithRawResponse(self._multipart.abort)

    @cached_property
    def complete(self) -> CompleteResourceWithRawResponse:
        return CompleteResourceWithRawResponse(self._multipart.complete)

    @cached_property
    def create(self) -> CreateResourceWithRawResponse:
        return CreateResourceWithRawResponse(self._multipart.create)

    @cached_property
    def part_url(self) -> PartURLResourceWithRawResponse:
        return PartURLResourceWithRawResponse(self._multipart.part_url)


class AsyncMultipartResourceWithRawResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

    @cached_property
    def abort(self) -> AsyncAbortResourceWithRawResponse:
        return AsyncAbortResourceWithRawResponse(self._multipart.abort)

    @cached_property
    def complete(self) -> AsyncCompleteResourceWithRawResponse:
        return AsyncCompleteResourceWithRawResponse(self._multipart.complete)

    @cached_property
    def create(self) -> AsyncCreateResourceWithRawResponse:
        return AsyncCreateResourceWithRawResponse(self._multipart.create)

    @cached_property
    def part_url(self) -> AsyncPartURLResourceWithRawResponse:
        return AsyncPartURLResourceWithRawResponse(self._multipart.part_url)


class MultipartResourceWithStreamingResponse:
    def __init__(self, multipart: MultipartResource) -> None:
        self._multipart = multipart

    @cached_property
    def abort(self) -> AbortResourceWithStreamingResponse:
        return AbortResourceWithStreamingResponse(self._multipart.abort)

    @cached_property
    def complete(self) -> CompleteResourceWithStreamingResponse:
        return CompleteResourceWithStreamingResponse(self._multipart.complete)

    @cached_property
    def create(self) -> CreateResourceWithStreamingResponse:
        return CreateResourceWithStreamingResponse(self._multipart.create)

    @cached_property
    def part_url(self) -> PartURLResourceWithStreamingResponse:
        return PartURLResourceWithStreamingResponse(self._multipart.part_url)


class AsyncMultipartResourceWithStreamingResponse:
    def __init__(self, multipart: AsyncMultipartResource) -> None:
        self._multipart = multipart

    @cached_property
    def abort(self) -> AsyncAbortResourceWithStreamingResponse:
        return AsyncAbortResourceWithStreamingResponse(self._multipart.abort)

    @cached_property
    def complete(self) -> AsyncCompleteResourceWithStreamingResponse:
        return AsyncCompleteResourceWithStreamingResponse(self._multipart.complete)

    @cached_property
    def create(self) -> AsyncCreateResourceWithStreamingResponse:
        return AsyncCreateResourceWithStreamingResponse(self._multipart.create)

    @cached_property
    def part_url(self) -> AsyncPartURLResourceWithStreamingResponse:
        return AsyncPartURLResourceWithStreamingResponse(self._multipart.part_url)
