# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAIAnswer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        ai_answer = client.docs.ai_answer.create(
            context="context",
            question="xxx",
        )
        assert ai_answer is None

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        ai_answer = client.docs.ai_answer.create(
            context="context",
            question="xxx",
            conversation_history=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert ai_answer is None

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.docs.ai_answer.with_raw_response.create(
            context="context",
            question="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_answer = response.parse()
        assert ai_answer is None

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.docs.ai_answer.with_streaming_response.create(
            context="context",
            question="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_answer = response.parse()
            assert ai_answer is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAIAnswer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        ai_answer = await async_client.docs.ai_answer.create(
            context="context",
            question="xxx",
        )
        assert ai_answer is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        ai_answer = await async_client.docs.ai_answer.create(
            context="context",
            question="xxx",
            conversation_history=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
        )
        assert ai_answer is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.docs.ai_answer.with_raw_response.create(
            context="context",
            question="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_answer = await response.parse()
        assert ai_answer is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.docs.ai_answer.with_streaming_response.create(
            context="context",
            question="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_answer = await response.parse()
            assert ai_answer is None

        assert cast(Any, response.is_closed) is True
