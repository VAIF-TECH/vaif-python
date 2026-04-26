# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.ai.copilot import RateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        rate = client.ai.copilot.rate.create(
            message_id="messageId",
            rating=1,
        )
        assert_matches_type(RateCreateResponse, rate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        rate = client.ai.copilot.rate.create(
            message_id="messageId",
            rating=1,
            approved=True,
            feedback="feedback",
        )
        assert_matches_type(RateCreateResponse, rate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.ai.copilot.rate.with_raw_response.create(
            message_id="messageId",
            rating=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateCreateResponse, rate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.ai.copilot.rate.with_streaming_response.create(
            message_id="messageId",
            rating=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateCreateResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.ai.copilot.rate.with_raw_response.create(
                message_id="",
                rating=1,
            )


class TestAsyncRate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        rate = await async_client.ai.copilot.rate.create(
            message_id="messageId",
            rating=1,
        )
        assert_matches_type(RateCreateResponse, rate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        rate = await async_client.ai.copilot.rate.create(
            message_id="messageId",
            rating=1,
            approved=True,
            feedback="feedback",
        )
        assert_matches_type(RateCreateResponse, rate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.rate.with_raw_response.create(
            message_id="messageId",
            rating=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateCreateResponse, rate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.rate.with_streaming_response.create(
            message_id="messageId",
            rating=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateCreateResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.ai.copilot.rate.with_raw_response.create(
                message_id="",
                rating=1,
            )
