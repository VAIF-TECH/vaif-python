# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MigrationsResource", "AsyncMigrationsResource"]


class MigrationsResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> MigrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return MigrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return MigrationsResourceWithStreamingResponse(self)


class AsyncMigrationsResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMigrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncMigrationsResourceWithStreamingResponse(self)


class MigrationsResourceWithRawResponse:
    def __init__(self, migrations: MigrationsResource) -> None:
        self._migrations = migrations

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._migrations.project)


class AsyncMigrationsResourceWithRawResponse:
    def __init__(self, migrations: AsyncMigrationsResource) -> None:
        self._migrations = migrations

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._migrations.project)


class MigrationsResourceWithStreamingResponse:
    def __init__(self, migrations: MigrationsResource) -> None:
        self._migrations = migrations

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._migrations.project)


class AsyncMigrationsResourceWithStreamingResponse:
    def __init__(self, migrations: AsyncMigrationsResource) -> None:
        self._migrations = migrations

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._migrations.project)
