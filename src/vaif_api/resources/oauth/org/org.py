# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from .configure import (
    ConfigureResource,
    AsyncConfigureResource,
    ConfigureResourceWithRawResponse,
    AsyncConfigureResourceWithRawResponse,
    ConfigureResourceWithStreamingResponse,
    AsyncConfigureResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .provider.provider import (
    ProviderResource,
    AsyncProviderResource,
    ProviderResourceWithRawResponse,
    AsyncProviderResourceWithRawResponse,
    ProviderResourceWithStreamingResponse,
    AsyncProviderResourceWithStreamingResponse,
)
from ....types.oauth.org_retrieve_response import OrgRetrieveResponse

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def configure(self) -> ConfigureResource:
        return ConfigureResource(self._client)

    @cached_property
    def provider(self) -> ProviderResource:
        return ProviderResource(self._client)

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
    ) -> OrgRetrieveResponse:
        """
        List OAuth configurations for an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/oauth/org/{org_id}", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgRetrieveResponse,
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def configure(self) -> AsyncConfigureResource:
        return AsyncConfigureResource(self._client)

    @cached_property
    def provider(self) -> AsyncProviderResource:
        return AsyncProviderResource(self._client)

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
    ) -> OrgRetrieveResponse:
        """
        List OAuth configurations for an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/oauth/org/{org_id}", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgRetrieveResponse,
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.retrieve = to_raw_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def configure(self) -> ConfigureResourceWithRawResponse:
        return ConfigureResourceWithRawResponse(self._org.configure)

    @cached_property
    def provider(self) -> ProviderResourceWithRawResponse:
        return ProviderResourceWithRawResponse(self._org.provider)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.retrieve = async_to_raw_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def configure(self) -> AsyncConfigureResourceWithRawResponse:
        return AsyncConfigureResourceWithRawResponse(self._org.configure)

    @cached_property
    def provider(self) -> AsyncProviderResourceWithRawResponse:
        return AsyncProviderResourceWithRawResponse(self._org.provider)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.retrieve = to_streamed_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def configure(self) -> ConfigureResourceWithStreamingResponse:
        return ConfigureResourceWithStreamingResponse(self._org.configure)

    @cached_property
    def provider(self) -> ProviderResourceWithStreamingResponse:
        return ProviderResourceWithStreamingResponse(self._org.provider)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.retrieve = async_to_streamed_response_wrapper(
            org.retrieve,
        )

    @cached_property
    def configure(self) -> AsyncConfigureResourceWithStreamingResponse:
        return AsyncConfigureResourceWithStreamingResponse(self._org.configure)

    @cached_property
    def provider(self) -> AsyncProviderResourceWithStreamingResponse:
        return AsyncProviderResourceWithStreamingResponse(self._org.provider)
