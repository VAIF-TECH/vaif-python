# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthorize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        authorize = client.github.oauth.authorize.list()
        assert authorize is None

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.github.oauth.authorize.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorize = response.parse()
        assert authorize is None

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.github.oauth.authorize.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorize = response.parse()
            assert authorize is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthorize:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        authorize = await async_client.github.oauth.authorize.list()
        assert authorize is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.github.oauth.authorize.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorize = await response.parse()
        assert authorize is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.github.oauth.authorize.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorize = await response.parse()
            assert authorize is None

        assert cast(Any, response.is_closed) is True
