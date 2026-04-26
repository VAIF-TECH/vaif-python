# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage.multipart import create_create_params
from ....types.storage.multipart.create_create_response import CreateCreateResponse

__all__ = ["CreateResource", "AsyncCreateResource"]


class CreateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CreateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CreateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bucket_id: str,
        key: str,
        content_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCreateResponse:
        """
        Initiate a multipart upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/multipart/create",
            body=maybe_transform(
                {
                    "bucket_id": bucket_id,
                    "key": key,
                    "content_type": content_type,
                },
                create_create_params.CreateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateCreateResponse,
        )


class AsyncCreateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCreateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bucket_id: str,
        key: str,
        content_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateCreateResponse:
        """
        Initiate a multipart upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/multipart/create",
            body=await async_maybe_transform(
                {
                    "bucket_id": bucket_id,
                    "key": key,
                    "content_type": content_type,
                },
                create_create_params.CreateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateCreateResponse,
        )


class CreateResourceWithRawResponse:
    def __init__(self, create: CreateResource) -> None:
        self._create = create

        self.create = to_raw_response_wrapper(
            create.create,
        )


class AsyncCreateResourceWithRawResponse:
    def __init__(self, create: AsyncCreateResource) -> None:
        self._create = create

        self.create = async_to_raw_response_wrapper(
            create.create,
        )


class CreateResourceWithStreamingResponse:
    def __init__(self, create: CreateResource) -> None:
        self._create = create

        self.create = to_streamed_response_wrapper(
            create.create,
        )


class AsyncCreateResourceWithStreamingResponse:
    def __init__(self, create: AsyncCreateResource) -> None:
        self._create = create

        self.create = async_to_streamed_response_wrapper(
            create.create,
        )
