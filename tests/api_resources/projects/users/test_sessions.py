# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        session = client.projects.users.sessions.delete(
            session_id="sessionId",
            project_id="projectId",
            user_id="userId",
        )
        assert session is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.users.sessions.with_raw_response.delete(
            session_id="sessionId",
            project_id="projectId",
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.users.sessions.with_streaming_response.delete(
            session_id="sessionId",
            project_id="projectId",
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.sessions.with_raw_response.delete(
                session_id="sessionId",
                project_id="",
                user_id="userId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.sessions.with_raw_response.delete(
                session_id="sessionId",
                project_id="projectId",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.projects.users.sessions.with_raw_response.delete(
                session_id="",
                project_id="projectId",
                user_id="userId",
            )

    @parametrize
    def test_method_get_sessions(self, client: Vaif) -> None:
        session = client.projects.users.sessions.get_sessions(
            user_id="userId",
            project_id="projectId",
        )
        assert session is None

    @parametrize
    def test_raw_response_get_sessions(self, client: Vaif) -> None:
        response = client.projects.users.sessions.with_raw_response.get_sessions(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_get_sessions(self, client: Vaif) -> None:
        with client.projects.users.sessions.with_streaming_response.get_sessions(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_sessions(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.sessions.with_raw_response.get_sessions(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.sessions.with_raw_response.get_sessions(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_revoke_all(self, client: Vaif) -> None:
        session = client.projects.users.sessions.revoke_all(
            user_id="userId",
            project_id="projectId",
        )
        assert session is None

    @parametrize
    def test_raw_response_revoke_all(self, client: Vaif) -> None:
        response = client.projects.users.sessions.with_raw_response.revoke_all(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_revoke_all(self, client: Vaif) -> None:
        with client.projects.users.sessions.with_streaming_response.revoke_all(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke_all(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.sessions.with_raw_response.revoke_all(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.sessions.with_raw_response.revoke_all(
                user_id="",
                project_id="projectId",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        session = await async_client.projects.users.sessions.delete(
            session_id="sessionId",
            project_id="projectId",
            user_id="userId",
        )
        assert session is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.sessions.with_raw_response.delete(
            session_id="sessionId",
            project_id="projectId",
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.sessions.with_streaming_response.delete(
            session_id="sessionId",
            project_id="projectId",
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.delete(
                session_id="sessionId",
                project_id="",
                user_id="userId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.delete(
                session_id="sessionId",
                project_id="projectId",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.delete(
                session_id="",
                project_id="projectId",
                user_id="userId",
            )

    @parametrize
    async def test_method_get_sessions(self, async_client: AsyncVaif) -> None:
        session = await async_client.projects.users.sessions.get_sessions(
            user_id="userId",
            project_id="projectId",
        )
        assert session is None

    @parametrize
    async def test_raw_response_get_sessions(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.sessions.with_raw_response.get_sessions(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_get_sessions(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.sessions.with_streaming_response.get_sessions(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_sessions(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.get_sessions(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.get_sessions(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_revoke_all(self, async_client: AsyncVaif) -> None:
        session = await async_client.projects.users.sessions.revoke_all(
            user_id="userId",
            project_id="projectId",
        )
        assert session is None

    @parametrize
    async def test_raw_response_revoke_all(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.sessions.with_raw_response.revoke_all(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_revoke_all(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.sessions.with_streaming_response.revoke_all(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke_all(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.revoke_all(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.sessions.with_raw_response.revoke_all(
                user_id="",
                project_id="projectId",
            )
