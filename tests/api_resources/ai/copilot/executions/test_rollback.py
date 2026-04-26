# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.ai.copilot.executions import RollbackRollbackResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRollback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rollback(self, client: Vaif) -> None:
        rollback = client.ai.copilot.executions.rollback.rollback(
            execution_id="executionId",
            checkpoint_id="checkpointId",
        )
        assert_matches_type(RollbackRollbackResponse, rollback, path=["response"])

    @parametrize
    def test_raw_response_rollback(self, client: Vaif) -> None:
        response = client.ai.copilot.executions.rollback.with_raw_response.rollback(
            execution_id="executionId",
            checkpoint_id="checkpointId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollback = response.parse()
        assert_matches_type(RollbackRollbackResponse, rollback, path=["response"])

    @parametrize
    def test_streaming_response_rollback(self, client: Vaif) -> None:
        with client.ai.copilot.executions.rollback.with_streaming_response.rollback(
            execution_id="executionId",
            checkpoint_id="checkpointId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollback = response.parse()
            assert_matches_type(RollbackRollbackResponse, rollback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rollback(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.ai.copilot.executions.rollback.with_raw_response.rollback(
                execution_id="",
                checkpoint_id="checkpointId",
            )


class TestAsyncRollback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_rollback(self, async_client: AsyncVaif) -> None:
        rollback = await async_client.ai.copilot.executions.rollback.rollback(
            execution_id="executionId",
            checkpoint_id="checkpointId",
        )
        assert_matches_type(RollbackRollbackResponse, rollback, path=["response"])

    @parametrize
    async def test_raw_response_rollback(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.executions.rollback.with_raw_response.rollback(
            execution_id="executionId",
            checkpoint_id="checkpointId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollback = await response.parse()
        assert_matches_type(RollbackRollbackResponse, rollback, path=["response"])

    @parametrize
    async def test_streaming_response_rollback(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.executions.rollback.with_streaming_response.rollback(
            execution_id="executionId",
            checkpoint_id="checkpointId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollback = await response.parse()
            assert_matches_type(RollbackRollbackResponse, rollback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rollback(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.ai.copilot.executions.rollback.with_raw_response.rollback(
                execution_id="",
                checkpoint_id="checkpointId",
            )
