# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChangePassword:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        change_password = client.users.me.change_password.create()
        assert change_password is None

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.users.me.change_password.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change_password = response.parse()
        assert change_password is None

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.users.me.change_password.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change_password = response.parse()
            assert change_password is None

        assert cast(Any, response.is_closed) is True


class TestAsyncChangePassword:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        change_password = await async_client.users.me.change_password.create()
        assert change_password is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.users.me.change_password.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change_password = await response.parse()
        assert change_password is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.users.me.change_password.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change_password = await response.parse()
            assert change_password is None

        assert cast(Any, response.is_closed) is True
