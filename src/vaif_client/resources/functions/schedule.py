# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.functions import schedule_schedule_params

__all__ = ["ScheduleResource", "AsyncScheduleResource"]


class ScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ScheduleResourceWithStreamingResponse(self)

    def get_schedule(
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
            path_template("/functions/{function_id}/schedule", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def schedule(
        self,
        function_id: str,
        *,
        cron: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._put(
            path_template("/functions/{function_id}/schedule", function_id=function_id),
            body=maybe_transform(
                {
                    "cron": cron,
                    "enabled": enabled,
                },
                schedule_schedule_params.ScheduleScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def schedule2(
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
        return self._delete(
            path_template("/functions/{function_id}/schedule", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncScheduleResourceWithStreamingResponse(self)

    async def get_schedule(
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
            path_template("/functions/{function_id}/schedule", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def schedule(
        self,
        function_id: str,
        *,
        cron: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._put(
            path_template("/functions/{function_id}/schedule", function_id=function_id),
            body=await async_maybe_transform(
                {
                    "cron": cron,
                    "enabled": enabled,
                },
                schedule_schedule_params.ScheduleScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def schedule2(
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
        return await self._delete(
            path_template("/functions/{function_id}/schedule", function_id=function_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ScheduleResourceWithRawResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.get_schedule = to_raw_response_wrapper(
            schedule.get_schedule,
        )
        self.schedule = to_raw_response_wrapper(
            schedule.schedule,
        )
        self.schedule2 = to_raw_response_wrapper(
            schedule.schedule2,
        )


class AsyncScheduleResourceWithRawResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.get_schedule = async_to_raw_response_wrapper(
            schedule.get_schedule,
        )
        self.schedule = async_to_raw_response_wrapper(
            schedule.schedule,
        )
        self.schedule2 = async_to_raw_response_wrapper(
            schedule.schedule2,
        )


class ScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.get_schedule = to_streamed_response_wrapper(
            schedule.get_schedule,
        )
        self.schedule = to_streamed_response_wrapper(
            schedule.schedule,
        )
        self.schedule2 = to_streamed_response_wrapper(
            schedule.schedule2,
        )


class AsyncScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.get_schedule = async_to_streamed_response_wrapper(
            schedule.get_schedule,
        )
        self.schedule = async_to_streamed_response_wrapper(
            schedule.schedule,
        )
        self.schedule2 = async_to_streamed_response_wrapper(
            schedule.schedule2,
        )
