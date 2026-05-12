# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["AtomResource", "AsyncAtomResource"]


class AtomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AtomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AtomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AtomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AtomResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Atom feed for incidents"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/status/atom",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAtomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAtomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAtomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAtomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAtomResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Atom feed for incidents"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/status/atom",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AtomResourceWithRawResponse:
    def __init__(self, atom: AtomResource) -> None:
        self._atom = atom

        self.list = to_raw_response_wrapper(
            atom.list,
        )


class AsyncAtomResourceWithRawResponse:
    def __init__(self, atom: AsyncAtomResource) -> None:
        self._atom = atom

        self.list = async_to_raw_response_wrapper(
            atom.list,
        )


class AtomResourceWithStreamingResponse:
    def __init__(self, atom: AtomResource) -> None:
        self._atom = atom

        self.list = to_streamed_response_wrapper(
            atom.list,
        )


class AsyncAtomResourceWithStreamingResponse:
    def __init__(self, atom: AsyncAtomResource) -> None:
        self._atom = atom

        self.list = async_to_streamed_response_wrapper(
            atom.list,
        )
