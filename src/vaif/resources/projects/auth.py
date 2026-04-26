# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.projects import (
    auth_login_params,
    auth_signup_params,
    auth_update_params,
    auth_confirm_params,
    auth_settings_params,
    auth_reset_password_params,
    auth_forgot_password_params,
)
from ...types.projects.auth_login_response import AuthLoginResponse
from ...types.projects.auth_signup_response import AuthSignupResponse
from ...types.projects.auth_update_response import AuthUpdateResponse
from ...types.projects.auth_confirm_response import AuthConfirmResponse
from ...types.projects.auth_settings_response import AuthSettingsResponse
from ...types.projects.auth_reset_password_response import AuthResetPasswordResponse
from ...types.projects.auth_forgot_password_response import AuthForgotPasswordResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
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

    def update(
        self,
        provider: str,
        *,
        project_id: str,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        enabled: bool | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._put(
            path_template(
                "/projects/{project_id}/auth/oauth-apps/{provider}", project_id=project_id, provider=provider
            ),
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,
                    "enabled": enabled,
                    "scopes": scopes,
                },
                auth_update_params.AuthUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthUpdateResponse,
        )

    def delete(
        self,
        provider: str,
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
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/projects/{project_id}/auth/oauth-apps/{provider}", project_id=project_id, provider=provider
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def confirm(
        self,
        project_id: str,
        *,
        token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfirmResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/auth/verify-email/confirm", project_id=project_id),
            body=maybe_transform({"token": token}, auth_confirm_params.AuthConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfirmResponse,
        )

    def forgot_password(
        self,
        project_id: str,
        *,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthForgotPasswordResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/auth/forgot-password", project_id=project_id),
            body=maybe_transform({"email": email}, auth_forgot_password_params.AuthForgotPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthForgotPasswordResponse,
        )

    def get_me(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/auth/me", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_oauth_apps(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/auth/oauth-apps", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_settings(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/auth/settings", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def login(
        self,
        project_id: str,
        *,
        email: str | Omit = omit,
        password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthLoginResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/auth/login", project_id=project_id),
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLoginResponse,
        )

    def logout(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/auth/logout", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def refresh(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/auth/refresh", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def reset_password(
        self,
        project_id: str,
        *,
        token: str | Omit = omit,
        password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthResetPasswordResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/auth/reset-password", project_id=project_id),
            body=maybe_transform(
                {
                    "token": token,
                    "password": password,
                },
                auth_reset_password_params.AuthResetPasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthResetPasswordResponse,
        )

    def send(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/auth/verify-email/send", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def settings(
        self,
        project_id: str,
        *,
        access_token_lifetime_minutes: int | Omit = omit,
        allowed_redirect_urls: SequenceNotStr[str] | Omit = omit,
        allow_password_recovery: bool | Omit = omit,
        allow_sign_up: bool | Omit = omit,
        lockout_duration_minutes: int | Omit = omit,
        max_sign_in_attempts: int | Omit = omit,
        mfa_enabled: bool | Omit = omit,
        mfa_enforced: bool | Omit = omit,
        min_password_length: int | Omit = omit,
        refresh_token_lifetime_days: int | Omit = omit,
        require_email_verification: bool | Omit = omit,
        require_numbers: bool | Omit = omit,
        require_phone_verification: bool | Omit = omit,
        require_special_chars: bool | Omit = omit,
        require_uppercase: bool | Omit = omit,
        single_session_mode: bool | Omit = omit,
        user_table_auto_create: bool | Omit = omit,
        user_table_name: Optional[str] | Omit = omit,
        user_table_sync_fields: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._patch(
            path_template("/projects/{project_id}/auth/settings", project_id=project_id),
            body=maybe_transform(
                {
                    "access_token_lifetime_minutes": access_token_lifetime_minutes,
                    "allowed_redirect_urls": allowed_redirect_urls,
                    "allow_password_recovery": allow_password_recovery,
                    "allow_sign_up": allow_sign_up,
                    "lockout_duration_minutes": lockout_duration_minutes,
                    "max_sign_in_attempts": max_sign_in_attempts,
                    "mfa_enabled": mfa_enabled,
                    "mfa_enforced": mfa_enforced,
                    "min_password_length": min_password_length,
                    "refresh_token_lifetime_days": refresh_token_lifetime_days,
                    "require_email_verification": require_email_verification,
                    "require_numbers": require_numbers,
                    "require_phone_verification": require_phone_verification,
                    "require_special_chars": require_special_chars,
                    "require_uppercase": require_uppercase,
                    "single_session_mode": single_session_mode,
                    "user_table_auto_create": user_table_auto_create,
                    "user_table_name": user_table_name,
                    "user_table_sync_fields": user_table_sync_fields,
                },
                auth_settings_params.AuthSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSettingsResponse,
        )

    def signup(
        self,
        project_id: str,
        *,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        password: str | Omit = omit,
        phone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSignupResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/auth/signup", project_id=project_id),
            body=maybe_transform(
                {
                    "email": email,
                    "metadata": metadata,
                    "password": password,
                    "phone": phone,
                },
                auth_signup_params.AuthSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSignupResponse,
        )

    def sync_users(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/projects/{project_id}/auth/sync-users", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAuthResource(AsyncAPIResource):
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

    async def update(
        self,
        provider: str,
        *,
        project_id: str,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        enabled: bool | Omit = omit,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._put(
            path_template(
                "/projects/{project_id}/auth/oauth-apps/{provider}", project_id=project_id, provider=provider
            ),
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,
                    "enabled": enabled,
                    "scopes": scopes,
                },
                auth_update_params.AuthUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthUpdateResponse,
        )

    async def delete(
        self,
        provider: str,
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
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/projects/{project_id}/auth/oauth-apps/{provider}", project_id=project_id, provider=provider
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def confirm(
        self,
        project_id: str,
        *,
        token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthConfirmResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/auth/verify-email/confirm", project_id=project_id),
            body=await async_maybe_transform({"token": token}, auth_confirm_params.AuthConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthConfirmResponse,
        )

    async def forgot_password(
        self,
        project_id: str,
        *,
        email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthForgotPasswordResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/auth/forgot-password", project_id=project_id),
            body=await async_maybe_transform({"email": email}, auth_forgot_password_params.AuthForgotPasswordParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthForgotPasswordResponse,
        )

    async def get_me(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/auth/me", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_oauth_apps(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/auth/oauth-apps", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_settings(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/auth/settings", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def login(
        self,
        project_id: str,
        *,
        email: str | Omit = omit,
        password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthLoginResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/auth/login", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                auth_login_params.AuthLoginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthLoginResponse,
        )

    async def logout(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/auth/logout", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def refresh(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/auth/refresh", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def reset_password(
        self,
        project_id: str,
        *,
        token: str | Omit = omit,
        password: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthResetPasswordResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/auth/reset-password", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "token": token,
                    "password": password,
                },
                auth_reset_password_params.AuthResetPasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthResetPasswordResponse,
        )

    async def send(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/auth/verify-email/send", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def settings(
        self,
        project_id: str,
        *,
        access_token_lifetime_minutes: int | Omit = omit,
        allowed_redirect_urls: SequenceNotStr[str] | Omit = omit,
        allow_password_recovery: bool | Omit = omit,
        allow_sign_up: bool | Omit = omit,
        lockout_duration_minutes: int | Omit = omit,
        max_sign_in_attempts: int | Omit = omit,
        mfa_enabled: bool | Omit = omit,
        mfa_enforced: bool | Omit = omit,
        min_password_length: int | Omit = omit,
        refresh_token_lifetime_days: int | Omit = omit,
        require_email_verification: bool | Omit = omit,
        require_numbers: bool | Omit = omit,
        require_phone_verification: bool | Omit = omit,
        require_special_chars: bool | Omit = omit,
        require_uppercase: bool | Omit = omit,
        single_session_mode: bool | Omit = omit,
        user_table_auto_create: bool | Omit = omit,
        user_table_name: Optional[str] | Omit = omit,
        user_table_sync_fields: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._patch(
            path_template("/projects/{project_id}/auth/settings", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "access_token_lifetime_minutes": access_token_lifetime_minutes,
                    "allowed_redirect_urls": allowed_redirect_urls,
                    "allow_password_recovery": allow_password_recovery,
                    "allow_sign_up": allow_sign_up,
                    "lockout_duration_minutes": lockout_duration_minutes,
                    "max_sign_in_attempts": max_sign_in_attempts,
                    "mfa_enabled": mfa_enabled,
                    "mfa_enforced": mfa_enforced,
                    "min_password_length": min_password_length,
                    "refresh_token_lifetime_days": refresh_token_lifetime_days,
                    "require_email_verification": require_email_verification,
                    "require_numbers": require_numbers,
                    "require_phone_verification": require_phone_verification,
                    "require_special_chars": require_special_chars,
                    "require_uppercase": require_uppercase,
                    "single_session_mode": single_session_mode,
                    "user_table_auto_create": user_table_auto_create,
                    "user_table_name": user_table_name,
                    "user_table_sync_fields": user_table_sync_fields,
                },
                auth_settings_params.AuthSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSettingsResponse,
        )

    async def signup(
        self,
        project_id: str,
        *,
        email: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        password: str | Omit = omit,
        phone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSignupResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/auth/signup", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "metadata": metadata,
                    "password": password,
                    "phone": phone,
                },
                auth_signup_params.AuthSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthSignupResponse,
        )

    async def sync_users(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/projects/{project_id}/auth/sync-users", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.update = to_raw_response_wrapper(
            auth.update,
        )
        self.delete = to_raw_response_wrapper(
            auth.delete,
        )
        self.confirm = to_raw_response_wrapper(
            auth.confirm,
        )
        self.forgot_password = to_raw_response_wrapper(
            auth.forgot_password,
        )
        self.get_me = to_raw_response_wrapper(
            auth.get_me,
        )
        self.get_oauth_apps = to_raw_response_wrapper(
            auth.get_oauth_apps,
        )
        self.get_settings = to_raw_response_wrapper(
            auth.get_settings,
        )
        self.login = to_raw_response_wrapper(
            auth.login,
        )
        self.logout = to_raw_response_wrapper(
            auth.logout,
        )
        self.refresh = to_raw_response_wrapper(
            auth.refresh,
        )
        self.reset_password = to_raw_response_wrapper(
            auth.reset_password,
        )
        self.send = to_raw_response_wrapper(
            auth.send,
        )
        self.settings = to_raw_response_wrapper(
            auth.settings,
        )
        self.signup = to_raw_response_wrapper(
            auth.signup,
        )
        self.sync_users = to_raw_response_wrapper(
            auth.sync_users,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.update = async_to_raw_response_wrapper(
            auth.update,
        )
        self.delete = async_to_raw_response_wrapper(
            auth.delete,
        )
        self.confirm = async_to_raw_response_wrapper(
            auth.confirm,
        )
        self.forgot_password = async_to_raw_response_wrapper(
            auth.forgot_password,
        )
        self.get_me = async_to_raw_response_wrapper(
            auth.get_me,
        )
        self.get_oauth_apps = async_to_raw_response_wrapper(
            auth.get_oauth_apps,
        )
        self.get_settings = async_to_raw_response_wrapper(
            auth.get_settings,
        )
        self.login = async_to_raw_response_wrapper(
            auth.login,
        )
        self.logout = async_to_raw_response_wrapper(
            auth.logout,
        )
        self.refresh = async_to_raw_response_wrapper(
            auth.refresh,
        )
        self.reset_password = async_to_raw_response_wrapper(
            auth.reset_password,
        )
        self.send = async_to_raw_response_wrapper(
            auth.send,
        )
        self.settings = async_to_raw_response_wrapper(
            auth.settings,
        )
        self.signup = async_to_raw_response_wrapper(
            auth.signup,
        )
        self.sync_users = async_to_raw_response_wrapper(
            auth.sync_users,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.update = to_streamed_response_wrapper(
            auth.update,
        )
        self.delete = to_streamed_response_wrapper(
            auth.delete,
        )
        self.confirm = to_streamed_response_wrapper(
            auth.confirm,
        )
        self.forgot_password = to_streamed_response_wrapper(
            auth.forgot_password,
        )
        self.get_me = to_streamed_response_wrapper(
            auth.get_me,
        )
        self.get_oauth_apps = to_streamed_response_wrapper(
            auth.get_oauth_apps,
        )
        self.get_settings = to_streamed_response_wrapper(
            auth.get_settings,
        )
        self.login = to_streamed_response_wrapper(
            auth.login,
        )
        self.logout = to_streamed_response_wrapper(
            auth.logout,
        )
        self.refresh = to_streamed_response_wrapper(
            auth.refresh,
        )
        self.reset_password = to_streamed_response_wrapper(
            auth.reset_password,
        )
        self.send = to_streamed_response_wrapper(
            auth.send,
        )
        self.settings = to_streamed_response_wrapper(
            auth.settings,
        )
        self.signup = to_streamed_response_wrapper(
            auth.signup,
        )
        self.sync_users = to_streamed_response_wrapper(
            auth.sync_users,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.update = async_to_streamed_response_wrapper(
            auth.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            auth.delete,
        )
        self.confirm = async_to_streamed_response_wrapper(
            auth.confirm,
        )
        self.forgot_password = async_to_streamed_response_wrapper(
            auth.forgot_password,
        )
        self.get_me = async_to_streamed_response_wrapper(
            auth.get_me,
        )
        self.get_oauth_apps = async_to_streamed_response_wrapper(
            auth.get_oauth_apps,
        )
        self.get_settings = async_to_streamed_response_wrapper(
            auth.get_settings,
        )
        self.login = async_to_streamed_response_wrapper(
            auth.login,
        )
        self.logout = async_to_streamed_response_wrapper(
            auth.logout,
        )
        self.refresh = async_to_streamed_response_wrapper(
            auth.refresh,
        )
        self.reset_password = async_to_streamed_response_wrapper(
            auth.reset_password,
        )
        self.send = async_to_streamed_response_wrapper(
            auth.send,
        )
        self.settings = async_to_streamed_response_wrapper(
            auth.settings,
        )
        self.signup = async_to_streamed_response_wrapper(
            auth.signup,
        )
        self.sync_users = async_to_streamed_response_wrapper(
            auth.sync_users,
        )
