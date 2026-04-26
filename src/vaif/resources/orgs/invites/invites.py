# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .accept import (
    AcceptResource,
    AsyncAcceptResource,
    AcceptResourceWithRawResponse,
    AsyncAcceptResourceWithRawResponse,
    AcceptResourceWithStreamingResponse,
    AsyncAcceptResourceWithStreamingResponse,
)
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

__all__ = ["InvitesResource", "AsyncInvitesResource"]


class InvitesResource(SyncAPIResource):
    @cached_property
    def accept(self) -> AcceptResource:
        return AcceptResource(self._client)

    @cached_property
    def with_raw_response(self) -> InvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return InvitesResourceWithStreamingResponse(self)

    def delete(
        self,
        invite_id: str,
        *,
        org_id: str,
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
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/orgs/{org_id}/invites/{invite_id}", org_id=org_id, invite_id=invite_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_invites(
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
            path_template("/orgs/{org_id}/invites", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInvitesResource(AsyncAPIResource):
    @cached_property
    def accept(self) -> AsyncAcceptResource:
        return AsyncAcceptResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncInvitesResourceWithStreamingResponse(self)

    async def delete(
        self,
        invite_id: str,
        *,
        org_id: str,
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
        if not invite_id:
            raise ValueError(f"Expected a non-empty value for `invite_id` but received {invite_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/orgs/{org_id}/invites/{invite_id}", org_id=org_id, invite_id=invite_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_invites(
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
            path_template("/orgs/{org_id}/invites", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InvitesResourceWithRawResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.delete = to_raw_response_wrapper(
            invites.delete,
        )
        self.get_invites = to_raw_response_wrapper(
            invites.get_invites,
        )

    @cached_property
    def accept(self) -> AcceptResourceWithRawResponse:
        return AcceptResourceWithRawResponse(self._invites.accept)


class AsyncInvitesResourceWithRawResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.delete = async_to_raw_response_wrapper(
            invites.delete,
        )
        self.get_invites = async_to_raw_response_wrapper(
            invites.get_invites,
        )

    @cached_property
    def accept(self) -> AsyncAcceptResourceWithRawResponse:
        return AsyncAcceptResourceWithRawResponse(self._invites.accept)


class InvitesResourceWithStreamingResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.delete = to_streamed_response_wrapper(
            invites.delete,
        )
        self.get_invites = to_streamed_response_wrapper(
            invites.get_invites,
        )

    @cached_property
    def accept(self) -> AcceptResourceWithStreamingResponse:
        return AcceptResourceWithStreamingResponse(self._invites.accept)


class AsyncInvitesResourceWithStreamingResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.delete = async_to_streamed_response_wrapper(
            invites.delete,
        )
        self.get_invites = async_to_streamed_response_wrapper(
            invites.get_invites,
        )

    @cached_property
    def accept(self) -> AsyncAcceptResourceWithStreamingResponse:
        return AsyncAcceptResourceWithStreamingResponse(self._invites.accept)
