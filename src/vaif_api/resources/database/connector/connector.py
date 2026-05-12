# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .test import (
    TestResource,
    AsyncTestResource,
    TestResourceWithRawResponse,
    AsyncTestResourceWithRawResponse,
    TestResourceWithStreamingResponse,
    AsyncTestResourceWithStreamingResponse,
)
from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from .tables import (
    TablesResource,
    AsyncTablesResource,
    TablesResourceWithRawResponse,
    AsyncTablesResourceWithRawResponse,
    TablesResourceWithStreamingResponse,
    AsyncTablesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ConnectorResource", "AsyncConnectorResource"]


class ConnectorResource(SyncAPIResource):
    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def tables(self) -> TablesResource:
        return TablesResource(self._client)

    @cached_property
    def test(self) -> TestResource:
        return TestResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ConnectorResourceWithStreamingResponse(self)


class AsyncConnectorResource(AsyncAPIResource):
    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def tables(self) -> AsyncTablesResource:
        return AsyncTablesResource(self._client)

    @cached_property
    def test(self) -> AsyncTestResource:
        return AsyncTestResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncConnectorResourceWithStreamingResponse(self)


class ConnectorResourceWithRawResponse:
    def __init__(self, connector: ConnectorResource) -> None:
        self._connector = connector

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._connector.query)

    @cached_property
    def tables(self) -> TablesResourceWithRawResponse:
        return TablesResourceWithRawResponse(self._connector.tables)

    @cached_property
    def test(self) -> TestResourceWithRawResponse:
        return TestResourceWithRawResponse(self._connector.test)


class AsyncConnectorResourceWithRawResponse:
    def __init__(self, connector: AsyncConnectorResource) -> None:
        self._connector = connector

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._connector.query)

    @cached_property
    def tables(self) -> AsyncTablesResourceWithRawResponse:
        return AsyncTablesResourceWithRawResponse(self._connector.tables)

    @cached_property
    def test(self) -> AsyncTestResourceWithRawResponse:
        return AsyncTestResourceWithRawResponse(self._connector.test)


class ConnectorResourceWithStreamingResponse:
    def __init__(self, connector: ConnectorResource) -> None:
        self._connector = connector

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._connector.query)

    @cached_property
    def tables(self) -> TablesResourceWithStreamingResponse:
        return TablesResourceWithStreamingResponse(self._connector.tables)

    @cached_property
    def test(self) -> TestResourceWithStreamingResponse:
        return TestResourceWithStreamingResponse(self._connector.test)


class AsyncConnectorResourceWithStreamingResponse:
    def __init__(self, connector: AsyncConnectorResource) -> None:
        self._connector = connector

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._connector.query)

    @cached_property
    def tables(self) -> AsyncTablesResourceWithStreamingResponse:
        return AsyncTablesResourceWithStreamingResponse(self._connector.tables)

    @cached_property
    def test(self) -> AsyncTestResourceWithStreamingResponse:
        return AsyncTestResourceWithStreamingResponse(self._connector.test)
