# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from .rollback import (
    RollbackResource,
    AsyncRollbackResource,
    RollbackResourceWithRawResponse,
    AsyncRollbackResourceWithRawResponse,
    RollbackResourceWithStreamingResponse,
    AsyncRollbackResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from .....types.ai.copilot import deploy_create_params

__all__ = ["DeployResource", "AsyncDeployResource"]


class DeployResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def rollback(self) -> RollbackResource:
        return RollbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeployResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DeployResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeployResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DeployResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        resources: Iterable[deploy_create_params.Resource],
        dry_run: bool | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deploy Copilot-generated resources (SSE stream)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/ai/copilot/deploy",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "resources": resources,
                    "dry_run": dry_run,
                    "session_id": session_id,
                },
                deploy_create_params.DeployCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        deploy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get a single deploy record

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deploy_id:
            raise ValueError(f"Expected a non-empty value for `deploy_id` but received {deploy_id!r}")
        return self._get(
            path_template("/ai/copilot/deploy/{deploy_id}", deploy_id=deploy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDeployResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def rollback(self) -> AsyncRollbackResource:
        return AsyncRollbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeployResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeployResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeployResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDeployResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        resources: Iterable[deploy_create_params.Resource],
        dry_run: bool | Omit = omit,
        session_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deploy Copilot-generated resources (SSE stream)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/ai/copilot/deploy",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "resources": resources,
                    "dry_run": dry_run,
                    "session_id": session_id,
                },
                deploy_create_params.DeployCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        deploy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get a single deploy record

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deploy_id:
            raise ValueError(f"Expected a non-empty value for `deploy_id` but received {deploy_id!r}")
        return await self._get(
            path_template("/ai/copilot/deploy/{deploy_id}", deploy_id=deploy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DeployResourceWithRawResponse:
    def __init__(self, deploy: DeployResource) -> None:
        self._deploy = deploy

        self.create = to_raw_response_wrapper(
            deploy.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deploy.retrieve,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._deploy.history)

    @cached_property
    def rollback(self) -> RollbackResourceWithRawResponse:
        return RollbackResourceWithRawResponse(self._deploy.rollback)


class AsyncDeployResourceWithRawResponse:
    def __init__(self, deploy: AsyncDeployResource) -> None:
        self._deploy = deploy

        self.create = async_to_raw_response_wrapper(
            deploy.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deploy.retrieve,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._deploy.history)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithRawResponse:
        return AsyncRollbackResourceWithRawResponse(self._deploy.rollback)


class DeployResourceWithStreamingResponse:
    def __init__(self, deploy: DeployResource) -> None:
        self._deploy = deploy

        self.create = to_streamed_response_wrapper(
            deploy.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deploy.retrieve,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._deploy.history)

    @cached_property
    def rollback(self) -> RollbackResourceWithStreamingResponse:
        return RollbackResourceWithStreamingResponse(self._deploy.rollback)


class AsyncDeployResourceWithStreamingResponse:
    def __init__(self, deploy: AsyncDeployResource) -> None:
        self._deploy = deploy

        self.create = async_to_streamed_response_wrapper(
            deploy.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deploy.retrieve,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._deploy.history)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithStreamingResponse:
        return AsyncRollbackResourceWithStreamingResponse(self._deploy.rollback)
