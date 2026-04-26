# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.auth.me import ContextListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        context = client.auth.me.context.list()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.auth.me.context.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.auth.me.context.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextListResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContext:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        context = await async_client.auth.me.context.list()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.me.context.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.me.context.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextListResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True
