# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.projects.users import ban_ban_params
from ....types.projects.users.ban_ban_response import BanBanResponse

__all__ = ["BanResource", "AsyncBanResource"]


class BanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return BanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return BanResourceWithStreamingResponse(self)

    def ban(
        self,
        user_id: str,
        *,
        project_id: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BanBanResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/projects/{project_id}/users/{user_id}/ban", project_id=project_id, user_id=user_id),
            body=maybe_transform({"reason": reason}, ban_ban_params.BanBanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BanBanResponse,
        )


class AsyncBanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncBanResourceWithStreamingResponse(self)

    async def ban(
        self,
        user_id: str,
        *,
        project_id: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BanBanResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/users/{user_id}/ban", project_id=project_id, user_id=user_id),
            body=await async_maybe_transform({"reason": reason}, ban_ban_params.BanBanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BanBanResponse,
        )


class BanResourceWithRawResponse:
    def __init__(self, ban: BanResource) -> None:
        self._ban = ban

        self.ban = to_raw_response_wrapper(
            ban.ban,
        )


class AsyncBanResourceWithRawResponse:
    def __init__(self, ban: AsyncBanResource) -> None:
        self._ban = ban

        self.ban = async_to_raw_response_wrapper(
            ban.ban,
        )


class BanResourceWithStreamingResponse:
    def __init__(self, ban: BanResource) -> None:
        self._ban = ban

        self.ban = to_streamed_response_wrapper(
            ban.ban,
        )


class AsyncBanResourceWithStreamingResponse:
    def __init__(self, ban: AsyncBanResource) -> None:
        self._ban = ban

        self.ban = async_to_streamed_response_wrapper(
            ban.ban,
        )
