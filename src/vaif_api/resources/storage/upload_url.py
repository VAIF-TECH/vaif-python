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
from ...types.storage import upload_url_create_params
from ...types.storage.upload_url_create_response import UploadURLCreateResponse

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

    def create(
        self,
        *,
        key: str,
        bucket: str | Omit = omit,
        size_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadURLCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/upload-url",
            body=maybe_transform(
                {
                    "key": key,
                    "bucket": bucket,
                    "size_bytes": size_bytes,
                },
                upload_url_create_params.UploadURLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadURLCreateResponse,
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

    async def create(
        self,
        *,
        key: str,
        bucket: str | Omit = omit,
        size_bytes: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadURLCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/upload-url",
            body=await async_maybe_transform(
                {
                    "key": key,
                    "bucket": bucket,
                    "size_bytes": size_bytes,
                },
                upload_url_create_params.UploadURLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadURLCreateResponse,
        )


class UploadURLResourceWithRawResponse:
    def __init__(self, upload_url: UploadURLResource) -> None:
        self._upload_url = upload_url

        self.create = to_raw_response_wrapper(
            upload_url.create,
        )


class AsyncUploadURLResourceWithRawResponse:
    def __init__(self, upload_url: AsyncUploadURLResource) -> None:
        self._upload_url = upload_url

        self.create = async_to_raw_response_wrapper(
            upload_url.create,
        )


class UploadURLResourceWithStreamingResponse:
    def __init__(self, upload_url: UploadURLResource) -> None:
        self._upload_url = upload_url

        self.create = to_streamed_response_wrapper(
            upload_url.create,
        )


class AsyncUploadURLResourceWithStreamingResponse:
    def __init__(self, upload_url: AsyncUploadURLResource) -> None:
        self._upload_url = upload_url

        self.create = async_to_streamed_response_wrapper(
            upload_url.create,
        )
