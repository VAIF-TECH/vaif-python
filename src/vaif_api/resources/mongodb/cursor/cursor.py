# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .next import (
    NextResource,
    AsyncNextResource,
    NextResourceWithRawResponse,
    AsyncNextResourceWithRawResponse,
    NextResourceWithStreamingResponse,
    AsyncNextResourceWithStreamingResponse,
)
from .close import (
    CloseResource,
    AsyncCloseResource,
    CloseResourceWithRawResponse,
    AsyncCloseResourceWithRawResponse,
    CloseResourceWithStreamingResponse,
    AsyncCloseResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CursorResource", "AsyncCursorResource"]


class CursorResource(SyncAPIResource):
    @cached_property
    def close(self) -> CloseResource:
        return CloseResource(self._client)

    @cached_property
    def next(self) -> NextResource:
        return NextResource(self._client)

    @cached_property
    def with_raw_response(self) -> CursorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CursorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CursorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CursorResourceWithStreamingResponse(self)


class AsyncCursorResource(AsyncAPIResource):
    @cached_property
    def close(self) -> AsyncCloseResource:
        return AsyncCloseResource(self._client)

    @cached_property
    def next(self) -> AsyncNextResource:
        return AsyncNextResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCursorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCursorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCursorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCursorResourceWithStreamingResponse(self)


class CursorResourceWithRawResponse:
    def __init__(self, cursor: CursorResource) -> None:
        self._cursor = cursor

    @cached_property
    def close(self) -> CloseResourceWithRawResponse:
        return CloseResourceWithRawResponse(self._cursor.close)

    @cached_property
    def next(self) -> NextResourceWithRawResponse:
        return NextResourceWithRawResponse(self._cursor.next)


class AsyncCursorResourceWithRawResponse:
    def __init__(self, cursor: AsyncCursorResource) -> None:
        self._cursor = cursor

    @cached_property
    def close(self) -> AsyncCloseResourceWithRawResponse:
        return AsyncCloseResourceWithRawResponse(self._cursor.close)

    @cached_property
    def next(self) -> AsyncNextResourceWithRawResponse:
        return AsyncNextResourceWithRawResponse(self._cursor.next)


class CursorResourceWithStreamingResponse:
    def __init__(self, cursor: CursorResource) -> None:
        self._cursor = cursor

    @cached_property
    def close(self) -> CloseResourceWithStreamingResponse:
        return CloseResourceWithStreamingResponse(self._cursor.close)

    @cached_property
    def next(self) -> NextResourceWithStreamingResponse:
        return NextResourceWithStreamingResponse(self._cursor.next)


class AsyncCursorResourceWithStreamingResponse:
    def __init__(self, cursor: AsyncCursorResource) -> None:
        self._cursor = cursor

    @cached_property
    def close(self) -> AsyncCloseResourceWithStreamingResponse:
        return AsyncCloseResourceWithStreamingResponse(self._cursor.close)

    @cached_property
    def next(self) -> AsyncNextResourceWithStreamingResponse:
        return AsyncNextResourceWithStreamingResponse(self._cursor.next)
