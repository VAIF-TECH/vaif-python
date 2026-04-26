# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.status import SubscribeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscribe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        subscribe = client.status.subscribe.create(
            email="dev@stainless.com",
        )
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.status.subscribe.with_raw_response.create(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = response.parse()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.status.subscribe.with_streaming_response.create(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = response.parse()
            assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscribe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        subscribe = await async_client.status.subscribe.create(
            email="dev@stainless.com",
        )
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.status.subscribe.with_raw_response.create(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = await response.parse()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.status.subscribe.with_streaming_response.create(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = await response.parse()
            assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True
