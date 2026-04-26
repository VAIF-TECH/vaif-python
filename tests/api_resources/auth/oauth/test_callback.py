# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_callback(self, client: Vaif) -> None:
        callback = client.auth.oauth.callback.get_callback(
            provider="google",
        )
        assert callback is None

    @parametrize
    def test_method_get_callback_with_all_params(self, client: Vaif) -> None:
        callback = client.auth.oauth.callback.get_callback(
            provider="google",
            code="code",
            error="error",
            error_description="error_description",
            state="state",
        )
        assert callback is None

    @parametrize
    def test_raw_response_get_callback(self, client: Vaif) -> None:
        response = client.auth.oauth.callback.with_raw_response.get_callback(
            provider="google",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert callback is None

    @parametrize
    def test_streaming_response_get_callback(self, client: Vaif) -> None:
        with client.auth.oauth.callback.with_streaming_response.get_callback(
            provider="google",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCallback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_callback(self, async_client: AsyncVaif) -> None:
        callback = await async_client.auth.oauth.callback.get_callback(
            provider="google",
        )
        assert callback is None

    @parametrize
    async def test_method_get_callback_with_all_params(self, async_client: AsyncVaif) -> None:
        callback = await async_client.auth.oauth.callback.get_callback(
            provider="google",
            code="code",
            error="error",
            error_description="error_description",
            state="state",
        )
        assert callback is None

    @parametrize
    async def test_raw_response_get_callback(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.oauth.callback.with_raw_response.get_callback(
            provider="google",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert callback is None

    @parametrize
    async def test_streaming_response_get_callback(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.oauth.callback.with_streaming_response.get_callback(
            provider="google",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert callback is None

        assert cast(Any, response.is_closed) is True
