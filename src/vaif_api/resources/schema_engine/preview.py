# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.schema_engine import preview_create_params
from ...types.schema_engine.preview_create_response import PreviewCreateResponse

__all__ = ["PreviewResource", "AsyncPreviewResource"]


class PreviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return PreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return PreviewResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        definition: preview_create_params.Definition,
        project_id: str,
        allow_destructive: bool | Omit = omit,
        env_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewCreateResponse:
        """
        Preview schema migration changes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/schema-engine/preview",
            body=maybe_transform(
                {
                    "definition": definition,
                    "project_id": project_id,
                    "allow_destructive": allow_destructive,
                    "env_id": env_id,
                },
                preview_create_params.PreviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewCreateResponse,
        )


class AsyncPreviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncPreviewResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        definition: preview_create_params.Definition,
        project_id: str,
        allow_destructive: bool | Omit = omit,
        env_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewCreateResponse:
        """
        Preview schema migration changes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/schema-engine/preview",
            body=await async_maybe_transform(
                {
                    "definition": definition,
                    "project_id": project_id,
                    "allow_destructive": allow_destructive,
                    "env_id": env_id,
                },
                preview_create_params.PreviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewCreateResponse,
        )


class PreviewResourceWithRawResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

        self.create = to_raw_response_wrapper(
            preview.create,
        )


class AsyncPreviewResourceWithRawResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

        self.create = async_to_raw_response_wrapper(
            preview.create,
        )


class PreviewResourceWithStreamingResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

        self.create = to_streamed_response_wrapper(
            preview.create,
        )


class AsyncPreviewResourceWithStreamingResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

        self.create = async_to_streamed_response_wrapper(
            preview.create,
        )
