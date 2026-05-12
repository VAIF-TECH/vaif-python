# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .upload import (
    UploadResource,
    AsyncUploadResource,
    UploadResourceWithRawResponse,
    AsyncUploadResourceWithRawResponse,
    UploadResourceWithStreamingResponse,
    AsyncUploadResourceWithStreamingResponse,
)
from .download import (
    DownloadResource,
    AsyncDownloadResource,
    DownloadResourceWithRawResponse,
    AsyncDownloadResourceWithRawResponse,
    DownloadResourceWithStreamingResponse,
    AsyncDownloadResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .upload_url import (
    UploadURLResource,
    AsyncUploadURLResource,
    UploadURLResourceWithRawResponse,
    AsyncUploadURLResourceWithRawResponse,
    UploadURLResourceWithStreamingResponse,
    AsyncUploadURLResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .files.files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .download_url import (
    DownloadURLResource,
    AsyncDownloadURLResource,
    DownloadURLResourceWithRawResponse,
    AsyncDownloadURLResourceWithRawResponse,
    DownloadURLResourceWithStreamingResponse,
    AsyncDownloadURLResourceWithStreamingResponse,
)
from .upload_base64 import (
    UploadBase64Resource,
    AsyncUploadBase64Resource,
    UploadBase64ResourceWithRawResponse,
    AsyncUploadBase64ResourceWithRawResponse,
    UploadBase64ResourceWithStreamingResponse,
    AsyncUploadBase64ResourceWithStreamingResponse,
)
from .buckets.buckets import (
    BucketsResource,
    AsyncBucketsResource,
    BucketsResourceWithRawResponse,
    AsyncBucketsResourceWithRawResponse,
    BucketsResourceWithStreamingResponse,
    AsyncBucketsResourceWithStreamingResponse,
)
from .upload_from_url import (
    UploadFromURLResource,
    AsyncUploadFromURLResource,
    UploadFromURLResourceWithRawResponse,
    AsyncUploadFromURLResourceWithRawResponse,
    UploadFromURLResourceWithStreamingResponse,
    AsyncUploadFromURLResourceWithStreamingResponse,
)
from .multipart.multipart import (
    MultipartResource,
    AsyncMultipartResource,
    MultipartResourceWithRawResponse,
    AsyncMultipartResourceWithRawResponse,
    MultipartResourceWithStreamingResponse,
    AsyncMultipartResourceWithStreamingResponse,
)

__all__ = ["StorageResource", "AsyncStorageResource"]


class StorageResource(SyncAPIResource):
    @cached_property
    def buckets(self) -> BucketsResource:
        return BucketsResource(self._client)

    @cached_property
    def download(self) -> DownloadResource:
        return DownloadResource(self._client)

    @cached_property
    def download_url(self) -> DownloadURLResource:
        return DownloadURLResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def multipart(self) -> MultipartResource:
        return MultipartResource(self._client)

    @cached_property
    def upload(self) -> UploadResource:
        return UploadResource(self._client)

    @cached_property
    def upload_base64(self) -> UploadBase64Resource:
        return UploadBase64Resource(self._client)

    @cached_property
    def upload_from_url(self) -> UploadFromURLResource:
        return UploadFromURLResource(self._client)

    @cached_property
    def upload_url(self) -> UploadURLResource:
        return UploadURLResource(self._client)

    @cached_property
    def with_raw_response(self) -> StorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return StorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return StorageResourceWithStreamingResponse(self)


class AsyncStorageResource(AsyncAPIResource):
    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        return AsyncBucketsResource(self._client)

    @cached_property
    def download(self) -> AsyncDownloadResource:
        return AsyncDownloadResource(self._client)

    @cached_property
    def download_url(self) -> AsyncDownloadURLResource:
        return AsyncDownloadURLResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def multipart(self) -> AsyncMultipartResource:
        return AsyncMultipartResource(self._client)

    @cached_property
    def upload(self) -> AsyncUploadResource:
        return AsyncUploadResource(self._client)

    @cached_property
    def upload_base64(self) -> AsyncUploadBase64Resource:
        return AsyncUploadBase64Resource(self._client)

    @cached_property
    def upload_from_url(self) -> AsyncUploadFromURLResource:
        return AsyncUploadFromURLResource(self._client)

    @cached_property
    def upload_url(self) -> AsyncUploadURLResource:
        return AsyncUploadURLResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncStorageResourceWithStreamingResponse(self)


class StorageResourceWithRawResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

    @cached_property
    def buckets(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self._storage.buckets)

    @cached_property
    def download(self) -> DownloadResourceWithRawResponse:
        return DownloadResourceWithRawResponse(self._storage.download)

    @cached_property
    def download_url(self) -> DownloadURLResourceWithRawResponse:
        return DownloadURLResourceWithRawResponse(self._storage.download_url)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._storage.files)

    @cached_property
    def multipart(self) -> MultipartResourceWithRawResponse:
        return MultipartResourceWithRawResponse(self._storage.multipart)

    @cached_property
    def upload(self) -> UploadResourceWithRawResponse:
        return UploadResourceWithRawResponse(self._storage.upload)

    @cached_property
    def upload_base64(self) -> UploadBase64ResourceWithRawResponse:
        return UploadBase64ResourceWithRawResponse(self._storage.upload_base64)

    @cached_property
    def upload_from_url(self) -> UploadFromURLResourceWithRawResponse:
        return UploadFromURLResourceWithRawResponse(self._storage.upload_from_url)

    @cached_property
    def upload_url(self) -> UploadURLResourceWithRawResponse:
        return UploadURLResourceWithRawResponse(self._storage.upload_url)


class AsyncStorageResourceWithRawResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self._storage.buckets)

    @cached_property
    def download(self) -> AsyncDownloadResourceWithRawResponse:
        return AsyncDownloadResourceWithRawResponse(self._storage.download)

    @cached_property
    def download_url(self) -> AsyncDownloadURLResourceWithRawResponse:
        return AsyncDownloadURLResourceWithRawResponse(self._storage.download_url)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._storage.files)

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithRawResponse:
        return AsyncMultipartResourceWithRawResponse(self._storage.multipart)

    @cached_property
    def upload(self) -> AsyncUploadResourceWithRawResponse:
        return AsyncUploadResourceWithRawResponse(self._storage.upload)

    @cached_property
    def upload_base64(self) -> AsyncUploadBase64ResourceWithRawResponse:
        return AsyncUploadBase64ResourceWithRawResponse(self._storage.upload_base64)

    @cached_property
    def upload_from_url(self) -> AsyncUploadFromURLResourceWithRawResponse:
        return AsyncUploadFromURLResourceWithRawResponse(self._storage.upload_from_url)

    @cached_property
    def upload_url(self) -> AsyncUploadURLResourceWithRawResponse:
        return AsyncUploadURLResourceWithRawResponse(self._storage.upload_url)


class StorageResourceWithStreamingResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

    @cached_property
    def buckets(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self._storage.buckets)

    @cached_property
    def download(self) -> DownloadResourceWithStreamingResponse:
        return DownloadResourceWithStreamingResponse(self._storage.download)

    @cached_property
    def download_url(self) -> DownloadURLResourceWithStreamingResponse:
        return DownloadURLResourceWithStreamingResponse(self._storage.download_url)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._storage.files)

    @cached_property
    def multipart(self) -> MultipartResourceWithStreamingResponse:
        return MultipartResourceWithStreamingResponse(self._storage.multipart)

    @cached_property
    def upload(self) -> UploadResourceWithStreamingResponse:
        return UploadResourceWithStreamingResponse(self._storage.upload)

    @cached_property
    def upload_base64(self) -> UploadBase64ResourceWithStreamingResponse:
        return UploadBase64ResourceWithStreamingResponse(self._storage.upload_base64)

    @cached_property
    def upload_from_url(self) -> UploadFromURLResourceWithStreamingResponse:
        return UploadFromURLResourceWithStreamingResponse(self._storage.upload_from_url)

    @cached_property
    def upload_url(self) -> UploadURLResourceWithStreamingResponse:
        return UploadURLResourceWithStreamingResponse(self._storage.upload_url)


class AsyncStorageResourceWithStreamingResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self._storage.buckets)

    @cached_property
    def download(self) -> AsyncDownloadResourceWithStreamingResponse:
        return AsyncDownloadResourceWithStreamingResponse(self._storage.download)

    @cached_property
    def download_url(self) -> AsyncDownloadURLResourceWithStreamingResponse:
        return AsyncDownloadURLResourceWithStreamingResponse(self._storage.download_url)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._storage.files)

    @cached_property
    def multipart(self) -> AsyncMultipartResourceWithStreamingResponse:
        return AsyncMultipartResourceWithStreamingResponse(self._storage.multipart)

    @cached_property
    def upload(self) -> AsyncUploadResourceWithStreamingResponse:
        return AsyncUploadResourceWithStreamingResponse(self._storage.upload)

    @cached_property
    def upload_base64(self) -> AsyncUploadBase64ResourceWithStreamingResponse:
        return AsyncUploadBase64ResourceWithStreamingResponse(self._storage.upload_base64)

    @cached_property
    def upload_from_url(self) -> AsyncUploadFromURLResourceWithStreamingResponse:
        return AsyncUploadFromURLResourceWithStreamingResponse(self._storage.upload_from_url)

    @cached_property
    def upload_url(self) -> AsyncUploadURLResourceWithStreamingResponse:
        return AsyncUploadURLResourceWithStreamingResponse(self._storage.upload_url)
