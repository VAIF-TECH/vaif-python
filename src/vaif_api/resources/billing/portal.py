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
from ...types.billing import portal_create_params
from ...types.billing.portal_create_response import PortalCreateResponse

__all__ = ["PortalResource", "AsyncPortalResource"]


class PortalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return PortalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return PortalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        org_id: str,
        return_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/portal",
            body=maybe_transform(
                {
                    "org_id": org_id,
                    "return_url": return_url,
                },
                portal_create_params.PortalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalCreateResponse,
        )


class AsyncPortalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncPortalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        org_id: str,
        return_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/portal",
            body=await async_maybe_transform(
                {
                    "org_id": org_id,
                    "return_url": return_url,
                },
                portal_create_params.PortalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortalCreateResponse,
        )


class PortalResourceWithRawResponse:
    def __init__(self, portal: PortalResource) -> None:
        self._portal = portal

        self.create = to_raw_response_wrapper(
            portal.create,
        )


class AsyncPortalResourceWithRawResponse:
    def __init__(self, portal: AsyncPortalResource) -> None:
        self._portal = portal

        self.create = async_to_raw_response_wrapper(
            portal.create,
        )


class PortalResourceWithStreamingResponse:
    def __init__(self, portal: PortalResource) -> None:
        self._portal = portal

        self.create = to_streamed_response_wrapper(
            portal.create,
        )


class AsyncPortalResourceWithStreamingResponse:
    def __init__(self, portal: AsyncPortalResource) -> None:
        self._portal = portal

        self.create = async_to_streamed_response_wrapper(
            portal.create,
        )
