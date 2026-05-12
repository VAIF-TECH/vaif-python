# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .steps import (
    StepsResource,
    AsyncStepsResource,
    StepsResourceWithRawResponse,
    AsyncStepsResourceWithRawResponse,
    StepsResourceWithStreamingResponse,
    AsyncStepsResourceWithStreamingResponse,
)
from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from .promote import (
    PromoteResource,
    AsyncPromoteResource,
    PromoteResourceWithRawResponse,
    AsyncPromoteResourceWithRawResponse,
    PromoteResourceWithStreamingResponse,
    AsyncPromoteResourceWithStreamingResponse,
)
from .trigger import (
    TriggerResource,
    AsyncTriggerResource,
    TriggerResourceWithRawResponse,
    AsyncTriggerResourceWithRawResponse,
    TriggerResourceWithStreamingResponse,
    AsyncTriggerResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from .rollback import (
    RollbackResource,
    AsyncRollbackResource,
    RollbackResourceWithRawResponse,
    AsyncRollbackResourceWithRawResponse,
    RollbackResourceWithStreamingResponse,
    AsyncRollbackResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .tokens.tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from ..._base_client import make_request_options

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def promote(self) -> PromoteResource:
        return PromoteResource(self._client)

    @cached_property
    def rollback(self) -> RollbackResource:
        return RollbackResource(self._client)

    @cached_property
    def steps(self) -> StepsResource:
        return StepsResource(self._client)

    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def trigger(self) -> TriggerResource:
        return TriggerResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        deployment_id: str,
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
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/deployments/{deployment_id}", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def promote(self) -> AsyncPromoteResource:
        return AsyncPromoteResource(self._client)

    @cached_property
    def rollback(self) -> AsyncRollbackResource:
        return AsyncRollbackResource(self._client)

    @cached_property
    def steps(self) -> AsyncStepsResource:
        return AsyncStepsResource(self._client)

    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def trigger(self) -> AsyncTriggerResource:
        return AsyncTriggerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        deployment_id: str,
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
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/deployments/{deployment_id}", deployment_id=deployment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.retrieve = to_raw_response_wrapper(
            deployments.retrieve,
        )

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._deployments.project)

    @cached_property
    def promote(self) -> PromoteResourceWithRawResponse:
        return PromoteResourceWithRawResponse(self._deployments.promote)

    @cached_property
    def rollback(self) -> RollbackResourceWithRawResponse:
        return RollbackResourceWithRawResponse(self._deployments.rollback)

    @cached_property
    def steps(self) -> StepsResourceWithRawResponse:
        return StepsResourceWithRawResponse(self._deployments.steps)

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._deployments.tokens)

    @cached_property
    def trigger(self) -> TriggerResourceWithRawResponse:
        return TriggerResourceWithRawResponse(self._deployments.trigger)


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.retrieve = async_to_raw_response_wrapper(
            deployments.retrieve,
        )

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._deployments.project)

    @cached_property
    def promote(self) -> AsyncPromoteResourceWithRawResponse:
        return AsyncPromoteResourceWithRawResponse(self._deployments.promote)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithRawResponse:
        return AsyncRollbackResourceWithRawResponse(self._deployments.rollback)

    @cached_property
    def steps(self) -> AsyncStepsResourceWithRawResponse:
        return AsyncStepsResourceWithRawResponse(self._deployments.steps)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._deployments.tokens)

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithRawResponse:
        return AsyncTriggerResourceWithRawResponse(self._deployments.trigger)


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.retrieve = to_streamed_response_wrapper(
            deployments.retrieve,
        )

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._deployments.project)

    @cached_property
    def promote(self) -> PromoteResourceWithStreamingResponse:
        return PromoteResourceWithStreamingResponse(self._deployments.promote)

    @cached_property
    def rollback(self) -> RollbackResourceWithStreamingResponse:
        return RollbackResourceWithStreamingResponse(self._deployments.rollback)

    @cached_property
    def steps(self) -> StepsResourceWithStreamingResponse:
        return StepsResourceWithStreamingResponse(self._deployments.steps)

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._deployments.tokens)

    @cached_property
    def trigger(self) -> TriggerResourceWithStreamingResponse:
        return TriggerResourceWithStreamingResponse(self._deployments.trigger)


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.retrieve = async_to_streamed_response_wrapper(
            deployments.retrieve,
        )

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._deployments.project)

    @cached_property
    def promote(self) -> AsyncPromoteResourceWithStreamingResponse:
        return AsyncPromoteResourceWithStreamingResponse(self._deployments.promote)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithStreamingResponse:
        return AsyncRollbackResourceWithStreamingResponse(self._deployments.rollback)

    @cached_property
    def steps(self) -> AsyncStepsResourceWithStreamingResponse:
        return AsyncStepsResourceWithStreamingResponse(self._deployments.steps)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._deployments.tokens)

    @cached_property
    def trigger(self) -> AsyncTriggerResourceWithStreamingResponse:
        return AsyncTriggerResourceWithStreamingResponse(self._deployments.trigger)
