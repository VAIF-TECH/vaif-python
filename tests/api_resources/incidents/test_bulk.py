# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.incidents import BulkCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        bulk = client.incidents.bulk.create(
            action="acknowledge",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.incidents.bulk.with_raw_response.create(
            action="acknowledge",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.incidents.bulk.with_streaming_response.create(
            action="acknowledge",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        bulk = await async_client.incidents.bulk.create(
            action="acknowledge",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.incidents.bulk.with_raw_response.create(
            action="acknowledge",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.incidents.bulk.with_streaming_response.create(
            action="acknowledge",
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
