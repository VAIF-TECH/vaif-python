# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.auth import LogoutCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogout:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        logout = client.auth.logout.create()
        assert_matches_type(LogoutCreateResponse, logout, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.auth.logout.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logout = response.parse()
        assert_matches_type(LogoutCreateResponse, logout, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.auth.logout.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logout = response.parse()
            assert_matches_type(LogoutCreateResponse, logout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogout:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        logout = await async_client.auth.logout.create()
        assert_matches_type(LogoutCreateResponse, logout, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.logout.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logout = await response.parse()
        assert_matches_type(LogoutCreateResponse, logout, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.logout.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logout = await response.parse()
            assert_matches_type(LogoutCreateResponse, logout, path=["response"])

        assert cast(Any, response.is_closed) is True
