# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.ai.copilot import ExecuteCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        execute = client.ai.copilot.execute.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        execute = client.ai.copilot.execute.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dry_run=True,
            step_ids=["string"],
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.ai.copilot.execute.with_raw_response.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = response.parse()
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.ai.copilot.execute.with_streaming_response.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = response.parse()
            assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExecute:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        execute = await async_client.ai.copilot.execute.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        execute = await async_client.ai.copilot.execute.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dry_run=True,
            step_ids=["string"],
        )
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.execute.with_raw_response.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execute = await response.parse()
        assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.execute.with_streaming_response.create(
            plan_id="planId",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execute = await response.parse()
            assert_matches_type(ExecuteCreateResponse, execute, path=["response"])

        assert cast(Any, response.is_closed) is True
