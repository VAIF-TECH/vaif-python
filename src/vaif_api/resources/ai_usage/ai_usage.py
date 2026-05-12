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

__all__ = ["AIUsageResource", "AsyncAIUsageResource"]


class AIUsageResource(SyncAPIResource):
    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AIUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AIUsageResourceWithStreamingResponse(self)


class AsyncAIUsageResource(AsyncAPIResource):
    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAIUsageResourceWithStreamingResponse(self)


class AIUsageResourceWithRawResponse:
    def __init__(self, ai_usage: AIUsageResource) -> None:
        self._ai_usage = ai_usage

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._ai_usage.org)


class AsyncAIUsageResourceWithRawResponse:
    def __init__(self, ai_usage: AsyncAIUsageResource) -> None:
        self._ai_usage = ai_usage

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._ai_usage.org)


class AIUsageResourceWithStreamingResponse:
    def __init__(self, ai_usage: AIUsageResource) -> None:
        self._ai_usage = ai_usage

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._ai_usage.org)


class AsyncAIUsageResourceWithStreamingResponse:
    def __init__(self, ai_usage: AsyncAIUsageResource) -> None:
        self._ai_usage = ai_usage

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._ai_usage.org)
