# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from .stream import (
    StreamResource,
    AsyncStreamResource,
    StreamResourceWithRawResponse,
    AsyncStreamResourceWithRawResponse,
    StreamResourceWithStreamingResponse,
    AsyncStreamResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ai.copilot import chat_create_params

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def stream(self) -> StreamResource:
        return StreamResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message: str,
        project_id: str,
        attachments: Iterable[chat_create_params.Attachment] | Omit = omit,
        generation_options: chat_create_params.GenerationOptions | Omit = omit,
        generation_types: List[Literal["schema", "storage", "functions", "backend", "fullstack"]] | Omit = omit,
        model_id: str | Omit = omit,
        pinned_context: chat_create_params.PinnedContext | Omit = omit,
        session_id: str | Omit = omit,
        stream: bool | Omit = omit,
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
        return self._post(
            "/ai/copilot/chat",
            body=maybe_transform(
                {
                    "message": message,
                    "project_id": project_id,
                    "attachments": attachments,
                    "generation_options": generation_options,
                    "generation_types": generation_types,
                    "model_id": model_id,
                    "pinned_context": pinned_context,
                    "session_id": session_id,
                    "stream": stream,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def stream(self) -> AsyncStreamResource:
        return AsyncStreamResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message: str,
        project_id: str,
        attachments: Iterable[chat_create_params.Attachment] | Omit = omit,
        generation_options: chat_create_params.GenerationOptions | Omit = omit,
        generation_types: List[Literal["schema", "storage", "functions", "backend", "fullstack"]] | Omit = omit,
        model_id: str | Omit = omit,
        pinned_context: chat_create_params.PinnedContext | Omit = omit,
        session_id: str | Omit = omit,
        stream: bool | Omit = omit,
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
        return await self._post(
            "/ai/copilot/chat",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "project_id": project_id,
                    "attachments": attachments,
                    "generation_options": generation_options,
                    "generation_types": generation_types,
                    "model_id": model_id,
                    "pinned_context": pinned_context,
                    "session_id": session_id,
                    "stream": stream,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_raw_response_wrapper(
            chat.create,
        )

    @cached_property
    def stream(self) -> StreamResourceWithRawResponse:
        return StreamResourceWithRawResponse(self._chat.stream)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_raw_response_wrapper(
            chat.create,
        )

    @cached_property
    def stream(self) -> AsyncStreamResourceWithRawResponse:
        return AsyncStreamResourceWithRawResponse(self._chat.stream)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_streamed_response_wrapper(
            chat.create,
        )

    @cached_property
    def stream(self) -> StreamResourceWithStreamingResponse:
        return StreamResourceWithStreamingResponse(self._chat.stream)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_streamed_response_wrapper(
            chat.create,
        )

    @cached_property
    def stream(self) -> AsyncStreamResourceWithStreamingResponse:
        return AsyncStreamResourceWithStreamingResponse(self._chat.stream)
