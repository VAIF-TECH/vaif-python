# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.auth.cli import CallbackCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        callback = client.auth.cli.callback.create(
            code="x",
        )
        assert_matches_type(CallbackCreateResponse, callback, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.auth.cli.callback.with_raw_response.create(
            code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert_matches_type(CallbackCreateResponse, callback, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.auth.cli.callback.with_streaming_response.create(
            code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert_matches_type(CallbackCreateResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCallback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        callback = await async_client.auth.cli.callback.create(
            code="x",
        )
        assert_matches_type(CallbackCreateResponse, callback, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.cli.callback.with_raw_response.create(
            code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert_matches_type(CallbackCreateResponse, callback, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.cli.callback.with_streaming_response.create(
            code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert_matches_type(CallbackCreateResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True
