# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from .....types.ai.copilot.executions import resume_resume_params
from .....types.ai.copilot.executions.resume_resume_response import ResumeResumeResponse

__all__ = ["ResumeResource", "AsyncResumeResource"]


class ResumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ResumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ResumeResourceWithStreamingResponse(self)

    def resume(
        self,
        execution_id: str,
        *,
        from_checkpoint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeResumeResponse:
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
            path_template("/ai/copilot/execution/{execution_id}/resume", execution_id=execution_id),
            body=maybe_transform({"from_checkpoint": from_checkpoint}, resume_resume_params.ResumeResumeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeResumeResponse,
        )


class AsyncResumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncResumeResourceWithStreamingResponse(self)

    async def resume(
        self,
        execution_id: str,
        *,
        from_checkpoint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResumeResumeResponse:
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
            path_template("/ai/copilot/execution/{execution_id}/resume", execution_id=execution_id),
            body=await async_maybe_transform(
                {"from_checkpoint": from_checkpoint}, resume_resume_params.ResumeResumeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResumeResumeResponse,
        )


class ResumeResourceWithRawResponse:
    def __init__(self, resume: ResumeResource) -> None:
        self._resume = resume

        self.resume = to_raw_response_wrapper(
            resume.resume,
        )


class AsyncResumeResourceWithRawResponse:
    def __init__(self, resume: AsyncResumeResource) -> None:
        self._resume = resume

        self.resume = async_to_raw_response_wrapper(
            resume.resume,
        )


class ResumeResourceWithStreamingResponse:
    def __init__(self, resume: ResumeResource) -> None:
        self._resume = resume

        self.resume = to_streamed_response_wrapper(
            resume.resume,
        )


class AsyncResumeResourceWithStreamingResponse:
    def __init__(self, resume: AsyncResumeResource) -> None:
        self._resume = resume

        self.resume = async_to_streamed_response_wrapper(
            resume.resume,
        )
