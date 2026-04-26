# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["DomainVerificationResource", "AsyncDomainVerificationResource"]


class DomainVerificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DomainVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DomainVerificationResourceWithStreamingResponse(self)

    def get_domain_verification(
        self,
        env_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not env_id:
            raise ValueError(f"Expected a non-empty value for `env_id` but received {env_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/projects/{project_id}/environments/{env_id}/domain-verification", project_id=project_id, env_id=env_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDomainVerificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDomainVerificationResourceWithStreamingResponse(self)

    async def get_domain_verification(
        self,
        env_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not env_id:
            raise ValueError(f"Expected a non-empty value for `env_id` but received {env_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/projects/{project_id}/environments/{env_id}/domain-verification", project_id=project_id, env_id=env_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DomainVerificationResourceWithRawResponse:
    def __init__(self, domain_verification: DomainVerificationResource) -> None:
        self._domain_verification = domain_verification

        self.get_domain_verification = to_raw_response_wrapper(
            domain_verification.get_domain_verification,
        )


class AsyncDomainVerificationResourceWithRawResponse:
    def __init__(self, domain_verification: AsyncDomainVerificationResource) -> None:
        self._domain_verification = domain_verification

        self.get_domain_verification = async_to_raw_response_wrapper(
            domain_verification.get_domain_verification,
        )


class DomainVerificationResourceWithStreamingResponse:
    def __init__(self, domain_verification: DomainVerificationResource) -> None:
        self._domain_verification = domain_verification

        self.get_domain_verification = to_streamed_response_wrapper(
            domain_verification.get_domain_verification,
        )


class AsyncDomainVerificationResourceWithStreamingResponse:
    def __init__(self, domain_verification: AsyncDomainVerificationResource) -> None:
        self._domain_verification = domain_verification

        self.get_domain_verification = async_to_streamed_response_wrapper(
            domain_verification.get_domain_verification,
        )
