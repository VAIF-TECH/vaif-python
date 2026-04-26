# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        oauth = client.auth.oauth.retrieve(
            provider="google",
        )
        assert oauth is None

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Vaif) -> None:
        oauth = client.auth.oauth.retrieve(
            provider="google",
            mode="login",
            redirect="redirect",
        )
        assert oauth is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.auth.oauth.with_raw_response.retrieve(
            provider="google",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.auth.oauth.with_streaming_response.retrieve(
            provider="google",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        oauth = await async_client.auth.oauth.retrieve(
            provider="google",
        )
        assert oauth is None

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncVaif) -> None:
        oauth = await async_client.auth.oauth.retrieve(
            provider="google",
            mode="login",
            redirect="redirect",
        )
        assert oauth is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.oauth.with_raw_response.retrieve(
            provider="google",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.oauth.with_streaming_response.retrieve(
            provider="google",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True
