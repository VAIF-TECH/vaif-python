# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import contact_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.contact_create_response import ContactCreateResponse

__all__ = ["ContactResource", "AsyncContactResource"]


class ContactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ContactResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        message: str,
        name: str,
        subject: Literal["Sales Inquiry", "Partnership Opportunity", "Technical Support", "Other"],
        company: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Submit a contact form

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contact",
            body=maybe_transform(
                {
                    "email": email,
                    "message": message,
                    "name": name,
                    "subject": subject,
                    "company": company,
                    "website": website,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )


class AsyncContactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncContactResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        message: str,
        name: str,
        subject: Literal["Sales Inquiry", "Partnership Opportunity", "Technical Support", "Other"],
        company: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Submit a contact form

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contact",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "message": message,
                    "name": name,
                    "subject": subject,
                    "company": company,
                    "website": website,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )


class ContactResourceWithRawResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

        self.create = to_raw_response_wrapper(
            contact.create,
        )


class AsyncContactResourceWithRawResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

        self.create = async_to_raw_response_wrapper(
            contact.create,
        )


class ContactResourceWithStreamingResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

        self.create = to_streamed_response_wrapper(
            contact.create,
        )


class AsyncContactResourceWithStreamingResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

        self.create = async_to_streamed_response_wrapper(
            contact.create,
        )
