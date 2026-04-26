# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .full import (
    FullResource,
    AsyncFullResource,
    FullResourceWithRawResponse,
    AsyncFullResourceWithRawResponse,
    FullResourceWithStreamingResponse,
    AsyncFullResourceWithStreamingResponse,
)
from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OpenAPIResource", "AsyncOpenAPIResource"]


class OpenAPIResource(SyncAPIResource):
    @cached_property
    def full(self) -> FullResource:
        return FullResource(self._client)

    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> OpenAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return OpenAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return OpenAPIResourceWithStreamingResponse(self)


class AsyncOpenAPIResource(AsyncAPIResource):
    @cached_property
    def full(self) -> AsyncFullResource:
        return AsyncFullResource(self._client)

    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOpenAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncOpenAPIResourceWithStreamingResponse(self)


class OpenAPIResourceWithRawResponse:
    def __init__(self, openapi: OpenAPIResource) -> None:
        self._openapi = openapi

    @cached_property
    def full(self) -> FullResourceWithRawResponse:
        return FullResourceWithRawResponse(self._openapi.full)

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._openapi.project)


class AsyncOpenAPIResourceWithRawResponse:
    def __init__(self, openapi: AsyncOpenAPIResource) -> None:
        self._openapi = openapi

    @cached_property
    def full(self) -> AsyncFullResourceWithRawResponse:
        return AsyncFullResourceWithRawResponse(self._openapi.full)

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._openapi.project)


class OpenAPIResourceWithStreamingResponse:
    def __init__(self, openapi: OpenAPIResource) -> None:
        self._openapi = openapi

    @cached_property
    def full(self) -> FullResourceWithStreamingResponse:
        return FullResourceWithStreamingResponse(self._openapi.full)

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._openapi.project)


class AsyncOpenAPIResourceWithStreamingResponse:
    def __init__(self, openapi: AsyncOpenAPIResource) -> None:
        self._openapi = openapi

    @cached_property
    def full(self) -> AsyncFullResourceWithStreamingResponse:
        return AsyncFullResourceWithStreamingResponse(self._openapi.full)

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._openapi.project)
