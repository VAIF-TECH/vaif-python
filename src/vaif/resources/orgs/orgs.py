# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from .check_name import (
    CheckNameResource,
    AsyncCheckNameResource,
    CheckNameResourceWithRawResponse,
    AsyncCheckNameResourceWithRawResponse,
    CheckNameResourceWithStreamingResponse,
    AsyncCheckNameResourceWithStreamingResponse,
)
from .membership import (
    MembershipResource,
    AsyncMembershipResource,
    MembershipResourceWithRawResponse,
    AsyncMembershipResourceWithRawResponse,
    MembershipResourceWithStreamingResponse,
    AsyncMembershipResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .invites.invites import (
    InvitesResource,
    AsyncInvitesResource,
    InvitesResourceWithRawResponse,
    AsyncInvitesResourceWithRawResponse,
    InvitesResourceWithStreamingResponse,
    AsyncInvitesResourceWithStreamingResponse,
)
from .billing_contacts import (
    BillingContactsResource,
    AsyncBillingContactsResource,
    BillingContactsResourceWithRawResponse,
    AsyncBillingContactsResourceWithRawResponse,
    BillingContactsResourceWithStreamingResponse,
    AsyncBillingContactsResourceWithStreamingResponse,
)

__all__ = ["OrgsResource", "AsyncOrgsResource"]


class OrgsResource(SyncAPIResource):
    @cached_property
    def billing_contacts(self) -> BillingContactsResource:
        return BillingContactsResource(self._client)

    @cached_property
    def check_name(self) -> CheckNameResource:
        return CheckNameResource(self._client)

    @cached_property
    def invites(self) -> InvitesResource:
        return InvitesResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def membership(self) -> MembershipResource:
        return MembershipResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return OrgsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/orgs/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/orgs/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrgsResource(AsyncAPIResource):
    @cached_property
    def billing_contacts(self) -> AsyncBillingContactsResource:
        return AsyncBillingContactsResource(self._client)

    @cached_property
    def check_name(self) -> AsyncCheckNameResource:
        return AsyncCheckNameResource(self._client)

    @cached_property
    def invites(self) -> AsyncInvitesResource:
        return AsyncInvitesResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def membership(self) -> AsyncMembershipResource:
        return AsyncMembershipResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncOrgsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/orgs/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/orgs/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrgsResourceWithRawResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.create = to_raw_response_wrapper(
            orgs.create,
        )
        self.list = to_raw_response_wrapper(
            orgs.list,
        )

    @cached_property
    def billing_contacts(self) -> BillingContactsResourceWithRawResponse:
        return BillingContactsResourceWithRawResponse(self._orgs.billing_contacts)

    @cached_property
    def check_name(self) -> CheckNameResourceWithRawResponse:
        return CheckNameResourceWithRawResponse(self._orgs.check_name)

    @cached_property
    def invites(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self._orgs.invites)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._orgs.members)

    @cached_property
    def membership(self) -> MembershipResourceWithRawResponse:
        return MembershipResourceWithRawResponse(self._orgs.membership)

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._orgs.profile)


class AsyncOrgsResourceWithRawResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.create = async_to_raw_response_wrapper(
            orgs.create,
        )
        self.list = async_to_raw_response_wrapper(
            orgs.list,
        )

    @cached_property
    def billing_contacts(self) -> AsyncBillingContactsResourceWithRawResponse:
        return AsyncBillingContactsResourceWithRawResponse(self._orgs.billing_contacts)

    @cached_property
    def check_name(self) -> AsyncCheckNameResourceWithRawResponse:
        return AsyncCheckNameResourceWithRawResponse(self._orgs.check_name)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self._orgs.invites)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._orgs.members)

    @cached_property
    def membership(self) -> AsyncMembershipResourceWithRawResponse:
        return AsyncMembershipResourceWithRawResponse(self._orgs.membership)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._orgs.profile)


class OrgsResourceWithStreamingResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.create = to_streamed_response_wrapper(
            orgs.create,
        )
        self.list = to_streamed_response_wrapper(
            orgs.list,
        )

    @cached_property
    def billing_contacts(self) -> BillingContactsResourceWithStreamingResponse:
        return BillingContactsResourceWithStreamingResponse(self._orgs.billing_contacts)

    @cached_property
    def check_name(self) -> CheckNameResourceWithStreamingResponse:
        return CheckNameResourceWithStreamingResponse(self._orgs.check_name)

    @cached_property
    def invites(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self._orgs.invites)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._orgs.members)

    @cached_property
    def membership(self) -> MembershipResourceWithStreamingResponse:
        return MembershipResourceWithStreamingResponse(self._orgs.membership)

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._orgs.profile)


class AsyncOrgsResourceWithStreamingResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.create = async_to_streamed_response_wrapper(
            orgs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            orgs.list,
        )

    @cached_property
    def billing_contacts(self) -> AsyncBillingContactsResourceWithStreamingResponse:
        return AsyncBillingContactsResourceWithStreamingResponse(self._orgs.billing_contacts)

    @cached_property
    def check_name(self) -> AsyncCheckNameResourceWithStreamingResponse:
        return AsyncCheckNameResourceWithStreamingResponse(self._orgs.check_name)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._orgs.invites)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._orgs.members)

    @cached_property
    def membership(self) -> AsyncMembershipResourceWithStreamingResponse:
        return AsyncMembershipResourceWithStreamingResponse(self._orgs.membership)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._orgs.profile)
