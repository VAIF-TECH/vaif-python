# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.schema_engine import apply_create_params
from ...types.schema_engine.apply_create_response import ApplyCreateResponse

__all__ = ["ApplyResource", "AsyncApplyResource"]


class ApplyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApplyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ApplyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ApplyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        definition: apply_create_params.Definition,
        project_id: str,
        allow_destructive: bool | Omit = omit,
        env_id: str | Omit = omit,
        from_ai_workspace: bool | Omit = omit,
        migration_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplyCreateResponse:
        """
        Apply schema migration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/schema-engine/apply",
            body=maybe_transform(
                {
                    "definition": definition,
                    "project_id": project_id,
                    "allow_destructive": allow_destructive,
                    "env_id": env_id,
                    "from_ai_workspace": from_ai_workspace,
                    "migration_name": migration_name,
                },
                apply_create_params.ApplyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplyCreateResponse,
        )


class AsyncApplyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApplyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncApplyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        definition: apply_create_params.Definition,
        project_id: str,
        allow_destructive: bool | Omit = omit,
        env_id: str | Omit = omit,
        from_ai_workspace: bool | Omit = omit,
        migration_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplyCreateResponse:
        """
        Apply schema migration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/schema-engine/apply",
            body=await async_maybe_transform(
                {
                    "definition": definition,
                    "project_id": project_id,
                    "allow_destructive": allow_destructive,
                    "env_id": env_id,
                    "from_ai_workspace": from_ai_workspace,
                    "migration_name": migration_name,
                },
                apply_create_params.ApplyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplyCreateResponse,
        )


class ApplyResourceWithRawResponse:
    def __init__(self, apply: ApplyResource) -> None:
        self._apply = apply

        self.create = to_raw_response_wrapper(
            apply.create,
        )


class AsyncApplyResourceWithRawResponse:
    def __init__(self, apply: AsyncApplyResource) -> None:
        self._apply = apply

        self.create = async_to_raw_response_wrapper(
            apply.create,
        )


class ApplyResourceWithStreamingResponse:
    def __init__(self, apply: ApplyResource) -> None:
        self._apply = apply

        self.create = to_streamed_response_wrapper(
            apply.create,
        )


class AsyncApplyResourceWithStreamingResponse:
    def __init__(self, apply: AsyncApplyResource) -> None:
        self._apply = apply

        self.create = async_to_streamed_response_wrapper(
            apply.create,
        )
