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
from .verify_cname import (
    VerifyCnameResource,
    AsyncVerifyCnameResource,
    VerifyCnameResourceWithRawResponse,
    AsyncVerifyCnameResourceWithRawResponse,
    VerifyCnameResourceWithStreamingResponse,
    AsyncVerifyCnameResourceWithStreamingResponse,
)
from .domain_status import (
    DomainStatusResource,
    AsyncDomainStatusResource,
    DomainStatusResourceWithRawResponse,
    AsyncDomainStatusResourceWithRawResponse,
    DomainStatusResourceWithStreamingResponse,
    AsyncDomainStatusResourceWithStreamingResponse,
)
from .provision_ssl import (
    ProvisionSslResource,
    AsyncProvisionSslResource,
    ProvisionSslResourceWithRawResponse,
    AsyncProvisionSslResourceWithRawResponse,
    ProvisionSslResourceWithStreamingResponse,
    AsyncProvisionSslResourceWithStreamingResponse,
)
from .verify_domain import (
    VerifyDomainResource,
    AsyncVerifyDomainResource,
    VerifyDomainResourceWithRawResponse,
    AsyncVerifyDomainResourceWithRawResponse,
    VerifyDomainResourceWithStreamingResponse,
    AsyncVerifyDomainResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .domain_verification import (
    DomainVerificationResource,
    AsyncDomainVerificationResource,
    DomainVerificationResourceWithRawResponse,
    AsyncDomainVerificationResourceWithRawResponse,
    DomainVerificationResourceWithStreamingResponse,
    AsyncDomainVerificationResourceWithStreamingResponse,
)

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def domain_status(self) -> DomainStatusResource:
        return DomainStatusResource(self._client)

    @cached_property
    def domain_verification(self) -> DomainVerificationResource:
        return DomainVerificationResource(self._client)

    @cached_property
    def provision_ssl(self) -> ProvisionSslResource:
        return ProvisionSslResource(self._client)

    @cached_property
    def verify_cname(self) -> VerifyCnameResource:
        return VerifyCnameResource(self._client)

    @cached_property
    def verify_domain(self) -> VerifyDomainResource:
        return VerifyDomainResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def update(
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
        return self._patch(
            path_template("/projects/{project_id}/environments/{env_id}", project_id=project_id, env_id=env_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
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
        return self._delete(
            path_template("/projects/{project_id}/environments/{env_id}", project_id=project_id, env_id=env_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def backfill_urls(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/environments/backfill-urls", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bootstrap(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/environments/bootstrap", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def environments(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/environments", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_environments(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/environments", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def domain_status(self) -> AsyncDomainStatusResource:
        return AsyncDomainStatusResource(self._client)

    @cached_property
    def domain_verification(self) -> AsyncDomainVerificationResource:
        return AsyncDomainVerificationResource(self._client)

    @cached_property
    def provision_ssl(self) -> AsyncProvisionSslResource:
        return AsyncProvisionSslResource(self._client)

    @cached_property
    def verify_cname(self) -> AsyncVerifyCnameResource:
        return AsyncVerifyCnameResource(self._client)

    @cached_property
    def verify_domain(self) -> AsyncVerifyDomainResource:
        return AsyncVerifyDomainResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def update(
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
        return await self._patch(
            path_template("/projects/{project_id}/environments/{env_id}", project_id=project_id, env_id=env_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
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
        return await self._delete(
            path_template("/projects/{project_id}/environments/{env_id}", project_id=project_id, env_id=env_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def backfill_urls(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/environments/backfill-urls", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bootstrap(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/environments/bootstrap", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def environments(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/environments", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_environments(
        self,
        project_id: str,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/environments", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.update = to_raw_response_wrapper(
            environments.update,
        )
        self.delete = to_raw_response_wrapper(
            environments.delete,
        )
        self.backfill_urls = to_raw_response_wrapper(
            environments.backfill_urls,
        )
        self.bootstrap = to_raw_response_wrapper(
            environments.bootstrap,
        )
        self.environments = to_raw_response_wrapper(
            environments.environments,
        )
        self.get_environments = to_raw_response_wrapper(
            environments.get_environments,
        )

    @cached_property
    def domain_status(self) -> DomainStatusResourceWithRawResponse:
        return DomainStatusResourceWithRawResponse(self._environments.domain_status)

    @cached_property
    def domain_verification(self) -> DomainVerificationResourceWithRawResponse:
        return DomainVerificationResourceWithRawResponse(self._environments.domain_verification)

    @cached_property
    def provision_ssl(self) -> ProvisionSslResourceWithRawResponse:
        return ProvisionSslResourceWithRawResponse(self._environments.provision_ssl)

    @cached_property
    def verify_cname(self) -> VerifyCnameResourceWithRawResponse:
        return VerifyCnameResourceWithRawResponse(self._environments.verify_cname)

    @cached_property
    def verify_domain(self) -> VerifyDomainResourceWithRawResponse:
        return VerifyDomainResourceWithRawResponse(self._environments.verify_domain)


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.update = async_to_raw_response_wrapper(
            environments.update,
        )
        self.delete = async_to_raw_response_wrapper(
            environments.delete,
        )
        self.backfill_urls = async_to_raw_response_wrapper(
            environments.backfill_urls,
        )
        self.bootstrap = async_to_raw_response_wrapper(
            environments.bootstrap,
        )
        self.environments = async_to_raw_response_wrapper(
            environments.environments,
        )
        self.get_environments = async_to_raw_response_wrapper(
            environments.get_environments,
        )

    @cached_property
    def domain_status(self) -> AsyncDomainStatusResourceWithRawResponse:
        return AsyncDomainStatusResourceWithRawResponse(self._environments.domain_status)

    @cached_property
    def domain_verification(self) -> AsyncDomainVerificationResourceWithRawResponse:
        return AsyncDomainVerificationResourceWithRawResponse(self._environments.domain_verification)

    @cached_property
    def provision_ssl(self) -> AsyncProvisionSslResourceWithRawResponse:
        return AsyncProvisionSslResourceWithRawResponse(self._environments.provision_ssl)

    @cached_property
    def verify_cname(self) -> AsyncVerifyCnameResourceWithRawResponse:
        return AsyncVerifyCnameResourceWithRawResponse(self._environments.verify_cname)

    @cached_property
    def verify_domain(self) -> AsyncVerifyDomainResourceWithRawResponse:
        return AsyncVerifyDomainResourceWithRawResponse(self._environments.verify_domain)


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.update = to_streamed_response_wrapper(
            environments.update,
        )
        self.delete = to_streamed_response_wrapper(
            environments.delete,
        )
        self.backfill_urls = to_streamed_response_wrapper(
            environments.backfill_urls,
        )
        self.bootstrap = to_streamed_response_wrapper(
            environments.bootstrap,
        )
        self.environments = to_streamed_response_wrapper(
            environments.environments,
        )
        self.get_environments = to_streamed_response_wrapper(
            environments.get_environments,
        )

    @cached_property
    def domain_status(self) -> DomainStatusResourceWithStreamingResponse:
        return DomainStatusResourceWithStreamingResponse(self._environments.domain_status)

    @cached_property
    def domain_verification(self) -> DomainVerificationResourceWithStreamingResponse:
        return DomainVerificationResourceWithStreamingResponse(self._environments.domain_verification)

    @cached_property
    def provision_ssl(self) -> ProvisionSslResourceWithStreamingResponse:
        return ProvisionSslResourceWithStreamingResponse(self._environments.provision_ssl)

    @cached_property
    def verify_cname(self) -> VerifyCnameResourceWithStreamingResponse:
        return VerifyCnameResourceWithStreamingResponse(self._environments.verify_cname)

    @cached_property
    def verify_domain(self) -> VerifyDomainResourceWithStreamingResponse:
        return VerifyDomainResourceWithStreamingResponse(self._environments.verify_domain)


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.update = async_to_streamed_response_wrapper(
            environments.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            environments.delete,
        )
        self.backfill_urls = async_to_streamed_response_wrapper(
            environments.backfill_urls,
        )
        self.bootstrap = async_to_streamed_response_wrapper(
            environments.bootstrap,
        )
        self.environments = async_to_streamed_response_wrapper(
            environments.environments,
        )
        self.get_environments = async_to_streamed_response_wrapper(
            environments.get_environments,
        )

    @cached_property
    def domain_status(self) -> AsyncDomainStatusResourceWithStreamingResponse:
        return AsyncDomainStatusResourceWithStreamingResponse(self._environments.domain_status)

    @cached_property
    def domain_verification(self) -> AsyncDomainVerificationResourceWithStreamingResponse:
        return AsyncDomainVerificationResourceWithStreamingResponse(self._environments.domain_verification)

    @cached_property
    def provision_ssl(self) -> AsyncProvisionSslResourceWithStreamingResponse:
        return AsyncProvisionSslResourceWithStreamingResponse(self._environments.provision_ssl)

    @cached_property
    def verify_cname(self) -> AsyncVerifyCnameResourceWithStreamingResponse:
        return AsyncVerifyCnameResourceWithStreamingResponse(self._environments.verify_cname)

    @cached_property
    def verify_domain(self) -> AsyncVerifyDomainResourceWithStreamingResponse:
        return AsyncVerifyDomainResourceWithStreamingResponse(self._environments.verify_domain)
