# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tiers import (
    TiersResource,
    AsyncTiersResource,
    TiersResourceWithRawResponse,
    AsyncTiersResourceWithRawResponse,
    TiersResourceWithStreamingResponse,
    AsyncTiersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .wrappers.wrappers import (
    WrappersResource,
    AsyncWrappersResource,
    WrappersResourceWithRawResponse,
    AsyncWrappersResourceWithRawResponse,
    WrappersResourceWithStreamingResponse,
    AsyncWrappersResourceWithStreamingResponse,
)
from .connector.connector import (
    ConnectorResource,
    AsyncConnectorResource,
    ConnectorResourceWithRawResponse,
    AsyncConnectorResourceWithRawResponse,
    ConnectorResourceWithStreamingResponse,
    AsyncConnectorResourceWithStreamingResponse,
)
from .extensions.extensions import (
    ExtensionsResource,
    AsyncExtensionsResource,
    ExtensionsResourceWithRawResponse,
    AsyncExtensionsResourceWithRawResponse,
    ExtensionsResourceWithStreamingResponse,
    AsyncExtensionsResourceWithStreamingResponse,
)

__all__ = ["DatabaseResource", "AsyncDatabaseResource"]


class DatabaseResource(SyncAPIResource):
    @cached_property
    def connector(self) -> ConnectorResource:
        return ConnectorResource(self._client)

    @cached_property
    def extensions(self) -> ExtensionsResource:
        return ExtensionsResource(self._client)

    @cached_property
    def tiers(self) -> TiersResource:
        return TiersResource(self._client)

    @cached_property
    def wrappers(self) -> WrappersResource:
        return WrappersResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatabaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DatabaseResourceWithStreamingResponse(self)


class AsyncDatabaseResource(AsyncAPIResource):
    @cached_property
    def connector(self) -> AsyncConnectorResource:
        return AsyncConnectorResource(self._client)

    @cached_property
    def extensions(self) -> AsyncExtensionsResource:
        return AsyncExtensionsResource(self._client)

    @cached_property
    def tiers(self) -> AsyncTiersResource:
        return AsyncTiersResource(self._client)

    @cached_property
    def wrappers(self) -> AsyncWrappersResource:
        return AsyncWrappersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatabaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatabaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDatabaseResourceWithStreamingResponse(self)


class DatabaseResourceWithRawResponse:
    def __init__(self, database: DatabaseResource) -> None:
        self._database = database

    @cached_property
    def connector(self) -> ConnectorResourceWithRawResponse:
        return ConnectorResourceWithRawResponse(self._database.connector)

    @cached_property
    def extensions(self) -> ExtensionsResourceWithRawResponse:
        return ExtensionsResourceWithRawResponse(self._database.extensions)

    @cached_property
    def tiers(self) -> TiersResourceWithRawResponse:
        return TiersResourceWithRawResponse(self._database.tiers)

    @cached_property
    def wrappers(self) -> WrappersResourceWithRawResponse:
        return WrappersResourceWithRawResponse(self._database.wrappers)


class AsyncDatabaseResourceWithRawResponse:
    def __init__(self, database: AsyncDatabaseResource) -> None:
        self._database = database

    @cached_property
    def connector(self) -> AsyncConnectorResourceWithRawResponse:
        return AsyncConnectorResourceWithRawResponse(self._database.connector)

    @cached_property
    def extensions(self) -> AsyncExtensionsResourceWithRawResponse:
        return AsyncExtensionsResourceWithRawResponse(self._database.extensions)

    @cached_property
    def tiers(self) -> AsyncTiersResourceWithRawResponse:
        return AsyncTiersResourceWithRawResponse(self._database.tiers)

    @cached_property
    def wrappers(self) -> AsyncWrappersResourceWithRawResponse:
        return AsyncWrappersResourceWithRawResponse(self._database.wrappers)


class DatabaseResourceWithStreamingResponse:
    def __init__(self, database: DatabaseResource) -> None:
        self._database = database

    @cached_property
    def connector(self) -> ConnectorResourceWithStreamingResponse:
        return ConnectorResourceWithStreamingResponse(self._database.connector)

    @cached_property
    def extensions(self) -> ExtensionsResourceWithStreamingResponse:
        return ExtensionsResourceWithStreamingResponse(self._database.extensions)

    @cached_property
    def tiers(self) -> TiersResourceWithStreamingResponse:
        return TiersResourceWithStreamingResponse(self._database.tiers)

    @cached_property
    def wrappers(self) -> WrappersResourceWithStreamingResponse:
        return WrappersResourceWithStreamingResponse(self._database.wrappers)


class AsyncDatabaseResourceWithStreamingResponse:
    def __init__(self, database: AsyncDatabaseResource) -> None:
        self._database = database

    @cached_property
    def connector(self) -> AsyncConnectorResourceWithStreamingResponse:
        return AsyncConnectorResourceWithStreamingResponse(self._database.connector)

    @cached_property
    def extensions(self) -> AsyncExtensionsResourceWithStreamingResponse:
        return AsyncExtensionsResourceWithStreamingResponse(self._database.extensions)

    @cached_property
    def tiers(self) -> AsyncTiersResourceWithStreamingResponse:
        return AsyncTiersResourceWithStreamingResponse(self._database.tiers)

    @cached_property
    def wrappers(self) -> AsyncWrappersResourceWithStreamingResponse:
        return AsyncWrappersResourceWithStreamingResponse(self._database.wrappers)
