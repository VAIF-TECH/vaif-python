# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.plans import save_create_params
from ..._base_client import make_request_options
from ...types.plans.save_create_response import SaveCreateResponse

__all__ = ["SaveResource", "AsyncSaveResource"]


class SaveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SaveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SaveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SaveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SaveResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        org_id: str,
        plan: save_create_params.Plan,
        task_type: str,
        description: str | Omit = omit,
        visibility: Literal["public", "org_private", "unlisted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SaveCreateResponse:
        """
        Save an AI-generated plan

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/plans/save",
            body=maybe_transform(
                {
                    "name": name,
                    "org_id": org_id,
                    "plan": plan,
                    "task_type": task_type,
                    "description": description,
                    "visibility": visibility,
                },
                save_create_params.SaveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SaveCreateResponse,
        )


class AsyncSaveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSaveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSaveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSaveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSaveResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        org_id: str,
        plan: save_create_params.Plan,
        task_type: str,
        description: str | Omit = omit,
        visibility: Literal["public", "org_private", "unlisted"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SaveCreateResponse:
        """
        Save an AI-generated plan

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/plans/save",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "org_id": org_id,
                    "plan": plan,
                    "task_type": task_type,
                    "description": description,
                    "visibility": visibility,
                },
                save_create_params.SaveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SaveCreateResponse,
        )


class SaveResourceWithRawResponse:
    def __init__(self, save: SaveResource) -> None:
        self._save = save

        self.create = to_raw_response_wrapper(
            save.create,
        )


class AsyncSaveResourceWithRawResponse:
    def __init__(self, save: AsyncSaveResource) -> None:
        self._save = save

        self.create = async_to_raw_response_wrapper(
            save.create,
        )


class SaveResourceWithStreamingResponse:
    def __init__(self, save: SaveResource) -> None:
        self._save = save

        self.create = to_streamed_response_wrapper(
            save.create,
        )


class AsyncSaveResourceWithStreamingResponse:
    def __init__(self, save: AsyncSaveResource) -> None:
        self._save = save

        self.create = async_to_streamed_response_wrapper(
            save.create,
        )
