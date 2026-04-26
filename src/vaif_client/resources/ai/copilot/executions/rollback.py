# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
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
from .....types.ai.copilot.executions import rollback_rollback_params
from .....types.ai.copilot.executions.rollback_rollback_response import RollbackRollbackResponse

__all__ = ["RollbackResource", "AsyncRollbackResource"]


class RollbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RollbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return RollbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RollbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return RollbackResourceWithStreamingResponse(self)

    def rollback(
        self,
        execution_id: str,
        *,
        checkpoint_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RollbackRollbackResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._post(
            path_template("/ai/copilot/execution/{execution_id}/rollback", execution_id=execution_id),
            body=maybe_transform({"checkpoint_id": checkpoint_id}, rollback_rollback_params.RollbackRollbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RollbackRollbackResponse,
        )


class AsyncRollbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRollbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRollbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRollbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncRollbackResourceWithStreamingResponse(self)

    async def rollback(
        self,
        execution_id: str,
        *,
        checkpoint_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RollbackRollbackResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._post(
            path_template("/ai/copilot/execution/{execution_id}/rollback", execution_id=execution_id),
            body=await async_maybe_transform(
                {"checkpoint_id": checkpoint_id}, rollback_rollback_params.RollbackRollbackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RollbackRollbackResponse,
        )


class RollbackResourceWithRawResponse:
    def __init__(self, rollback: RollbackResource) -> None:
        self._rollback = rollback

        self.rollback = to_raw_response_wrapper(
            rollback.rollback,
        )


class AsyncRollbackResourceWithRawResponse:
    def __init__(self, rollback: AsyncRollbackResource) -> None:
        self._rollback = rollback

        self.rollback = async_to_raw_response_wrapper(
            rollback.rollback,
        )


class RollbackResourceWithStreamingResponse:
    def __init__(self, rollback: RollbackResource) -> None:
        self._rollback = rollback

        self.rollback = to_streamed_response_wrapper(
            rollback.rollback,
        )


class AsyncRollbackResourceWithStreamingResponse:
    def __init__(self, rollback: AsyncRollbackResource) -> None:
        self._rollback = rollback

        self.rollback = async_to_streamed_response_wrapper(
            rollback.rollback,
        )
