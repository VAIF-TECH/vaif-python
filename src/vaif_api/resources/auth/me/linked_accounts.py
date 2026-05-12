# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.auth.me.linked_account_list_response import LinkedAccountListResponse
from ....types.auth.me.linked_account_delete_response import LinkedAccountDeleteResponse

__all__ = ["LinkedAccountsResource", "AsyncLinkedAccountsResource"]


class LinkedAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinkedAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return LinkedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkedAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return LinkedAccountsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedAccountListResponse:
        """List OAuth accounts linked to the current user"""
        return self._get(
            "/auth/me/linked-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedAccountListResponse,
        )

    def delete(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedAccountDeleteResponse:
        """
        Unlink an OAuth provider from the current user's account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._delete(
            path_template("/auth/me/linked-accounts/{provider}", provider=provider),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedAccountDeleteResponse,
        )


class AsyncLinkedAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinkedAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkedAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncLinkedAccountsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedAccountListResponse:
        """List OAuth accounts linked to the current user"""
        return await self._get(
            "/auth/me/linked-accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedAccountListResponse,
        )

    async def delete(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedAccountDeleteResponse:
        """
        Unlink an OAuth provider from the current user's account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._delete(
            path_template("/auth/me/linked-accounts/{provider}", provider=provider),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedAccountDeleteResponse,
        )


class LinkedAccountsResourceWithRawResponse:
    def __init__(self, linked_accounts: LinkedAccountsResource) -> None:
        self._linked_accounts = linked_accounts

        self.list = to_raw_response_wrapper(
            linked_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            linked_accounts.delete,
        )


class AsyncLinkedAccountsResourceWithRawResponse:
    def __init__(self, linked_accounts: AsyncLinkedAccountsResource) -> None:
        self._linked_accounts = linked_accounts

        self.list = async_to_raw_response_wrapper(
            linked_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            linked_accounts.delete,
        )


class LinkedAccountsResourceWithStreamingResponse:
    def __init__(self, linked_accounts: LinkedAccountsResource) -> None:
        self._linked_accounts = linked_accounts

        self.list = to_streamed_response_wrapper(
            linked_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            linked_accounts.delete,
        )


class AsyncLinkedAccountsResourceWithStreamingResponse:
    def __init__(self, linked_accounts: AsyncLinkedAccountsResource) -> None:
        self._linked_accounts = linked_accounts

        self.list = async_to_streamed_response_wrapper(
            linked_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            linked_accounts.delete,
        )
