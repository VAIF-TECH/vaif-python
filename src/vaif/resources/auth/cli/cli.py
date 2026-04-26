# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .login import (
    LoginResource,
    AsyncLoginResource,
    LoginResourceWithRawResponse,
    AsyncLoginResourceWithRawResponse,
    LoginResourceWithStreamingResponse,
    AsyncLoginResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .callback import (
    CallbackResource,
    AsyncCallbackResource,
    CallbackResourceWithRawResponse,
    AsyncCallbackResourceWithRawResponse,
    CallbackResourceWithStreamingResponse,
    AsyncCallbackResourceWithStreamingResponse,
)
from .authorize import (
    AuthorizeResource,
    AsyncAuthorizeResource,
    AuthorizeResourceWithRawResponse,
    AsyncAuthorizeResourceWithRawResponse,
    AuthorizeResourceWithStreamingResponse,
    AsyncAuthorizeResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CliResource", "AsyncCliResource"]


class CliResource(SyncAPIResource):
    @cached_property
    def authorize(self) -> AuthorizeResource:
        return AuthorizeResource(self._client)

    @cached_property
    def callback(self) -> CallbackResource:
        return CallbackResource(self._client)

    @cached_property
    def login(self) -> LoginResource:
        return LoginResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def with_raw_response(self) -> CliResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CliResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CliResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CliResourceWithStreamingResponse(self)


class AsyncCliResource(AsyncAPIResource):
    @cached_property
    def authorize(self) -> AsyncAuthorizeResource:
        return AsyncAuthorizeResource(self._client)

    @cached_property
    def callback(self) -> AsyncCallbackResource:
        return AsyncCallbackResource(self._client)

    @cached_property
    def login(self) -> AsyncLoginResource:
        return AsyncLoginResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCliResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCliResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCliResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCliResourceWithStreamingResponse(self)


class CliResourceWithRawResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

    @cached_property
    def authorize(self) -> AuthorizeResourceWithRawResponse:
        return AuthorizeResourceWithRawResponse(self._cli.authorize)

    @cached_property
    def callback(self) -> CallbackResourceWithRawResponse:
        return CallbackResourceWithRawResponse(self._cli.callback)

    @cached_property
    def login(self) -> LoginResourceWithRawResponse:
        return LoginResourceWithRawResponse(self._cli.login)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._cli.token)


class AsyncCliResourceWithRawResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

    @cached_property
    def authorize(self) -> AsyncAuthorizeResourceWithRawResponse:
        return AsyncAuthorizeResourceWithRawResponse(self._cli.authorize)

    @cached_property
    def callback(self) -> AsyncCallbackResourceWithRawResponse:
        return AsyncCallbackResourceWithRawResponse(self._cli.callback)

    @cached_property
    def login(self) -> AsyncLoginResourceWithRawResponse:
        return AsyncLoginResourceWithRawResponse(self._cli.login)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._cli.token)


class CliResourceWithStreamingResponse:
    def __init__(self, cli: CliResource) -> None:
        self._cli = cli

    @cached_property
    def authorize(self) -> AuthorizeResourceWithStreamingResponse:
        return AuthorizeResourceWithStreamingResponse(self._cli.authorize)

    @cached_property
    def callback(self) -> CallbackResourceWithStreamingResponse:
        return CallbackResourceWithStreamingResponse(self._cli.callback)

    @cached_property
    def login(self) -> LoginResourceWithStreamingResponse:
        return LoginResourceWithStreamingResponse(self._cli.login)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._cli.token)


class AsyncCliResourceWithStreamingResponse:
    def __init__(self, cli: AsyncCliResource) -> None:
        self._cli = cli

    @cached_property
    def authorize(self) -> AsyncAuthorizeResourceWithStreamingResponse:
        return AsyncAuthorizeResourceWithStreamingResponse(self._cli.authorize)

    @cached_property
    def callback(self) -> AsyncCallbackResourceWithStreamingResponse:
        return AsyncCallbackResourceWithStreamingResponse(self._cli.callback)

    @cached_property
    def login(self) -> AsyncLoginResourceWithStreamingResponse:
        return AsyncLoginResourceWithStreamingResponse(self._cli.login)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._cli.token)
