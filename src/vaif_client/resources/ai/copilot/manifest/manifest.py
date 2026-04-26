# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .pause import (
    PauseResource,
    AsyncPauseResource,
    PauseResourceWithRawResponse,
    AsyncPauseResourceWithRawResponse,
    PauseResourceWithStreamingResponse,
    AsyncPauseResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["ManifestResource", "AsyncManifestResource"]


class ManifestResource(SyncAPIResource):
    @cached_property
    def pause(self) -> PauseResource:
        return PauseResource(self._client)

    @cached_property
    def with_raw_response(self) -> ManifestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ManifestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManifestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ManifestResourceWithStreamingResponse(self)

    def retrieve(
        self,
        manifest_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not manifest_id:
            raise ValueError(f"Expected a non-empty value for `manifest_id` but received {manifest_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/ai/copilot/manifest/{manifest_id}", manifest_id=manifest_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncManifestResource(AsyncAPIResource):
    @cached_property
    def pause(self) -> AsyncPauseResource:
        return AsyncPauseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncManifestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManifestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManifestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncManifestResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        manifest_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not manifest_id:
            raise ValueError(f"Expected a non-empty value for `manifest_id` but received {manifest_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/ai/copilot/manifest/{manifest_id}", manifest_id=manifest_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ManifestResourceWithRawResponse:
    def __init__(self, manifest: ManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = to_raw_response_wrapper(
            manifest.retrieve,
        )

    @cached_property
    def pause(self) -> PauseResourceWithRawResponse:
        return PauseResourceWithRawResponse(self._manifest.pause)


class AsyncManifestResourceWithRawResponse:
    def __init__(self, manifest: AsyncManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = async_to_raw_response_wrapper(
            manifest.retrieve,
        )

    @cached_property
    def pause(self) -> AsyncPauseResourceWithRawResponse:
        return AsyncPauseResourceWithRawResponse(self._manifest.pause)


class ManifestResourceWithStreamingResponse:
    def __init__(self, manifest: ManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = to_streamed_response_wrapper(
            manifest.retrieve,
        )

    @cached_property
    def pause(self) -> PauseResourceWithStreamingResponse:
        return PauseResourceWithStreamingResponse(self._manifest.pause)


class AsyncManifestResourceWithStreamingResponse:
    def __init__(self, manifest: AsyncManifestResource) -> None:
        self._manifest = manifest

        self.retrieve = async_to_streamed_response_wrapper(
            manifest.retrieve,
        )

    @cached_property
    def pause(self) -> AsyncPauseResourceWithStreamingResponse:
        return AsyncPauseResourceWithStreamingResponse(self._manifest.pause)
