# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from .auto_setup import (
    AutoSetupResource,
    AsyncAutoSetupResource,
    AutoSetupResourceWithRawResponse,
    AsyncAutoSetupResourceWithRawResponse,
    AutoSetupResourceWithStreamingResponse,
    AsyncAutoSetupResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .complete_step import (
    CompleteStepResource,
    AsyncCompleteStepResource,
    CompleteStepResourceWithRawResponse,
    AsyncCompleteStepResourceWithRawResponse,
    CompleteStepResourceWithStreamingResponse,
    AsyncCompleteStepResourceWithStreamingResponse,
)
from ...._base_client import make_request_options

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def auto_setup(self) -> AutoSetupResource:
        return AutoSetupResource(self._client)

    @cached_property
    def complete_step(self) -> CompleteStepResource:
        return CompleteStepResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)

    def retrieve(
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
            path_template("/onboarding/org/{org_id}", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def auto_setup(self) -> AsyncAutoSetupResource:
        return AsyncAutoSetupResource(self._client)

    @cached_property
    def complete_step(self) -> AsyncCompleteStepResource:
        return AsyncCompleteStepResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)

    async def retrieve(
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
            path_template("/onboarding/org/{org_id}", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.retrieve = to_raw_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def auto_setup(self) -> AutoSetupResourceWithRawResponse:
        return AutoSetupResourceWithRawResponse(self._org.auto_setup)

    @cached_property
    def complete_step(self) -> CompleteStepResourceWithRawResponse:
        return CompleteStepResourceWithRawResponse(self._org.complete_step)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.retrieve = async_to_raw_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def auto_setup(self) -> AsyncAutoSetupResourceWithRawResponse:
        return AsyncAutoSetupResourceWithRawResponse(self._org.auto_setup)

    @cached_property
    def complete_step(self) -> AsyncCompleteStepResourceWithRawResponse:
        return AsyncCompleteStepResourceWithRawResponse(self._org.complete_step)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.retrieve = to_streamed_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def auto_setup(self) -> AutoSetupResourceWithStreamingResponse:
        return AutoSetupResourceWithStreamingResponse(self._org.auto_setup)

    @cached_property
    def complete_step(self) -> CompleteStepResourceWithStreamingResponse:
        return CompleteStepResourceWithStreamingResponse(self._org.complete_step)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.retrieve = async_to_streamed_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def auto_setup(self) -> AsyncAutoSetupResourceWithStreamingResponse:
        return AsyncAutoSetupResourceWithStreamingResponse(self._org.auto_setup)

    @cached_property
    def complete_step(self) -> AsyncCompleteStepResourceWithStreamingResponse:
        return AsyncCompleteStepResourceWithStreamingResponse(self._org.complete_step)
