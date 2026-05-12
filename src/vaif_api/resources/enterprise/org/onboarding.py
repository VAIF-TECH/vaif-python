# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.enterprise.org import onboarding_onboarding_params
from ....types.enterprise.org.onboarding_onboarding_response import OnboardingOnboardingResponse

__all__ = ["OnboardingResource", "AsyncOnboardingResource"]


class OnboardingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnboardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return OnboardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnboardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return OnboardingResourceWithStreamingResponse(self)

    def get_onboarding(
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
            path_template("/enterprise/org/{org_id}/onboarding", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def onboarding(
        self,
        org_id: str,
        *,
        dismissed: bool | Omit = omit,
        steps: Dict[str, bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingOnboardingResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._patch(
            path_template("/enterprise/org/{org_id}/onboarding", org_id=org_id),
            body=maybe_transform(
                {
                    "dismissed": dismissed,
                    "steps": steps,
                },
                onboarding_onboarding_params.OnboardingOnboardingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingOnboardingResponse,
        )


class AsyncOnboardingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnboardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnboardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnboardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncOnboardingResourceWithStreamingResponse(self)

    async def get_onboarding(
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
            path_template("/enterprise/org/{org_id}/onboarding", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def onboarding(
        self,
        org_id: str,
        *,
        dismissed: bool | Omit = omit,
        steps: Dict[str, bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingOnboardingResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._patch(
            path_template("/enterprise/org/{org_id}/onboarding", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "dismissed": dismissed,
                    "steps": steps,
                },
                onboarding_onboarding_params.OnboardingOnboardingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingOnboardingResponse,
        )


class OnboardingResourceWithRawResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

        self.get_onboarding = to_raw_response_wrapper(
            onboarding.get_onboarding,
        )
        self.onboarding = to_raw_response_wrapper(
            onboarding.onboarding,
        )


class AsyncOnboardingResourceWithRawResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

        self.get_onboarding = async_to_raw_response_wrapper(
            onboarding.get_onboarding,
        )
        self.onboarding = async_to_raw_response_wrapper(
            onboarding.onboarding,
        )


class OnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

        self.get_onboarding = to_streamed_response_wrapper(
            onboarding.get_onboarding,
        )
        self.onboarding = to_streamed_response_wrapper(
            onboarding.onboarding,
        )


class AsyncOnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

        self.get_onboarding = async_to_streamed_response_wrapper(
            onboarding.get_onboarding,
        )
        self.onboarding = async_to_streamed_response_wrapper(
            onboarding.onboarding,
        )
