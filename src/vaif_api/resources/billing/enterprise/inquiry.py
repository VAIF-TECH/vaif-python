# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ....types.billing.enterprise import inquiry_create_params
from ....types.billing.enterprise.inquiry_create_response import InquiryCreateResponse

__all__ = ["InquiryResource", "AsyncInquiryResource"]


class InquiryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InquiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return InquiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InquiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return InquiryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company: str,
        email: str,
        name: str,
        message: str | Omit = omit,
        org_id: str | Omit = omit,
        phone: str | Omit = omit,
        team_size: Literal["1-10", "11-50", "51-200", "201-1000", "1000+"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InquiryCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/enterprise/inquiry",
            body=maybe_transform(
                {
                    "company": company,
                    "email": email,
                    "name": name,
                    "message": message,
                    "org_id": org_id,
                    "phone": phone,
                    "team_size": team_size,
                },
                inquiry_create_params.InquiryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InquiryCreateResponse,
        )


class AsyncInquiryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInquiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInquiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInquiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncInquiryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company: str,
        email: str,
        name: str,
        message: str | Omit = omit,
        org_id: str | Omit = omit,
        phone: str | Omit = omit,
        team_size: Literal["1-10", "11-50", "51-200", "201-1000", "1000+"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InquiryCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/enterprise/inquiry",
            body=await async_maybe_transform(
                {
                    "company": company,
                    "email": email,
                    "name": name,
                    "message": message,
                    "org_id": org_id,
                    "phone": phone,
                    "team_size": team_size,
                },
                inquiry_create_params.InquiryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InquiryCreateResponse,
        )


class InquiryResourceWithRawResponse:
    def __init__(self, inquiry: InquiryResource) -> None:
        self._inquiry = inquiry

        self.create = to_raw_response_wrapper(
            inquiry.create,
        )


class AsyncInquiryResourceWithRawResponse:
    def __init__(self, inquiry: AsyncInquiryResource) -> None:
        self._inquiry = inquiry

        self.create = async_to_raw_response_wrapper(
            inquiry.create,
        )


class InquiryResourceWithStreamingResponse:
    def __init__(self, inquiry: InquiryResource) -> None:
        self._inquiry = inquiry

        self.create = to_streamed_response_wrapper(
            inquiry.create,
        )


class AsyncInquiryResourceWithStreamingResponse:
    def __init__(self, inquiry: AsyncInquiryResource) -> None:
        self._inquiry = inquiry

        self.create = async_to_streamed_response_wrapper(
            inquiry.create,
        )
