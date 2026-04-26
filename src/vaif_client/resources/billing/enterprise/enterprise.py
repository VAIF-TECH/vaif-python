# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .inquiry import (
    InquiryResource,
    AsyncInquiryResource,
    InquiryResourceWithRawResponse,
    AsyncInquiryResourceWithRawResponse,
    InquiryResourceWithStreamingResponse,
    AsyncInquiryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EnterpriseResource", "AsyncEnterpriseResource"]


class EnterpriseResource(SyncAPIResource):
    @cached_property
    def inquiry(self) -> InquiryResource:
        return InquiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnterpriseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return EnterpriseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnterpriseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return EnterpriseResourceWithStreamingResponse(self)


class AsyncEnterpriseResource(AsyncAPIResource):
    @cached_property
    def inquiry(self) -> AsyncInquiryResource:
        return AsyncInquiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnterpriseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnterpriseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnterpriseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncEnterpriseResourceWithStreamingResponse(self)


class EnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquiry(self) -> InquiryResourceWithRawResponse:
        return InquiryResourceWithRawResponse(self._enterprise.inquiry)


class AsyncEnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquiry(self) -> AsyncInquiryResourceWithRawResponse:
        return AsyncInquiryResourceWithRawResponse(self._enterprise.inquiry)


class EnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquiry(self) -> InquiryResourceWithStreamingResponse:
        return InquiryResourceWithStreamingResponse(self._enterprise.inquiry)


class AsyncEnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquiry(self) -> AsyncInquiryResourceWithStreamingResponse:
        return AsyncInquiryResourceWithStreamingResponse(self._enterprise.inquiry)
