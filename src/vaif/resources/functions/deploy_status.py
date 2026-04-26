# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["DeployStatusResource", "AsyncDeployStatusResource"]


class DeployStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeployStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DeployStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeployStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DeployStatusResourceWithStreamingResponse(self)

    def get_deploy_status(
        self,
        function_id: str,
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
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/functions/{function_id}/deploy-status", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDeployStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeployStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeployStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeployStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDeployStatusResourceWithStreamingResponse(self)

    async def get_deploy_status(
        self,
        function_id: str,
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
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/functions/{function_id}/deploy-status", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DeployStatusResourceWithRawResponse:
    def __init__(self, deploy_status: DeployStatusResource) -> None:
        self._deploy_status = deploy_status

        self.get_deploy_status = to_raw_response_wrapper(
            deploy_status.get_deploy_status,
        )


class AsyncDeployStatusResourceWithRawResponse:
    def __init__(self, deploy_status: AsyncDeployStatusResource) -> None:
        self._deploy_status = deploy_status

        self.get_deploy_status = async_to_raw_response_wrapper(
            deploy_status.get_deploy_status,
        )


class DeployStatusResourceWithStreamingResponse:
    def __init__(self, deploy_status: DeployStatusResource) -> None:
        self._deploy_status = deploy_status

        self.get_deploy_status = to_streamed_response_wrapper(
            deploy_status.get_deploy_status,
        )


class AsyncDeployStatusResourceWithStreamingResponse:
    def __init__(self, deploy_status: AsyncDeployStatusResource) -> None:
        self._deploy_status = deploy_status

        self.get_deploy_status = async_to_streamed_response_wrapper(
            deploy_status.get_deploy_status,
        )
