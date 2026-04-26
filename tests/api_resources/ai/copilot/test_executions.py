# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        execution = client.ai.copilot.executions.retrieve(
            "executionId",
        )
        assert execution is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.ai.copilot.executions.with_raw_response.retrieve(
            "executionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert execution is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.ai.copilot.executions.with_streaming_response.retrieve(
            "executionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert execution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.ai.copilot.executions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_retrieve2(self, client: Vaif) -> None:
        execution = client.ai.copilot.executions.retrieve2(
            "sessionId",
        )
        assert execution is None

    @parametrize
    def test_raw_response_retrieve2(self, client: Vaif) -> None:
        response = client.ai.copilot.executions.with_raw_response.retrieve2(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert execution is None

    @parametrize
    def test_streaming_response_retrieve2(self, client: Vaif) -> None:
        with client.ai.copilot.executions.with_streaming_response.retrieve2(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert execution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve2(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.ai.copilot.executions.with_raw_response.retrieve2(
                "",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        execution = await async_client.ai.copilot.executions.retrieve(
            "executionId",
        )
        assert execution is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.executions.with_raw_response.retrieve(
            "executionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert execution is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.executions.with_streaming_response.retrieve(
            "executionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert execution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.ai.copilot.executions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_retrieve2(self, async_client: AsyncVaif) -> None:
        execution = await async_client.ai.copilot.executions.retrieve2(
            "sessionId",
        )
        assert execution is None

    @parametrize
    async def test_raw_response_retrieve2(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.executions.with_raw_response.retrieve2(
            "sessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert execution is None

    @parametrize
    async def test_streaming_response_retrieve2(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.executions.with_streaming_response.retrieve2(
            "sessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert execution is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve2(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.ai.copilot.executions.with_raw_response.retrieve2(
                "",
            )
