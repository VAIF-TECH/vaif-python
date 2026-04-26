# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .pause import (
    PauseResource,
    AsyncPauseResource,
    PauseResourceWithRawResponse,
    AsyncPauseResourceWithRawResponse,
    PauseResourceWithStreamingResponse,
    AsyncPauseResourceWithStreamingResponse,
)
from .resume import (
    ResumeResource,
    AsyncResumeResource,
    ResumeResourceWithRawResponse,
    AsyncResumeResourceWithRawResponse,
    ResumeResourceWithStreamingResponse,
    AsyncResumeResourceWithStreamingResponse,
)
from .rollback import (
    RollbackResource,
    AsyncRollbackResource,
    RollbackResourceWithRawResponse,
    AsyncRollbackResourceWithRawResponse,
    RollbackResourceWithStreamingResponse,
    AsyncRollbackResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def pause(self) -> PauseResource:
        return PauseResource(self._client)

    @cached_property
    def resume(self) -> ResumeResource:
        return ResumeResource(self._client)

    @cached_property
    def rollback(self) -> RollbackResource:
        return RollbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ExecutionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        execution_id: str,
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
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/ai/copilot/execution/{execution_id}", execution_id=execution_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve2(
        self,
        session_id: str,
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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/ai/copilot/executions/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def pause(self) -> AsyncPauseResource:
        return AsyncPauseResource(self._client)

    @cached_property
    def resume(self) -> AsyncResumeResource:
        return AsyncResumeResource(self._client)

    @cached_property
    def rollback(self) -> AsyncRollbackResource:
        return AsyncRollbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncExecutionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        execution_id: str,
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
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/ai/copilot/execution/{execution_id}", execution_id=execution_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve2(
        self,
        session_id: str,
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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/ai/copilot/executions/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_raw_response_wrapper(
            executions.retrieve,
        )
        self.retrieve2 = to_raw_response_wrapper(
            executions.retrieve2,
        )

    @cached_property
    def pause(self) -> PauseResourceWithRawResponse:
        return PauseResourceWithRawResponse(self._executions.pause)

    @cached_property
    def resume(self) -> ResumeResourceWithRawResponse:
        return ResumeResourceWithRawResponse(self._executions.resume)

    @cached_property
    def rollback(self) -> RollbackResourceWithRawResponse:
        return RollbackResourceWithRawResponse(self._executions.rollback)


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_raw_response_wrapper(
            executions.retrieve,
        )
        self.retrieve2 = async_to_raw_response_wrapper(
            executions.retrieve2,
        )

    @cached_property
    def pause(self) -> AsyncPauseResourceWithRawResponse:
        return AsyncPauseResourceWithRawResponse(self._executions.pause)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithRawResponse:
        return AsyncResumeResourceWithRawResponse(self._executions.resume)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithRawResponse:
        return AsyncRollbackResourceWithRawResponse(self._executions.rollback)


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.retrieve2 = to_streamed_response_wrapper(
            executions.retrieve2,
        )

    @cached_property
    def pause(self) -> PauseResourceWithStreamingResponse:
        return PauseResourceWithStreamingResponse(self._executions.pause)

    @cached_property
    def resume(self) -> ResumeResourceWithStreamingResponse:
        return ResumeResourceWithStreamingResponse(self._executions.resume)

    @cached_property
    def rollback(self) -> RollbackResourceWithStreamingResponse:
        return RollbackResourceWithStreamingResponse(self._executions.rollback)


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.retrieve = async_to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.retrieve2 = async_to_streamed_response_wrapper(
            executions.retrieve2,
        )

    @cached_property
    def pause(self) -> AsyncPauseResourceWithStreamingResponse:
        return AsyncPauseResourceWithStreamingResponse(self._executions.pause)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithStreamingResponse:
        return AsyncResumeResourceWithStreamingResponse(self._executions.resume)

    @cached_property
    def rollback(self) -> AsyncRollbackResourceWithStreamingResponse:
        return AsyncRollbackResourceWithStreamingResponse(self._executions.rollback)
