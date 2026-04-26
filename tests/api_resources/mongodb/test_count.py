# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_count(self, client: Vaif) -> None:
        count = client.mongodb.count.count(
            "collection",
        )
        assert count is None

    @parametrize
    def test_raw_response_count(self, client: Vaif) -> None:
        response = client.mongodb.count.with_raw_response.count(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        count = response.parse()
        assert count is None

    @parametrize
    def test_streaming_response_count(self, client: Vaif) -> None:
        with client.mongodb.count.with_streaming_response.count(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            count = response.parse()
            assert count is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_count(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.count.with_raw_response.count(
                "",
            )


class TestAsyncCount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_count(self, async_client: AsyncVaif) -> None:
        count = await async_client.mongodb.count.count(
            "collection",
        )
        assert count is None

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.count.with_raw_response.count(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        count = await response.parse()
        assert count is None

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.count.with_streaming_response.count(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            count = await response.parse()
            assert count is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_count(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.count.with_raw_response.count(
                "",
            )
