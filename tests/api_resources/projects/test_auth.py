# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.projects import (
    AuthLoginResponse,
    AuthSignupResponse,
    AuthUpdateResponse,
    AuthConfirmResponse,
    AuthSettingsResponse,
    AuthResetPasswordResponse,
    AuthForgotPasswordResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        auth = client.projects.auth.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
        )
        assert_matches_type(AuthUpdateResponse, auth, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
            enabled=True,
            scopes=["string"],
        )
        assert_matches_type(AuthUpdateResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthUpdateResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthUpdateResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.update(
                provider="provider",
                project_id="",
                client_id="x",
                client_secret="x",
                redirect_uri="https://example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.projects.auth.with_raw_response.update(
                provider="",
                project_id="projectId",
                client_id="x",
                client_secret="x",
                redirect_uri="https://example.com",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        auth = client.projects.auth.delete(
            provider="provider",
            project_id="projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.delete(
            provider="provider",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.delete(
            provider="provider",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.delete(
                provider="provider",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.projects.auth.with_raw_response.delete(
                provider="",
                project_id="projectId",
            )

    @parametrize
    def test_method_confirm(self, client: Vaif) -> None:
        auth = client.projects.auth.confirm(
            project_id="projectId",
        )
        assert_matches_type(AuthConfirmResponse, auth, path=["response"])

    @parametrize
    def test_method_confirm_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.confirm(
            project_id="projectId",
            token="x",
        )
        assert_matches_type(AuthConfirmResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_confirm(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.confirm(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthConfirmResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_confirm(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.confirm(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthConfirmResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_confirm(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.confirm(
                project_id="",
            )

    @parametrize
    def test_method_forgot_password(self, client: Vaif) -> None:
        auth = client.projects.auth.forgot_password(
            project_id="projectId",
        )
        assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

    @parametrize
    def test_method_forgot_password_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.forgot_password(
            project_id="projectId",
            email="dev@stainless.com",
        )
        assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_forgot_password(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.forgot_password(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_forgot_password(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.forgot_password(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_forgot_password(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.forgot_password(
                project_id="",
            )

    @parametrize
    def test_method_get_me(self, client: Vaif) -> None:
        auth = client.projects.auth.get_me(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_get_me(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.get_me(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_get_me(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.get_me(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_me(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.get_me(
                "",
            )

    @parametrize
    def test_method_get_oauth_apps(self, client: Vaif) -> None:
        auth = client.projects.auth.get_oauth_apps(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_get_oauth_apps(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.get_oauth_apps(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_get_oauth_apps(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.get_oauth_apps(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_oauth_apps(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.get_oauth_apps(
                "",
            )

    @parametrize
    def test_method_get_settings(self, client: Vaif) -> None:
        auth = client.projects.auth.get_settings(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_get_settings(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.get_settings(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_get_settings(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.get_settings(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_settings(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.get_settings(
                "",
            )

    @parametrize
    def test_method_login(self, client: Vaif) -> None:
        auth = client.projects.auth.login(
            project_id="projectId",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    def test_method_login_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.login(
            project_id="projectId",
            email="dev@stainless.com",
            password="x",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_login(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.login(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_login(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.login(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_login(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.login(
                project_id="",
            )

    @parametrize
    def test_method_logout(self, client: Vaif) -> None:
        auth = client.projects.auth.logout(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_logout(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.logout(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_logout(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.logout(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_logout(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.logout(
                "",
            )

    @parametrize
    def test_method_refresh(self, client: Vaif) -> None:
        auth = client.projects.auth.refresh(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_refresh(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.refresh(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_refresh(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.refresh(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refresh(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.refresh(
                "",
            )

    @parametrize
    def test_method_reset_password(self, client: Vaif) -> None:
        auth = client.projects.auth.reset_password(
            project_id="projectId",
        )
        assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

    @parametrize
    def test_method_reset_password_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.reset_password(
            project_id="projectId",
            token="x",
            password="x",
        )
        assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_reset_password(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.reset_password(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_reset_password(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.reset_password(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset_password(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.reset_password(
                project_id="",
            )

    @parametrize
    def test_method_send(self, client: Vaif) -> None:
        auth = client.projects.auth.send(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_send(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.send(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_send(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.send(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.send(
                "",
            )

    @parametrize
    def test_method_settings(self, client: Vaif) -> None:
        auth = client.projects.auth.settings(
            project_id="projectId",
        )
        assert_matches_type(AuthSettingsResponse, auth, path=["response"])

    @parametrize
    def test_method_settings_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.settings(
            project_id="projectId",
            access_token_lifetime_minutes=1,
            allowed_redirect_urls=["string"],
            allow_password_recovery=True,
            allow_sign_up=True,
            lockout_duration_minutes=0,
            max_sign_in_attempts=0,
            mfa_enabled=True,
            mfa_enforced=True,
            min_password_length=1,
            refresh_token_lifetime_days=1,
            require_email_verification=True,
            require_numbers=True,
            require_phone_verification=True,
            require_special_chars=True,
            require_uppercase=True,
            single_session_mode=True,
            user_table_auto_create=True,
            user_table_name="userTableName",
            user_table_sync_fields=["string"],
        )
        assert_matches_type(AuthSettingsResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_settings(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.settings(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSettingsResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_settings(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.settings(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSettingsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_settings(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.settings(
                project_id="",
            )

    @parametrize
    def test_method_signup(self, client: Vaif) -> None:
        auth = client.projects.auth.signup(
            project_id="projectId",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_method_signup_with_all_params(self, client: Vaif) -> None:
        auth = client.projects.auth.signup(
            project_id="projectId",
            email="dev@stainless.com",
            metadata={"foo": "bar"},
            password="x",
            phone="phone",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_signup(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.signup(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_signup(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.signup(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSignupResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_signup(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.signup(
                project_id="",
            )

    @parametrize
    def test_method_sync_users(self, client: Vaif) -> None:
        auth = client.projects.auth.sync_users(
            "projectId",
        )
        assert auth is None

    @parametrize
    def test_raw_response_sync_users(self, client: Vaif) -> None:
        response = client.projects.auth.with_raw_response.sync_users(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_sync_users(self, client: Vaif) -> None:
        with client.projects.auth.with_streaming_response.sync_users(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync_users(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.auth.with_raw_response.sync_users(
                "",
            )


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
        )
        assert_matches_type(AuthUpdateResponse, auth, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
            enabled=True,
            scopes=["string"],
        )
        assert_matches_type(AuthUpdateResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthUpdateResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.update(
            provider="provider",
            project_id="projectId",
            client_id="x",
            client_secret="x",
            redirect_uri="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthUpdateResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.update(
                provider="provider",
                project_id="",
                client_id="x",
                client_secret="x",
                redirect_uri="https://example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.projects.auth.with_raw_response.update(
                provider="",
                project_id="projectId",
                client_id="x",
                client_secret="x",
                redirect_uri="https://example.com",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.delete(
            provider="provider",
            project_id="projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.delete(
            provider="provider",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.delete(
            provider="provider",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.delete(
                provider="provider",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.projects.auth.with_raw_response.delete(
                provider="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_confirm(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.confirm(
            project_id="projectId",
        )
        assert_matches_type(AuthConfirmResponse, auth, path=["response"])

    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.confirm(
            project_id="projectId",
            token="x",
        )
        assert_matches_type(AuthConfirmResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.confirm(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthConfirmResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.confirm(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthConfirmResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.confirm(
                project_id="",
            )

    @parametrize
    async def test_method_forgot_password(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.forgot_password(
            project_id="projectId",
        )
        assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

    @parametrize
    async def test_method_forgot_password_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.forgot_password(
            project_id="projectId",
            email="dev@stainless.com",
        )
        assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_forgot_password(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.forgot_password(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_forgot_password(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.forgot_password(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthForgotPasswordResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_forgot_password(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.forgot_password(
                project_id="",
            )

    @parametrize
    async def test_method_get_me(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.get_me(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_get_me(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.get_me(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_get_me(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.get_me(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_me(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.get_me(
                "",
            )

    @parametrize
    async def test_method_get_oauth_apps(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.get_oauth_apps(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_get_oauth_apps(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.get_oauth_apps(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_get_oauth_apps(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.get_oauth_apps(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_oauth_apps(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.get_oauth_apps(
                "",
            )

    @parametrize
    async def test_method_get_settings(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.get_settings(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.get_settings(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.get_settings(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_settings(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.get_settings(
                "",
            )

    @parametrize
    async def test_method_login(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.login(
            project_id="projectId",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.login(
            project_id="projectId",
            email="dev@stainless.com",
            password="x",
        )
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_login(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.login(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthLoginResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.login(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_login(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.login(
                project_id="",
            )

    @parametrize
    async def test_method_logout(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.logout(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.logout(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.logout(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_logout(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.logout(
                "",
            )

    @parametrize
    async def test_method_refresh(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.refresh(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.refresh(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.refresh(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.refresh(
                "",
            )

    @parametrize
    async def test_method_reset_password(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.reset_password(
            project_id="projectId",
        )
        assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

    @parametrize
    async def test_method_reset_password_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.reset_password(
            project_id="projectId",
            token="x",
            password="x",
        )
        assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_reset_password(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.reset_password(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_reset_password(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.reset_password(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthResetPasswordResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset_password(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.reset_password(
                project_id="",
            )

    @parametrize
    async def test_method_send(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.send(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.send(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.send(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.send(
                "",
            )

    @parametrize
    async def test_method_settings(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.settings(
            project_id="projectId",
        )
        assert_matches_type(AuthSettingsResponse, auth, path=["response"])

    @parametrize
    async def test_method_settings_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.settings(
            project_id="projectId",
            access_token_lifetime_minutes=1,
            allowed_redirect_urls=["string"],
            allow_password_recovery=True,
            allow_sign_up=True,
            lockout_duration_minutes=0,
            max_sign_in_attempts=0,
            mfa_enabled=True,
            mfa_enforced=True,
            min_password_length=1,
            refresh_token_lifetime_days=1,
            require_email_verification=True,
            require_numbers=True,
            require_phone_verification=True,
            require_special_chars=True,
            require_uppercase=True,
            single_session_mode=True,
            user_table_auto_create=True,
            user_table_name="userTableName",
            user_table_sync_fields=["string"],
        )
        assert_matches_type(AuthSettingsResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_settings(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.settings(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSettingsResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_settings(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.settings(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSettingsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_settings(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.settings(
                project_id="",
            )

    @parametrize
    async def test_method_signup(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.signup(
            project_id="projectId",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_method_signup_with_all_params(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.signup(
            project_id="projectId",
            email="dev@stainless.com",
            metadata={"foo": "bar"},
            password="x",
            phone="phone",
        )
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_signup(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.signup(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSignupResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_signup(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.signup(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSignupResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_signup(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.signup(
                project_id="",
            )

    @parametrize
    async def test_method_sync_users(self, async_client: AsyncVaif) -> None:
        auth = await async_client.projects.auth.sync_users(
            "projectId",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_sync_users(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.auth.with_raw_response.sync_users(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_sync_users(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.auth.with_streaming_response.sync_users(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync_users(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.auth.with_raw_response.sync_users(
                "",
            )
