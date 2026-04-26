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
from .me.me import (
    MeResource,
    AsyncMeResource,
    MeResourceWithRawResponse,
    AsyncMeResourceWithRawResponse,
    MeResourceWithStreamingResponse,
    AsyncMeResourceWithStreamingResponse,
)
from .logout import (
    LogoutResource,
    AsyncLogoutResource,
    LogoutResourceWithRawResponse,
    AsyncLogoutResourceWithRawResponse,
    LogoutResourceWithStreamingResponse,
    AsyncLogoutResourceWithStreamingResponse,
)
from .signup import (
    SignupResource,
    AsyncSignupResource,
    SignupResourceWithRawResponse,
    AsyncSignupResourceWithRawResponse,
    SignupResourceWithStreamingResponse,
    AsyncSignupResourceWithStreamingResponse,
)
from .cli.cli import (
    CliResource,
    AsyncCliResource,
    CliResourceWithRawResponse,
    AsyncCliResourceWithRawResponse,
    CliResourceWithStreamingResponse,
    AsyncCliResourceWithStreamingResponse,
)
from .refresh import (
    RefreshResource,
    AsyncRefreshResource,
    RefreshResourceWithRawResponse,
    AsyncRefreshResourceWithRawResponse,
    RefreshResourceWithStreamingResponse,
    AsyncRefreshResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .oauth.oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from .reset_password import (
    ResetPasswordResource,
    AsyncResetPasswordResource,
    ResetPasswordResourceWithRawResponse,
    AsyncResetPasswordResourceWithRawResponse,
    ResetPasswordResourceWithStreamingResponse,
    AsyncResetPasswordResourceWithStreamingResponse,
)
from .forgot_password import (
    ForgotPasswordResource,
    AsyncForgotPasswordResource,
    ForgotPasswordResourceWithRawResponse,
    AsyncForgotPasswordResourceWithRawResponse,
    ForgotPasswordResourceWithStreamingResponse,
    AsyncForgotPasswordResourceWithStreamingResponse,
)
from .verify_email.verify_email import (
    VerifyEmailResource,
    AsyncVerifyEmailResource,
    VerifyEmailResourceWithRawResponse,
    AsyncVerifyEmailResourceWithRawResponse,
    VerifyEmailResourceWithStreamingResponse,
    AsyncVerifyEmailResourceWithStreamingResponse,
)

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def cli(self) -> CliResource:
        return CliResource(self._client)

    @cached_property
    def forgot_password(self) -> ForgotPasswordResource:
        return ForgotPasswordResource(self._client)

    @cached_property
    def login(self) -> LoginResource:
        return LoginResource(self._client)

    @cached_property
    def logout(self) -> LogoutResource:
        return LogoutResource(self._client)

    @cached_property
    def me(self) -> MeResource:
        return MeResource(self._client)

    @cached_property
    def oauth(self) -> OAuthResource:
        return OAuthResource(self._client)

    @cached_property
    def refresh(self) -> RefreshResource:
        return RefreshResource(self._client)

    @cached_property
    def reset_password(self) -> ResetPasswordResource:
        return ResetPasswordResource(self._client)

    @cached_property
    def signup(self) -> SignupResource:
        return SignupResource(self._client)

    @cached_property
    def verify_email(self) -> VerifyEmailResource:
        return VerifyEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def cli(self) -> AsyncCliResource:
        return AsyncCliResource(self._client)

    @cached_property
    def forgot_password(self) -> AsyncForgotPasswordResource:
        return AsyncForgotPasswordResource(self._client)

    @cached_property
    def login(self) -> AsyncLoginResource:
        return AsyncLoginResource(self._client)

    @cached_property
    def logout(self) -> AsyncLogoutResource:
        return AsyncLogoutResource(self._client)

    @cached_property
    def me(self) -> AsyncMeResource:
        return AsyncMeResource(self._client)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        return AsyncOAuthResource(self._client)

    @cached_property
    def refresh(self) -> AsyncRefreshResource:
        return AsyncRefreshResource(self._client)

    @cached_property
    def reset_password(self) -> AsyncResetPasswordResource:
        return AsyncResetPasswordResource(self._client)

    @cached_property
    def signup(self) -> AsyncSignupResource:
        return AsyncSignupResource(self._client)

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResource:
        return AsyncVerifyEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def cli(self) -> CliResourceWithRawResponse:
        return CliResourceWithRawResponse(self._auth.cli)

    @cached_property
    def forgot_password(self) -> ForgotPasswordResourceWithRawResponse:
        return ForgotPasswordResourceWithRawResponse(self._auth.forgot_password)

    @cached_property
    def login(self) -> LoginResourceWithRawResponse:
        return LoginResourceWithRawResponse(self._auth.login)

    @cached_property
    def logout(self) -> LogoutResourceWithRawResponse:
        return LogoutResourceWithRawResponse(self._auth.logout)

    @cached_property
    def me(self) -> MeResourceWithRawResponse:
        return MeResourceWithRawResponse(self._auth.me)

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self._auth.oauth)

    @cached_property
    def refresh(self) -> RefreshResourceWithRawResponse:
        return RefreshResourceWithRawResponse(self._auth.refresh)

    @cached_property
    def reset_password(self) -> ResetPasswordResourceWithRawResponse:
        return ResetPasswordResourceWithRawResponse(self._auth.reset_password)

    @cached_property
    def signup(self) -> SignupResourceWithRawResponse:
        return SignupResourceWithRawResponse(self._auth.signup)

    @cached_property
    def verify_email(self) -> VerifyEmailResourceWithRawResponse:
        return VerifyEmailResourceWithRawResponse(self._auth.verify_email)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def cli(self) -> AsyncCliResourceWithRawResponse:
        return AsyncCliResourceWithRawResponse(self._auth.cli)

    @cached_property
    def forgot_password(self) -> AsyncForgotPasswordResourceWithRawResponse:
        return AsyncForgotPasswordResourceWithRawResponse(self._auth.forgot_password)

    @cached_property
    def login(self) -> AsyncLoginResourceWithRawResponse:
        return AsyncLoginResourceWithRawResponse(self._auth.login)

    @cached_property
    def logout(self) -> AsyncLogoutResourceWithRawResponse:
        return AsyncLogoutResourceWithRawResponse(self._auth.logout)

    @cached_property
    def me(self) -> AsyncMeResourceWithRawResponse:
        return AsyncMeResourceWithRawResponse(self._auth.me)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self._auth.oauth)

    @cached_property
    def refresh(self) -> AsyncRefreshResourceWithRawResponse:
        return AsyncRefreshResourceWithRawResponse(self._auth.refresh)

    @cached_property
    def reset_password(self) -> AsyncResetPasswordResourceWithRawResponse:
        return AsyncResetPasswordResourceWithRawResponse(self._auth.reset_password)

    @cached_property
    def signup(self) -> AsyncSignupResourceWithRawResponse:
        return AsyncSignupResourceWithRawResponse(self._auth.signup)

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResourceWithRawResponse:
        return AsyncVerifyEmailResourceWithRawResponse(self._auth.verify_email)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

    @cached_property
    def cli(self) -> CliResourceWithStreamingResponse:
        return CliResourceWithStreamingResponse(self._auth.cli)

    @cached_property
    def forgot_password(self) -> ForgotPasswordResourceWithStreamingResponse:
        return ForgotPasswordResourceWithStreamingResponse(self._auth.forgot_password)

    @cached_property
    def login(self) -> LoginResourceWithStreamingResponse:
        return LoginResourceWithStreamingResponse(self._auth.login)

    @cached_property
    def logout(self) -> LogoutResourceWithStreamingResponse:
        return LogoutResourceWithStreamingResponse(self._auth.logout)

    @cached_property
    def me(self) -> MeResourceWithStreamingResponse:
        return MeResourceWithStreamingResponse(self._auth.me)

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self._auth.oauth)

    @cached_property
    def refresh(self) -> RefreshResourceWithStreamingResponse:
        return RefreshResourceWithStreamingResponse(self._auth.refresh)

    @cached_property
    def reset_password(self) -> ResetPasswordResourceWithStreamingResponse:
        return ResetPasswordResourceWithStreamingResponse(self._auth.reset_password)

    @cached_property
    def signup(self) -> SignupResourceWithStreamingResponse:
        return SignupResourceWithStreamingResponse(self._auth.signup)

    @cached_property
    def verify_email(self) -> VerifyEmailResourceWithStreamingResponse:
        return VerifyEmailResourceWithStreamingResponse(self._auth.verify_email)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

    @cached_property
    def cli(self) -> AsyncCliResourceWithStreamingResponse:
        return AsyncCliResourceWithStreamingResponse(self._auth.cli)

    @cached_property
    def forgot_password(self) -> AsyncForgotPasswordResourceWithStreamingResponse:
        return AsyncForgotPasswordResourceWithStreamingResponse(self._auth.forgot_password)

    @cached_property
    def login(self) -> AsyncLoginResourceWithStreamingResponse:
        return AsyncLoginResourceWithStreamingResponse(self._auth.login)

    @cached_property
    def logout(self) -> AsyncLogoutResourceWithStreamingResponse:
        return AsyncLogoutResourceWithStreamingResponse(self._auth.logout)

    @cached_property
    def me(self) -> AsyncMeResourceWithStreamingResponse:
        return AsyncMeResourceWithStreamingResponse(self._auth.me)

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self._auth.oauth)

    @cached_property
    def refresh(self) -> AsyncRefreshResourceWithStreamingResponse:
        return AsyncRefreshResourceWithStreamingResponse(self._auth.refresh)

    @cached_property
    def reset_password(self) -> AsyncResetPasswordResourceWithStreamingResponse:
        return AsyncResetPasswordResourceWithStreamingResponse(self._auth.reset_password)

    @cached_property
    def signup(self) -> AsyncSignupResourceWithStreamingResponse:
        return AsyncSignupResourceWithStreamingResponse(self._auth.signup)

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResourceWithStreamingResponse:
        return AsyncVerifyEmailResourceWithStreamingResponse(self._auth.verify_email)
