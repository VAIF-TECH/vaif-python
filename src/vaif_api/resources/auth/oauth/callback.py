# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.auth.oauth import callback_get_callback_params

__all__ = ["CallbackResource", "AsyncCallbackResource"]


class CallbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CallbackResourceWithStreamingResponse(self)

    def get_callback(
        self,
        provider: Literal["google", "github", "microsoft", "apple"],
        *,
        code: str | Omit = omit,
        error: str | Omit = omit,
        error_description: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Handle OAuth redirect from provider — redirects to the app with a token or error

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/auth/oauth/{provider}/callback", provider=provider),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "error": error,
                        "error_description": error_description,
                        "state": state,
                    },
                    callback_get_callback_params.CallbackGetCallbackParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncCallbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCallbackResourceWithStreamingResponse(self)

    async def get_callback(
        self,
        provider: Literal["google", "github", "microsoft", "apple"],
        *,
        code: str | Omit = omit,
        error: str | Omit = omit,
        error_description: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Handle OAuth redirect from provider — redirects to the app with a token or error

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/auth/oauth/{provider}/callback", provider=provider),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "error": error,
                        "error_description": error_description,
                        "state": state,
                    },
                    callback_get_callback_params.CallbackGetCallbackParams,
                ),
            ),
            cast_to=NoneType,
        )


class CallbackResourceWithRawResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.get_callback = to_raw_response_wrapper(
            callback.get_callback,
        )


class AsyncCallbackResourceWithRawResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.get_callback = async_to_raw_response_wrapper(
            callback.get_callback,
        )


class CallbackResourceWithStreamingResponse:
    def __init__(self, callback: CallbackResource) -> None:
        self._callback = callback

        self.get_callback = to_streamed_response_wrapper(
            callback.get_callback,
        )


class AsyncCallbackResourceWithStreamingResponse:
    def __init__(self, callback: AsyncCallbackResource) -> None:
        self._callback = callback

        self.get_callback = async_to_streamed_response_wrapper(
            callback.get_callback,
        )
