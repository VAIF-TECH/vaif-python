# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAggregate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_aggregate(self, client: Vaif) -> None:
        aggregate = client.mongodb.aggregate.aggregate(
            "collection",
        )
        assert aggregate is None

    @parametrize
    def test_raw_response_aggregate(self, client: Vaif) -> None:
        response = client.mongodb.aggregate.with_raw_response.aggregate(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate = response.parse()
        assert aggregate is None

    @parametrize
    def test_streaming_response_aggregate(self, client: Vaif) -> None:
        with client.mongodb.aggregate.with_streaming_response.aggregate(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate = response.parse()
            assert aggregate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_aggregate(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.aggregate.with_raw_response.aggregate(
                "",
            )

    @parametrize
    def test_method_cursor(self, client: Vaif) -> None:
        aggregate = client.mongodb.aggregate.cursor(
            "collection",
        )
        assert aggregate is None

    @parametrize
    def test_raw_response_cursor(self, client: Vaif) -> None:
        response = client.mongodb.aggregate.with_raw_response.cursor(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate = response.parse()
        assert aggregate is None

    @parametrize
    def test_streaming_response_cursor(self, client: Vaif) -> None:
        with client.mongodb.aggregate.with_streaming_response.cursor(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate = response.parse()
            assert aggregate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cursor(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.aggregate.with_raw_response.cursor(
                "",
            )


class TestAsyncAggregate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_aggregate(self, async_client: AsyncVaif) -> None:
        aggregate = await async_client.mongodb.aggregate.aggregate(
            "collection",
        )
        assert aggregate is None

    @parametrize
    async def test_raw_response_aggregate(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.aggregate.with_raw_response.aggregate(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate = await response.parse()
        assert aggregate is None

    @parametrize
    async def test_streaming_response_aggregate(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.aggregate.with_streaming_response.aggregate(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate = await response.parse()
            assert aggregate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_aggregate(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.aggregate.with_raw_response.aggregate(
                "",
            )

    @parametrize
    async def test_method_cursor(self, async_client: AsyncVaif) -> None:
        aggregate = await async_client.mongodb.aggregate.cursor(
            "collection",
        )
        assert aggregate is None

    @parametrize
    async def test_raw_response_cursor(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.aggregate.with_raw_response.cursor(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate = await response.parse()
        assert aggregate is None

    @parametrize
    async def test_streaming_response_cursor(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.aggregate.with_streaming_response.cursor(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate = await response.parse()
            assert aggregate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cursor(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.aggregate.with_raw_response.cursor(
                "",
            )
