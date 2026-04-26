# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindByID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        find_by_id = client.mongodb.find_by_id.retrieve(
            id="id",
            collection="collection",
        )
        assert find_by_id is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.mongodb.find_by_id.with_raw_response.retrieve(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find_by_id = response.parse()
        assert find_by_id is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.mongodb.find_by_id.with_streaming_response.retrieve(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find_by_id = response.parse()
            assert find_by_id is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.find_by_id.with_raw_response.retrieve(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mongodb.find_by_id.with_raw_response.retrieve(
                id="",
                collection="collection",
            )


class TestAsyncFindByID:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        find_by_id = await async_client.mongodb.find_by_id.retrieve(
            id="id",
            collection="collection",
        )
        assert find_by_id is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.find_by_id.with_raw_response.retrieve(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find_by_id = await response.parse()
        assert find_by_id is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.find_by_id.with_streaming_response.retrieve(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find_by_id = await response.parse()
            assert find_by_id is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.find_by_id.with_raw_response.retrieve(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mongodb.find_by_id.with_raw_response.retrieve(
                id="",
                collection="collection",
            )
