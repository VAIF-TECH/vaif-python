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

__all__ = ["SSOResource", "AsyncSSOResource"]


class SSOResource(SyncAPIResource):
    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> SSOResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SSOResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSOResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SSOResourceWithStreamingResponse(self)


class AsyncSSOResource(AsyncAPIResource):
    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSSOResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSOResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSOResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSSOResourceWithStreamingResponse(self)


class SSOResourceWithRawResponse:
    def __init__(self, sso: SSOResource) -> None:
        self._sso = sso

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._sso.org)


class AsyncSSOResourceWithRawResponse:
    def __init__(self, sso: AsyncSSOResource) -> None:
        self._sso = sso

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._sso.org)


class SSOResourceWithStreamingResponse:
    def __init__(self, sso: SSOResource) -> None:
        self._sso = sso

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._sso.org)


class AsyncSSOResourceWithStreamingResponse:
    def __init__(self, sso: AsyncSSOResource) -> None:
        self._sso = sso

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._sso.org)
