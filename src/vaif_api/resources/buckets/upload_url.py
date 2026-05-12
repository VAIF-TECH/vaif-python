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

__all__ = ["UploadURLResource", "AsyncUploadURLResource"]


class UploadURLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return UploadURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return UploadURLResourceWithStreamingResponse(self)

    def upload_url(
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
            path_template("/buckets/{bucket_id}/upload-url", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUploadURLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncUploadURLResourceWithStreamingResponse(self)

    async def upload_url(
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
            path_template("/buckets/{bucket_id}/upload-url", bucket_id=bucket_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UploadURLResourceWithRawResponse:
    def __init__(self, upload_url: UploadURLResource) -> None:
        self._upload_url = upload_url

        self.upload_url = to_raw_response_wrapper(
            upload_url.upload_url,
        )


class AsyncUploadURLResourceWithRawResponse:
    def __init__(self, upload_url: AsyncUploadURLResource) -> None:
        self._upload_url = upload_url

        self.upload_url = async_to_raw_response_wrapper(
            upload_url.upload_url,
        )


class UploadURLResourceWithStreamingResponse:
    def __init__(self, upload_url: UploadURLResource) -> None:
        self._upload_url = upload_url

        self.upload_url = to_streamed_response_wrapper(
            upload_url.upload_url,
        )


class AsyncUploadURLResourceWithStreamingResponse:
    def __init__(self, upload_url: AsyncUploadURLResource) -> None:
        self._upload_url = upload_url

        self.upload_url = async_to_streamed_response_wrapper(
            upload_url.upload_url,
        )
