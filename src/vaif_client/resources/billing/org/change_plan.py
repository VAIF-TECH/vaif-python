# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.billing.org import change_plan_change_plan_params
from ....types.billing.org.change_plan_change_plan_response import ChangePlanChangePlanResponse

__all__ = ["ChangePlanResource", "AsyncChangePlanResource"]


class ChangePlanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChangePlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ChangePlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChangePlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ChangePlanResourceWithStreamingResponse(self)

    def change_plan(
        self,
        org_id: str,
        *,
        plan: Literal["starter", "pro", "agency", "studio_plus"],
        interval: Literal["monthly", "yearly"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChangePlanChangePlanResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/billing/org/{org_id}/change-plan", org_id=org_id),
            body=maybe_transform(
                {
                    "plan": plan,
                    "interval": interval,
                },
                change_plan_change_plan_params.ChangePlanChangePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChangePlanChangePlanResponse,
        )


class AsyncChangePlanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChangePlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChangePlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChangePlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncChangePlanResourceWithStreamingResponse(self)

    async def change_plan(
        self,
        org_id: str,
        *,
        plan: Literal["starter", "pro", "agency", "studio_plus"],
        interval: Literal["monthly", "yearly"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChangePlanChangePlanResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/billing/org/{org_id}/change-plan", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "plan": plan,
                    "interval": interval,
                },
                change_plan_change_plan_params.ChangePlanChangePlanParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChangePlanChangePlanResponse,
        )


class ChangePlanResourceWithRawResponse:
    def __init__(self, change_plan: ChangePlanResource) -> None:
        self._change_plan = change_plan

        self.change_plan = to_raw_response_wrapper(
            change_plan.change_plan,
        )


class AsyncChangePlanResourceWithRawResponse:
    def __init__(self, change_plan: AsyncChangePlanResource) -> None:
        self._change_plan = change_plan

        self.change_plan = async_to_raw_response_wrapper(
            change_plan.change_plan,
        )


class ChangePlanResourceWithStreamingResponse:
    def __init__(self, change_plan: ChangePlanResource) -> None:
        self._change_plan = change_plan

        self.change_plan = to_streamed_response_wrapper(
            change_plan.change_plan,
        )


class AsyncChangePlanResourceWithStreamingResponse:
    def __init__(self, change_plan: AsyncChangePlanResource) -> None:
        self._change_plan = change_plan

        self.change_plan = async_to_streamed_response_wrapper(
            change_plan.change_plan,
        )
