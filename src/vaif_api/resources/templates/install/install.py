# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .apply import (
    ApplyResource,
    AsyncApplyResource,
    ApplyResourceWithRawResponse,
    AsyncApplyResourceWithRawResponse,
    ApplyResourceWithStreamingResponse,
    AsyncApplyResourceWithStreamingResponse,
)
from .preview import (
    PreviewResource,
    AsyncPreviewResource,
    PreviewResourceWithRawResponse,
    AsyncPreviewResourceWithRawResponse,
    PreviewResourceWithStreamingResponse,
    AsyncPreviewResourceWithStreamingResponse,
)
from .rollback import (
    RollbackResource,
    AsyncRollbackResource,
    RollbackResourceWithRawResponse,
    AsyncRollbackResourceWithRawResponse,
    RollbackResourceWithStreamingResponse,
    AsyncRollbackResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InstallResource", "AsyncInstallResource"]


class InstallResource(SyncAPIResource):
    @cached_property
    def apply(self) -> ApplyResource:
        return ApplyResource(self._client)

    @cached_property
    def preview(self) -> PreviewResource:
        return PreviewResource(self._client)

    @cached_property
    def rollback(self) -> RollbackResource:
        return RollbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return InstallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return InstallResourceWithStreamingResponse(self)


class AsyncInstallResource(AsyncAPIResource):
    @cached_property
    def apply(self) -> AsyncApplyResource:
        return AsyncApplyResource(self._client)

    @cached_property
    def preview(self) -> AsyncPreviewResource:
        return AsyncPreviewResource(self._client)

    @cached_property
    def rollback(self) -> AsyncRollbackResource:
        return AsyncRollbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncInstallResourceWithStreamingResponse(self)


class InstallResourceWithRawResponse:
    def __init__(self, install: InstallResource) -> None:
        self._install = install

    @cached_property
    def apply(self) -> ApplyResourceWithRawResponse:
        return ApplyResourceWithRawResponse(self._install.apply)

    @cached_property
    def preview(self) -> PreviewResourceWithRawResponse:
        return PreviewResourceWithRawResponse(self._install.preview)

    @cached_property
    def rollback(self) -> RollbackResourceWithRawResponse:
        return RollbackResourceWithRawResponse(self._install.rollback)


class AsyncInstallResourceWithRawResponse:
    def __init__(self, install: AsyncInstallResource) -> None:
        self._install = install

    @cached_property
    def apply(self) -> AsyncApplyResourceWithRawResponse:
        return AsyncApplyResourceWithRawResponse(self._install.apply)

    @cached_property
    def preview(self) -> AsyncPreviewResourceWithRawResponse:
        return AsyncPreviewResourceWithRawResponse(self._install.preview)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithRawResponse:
        return AsyncRollbackResourceWithRawResponse(self._install.rollback)


class InstallResourceWithStreamingResponse:
    def __init__(self, install: InstallResource) -> None:
        self._install = install

    @cached_property
    def apply(self) -> ApplyResourceWithStreamingResponse:
        return ApplyResourceWithStreamingResponse(self._install.apply)

    @cached_property
    def preview(self) -> PreviewResourceWithStreamingResponse:
        return PreviewResourceWithStreamingResponse(self._install.preview)

    @cached_property
    def rollback(self) -> RollbackResourceWithStreamingResponse:
        return RollbackResourceWithStreamingResponse(self._install.rollback)


class AsyncInstallResourceWithStreamingResponse:
    def __init__(self, install: AsyncInstallResource) -> None:
        self._install = install

    @cached_property
    def apply(self) -> AsyncApplyResourceWithStreamingResponse:
        return AsyncApplyResourceWithStreamingResponse(self._install.apply)

    @cached_property
    def preview(self) -> AsyncPreviewResourceWithStreamingResponse:
        return AsyncPreviewResourceWithStreamingResponse(self._install.preview)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithStreamingResponse:
        return AsyncRollbackResourceWithStreamingResponse(self._install.rollback)
