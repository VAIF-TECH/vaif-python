# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .copy import (
    CopyResource,
    AsyncCopyResource,
    CopyResourceWithRawResponse,
    AsyncCopyResourceWithRawResponse,
    CopyResourceWithStreamingResponse,
    AsyncCopyResourceWithStreamingResponse,
)
from .move import (
    MoveResource,
    AsyncMoveResource,
    MoveResourceWithRawResponse,
    AsyncMoveResourceWithRawResponse,
    MoveResourceWithStreamingResponse,
    AsyncMoveResourceWithStreamingResponse,
)
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .delete_batch import (
    DeleteBatchResource,
    AsyncDeleteBatchResource,
    DeleteBatchResourceWithRawResponse,
    AsyncDeleteBatchResourceWithRawResponse,
    DeleteBatchResourceWithStreamingResponse,
    AsyncDeleteBatchResourceWithStreamingResponse,
)

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def copy(self) -> CopyResource:
        return CopyResource(self._client)

    @cached_property
    def delete_batch(self) -> DeleteBatchResource:
        return DeleteBatchResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def move(self) -> MoveResource:
        return MoveResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def copy(self) -> AsyncCopyResource:
        return AsyncCopyResource(self._client)

    @cached_property
    def delete_batch(self) -> AsyncDeleteBatchResource:
        return AsyncDeleteBatchResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def move(self) -> AsyncMoveResource:
        return AsyncMoveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

    @cached_property
    def copy(self) -> CopyResourceWithRawResponse:
        return CopyResourceWithRawResponse(self._files.copy)

    @cached_property
    def delete_batch(self) -> DeleteBatchResourceWithRawResponse:
        return DeleteBatchResourceWithRawResponse(self._files.delete_batch)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._files.metadata)

    @cached_property
    def move(self) -> MoveResourceWithRawResponse:
        return MoveResourceWithRawResponse(self._files.move)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

    @cached_property
    def copy(self) -> AsyncCopyResourceWithRawResponse:
        return AsyncCopyResourceWithRawResponse(self._files.copy)

    @cached_property
    def delete_batch(self) -> AsyncDeleteBatchResourceWithRawResponse:
        return AsyncDeleteBatchResourceWithRawResponse(self._files.delete_batch)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._files.metadata)

    @cached_property
    def move(self) -> AsyncMoveResourceWithRawResponse:
        return AsyncMoveResourceWithRawResponse(self._files.move)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

    @cached_property
    def copy(self) -> CopyResourceWithStreamingResponse:
        return CopyResourceWithStreamingResponse(self._files.copy)

    @cached_property
    def delete_batch(self) -> DeleteBatchResourceWithStreamingResponse:
        return DeleteBatchResourceWithStreamingResponse(self._files.delete_batch)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._files.metadata)

    @cached_property
    def move(self) -> MoveResourceWithStreamingResponse:
        return MoveResourceWithStreamingResponse(self._files.move)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

    @cached_property
    def copy(self) -> AsyncCopyResourceWithStreamingResponse:
        return AsyncCopyResourceWithStreamingResponse(self._files.copy)

    @cached_property
    def delete_batch(self) -> AsyncDeleteBatchResourceWithStreamingResponse:
        return AsyncDeleteBatchResourceWithStreamingResponse(self._files.delete_batch)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._files.metadata)

    @cached_property
    def move(self) -> AsyncMoveResourceWithStreamingResponse:
        return AsyncMoveResourceWithStreamingResponse(self._files.move)
