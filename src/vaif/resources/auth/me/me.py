# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from .context import (
    ContextResource,
    AsyncContextResource,
    ContextResourceWithRawResponse,
    AsyncContextResourceWithRawResponse,
    ContextResourceWithStreamingResponse,
    AsyncContextResourceWithStreamingResponse,
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
from ....types.auth import me_update_params
from ...._base_client import make_request_options
from .linked_accounts import (
    LinkedAccountsResource,
    AsyncLinkedAccountsResource,
    LinkedAccountsResourceWithRawResponse,
    AsyncLinkedAccountsResourceWithRawResponse,
    LinkedAccountsResourceWithStreamingResponse,
    AsyncLinkedAccountsResourceWithStreamingResponse,
)
from ....types.auth.me_list_response import MeListResponse
from ....types.auth.me_update_response import MeUpdateResponse

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def context(self) -> ContextResource:
        return ContextResource(self._client)

    @cached_property
    def linked_accounts(self) -> LinkedAccountsResource:
        return LinkedAccountsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        avatar_url: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        phone: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeUpdateResponse:
        """
        Update the current authenticated user's profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/auth/me",
            body=maybe_transform(
                {
                    "avatar_url": avatar_url,
                    "name": name,
                    "phone": phone,
                    "timezone": timezone,
                },
                me_update_params.MeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeListResponse:
        """Get the current authenticated user's profile"""
        return self._get(
            "/auth/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeListResponse,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def context(self) -> AsyncContextResource:
        return AsyncContextResource(self._client)

    @cached_property
    def linked_accounts(self) -> AsyncLinkedAccountsResource:
        return AsyncLinkedAccountsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        avatar_url: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        phone: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeUpdateResponse:
        """
        Update the current authenticated user's profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/auth/me",
            body=await async_maybe_transform(
                {
                    "avatar_url": avatar_url,
                    "name": name,
                    "phone": phone,
                    "timezone": timezone,
                },
                me_update_params.MeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeListResponse:
        """Get the current authenticated user's profile"""
        return await self._get(
            "/auth/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeListResponse,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.update = to_raw_response_wrapper(
            me.update,
        )
        self.list = to_raw_response_wrapper(
            me.list,
        )

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._me.admin)

    @cached_property
    def context(self) -> ContextResourceWithRawResponse:
        return ContextResourceWithRawResponse(self._me.context)

    @cached_property
    def linked_accounts(self) -> LinkedAccountsResourceWithRawResponse:
        return LinkedAccountsResourceWithRawResponse(self._me.linked_accounts)


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.update = async_to_raw_response_wrapper(
            me.update,
        )
        self.list = async_to_raw_response_wrapper(
            me.list,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._me.admin)

    @cached_property
    def context(self) -> AsyncContextResourceWithRawResponse:
        return AsyncContextResourceWithRawResponse(self._me.context)

    @cached_property
    def linked_accounts(self) -> AsyncLinkedAccountsResourceWithRawResponse:
        return AsyncLinkedAccountsResourceWithRawResponse(self._me.linked_accounts)


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.update = to_streamed_response_wrapper(
            me.update,
        )
        self.list = to_streamed_response_wrapper(
            me.list,
        )

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._me.admin)

    @cached_property
    def context(self) -> ContextResourceWithStreamingResponse:
        return ContextResourceWithStreamingResponse(self._me.context)

    @cached_property
    def linked_accounts(self) -> LinkedAccountsResourceWithStreamingResponse:
        return LinkedAccountsResourceWithStreamingResponse(self._me.linked_accounts)


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.update = async_to_streamed_response_wrapper(
            me.update,
        )
        self.list = async_to_streamed_response_wrapper(
            me.list,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._me.admin)

    @cached_property
    def context(self) -> AsyncContextResourceWithStreamingResponse:
        return AsyncContextResourceWithStreamingResponse(self._me.context)

    @cached_property
    def linked_accounts(self) -> AsyncLinkedAccountsResourceWithStreamingResponse:
        return AsyncLinkedAccountsResourceWithStreamingResponse(self._me.linked_accounts)
