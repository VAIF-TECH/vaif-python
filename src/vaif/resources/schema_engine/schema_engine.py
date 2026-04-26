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
from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from .preview import (
    PreviewResource,
    AsyncPreviewResource,
    PreviewResourceWithRawResponse,
    AsyncPreviewResourceWithRawResponse,
    PreviewResourceWithStreamingResponse,
    AsyncPreviewResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .introspect import (
    IntrospectResource,
    AsyncIntrospectResource,
    IntrospectResourceWithRawResponse,
    AsyncIntrospectResourceWithRawResponse,
    IntrospectResourceWithStreamingResponse,
    AsyncIntrospectResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .migrations.migrations import (
    MigrationsResource,
    AsyncMigrationsResource,
    MigrationsResourceWithRawResponse,
    AsyncMigrationsResourceWithRawResponse,
    MigrationsResourceWithStreamingResponse,
    AsyncMigrationsResourceWithStreamingResponse,
)

__all__ = ["SchemaEngineResource", "AsyncSchemaEngineResource"]


class SchemaEngineResource(SyncAPIResource):
    @cached_property
    def apply(self) -> ApplyResource:
        return ApplyResource(self._client)

    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def introspect(self) -> IntrospectResource:
        return IntrospectResource(self._client)

    @cached_property
    def migrations(self) -> MigrationsResource:
        return MigrationsResource(self._client)

    @cached_property
    def preview(self) -> PreviewResource:
        return PreviewResource(self._client)

    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def with_raw_response(self) -> SchemaEngineResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SchemaEngineResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaEngineResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SchemaEngineResourceWithStreamingResponse(self)


class AsyncSchemaEngineResource(AsyncAPIResource):
    @cached_property
    def apply(self) -> AsyncApplyResource:
        return AsyncApplyResource(self._client)

    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def introspect(self) -> AsyncIntrospectResource:
        return AsyncIntrospectResource(self._client)

    @cached_property
    def migrations(self) -> AsyncMigrationsResource:
        return AsyncMigrationsResource(self._client)

    @cached_property
    def preview(self) -> AsyncPreviewResource:
        return AsyncPreviewResource(self._client)

    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSchemaEngineResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaEngineResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaEngineResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSchemaEngineResourceWithStreamingResponse(self)


class SchemaEngineResourceWithRawResponse:
    def __init__(self, schema_engine: SchemaEngineResource) -> None:
        self._schema_engine = schema_engine

    @cached_property
    def apply(self) -> ApplyResourceWithRawResponse:
        return ApplyResourceWithRawResponse(self._schema_engine.apply)

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._schema_engine.changes)

    @cached_property
    def introspect(self) -> IntrospectResourceWithRawResponse:
        return IntrospectResourceWithRawResponse(self._schema_engine.introspect)

    @cached_property
    def migrations(self) -> MigrationsResourceWithRawResponse:
        return MigrationsResourceWithRawResponse(self._schema_engine.migrations)

    @cached_property
    def preview(self) -> PreviewResourceWithRawResponse:
        return PreviewResourceWithRawResponse(self._schema_engine.preview)

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._schema_engine.query)


class AsyncSchemaEngineResourceWithRawResponse:
    def __init__(self, schema_engine: AsyncSchemaEngineResource) -> None:
        self._schema_engine = schema_engine

    @cached_property
    def apply(self) -> AsyncApplyResourceWithRawResponse:
        return AsyncApplyResourceWithRawResponse(self._schema_engine.apply)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._schema_engine.changes)

    @cached_property
    def introspect(self) -> AsyncIntrospectResourceWithRawResponse:
        return AsyncIntrospectResourceWithRawResponse(self._schema_engine.introspect)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithRawResponse:
        return AsyncMigrationsResourceWithRawResponse(self._schema_engine.migrations)

    @cached_property
    def preview(self) -> AsyncPreviewResourceWithRawResponse:
        return AsyncPreviewResourceWithRawResponse(self._schema_engine.preview)

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._schema_engine.query)


class SchemaEngineResourceWithStreamingResponse:
    def __init__(self, schema_engine: SchemaEngineResource) -> None:
        self._schema_engine = schema_engine

    @cached_property
    def apply(self) -> ApplyResourceWithStreamingResponse:
        return ApplyResourceWithStreamingResponse(self._schema_engine.apply)

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._schema_engine.changes)

    @cached_property
    def introspect(self) -> IntrospectResourceWithStreamingResponse:
        return IntrospectResourceWithStreamingResponse(self._schema_engine.introspect)

    @cached_property
    def migrations(self) -> MigrationsResourceWithStreamingResponse:
        return MigrationsResourceWithStreamingResponse(self._schema_engine.migrations)

    @cached_property
    def preview(self) -> PreviewResourceWithStreamingResponse:
        return PreviewResourceWithStreamingResponse(self._schema_engine.preview)

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._schema_engine.query)


class AsyncSchemaEngineResourceWithStreamingResponse:
    def __init__(self, schema_engine: AsyncSchemaEngineResource) -> None:
        self._schema_engine = schema_engine

    @cached_property
    def apply(self) -> AsyncApplyResourceWithStreamingResponse:
        return AsyncApplyResourceWithStreamingResponse(self._schema_engine.apply)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._schema_engine.changes)

    @cached_property
    def introspect(self) -> AsyncIntrospectResourceWithStreamingResponse:
        return AsyncIntrospectResourceWithStreamingResponse(self._schema_engine.introspect)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithStreamingResponse:
        return AsyncMigrationsResourceWithStreamingResponse(self._schema_engine.migrations)

    @cached_property
    def preview(self) -> AsyncPreviewResourceWithStreamingResponse:
        return AsyncPreviewResourceWithStreamingResponse(self._schema_engine.preview)

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._schema_engine.query)
