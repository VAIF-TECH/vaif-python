# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .org import (
    OrgResource,
    AsyncOrgResource,
    OrgResourceWithRawResponse,
    AsyncOrgResourceWithRawResponse,
    OrgResourceWithStreamingResponse,
    AsyncOrgResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ActivationResource", "AsyncActivationResource"]


class ActivationResource(SyncAPIResource):
    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> ActivationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ActivationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ActivationResourceWithStreamingResponse(self)


class AsyncActivationResource(AsyncAPIResource):
    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncActivationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncActivationResourceWithStreamingResponse(self)


class ActivationResourceWithRawResponse:
    def __init__(self, activation: ActivationResource) -> None:
        self._activation = activation

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._activation.org)


class AsyncActivationResourceWithRawResponse:
    def __init__(self, activation: AsyncActivationResource) -> None:
        self._activation = activation

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._activation.org)


class ActivationResourceWithStreamingResponse:
    def __init__(self, activation: ActivationResource) -> None:
        self._activation = activation

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._activation.org)


class AsyncActivationResourceWithStreamingResponse:
    def __init__(self, activation: AsyncActivationResource) -> None:
        self._activation = activation

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._activation.org)
