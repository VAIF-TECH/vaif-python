# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReplaceOne:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_replace_one(self, client: Vaif) -> None:
        replace_one = client.mongodb.replace_one.replace_one(
            "collection",
        )
        assert replace_one is None

    @parametrize
    def test_raw_response_replace_one(self, client: Vaif) -> None:
        response = client.mongodb.replace_one.with_raw_response.replace_one(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replace_one = response.parse()
        assert replace_one is None

    @parametrize
    def test_streaming_response_replace_one(self, client: Vaif) -> None:
        with client.mongodb.replace_one.with_streaming_response.replace_one(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replace_one = response.parse()
            assert replace_one is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace_one(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.replace_one.with_raw_response.replace_one(
                "",
            )


class TestAsyncReplaceOne:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_replace_one(self, async_client: AsyncVaif) -> None:
        replace_one = await async_client.mongodb.replace_one.replace_one(
            "collection",
        )
        assert replace_one is None

    @parametrize
    async def test_raw_response_replace_one(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.replace_one.with_raw_response.replace_one(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        replace_one = await response.parse()
        assert replace_one is None

    @parametrize
    async def test_streaming_response_replace_one(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.replace_one.with_streaming_response.replace_one(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            replace_one = await response.parse()
            assert replace_one is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace_one(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.replace_one.with_raw_response.replace_one(
                "",
            )
