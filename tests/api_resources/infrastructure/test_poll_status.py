# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPollStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        poll_status = client.infrastructure.poll_status.create()
        assert poll_status is None

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.infrastructure.poll_status.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll_status = response.parse()
        assert poll_status is None

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.infrastructure.poll_status.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll_status = response.parse()
            assert poll_status is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPollStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        poll_status = await async_client.infrastructure.poll_status.create()
        assert poll_status is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.infrastructure.poll_status.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        poll_status = await response.parse()
        assert poll_status is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.infrastructure.poll_status.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            poll_status = await response.parse()
            assert poll_status is None

        assert cast(Any, response.is_closed) is True
