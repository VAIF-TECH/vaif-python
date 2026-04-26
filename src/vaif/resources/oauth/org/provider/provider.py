# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .refresh import (
    RefreshResource,
    AsyncRefreshResource,
    RefreshResourceWithRawResponse,
    AsyncRefreshResourceWithRawResponse,
    RefreshResourceWithStreamingResponse,
    AsyncRefreshResourceWithStreamingResponse,
)
from .authorize import (
    AuthorizeResource,
    AsyncAuthorizeResource,
    AuthorizeResourceWithRawResponse,
    AsyncAuthorizeResourceWithRawResponse,
    AuthorizeResourceWithStreamingResponse,
    AsyncAuthorizeResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.oauth.org import provider_update_params
from .....types.oauth.org.provider_delete_response import ProviderDeleteResponse
from .....types.oauth.org.provider_update_response import ProviderUpdateResponse

__all__ = ["ProviderResource", "AsyncProviderResource"]


class ProviderResource(SyncAPIResource):
    @cached_property
    def authorize(self) -> AuthorizeResource:
        return AuthorizeResource(self._client)

    @cached_property
    def refresh(self) -> RefreshResource:
        return RefreshResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ProviderResourceWithStreamingResponse(self)

    def update(
        self,
        provider: str,
        *,
        org_id: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        enabled: bool | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderUpdateResponse:
        """
        Update OAuth provider configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._patch(
            path_template("/oauth/org/{org_id}/provider/{provider}", org_id=org_id, provider=provider),
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "enabled": enabled,
                    "redirect_uri": redirect_uri,
                },
                provider_update_params.ProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderUpdateResponse,
        )

    def delete(
        self,
        provider: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderDeleteResponse:
        """
        Delete OAuth provider configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._delete(
            path_template("/oauth/org/{org_id}/provider/{provider}", org_id=org_id, provider=provider),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderDeleteResponse,
        )


class AsyncProviderResource(AsyncAPIResource):
    @cached_property
    def authorize(self) -> AsyncAuthorizeResource:
        return AsyncAuthorizeResource(self._client)

    @cached_property
    def refresh(self) -> AsyncRefreshResource:
        return AsyncRefreshResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncProviderResourceWithStreamingResponse(self)

    async def update(
        self,
        provider: str,
        *,
        org_id: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        enabled: bool | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderUpdateResponse:
        """
        Update OAuth provider configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._patch(
            path_template("/oauth/org/{org_id}/provider/{provider}", org_id=org_id, provider=provider),
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "enabled": enabled,
                    "redirect_uri": redirect_uri,
                },
                provider_update_params.ProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderUpdateResponse,
        )

    async def delete(
        self,
        provider: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderDeleteResponse:
        """
        Delete OAuth provider configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._delete(
            path_template("/oauth/org/{org_id}/provider/{provider}", org_id=org_id, provider=provider),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderDeleteResponse,
        )


class ProviderResourceWithRawResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.update = to_raw_response_wrapper(
            provider.update,
        )
        self.delete = to_raw_response_wrapper(
            provider.delete,
        )

    @cached_property
    def authorize(self) -> AuthorizeResourceWithRawResponse:
        return AuthorizeResourceWithRawResponse(self._provider.authorize)

    @cached_property
    def refresh(self) -> RefreshResourceWithRawResponse:
        return RefreshResourceWithRawResponse(self._provider.refresh)


class AsyncProviderResourceWithRawResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.update = async_to_raw_response_wrapper(
            provider.update,
        )
        self.delete = async_to_raw_response_wrapper(
            provider.delete,
        )

    @cached_property
    def authorize(self) -> AsyncAuthorizeResourceWithRawResponse:
        return AsyncAuthorizeResourceWithRawResponse(self._provider.authorize)

    @cached_property
    def refresh(self) -> AsyncRefreshResourceWithRawResponse:
        return AsyncRefreshResourceWithRawResponse(self._provider.refresh)


class ProviderResourceWithStreamingResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.update = to_streamed_response_wrapper(
            provider.update,
        )
        self.delete = to_streamed_response_wrapper(
            provider.delete,
        )

    @cached_property
    def authorize(self) -> AuthorizeResourceWithStreamingResponse:
        return AuthorizeResourceWithStreamingResponse(self._provider.authorize)

    @cached_property
    def refresh(self) -> RefreshResourceWithStreamingResponse:
        return RefreshResourceWithStreamingResponse(self._provider.refresh)


class AsyncProviderResourceWithStreamingResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.update = async_to_streamed_response_wrapper(
            provider.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            provider.delete,
        )

    @cached_property
    def authorize(self) -> AsyncAuthorizeResourceWithStreamingResponse:
        return AsyncAuthorizeResourceWithStreamingResponse(self._provider.authorize)

    @cached_property
    def refresh(self) -> AsyncRefreshResourceWithStreamingResponse:
        return AsyncRefreshResourceWithStreamingResponse(self._provider.refresh)
