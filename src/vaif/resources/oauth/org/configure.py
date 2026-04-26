# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.oauth.org import configure_configure_params
from ....types.oauth.org.configure_configure_response import ConfigureConfigureResponse

__all__ = ["ConfigureResource", "AsyncConfigureResource"]


class ConfigureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ConfigureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ConfigureResourceWithStreamingResponse(self)

    def configure(
        self,
        org_id: str,
        *,
        client_id: str,
        client_secret: str,
        provider: Literal["google", "apple", "github"],
        redirect_uri: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigureConfigureResponse:
        """
        Configure OAuth for an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/oauth/org/{org_id}/configure", org_id=org_id),
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "provider": provider,
                    "redirect_uri": redirect_uri,
                },
                configure_configure_params.ConfigureConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigureConfigureResponse,
        )


class AsyncConfigureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncConfigureResourceWithStreamingResponse(self)

    async def configure(
        self,
        org_id: str,
        *,
        client_id: str,
        client_secret: str,
        provider: Literal["google", "apple", "github"],
        redirect_uri: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigureConfigureResponse:
        """
        Configure OAuth for an organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/oauth/org/{org_id}/configure", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "provider": provider,
                    "redirect_uri": redirect_uri,
                },
                configure_configure_params.ConfigureConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigureConfigureResponse,
        )


class ConfigureResourceWithRawResponse:
    def __init__(self, configure: ConfigureResource) -> None:
        self._configure = configure

        self.configure = to_raw_response_wrapper(
            configure.configure,
        )


class AsyncConfigureResourceWithRawResponse:
    def __init__(self, configure: AsyncConfigureResource) -> None:
        self._configure = configure

        self.configure = async_to_raw_response_wrapper(
            configure.configure,
        )


class ConfigureResourceWithStreamingResponse:
    def __init__(self, configure: ConfigureResource) -> None:
        self._configure = configure

        self.configure = to_streamed_response_wrapper(
            configure.configure,
        )


class AsyncConfigureResourceWithStreamingResponse:
    def __init__(self, configure: AsyncConfigureResource) -> None:
        self._configure = configure

        self.configure = async_to_streamed_response_wrapper(
            configure.configure,
        )
