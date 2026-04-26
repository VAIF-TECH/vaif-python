# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRollback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rollback(self, client: Vaif) -> None:
        rollback = client.ai.copilot.deploy.rollback.rollback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert rollback is None

    @parametrize
    def test_raw_response_rollback(self, client: Vaif) -> None:
        response = client.ai.copilot.deploy.rollback.with_raw_response.rollback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollback = response.parse()
        assert rollback is None

    @parametrize
    def test_streaming_response_rollback(self, client: Vaif) -> None:
        with client.ai.copilot.deploy.rollback.with_streaming_response.rollback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollback = response.parse()
            assert rollback is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rollback(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deploy_id` but received ''"):
            client.ai.copilot.deploy.rollback.with_raw_response.rollback(
                "",
            )


class TestAsyncRollback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_rollback(self, async_client: AsyncVaif) -> None:
        rollback = await async_client.ai.copilot.deploy.rollback.rollback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert rollback is None

    @parametrize
    async def test_raw_response_rollback(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.deploy.rollback.with_raw_response.rollback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollback = await response.parse()
        assert rollback is None

    @parametrize
    async def test_streaming_response_rollback(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.deploy.rollback.with_streaming_response.rollback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollback = await response.parse()
            assert rollback is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rollback(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deploy_id` but received ''"):
            await async_client.ai.copilot.deploy.rollback.with_raw_response.rollback(
                "",
            )
