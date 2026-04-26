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

__all__ = ["ValueResource", "AsyncValueResource"]


class ValueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ValueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ValueResourceWithStreamingResponse(self)

    def get_value(
        self,
        env_var_id: str,
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
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/projects/{project_id}/env-vars/{env_var_id}/value", project_id=project_id, env_var_id=env_var_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncValueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncValueResourceWithStreamingResponse(self)

    async def get_value(
        self,
        env_var_id: str,
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
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/projects/{project_id}/env-vars/{env_var_id}/value", project_id=project_id, env_var_id=env_var_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ValueResourceWithRawResponse:
    def __init__(self, value: ValueResource) -> None:
        self._value = value

        self.get_value = to_raw_response_wrapper(
            value.get_value,
        )


class AsyncValueResourceWithRawResponse:
    def __init__(self, value: AsyncValueResource) -> None:
        self._value = value

        self.get_value = async_to_raw_response_wrapper(
            value.get_value,
        )


class ValueResourceWithStreamingResponse:
    def __init__(self, value: ValueResource) -> None:
        self._value = value

        self.get_value = to_streamed_response_wrapper(
            value.get_value,
        )


class AsyncValueResourceWithStreamingResponse:
    def __init__(self, value: AsyncValueResource) -> None:
        self._value = value

        self.get_value = async_to_streamed_response_wrapper(
            value.get_value,
        )
