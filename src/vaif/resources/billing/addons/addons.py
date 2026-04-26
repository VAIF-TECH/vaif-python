# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .catalog import (
    CatalogResource,
    AsyncCatalogResource,
    CatalogResourceWithRawResponse,
    AsyncCatalogResourceWithRawResponse,
    CatalogResourceWithStreamingResponse,
    AsyncCatalogResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AddonsResource", "AsyncAddonsResource"]


class AddonsResource(SyncAPIResource):
    @cached_property
    def catalog(self) -> CatalogResource:
        return CatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AddonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AddonsResourceWithStreamingResponse(self)


class AsyncAddonsResource(AsyncAPIResource):
    @cached_property
    def catalog(self) -> AsyncCatalogResource:
        return AsyncCatalogResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAddonsResourceWithStreamingResponse(self)


class AddonsResourceWithRawResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

    @cached_property
    def catalog(self) -> CatalogResourceWithRawResponse:
        return CatalogResourceWithRawResponse(self._addons.catalog)


class AsyncAddonsResourceWithRawResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithRawResponse:
        return AsyncCatalogResourceWithRawResponse(self._addons.catalog)


class AddonsResourceWithStreamingResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

    @cached_property
    def catalog(self) -> CatalogResourceWithStreamingResponse:
        return CatalogResourceWithStreamingResponse(self._addons.catalog)


class AsyncAddonsResourceWithStreamingResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

    @cached_property
    def catalog(self) -> AsyncCatalogResourceWithStreamingResponse:
        return AsyncCatalogResourceWithStreamingResponse(self._addons.catalog)
