# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnterprise:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        enterprise = client.pricing.enterprise.list()
        assert enterprise is None

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.pricing.enterprise.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert enterprise is None

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.pricing.enterprise.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert enterprise is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEnterprise:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        enterprise = await async_client.pricing.enterprise.list()
        assert enterprise is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.pricing.enterprise.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert enterprise is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.pricing.enterprise.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert enterprise is None

        assert cast(Any, response.is_closed) is True
