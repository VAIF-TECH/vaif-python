# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["UploadFromURLResource", "AsyncUploadFromURLResource"]


class UploadFromURLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadFromURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return UploadFromURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadFromURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return UploadFromURLResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/storage/upload-from-url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUploadFromURLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadFromURLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadFromURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadFromURLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncUploadFromURLResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/storage/upload-from-url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UploadFromURLResourceWithRawResponse:
    def __init__(self, upload_from_url: UploadFromURLResource) -> None:
        self._upload_from_url = upload_from_url

        self.create = to_raw_response_wrapper(
            upload_from_url.create,
        )


class AsyncUploadFromURLResourceWithRawResponse:
    def __init__(self, upload_from_url: AsyncUploadFromURLResource) -> None:
        self._upload_from_url = upload_from_url

        self.create = async_to_raw_response_wrapper(
            upload_from_url.create,
        )


class UploadFromURLResourceWithStreamingResponse:
    def __init__(self, upload_from_url: UploadFromURLResource) -> None:
        self._upload_from_url = upload_from_url

        self.create = to_streamed_response_wrapper(
            upload_from_url.create,
        )


class AsyncUploadFromURLResourceWithStreamingResponse:
    def __init__(self, upload_from_url: AsyncUploadFromURLResource) -> None:
        self._upload_from_url = upload_from_url

        self.create = async_to_streamed_response_wrapper(
            upload_from_url.create,
        )
