# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .org import (
    OrgResource,
    AsyncOrgResource,
    OrgResourceWithRawResponse,
    AsyncOrgResourceWithRawResponse,
    OrgResourceWithStreamingResponse,
    AsyncOrgResourceWithStreamingResponse,
)
from .save import (
    SaveResource,
    AsyncSaveResource,
    SaveResourceWithRawResponse,
    AsyncSaveResourceWithRawResponse,
    SaveResourceWithStreamingResponse,
    AsyncSaveResourceWithStreamingResponse,
)
from .apply import (
    ApplyResource,
    AsyncApplyResource,
    ApplyResourceWithRawResponse,
    AsyncApplyResourceWithRawResponse,
    ApplyResourceWithStreamingResponse,
    AsyncApplyResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.plan_retrieve_response import PlanRetrieveResponse

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    @cached_property
    def apply(self) -> ApplyResource:
        return ApplyResource(self._client)

    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def save(self) -> SaveResource:
        return SaveResource(self._client)

    @cached_property
    def with_raw_response(self) -> PlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return PlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return PlansResourceWithStreamingResponse(self)

    def retrieve(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanRetrieveResponse:
        """
        Get a saved plan by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get(
            path_template("/plans/{plan_id}", plan_id=plan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRetrieveResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    @cached_property
    def apply(self) -> AsyncApplyResource:
        return AsyncApplyResource(self._client)

    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def save(self) -> AsyncSaveResource:
        return AsyncSaveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncPlansResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanRetrieveResponse:
        """
        Get a saved plan by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._get(
            path_template("/plans/{plan_id}", plan_id=plan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRetrieveResponse,
        )


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.retrieve = to_raw_response_wrapper(
            plans.retrieve,
        )

    @cached_property
    def apply(self) -> ApplyResourceWithRawResponse:
        return ApplyResourceWithRawResponse(self._plans.apply)

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._plans.org)

    @cached_property
    def save(self) -> SaveResourceWithRawResponse:
        return SaveResourceWithRawResponse(self._plans.save)


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.retrieve = async_to_raw_response_wrapper(
            plans.retrieve,
        )

    @cached_property
    def apply(self) -> AsyncApplyResourceWithRawResponse:
        return AsyncApplyResourceWithRawResponse(self._plans.apply)

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._plans.org)

    @cached_property
    def save(self) -> AsyncSaveResourceWithRawResponse:
        return AsyncSaveResourceWithRawResponse(self._plans.save)


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.retrieve = to_streamed_response_wrapper(
            plans.retrieve,
        )

    @cached_property
    def apply(self) -> ApplyResourceWithStreamingResponse:
        return ApplyResourceWithStreamingResponse(self._plans.apply)

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._plans.org)

    @cached_property
    def save(self) -> SaveResourceWithStreamingResponse:
        return SaveResourceWithStreamingResponse(self._plans.save)


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.retrieve = async_to_streamed_response_wrapper(
            plans.retrieve,
        )

    @cached_property
    def apply(self) -> AsyncApplyResourceWithStreamingResponse:
        return AsyncApplyResourceWithStreamingResponse(self._plans.apply)

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._plans.org)

    @cached_property
    def save(self) -> AsyncSaveResourceWithStreamingResponse:
        return AsyncSaveResourceWithStreamingResponse(self._plans.save)
