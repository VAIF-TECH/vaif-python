# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTerminal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_exec(self, client: Vaif) -> None:
        terminal = client.projects.terminal.exec(
            "projectId",
        )
        assert terminal is None

    @parametrize
    def test_raw_response_exec(self, client: Vaif) -> None:
        response = client.projects.terminal.with_raw_response.exec(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @parametrize
    def test_streaming_response_exec(self, client: Vaif) -> None:
        with client.projects.terminal.with_streaming_response.exec(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_exec(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.terminal.with_raw_response.exec(
                "",
            )

    @parametrize
    def test_method_get_sessions(self, client: Vaif) -> None:
        terminal = client.projects.terminal.get_sessions(
            "projectId",
        )
        assert terminal is None

    @parametrize
    def test_raw_response_get_sessions(self, client: Vaif) -> None:
        response = client.projects.terminal.with_raw_response.get_sessions(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @parametrize
    def test_streaming_response_get_sessions(self, client: Vaif) -> None:
        with client.projects.terminal.with_streaming_response.get_sessions(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_sessions(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.terminal.with_raw_response.get_sessions(
                "",
            )


class TestAsyncTerminal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_exec(self, async_client: AsyncVaif) -> None:
        terminal = await async_client.projects.terminal.exec(
            "projectId",
        )
        assert terminal is None

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.terminal.with_raw_response.exec(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.terminal.with_streaming_response.exec(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_exec(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.terminal.with_raw_response.exec(
                "",
            )

    @parametrize
    async def test_method_get_sessions(self, async_client: AsyncVaif) -> None:
        terminal = await async_client.projects.terminal.get_sessions(
            "projectId",
        )
        assert terminal is None

    @parametrize
    async def test_raw_response_get_sessions(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.terminal.with_raw_response.get_sessions(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @parametrize
    async def test_streaming_response_get_sessions(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.terminal.with_streaming_response.get_sessions(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_sessions(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.terminal.with_raw_response.get_sessions(
                "",
            )
