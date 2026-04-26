# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .verify import (
    VerifyResource,
    AsyncVerifyResource,
    VerifyResourceWithRawResponse,
    AsyncVerifyResourceWithRawResponse,
    VerifyResourceWithStreamingResponse,
    AsyncVerifyResourceWithStreamingResponse,
)
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
from ....types.billing import checkout_create_params
from ....types.billing.checkout_create_response import CheckoutCreateResponse

__all__ = ["CheckoutResource", "AsyncCheckoutResource"]


class CheckoutResource(SyncAPIResource):
    @cached_property
    def verify(self) -> VerifyResource:
        return VerifyResource(self._client)

    @cached_property
    def with_raw_response(self) -> CheckoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CheckoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CheckoutResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        org_id: str,
        plan: Literal["starter", "pro", "agency", "studio_plus"],
        cancel_url: str | Omit = omit,
        interval: Literal["monthly", "yearly"] | Omit = omit,
        promo_code: str | Omit = omit,
        success_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/checkout",
            body=maybe_transform(
                {
                    "org_id": org_id,
                    "plan": plan,
                    "cancel_url": cancel_url,
                    "interval": interval,
                    "promo_code": promo_code,
                    "success_url": success_url,
                },
                checkout_create_params.CheckoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutCreateResponse,
        )


class AsyncCheckoutResource(AsyncAPIResource):
    @cached_property
    def verify(self) -> AsyncVerifyResource:
        return AsyncVerifyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCheckoutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckoutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCheckoutResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        org_id: str,
        plan: Literal["starter", "pro", "agency", "studio_plus"],
        cancel_url: str | Omit = omit,
        interval: Literal["monthly", "yearly"] | Omit = omit,
        promo_code: str | Omit = omit,
        success_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/checkout",
            body=await async_maybe_transform(
                {
                    "org_id": org_id,
                    "plan": plan,
                    "cancel_url": cancel_url,
                    "interval": interval,
                    "promo_code": promo_code,
                    "success_url": success_url,
                },
                checkout_create_params.CheckoutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutCreateResponse,
        )


class CheckoutResourceWithRawResponse:
    def __init__(self, checkout: CheckoutResource) -> None:
        self._checkout = checkout

        self.create = to_raw_response_wrapper(
            checkout.create,
        )

    @cached_property
    def verify(self) -> VerifyResourceWithRawResponse:
        return VerifyResourceWithRawResponse(self._checkout.verify)


class AsyncCheckoutResourceWithRawResponse:
    def __init__(self, checkout: AsyncCheckoutResource) -> None:
        self._checkout = checkout

        self.create = async_to_raw_response_wrapper(
            checkout.create,
        )

    @cached_property
    def verify(self) -> AsyncVerifyResourceWithRawResponse:
        return AsyncVerifyResourceWithRawResponse(self._checkout.verify)


class CheckoutResourceWithStreamingResponse:
    def __init__(self, checkout: CheckoutResource) -> None:
        self._checkout = checkout

        self.create = to_streamed_response_wrapper(
            checkout.create,
        )

    @cached_property
    def verify(self) -> VerifyResourceWithStreamingResponse:
        return VerifyResourceWithStreamingResponse(self._checkout.verify)


class AsyncCheckoutResourceWithStreamingResponse:
    def __init__(self, checkout: AsyncCheckoutResource) -> None:
        self._checkout = checkout

        self.create = async_to_streamed_response_wrapper(
            checkout.create,
        )

    @cached_property
    def verify(self) -> AsyncVerifyResourceWithStreamingResponse:
        return AsyncVerifyResourceWithStreamingResponse(self._checkout.verify)
