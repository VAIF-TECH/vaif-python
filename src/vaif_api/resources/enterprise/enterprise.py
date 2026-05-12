# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .inquire import (
    InquireResource,
    AsyncInquireResource,
    InquireResourceWithRawResponse,
    AsyncInquireResourceWithRawResponse,
    InquireResourceWithStreamingResponse,
    AsyncInquireResourceWithStreamingResponse,
)
from .org.org import (
    OrgResource,
    AsyncOrgResource,
    OrgResourceWithRawResponse,
    AsyncOrgResourceWithRawResponse,
    OrgResourceWithStreamingResponse,
    AsyncOrgResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .subdomain import (
    SubdomainResource,
    AsyncSubdomainResource,
    SubdomainResourceWithRawResponse,
    AsyncSubdomainResourceWithRawResponse,
    SubdomainResourceWithStreamingResponse,
    AsyncSubdomainResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .quotes.quotes import (
    QuotesResource,
    AsyncQuotesResource,
    QuotesResourceWithRawResponse,
    AsyncQuotesResourceWithRawResponse,
    QuotesResourceWithStreamingResponse,
    AsyncQuotesResourceWithStreamingResponse,
)

__all__ = ["EnterpriseResource", "AsyncEnterpriseResource"]


class EnterpriseResource(SyncAPIResource):
    @cached_property
    def inquire(self) -> InquireResource:
        return InquireResource(self._client)

    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def quotes(self) -> QuotesResource:
        return QuotesResource(self._client)

    @cached_property
    def subdomain(self) -> SubdomainResource:
        return SubdomainResource(self._client)

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
    def inquire(self) -> AsyncInquireResource:
        return AsyncInquireResource(self._client)

    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def quotes(self) -> AsyncQuotesResource:
        return AsyncQuotesResource(self._client)

    @cached_property
    def subdomain(self) -> AsyncSubdomainResource:
        return AsyncSubdomainResource(self._client)

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
    def inquire(self) -> InquireResourceWithRawResponse:
        return InquireResourceWithRawResponse(self._enterprise.inquire)

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._enterprise.org)

    @cached_property
    def quotes(self) -> QuotesResourceWithRawResponse:
        return QuotesResourceWithRawResponse(self._enterprise.quotes)

    @cached_property
    def subdomain(self) -> SubdomainResourceWithRawResponse:
        return SubdomainResourceWithRawResponse(self._enterprise.subdomain)


class AsyncEnterpriseResourceWithRawResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquire(self) -> AsyncInquireResourceWithRawResponse:
        return AsyncInquireResourceWithRawResponse(self._enterprise.inquire)

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._enterprise.org)

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithRawResponse:
        return AsyncQuotesResourceWithRawResponse(self._enterprise.quotes)

    @cached_property
    def subdomain(self) -> AsyncSubdomainResourceWithRawResponse:
        return AsyncSubdomainResourceWithRawResponse(self._enterprise.subdomain)


class EnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: EnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquire(self) -> InquireResourceWithStreamingResponse:
        return InquireResourceWithStreamingResponse(self._enterprise.inquire)

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._enterprise.org)

    @cached_property
    def quotes(self) -> QuotesResourceWithStreamingResponse:
        return QuotesResourceWithStreamingResponse(self._enterprise.quotes)

    @cached_property
    def subdomain(self) -> SubdomainResourceWithStreamingResponse:
        return SubdomainResourceWithStreamingResponse(self._enterprise.subdomain)


class AsyncEnterpriseResourceWithStreamingResponse:
    def __init__(self, enterprise: AsyncEnterpriseResource) -> None:
        self._enterprise = enterprise

    @cached_property
    def inquire(self) -> AsyncInquireResourceWithStreamingResponse:
        return AsyncInquireResourceWithStreamingResponse(self._enterprise.inquire)

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._enterprise.org)

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithStreamingResponse:
        return AsyncQuotesResourceWithStreamingResponse(self._enterprise.quotes)

    @cached_property
    def subdomain(self) -> AsyncSubdomainResourceWithStreamingResponse:
        return AsyncSubdomainResourceWithStreamingResponse(self._enterprise.subdomain)
