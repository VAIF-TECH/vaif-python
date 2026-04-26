# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnableAll:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        enable_all = client.realtime.enable_all.create()
        assert enable_all is None

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.realtime.enable_all.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enable_all = response.parse()
        assert enable_all is None

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.realtime.enable_all.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enable_all = response.parse()
            assert enable_all is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEnableAll:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        enable_all = await async_client.realtime.enable_all.create()
        assert enable_all is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.realtime.enable_all.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enable_all = await response.parse()
        assert enable_all is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.realtime.enable_all.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enable_all = await response.parse()
            assert enable_all is None

        assert cast(Any, response.is_closed) is True
