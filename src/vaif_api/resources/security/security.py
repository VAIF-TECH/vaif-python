# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .audit import (
    AuditResource,
    AsyncAuditResource,
    AuditResourceWithRawResponse,
    AsyncAuditResourceWithRawResponse,
    AuditResourceWithStreamingResponse,
    AsyncAuditResourceWithStreamingResponse,
)
from .overview import (
    OverviewResource,
    AsyncOverviewResource,
    OverviewResourceWithRawResponse,
    AsyncOverviewResourceWithRawResponse,
    OverviewResourceWithStreamingResponse,
    AsyncOverviewResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SecurityResource", "AsyncSecurityResource"]


class SecurityResource(SyncAPIResource):
    @cached_property
    def audit(self) -> AuditResource:
        return AuditResource(self._client)

    @cached_property
    def overview(self) -> OverviewResource:
        return OverviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SecurityResourceWithStreamingResponse(self)


class AsyncSecurityResource(AsyncAPIResource):
    @cached_property
    def audit(self) -> AsyncAuditResource:
        return AsyncAuditResource(self._client)

    @cached_property
    def overview(self) -> AsyncOverviewResource:
        return AsyncOverviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSecurityResourceWithStreamingResponse(self)


class SecurityResourceWithRawResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

    @cached_property
    def audit(self) -> AuditResourceWithRawResponse:
        return AuditResourceWithRawResponse(self._security.audit)

    @cached_property
    def overview(self) -> OverviewResourceWithRawResponse:
        return OverviewResourceWithRawResponse(self._security.overview)


class AsyncSecurityResourceWithRawResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

    @cached_property
    def audit(self) -> AsyncAuditResourceWithRawResponse:
        return AsyncAuditResourceWithRawResponse(self._security.audit)

    @cached_property
    def overview(self) -> AsyncOverviewResourceWithRawResponse:
        return AsyncOverviewResourceWithRawResponse(self._security.overview)


class SecurityResourceWithStreamingResponse:
    def __init__(self, security: SecurityResource) -> None:
        self._security = security

    @cached_property
    def audit(self) -> AuditResourceWithStreamingResponse:
        return AuditResourceWithStreamingResponse(self._security.audit)

    @cached_property
    def overview(self) -> OverviewResourceWithStreamingResponse:
        return OverviewResourceWithStreamingResponse(self._security.overview)


class AsyncSecurityResourceWithStreamingResponse:
    def __init__(self, security: AsyncSecurityResource) -> None:
        self._security = security

    @cached_property
    def audit(self) -> AsyncAuditResourceWithStreamingResponse:
        return AsyncAuditResourceWithStreamingResponse(self._security.audit)

    @cached_property
    def overview(self) -> AsyncOverviewResourceWithStreamingResponse:
        return AsyncOverviewResourceWithStreamingResponse(self._security.overview)
