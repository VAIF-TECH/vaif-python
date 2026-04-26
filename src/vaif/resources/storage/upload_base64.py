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
from ...types.storage import upload_base64_create_params
from ...types.storage.upload_base64_create_response import UploadBase64CreateResponse

__all__ = ["UploadBase64Resource", "AsyncUploadBase64Resource"]


class UploadBase64Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadBase64ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return UploadBase64ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadBase64ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return UploadBase64ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bucket: str,
        data: str,
        path: str,
        project_id: str,
        content_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadBase64CreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/upload-base64",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "data": data,
                    "path": path,
                    "project_id": project_id,
                    "content_type": content_type,
                },
                upload_base64_create_params.UploadBase64CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadBase64CreateResponse,
        )


class AsyncUploadBase64Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadBase64ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadBase64ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadBase64ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncUploadBase64ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bucket: str,
        data: str,
        path: str,
        project_id: str,
        content_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadBase64CreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/upload-base64",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "data": data,
                    "path": path,
                    "project_id": project_id,
                    "content_type": content_type,
                },
                upload_base64_create_params.UploadBase64CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadBase64CreateResponse,
        )


class UploadBase64ResourceWithRawResponse:
    def __init__(self, upload_base64: UploadBase64Resource) -> None:
        self._upload_base64 = upload_base64

        self.create = to_raw_response_wrapper(
            upload_base64.create,
        )


class AsyncUploadBase64ResourceWithRawResponse:
    def __init__(self, upload_base64: AsyncUploadBase64Resource) -> None:
        self._upload_base64 = upload_base64

        self.create = async_to_raw_response_wrapper(
            upload_base64.create,
        )


class UploadBase64ResourceWithStreamingResponse:
    def __init__(self, upload_base64: UploadBase64Resource) -> None:
        self._upload_base64 = upload_base64

        self.create = to_streamed_response_wrapper(
            upload_base64.create,
        )


class AsyncUploadBase64ResourceWithStreamingResponse:
    def __init__(self, upload_base64: AsyncUploadBase64Resource) -> None:
        self._upload_base64 = upload_base64

        self.create = async_to_streamed_response_wrapper(
            upload_base64.create,
        )
