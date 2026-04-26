# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.ai.copilot import SessionUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        session = client.ai.copilot.sessions.retrieve(
            "projectId",
        )
        assert session is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.ai.copilot.sessions.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.ai.copilot.sessions.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.ai.copilot.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        session = client.ai.copilot.sessions.update(
            session_id="sessionId",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        session = client.ai.copilot.sessions.update(
            session_id="sessionId",
            title="x",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.ai.copilot.sessions.with_raw_response.update(
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.ai.copilot.sessions.with_streaming_response.update(
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionUpdateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.ai.copilot.sessions.with_raw_response.update(
                session_id="",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        session = client.ai.copilot.sessions.delete(
            "sessionId",
        )
        assert session is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.ai.copilot.sessions.with_raw_response.delete(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.ai.copilot.sessions.with_streaming_response.delete(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.ai.copilot.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_retrieve2(self, client: Vaif) -> None:
        session = client.ai.copilot.sessions.retrieve2(
            "sessionId",
        )
        assert session is None

    @parametrize
    def test_raw_response_retrieve2(self, client: Vaif) -> None:
        response = client.ai.copilot.sessions.with_raw_response.retrieve2(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_retrieve2(self, client: Vaif) -> None:
        with client.ai.copilot.sessions.with_streaming_response.retrieve2(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve2(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.ai.copilot.sessions.with_raw_response.retrieve2(
                "",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        session = await async_client.ai.copilot.sessions.retrieve(
            "projectId",
        )
        assert session is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.sessions.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.sessions.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.ai.copilot.sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        session = await async_client.ai.copilot.sessions.update(
            session_id="sessionId",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        session = await async_client.ai.copilot.sessions.update(
            session_id="sessionId",
            title="x",
        )
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.sessions.with_raw_response.update(
            session_id="sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionUpdateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.sessions.with_streaming_response.update(
            session_id="sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionUpdateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.ai.copilot.sessions.with_raw_response.update(
                session_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        session = await async_client.ai.copilot.sessions.delete(
            "sessionId",
        )
        assert session is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.sessions.with_raw_response.delete(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.sessions.with_streaming_response.delete(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.ai.copilot.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_retrieve2(self, async_client: AsyncVaif) -> None:
        session = await async_client.ai.copilot.sessions.retrieve2(
            "sessionId",
        )
        assert session is None

    @parametrize
    async def test_raw_response_retrieve2(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.sessions.with_raw_response.retrieve2(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_retrieve2(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.sessions.with_streaming_response.retrieve2(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve2(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.ai.copilot.sessions.with_raw_response.retrieve2(
                "",
            )
