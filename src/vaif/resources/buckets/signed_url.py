# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["SignedURLResource", "AsyncSignedURLResource"]


class SignedURLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SignedURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SignedURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SignedURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SignedURLResourceWithStreamingResponse(self)

    def signed_url(
        self,
        bucket_id: str,
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
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/buckets/{bucket_id}/signed-url", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSignedURLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSignedURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSignedURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSignedURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSignedURLResourceWithStreamingResponse(self)

    async def signed_url(
        self,
        bucket_id: str,
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
        if not bucket_id:
            raise ValueError(f"Expected a non-empty value for `bucket_id` but received {bucket_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/buckets/{bucket_id}/signed-url", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SignedURLResourceWithRawResponse:
    def __init__(self, signed_url: SignedURLResource) -> None:
        self._signed_url = signed_url

        self.signed_url = to_raw_response_wrapper(
            signed_url.signed_url,
        )


class AsyncSignedURLResourceWithRawResponse:
    def __init__(self, signed_url: AsyncSignedURLResource) -> None:
        self._signed_url = signed_url

        self.signed_url = async_to_raw_response_wrapper(
            signed_url.signed_url,
        )


class SignedURLResourceWithStreamingResponse:
    def __init__(self, signed_url: SignedURLResource) -> None:
        self._signed_url = signed_url

        self.signed_url = to_streamed_response_wrapper(
            signed_url.signed_url,
        )


class AsyncSignedURLResourceWithStreamingResponse:
    def __init__(self, signed_url: AsyncSignedURLResource) -> None:
        self._signed_url = signed_url

        self.signed_url = async_to_streamed_response_wrapper(
            signed_url.signed_url,
        )
