# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....types.billing.org import tax_info_tax_info_params
from ....types.billing.org.tax_info_tax_info_response import TaxInfoTaxInfoResponse

__all__ = ["TaxInfoResource", "AsyncTaxInfoResource"]


class TaxInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaxInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return TaxInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaxInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return TaxInfoResourceWithStreamingResponse(self)

    def get_tax_info(
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
        return self._get(
            path_template("/billing/org/{org_id}/tax-info", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def tax_info(
        self,
        org_id: str,
        *,
        address: tax_info_tax_info_params.Address | Omit = omit,
        business_name: Optional[str] | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        tax_id_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxInfoTaxInfoResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._put(
            path_template("/billing/org/{org_id}/tax-info", org_id=org_id),
            body=maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "tax_id": tax_id,
                    "tax_id_type": tax_id_type,
                },
                tax_info_tax_info_params.TaxInfoTaxInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxInfoTaxInfoResponse,
        )


class AsyncTaxInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaxInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaxInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaxInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncTaxInfoResourceWithStreamingResponse(self)

    async def get_tax_info(
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
        return await self._get(
            path_template("/billing/org/{org_id}/tax-info", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def tax_info(
        self,
        org_id: str,
        *,
        address: tax_info_tax_info_params.Address | Omit = omit,
        business_name: Optional[str] | Omit = omit,
        tax_id: Optional[str] | Omit = omit,
        tax_id_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxInfoTaxInfoResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._put(
            path_template("/billing/org/{org_id}/tax-info", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "tax_id": tax_id,
                    "tax_id_type": tax_id_type,
                },
                tax_info_tax_info_params.TaxInfoTaxInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxInfoTaxInfoResponse,
        )


class TaxInfoResourceWithRawResponse:
    def __init__(self, tax_info: TaxInfoResource) -> None:
        self._tax_info = tax_info

        self.get_tax_info = to_raw_response_wrapper(
            tax_info.get_tax_info,
        )
        self.tax_info = to_raw_response_wrapper(
            tax_info.tax_info,
        )


class AsyncTaxInfoResourceWithRawResponse:
    def __init__(self, tax_info: AsyncTaxInfoResource) -> None:
        self._tax_info = tax_info

        self.get_tax_info = async_to_raw_response_wrapper(
            tax_info.get_tax_info,
        )
        self.tax_info = async_to_raw_response_wrapper(
            tax_info.tax_info,
        )


class TaxInfoResourceWithStreamingResponse:
    def __init__(self, tax_info: TaxInfoResource) -> None:
        self._tax_info = tax_info

        self.get_tax_info = to_streamed_response_wrapper(
            tax_info.get_tax_info,
        )
        self.tax_info = to_streamed_response_wrapper(
            tax_info.tax_info,
        )


class AsyncTaxInfoResourceWithStreamingResponse:
    def __init__(self, tax_info: AsyncTaxInfoResource) -> None:
        self._tax_info = tax_info

        self.get_tax_info = async_to_streamed_response_wrapper(
            tax_info.get_tax_info,
        )
        self.tax_info = async_to_streamed_response_wrapper(
            tax_info.tax_info,
        )
