# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.orgs import billing_contact_billing_contacts_params
from ..._base_client import make_request_options
from ...types.orgs.billing_contact_delete_response import BillingContactDeleteResponse
from ...types.orgs.billing_contact_billing_contacts_response import BillingContactBillingContactsResponse
from ...types.orgs.billing_contact_get_billing_contacts_response import BillingContactGetBillingContactsResponse

__all__ = ["BillingContactsResource", "AsyncBillingContactsResource"]


class BillingContactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return BillingContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return BillingContactsResourceWithStreamingResponse(self)

    def delete(
        self,
        contact_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingContactDeleteResponse:
        """
        Remove a billing contact from an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._delete(
            path_template("/orgs/{org_id}/billing-contacts/{contact_id}", org_id=org_id, contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingContactDeleteResponse,
        )

    def billing_contacts(
        self,
        org_id: str,
        *,
        email: str,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingContactBillingContactsResponse:
        """
        Add a billing contact to an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/orgs/{org_id}/billing-contacts", org_id=org_id),
            body=maybe_transform(
                {
                    "email": email,
                    "label": label,
                },
                billing_contact_billing_contacts_params.BillingContactBillingContactsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingContactBillingContactsResponse,
        )

    def get_billing_contacts(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingContactGetBillingContactsResponse:
        """
        List billing contacts for an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/orgs/{org_id}/billing-contacts", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingContactGetBillingContactsResponse,
        )


class AsyncBillingContactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncBillingContactsResourceWithStreamingResponse(self)

    async def delete(
        self,
        contact_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingContactDeleteResponse:
        """
        Remove a billing contact from an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._delete(
            path_template("/orgs/{org_id}/billing-contacts/{contact_id}", org_id=org_id, contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingContactDeleteResponse,
        )

    async def billing_contacts(
        self,
        org_id: str,
        *,
        email: str,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingContactBillingContactsResponse:
        """
        Add a billing contact to an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/orgs/{org_id}/billing-contacts", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "label": label,
                },
                billing_contact_billing_contacts_params.BillingContactBillingContactsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingContactBillingContactsResponse,
        )

    async def get_billing_contacts(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingContactGetBillingContactsResponse:
        """
        List billing contacts for an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/orgs/{org_id}/billing-contacts", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingContactGetBillingContactsResponse,
        )


class BillingContactsResourceWithRawResponse:
    def __init__(self, billing_contacts: BillingContactsResource) -> None:
        self._billing_contacts = billing_contacts

        self.delete = to_raw_response_wrapper(
            billing_contacts.delete,
        )
        self.billing_contacts = to_raw_response_wrapper(
            billing_contacts.billing_contacts,
        )
        self.get_billing_contacts = to_raw_response_wrapper(
            billing_contacts.get_billing_contacts,
        )


class AsyncBillingContactsResourceWithRawResponse:
    def __init__(self, billing_contacts: AsyncBillingContactsResource) -> None:
        self._billing_contacts = billing_contacts

        self.delete = async_to_raw_response_wrapper(
            billing_contacts.delete,
        )
        self.billing_contacts = async_to_raw_response_wrapper(
            billing_contacts.billing_contacts,
        )
        self.get_billing_contacts = async_to_raw_response_wrapper(
            billing_contacts.get_billing_contacts,
        )


class BillingContactsResourceWithStreamingResponse:
    def __init__(self, billing_contacts: BillingContactsResource) -> None:
        self._billing_contacts = billing_contacts

        self.delete = to_streamed_response_wrapper(
            billing_contacts.delete,
        )
        self.billing_contacts = to_streamed_response_wrapper(
            billing_contacts.billing_contacts,
        )
        self.get_billing_contacts = to_streamed_response_wrapper(
            billing_contacts.get_billing_contacts,
        )


class AsyncBillingContactsResourceWithStreamingResponse:
    def __init__(self, billing_contacts: AsyncBillingContactsResource) -> None:
        self._billing_contacts = billing_contacts

        self.delete = async_to_streamed_response_wrapper(
            billing_contacts.delete,
        )
        self.billing_contacts = async_to_streamed_response_wrapper(
            billing_contacts.billing_contacts,
        )
        self.get_billing_contacts = async_to_streamed_response_wrapper(
            billing_contacts.get_billing_contacts,
        )
