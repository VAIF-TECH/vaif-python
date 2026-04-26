# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .org.org import (
    OrgResource,
    AsyncOrgResource,
    OrgResourceWithRawResponse,
    AsyncOrgResourceWithRawResponse,
    OrgResourceWithStreamingResponse,
    AsyncOrgResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OnboardingResource", "AsyncOnboardingResource"]


class OnboardingResource(SyncAPIResource):
    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

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


class AsyncOnboardingResource(AsyncAPIResource):
    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

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


class OnboardingResourceWithRawResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._onboarding.org)


class AsyncOnboardingResourceWithRawResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._onboarding.org)


class OnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._onboarding.org)


class AsyncOnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._onboarding.org)
