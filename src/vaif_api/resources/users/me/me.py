# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from .preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .change_password import (
    ChangePasswordResource,
    AsyncChangePasswordResource,
    ChangePasswordResourceWithRawResponse,
    AsyncChangePasswordResourceWithRawResponse,
    ChangePasswordResourceWithStreamingResponse,
    AsyncChangePasswordResourceWithStreamingResponse,
)
from .request_account_delete import (
    RequestAccountDeleteResource,
    AsyncRequestAccountDeleteResource,
    RequestAccountDeleteResourceWithRawResponse,
    AsyncRequestAccountDeleteResourceWithRawResponse,
    RequestAccountDeleteResourceWithStreamingResponse,
    AsyncRequestAccountDeleteResourceWithStreamingResponse,
)

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def change_password(self) -> ChangePasswordResource:
        return ChangePasswordResource(self._client)

    @cached_property
    def preferences(self) -> PreferencesResource:
        return PreferencesResource(self._client)

    @cached_property
    def request_account_delete(self) -> RequestAccountDeleteResource:
        return RequestAccountDeleteResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            "/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def change_password(self) -> AsyncChangePasswordResource:
        return AsyncChangePasswordResource(self._client)

    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        return AsyncPreferencesResource(self._client)

    @cached_property
    def request_account_delete(self) -> AsyncRequestAccountDeleteResource:
        return AsyncRequestAccountDeleteResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            "/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.update = to_raw_response_wrapper(
            me.update,
        )
        self.list = to_raw_response_wrapper(
            me.list,
        )

    @cached_property
    def change_password(self) -> ChangePasswordResourceWithRawResponse:
        return ChangePasswordResourceWithRawResponse(self._me.change_password)

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        return PreferencesResourceWithRawResponse(self._me.preferences)

    @cached_property
    def request_account_delete(self) -> RequestAccountDeleteResourceWithRawResponse:
        return RequestAccountDeleteResourceWithRawResponse(self._me.request_account_delete)


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.update = async_to_raw_response_wrapper(
            me.update,
        )
        self.list = async_to_raw_response_wrapper(
            me.list,
        )

    @cached_property
    def change_password(self) -> AsyncChangePasswordResourceWithRawResponse:
        return AsyncChangePasswordResourceWithRawResponse(self._me.change_password)

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        return AsyncPreferencesResourceWithRawResponse(self._me.preferences)

    @cached_property
    def request_account_delete(self) -> AsyncRequestAccountDeleteResourceWithRawResponse:
        return AsyncRequestAccountDeleteResourceWithRawResponse(self._me.request_account_delete)


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.update = to_streamed_response_wrapper(
            me.update,
        )
        self.list = to_streamed_response_wrapper(
            me.list,
        )

    @cached_property
    def change_password(self) -> ChangePasswordResourceWithStreamingResponse:
        return ChangePasswordResourceWithStreamingResponse(self._me.change_password)

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        return PreferencesResourceWithStreamingResponse(self._me.preferences)

    @cached_property
    def request_account_delete(self) -> RequestAccountDeleteResourceWithStreamingResponse:
        return RequestAccountDeleteResourceWithStreamingResponse(self._me.request_account_delete)


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.update = async_to_streamed_response_wrapper(
            me.update,
        )
        self.list = async_to_streamed_response_wrapper(
            me.list,
        )

    @cached_property
    def change_password(self) -> AsyncChangePasswordResourceWithStreamingResponse:
        return AsyncChangePasswordResourceWithStreamingResponse(self._me.change_password)

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        return AsyncPreferencesResourceWithStreamingResponse(self._me.preferences)

    @cached_property
    def request_account_delete(self) -> AsyncRequestAccountDeleteResourceWithStreamingResponse:
        return AsyncRequestAccountDeleteResourceWithStreamingResponse(self._me.request_account_delete)
