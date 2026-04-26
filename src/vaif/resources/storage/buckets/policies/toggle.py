# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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

__all__ = ["ToggleResource", "AsyncToggleResource"]


class ToggleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToggleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ToggleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToggleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ToggleResourceWithStreamingResponse(self)

    def toggle(
        self,
        policy_id: str,
        *,
        bucket_id: str,
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
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/storage/buckets/{bucket_id}/policies/{policy_id}/toggle", bucket_id=bucket_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncToggleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToggleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToggleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToggleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncToggleResourceWithStreamingResponse(self)

    async def toggle(
        self,
        policy_id: str,
        *,
        bucket_id: str,
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
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/storage/buckets/{bucket_id}/policies/{policy_id}/toggle", bucket_id=bucket_id, policy_id=policy_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ToggleResourceWithRawResponse:
    def __init__(self, toggle: ToggleResource) -> None:
        self._toggle = toggle

        self.toggle = to_raw_response_wrapper(
            toggle.toggle,
        )


class AsyncToggleResourceWithRawResponse:
    def __init__(self, toggle: AsyncToggleResource) -> None:
        self._toggle = toggle

        self.toggle = async_to_raw_response_wrapper(
            toggle.toggle,
        )


class ToggleResourceWithStreamingResponse:
    def __init__(self, toggle: ToggleResource) -> None:
        self._toggle = toggle

        self.toggle = to_streamed_response_wrapper(
            toggle.toggle,
        )


class AsyncToggleResourceWithStreamingResponse:
    def __init__(self, toggle: AsyncToggleResource) -> None:
        self._toggle = toggle

        self.toggle = async_to_streamed_response_wrapper(
            toggle.toggle,
        )
