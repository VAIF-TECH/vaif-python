# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.auth import MeListResponse, MeUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        me = client.auth.me.update()
        assert_matches_type(MeUpdateResponse, me, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        me = client.auth.me.update(
            avatar_url="https://example.com",
            name="x",
            phone="phone",
            timezone="timezone",
        )
        assert_matches_type(MeUpdateResponse, me, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.auth.me.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeUpdateResponse, me, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.auth.me.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeUpdateResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        me = client.auth.me.list()
        assert_matches_type(MeListResponse, me, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.auth.me.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeListResponse, me, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.auth.me.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeListResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        me = await async_client.auth.me.update()
        assert_matches_type(MeUpdateResponse, me, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        me = await async_client.auth.me.update(
            avatar_url="https://example.com",
            name="x",
            phone="phone",
            timezone="timezone",
        )
        assert_matches_type(MeUpdateResponse, me, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.me.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeUpdateResponse, me, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.me.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeUpdateResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        me = await async_client.auth.me.list()
        assert_matches_type(MeListResponse, me, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.me.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeListResponse, me, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.me.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeListResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True
