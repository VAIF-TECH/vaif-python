# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["AutoSetupResource", "AsyncAutoSetupResource"]


class AutoSetupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoSetupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AutoSetupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoSetupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AutoSetupResourceWithStreamingResponse(self)

    def auto_setup(
        self,
        org_id: str,
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
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/onboarding/org/{org_id}/auto-setup", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAutoSetupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoSetupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoSetupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoSetupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAutoSetupResourceWithStreamingResponse(self)

    async def auto_setup(
        self,
        org_id: str,
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
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/onboarding/org/{org_id}/auto-setup", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AutoSetupResourceWithRawResponse:
    def __init__(self, auto_setup: AutoSetupResource) -> None:
        self._auto_setup = auto_setup

        self.auto_setup = to_raw_response_wrapper(
            auto_setup.auto_setup,
        )


class AsyncAutoSetupResourceWithRawResponse:
    def __init__(self, auto_setup: AsyncAutoSetupResource) -> None:
        self._auto_setup = auto_setup

        self.auto_setup = async_to_raw_response_wrapper(
            auto_setup.auto_setup,
        )


class AutoSetupResourceWithStreamingResponse:
    def __init__(self, auto_setup: AutoSetupResource) -> None:
        self._auto_setup = auto_setup

        self.auto_setup = to_streamed_response_wrapper(
            auto_setup.auto_setup,
        )


class AsyncAutoSetupResourceWithStreamingResponse:
    def __init__(self, auto_setup: AsyncAutoSetupResource) -> None:
        self._auto_setup = auto_setup

        self.auto_setup = async_to_streamed_response_wrapper(
            auto_setup.auto_setup,
        )
