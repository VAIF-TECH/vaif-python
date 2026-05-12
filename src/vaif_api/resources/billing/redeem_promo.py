# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.billing import redeem_promo_create_params
from ...types.billing.redeem_promo_create_response import RedeemPromoCreateResponse

__all__ = ["RedeemPromoResource", "AsyncRedeemPromoResource"]


class RedeemPromoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedeemPromoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RedeemPromoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedeemPromoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RedeemPromoResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedeemPromoCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/redeem-promo",
            body=maybe_transform(
                {
                    "code": code,
                    "org_id": org_id,
                },
                redeem_promo_create_params.RedeemPromoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedeemPromoCreateResponse,
        )


class AsyncRedeemPromoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedeemPromoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedeemPromoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedeemPromoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRedeemPromoResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedeemPromoCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/redeem-promo",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "org_id": org_id,
                },
                redeem_promo_create_params.RedeemPromoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedeemPromoCreateResponse,
        )


class RedeemPromoResourceWithRawResponse:
    def __init__(self, redeem_promo: RedeemPromoResource) -> None:
        self._redeem_promo = redeem_promo

        self.create = to_raw_response_wrapper(
            redeem_promo.create,
        )


class AsyncRedeemPromoResourceWithRawResponse:
    def __init__(self, redeem_promo: AsyncRedeemPromoResource) -> None:
        self._redeem_promo = redeem_promo

        self.create = async_to_raw_response_wrapper(
            redeem_promo.create,
        )


class RedeemPromoResourceWithStreamingResponse:
    def __init__(self, redeem_promo: RedeemPromoResource) -> None:
        self._redeem_promo = redeem_promo

        self.create = to_streamed_response_wrapper(
            redeem_promo.create,
        )


class AsyncRedeemPromoResourceWithStreamingResponse:
    def __init__(self, redeem_promo: AsyncRedeemPromoResource) -> None:
        self._redeem_promo = redeem_promo

        self.create = async_to_streamed_response_wrapper(
            redeem_promo.create,
        )
