# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindOneAndReplace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_find_one_and_replace(self, client: Vaif) -> None:
        find_one_and_replace = client.mongodb.find_one_and_replace.find_one_and_replace(
            "collection",
        )
        assert find_one_and_replace is None

    @parametrize
    def test_raw_response_find_one_and_replace(self, client: Vaif) -> None:
        response = client.mongodb.find_one_and_replace.with_raw_response.find_one_and_replace(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find_one_and_replace = response.parse()
        assert find_one_and_replace is None

    @parametrize
    def test_streaming_response_find_one_and_replace(self, client: Vaif) -> None:
        with client.mongodb.find_one_and_replace.with_streaming_response.find_one_and_replace(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find_one_and_replace = response.parse()
            assert find_one_and_replace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_find_one_and_replace(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.find_one_and_replace.with_raw_response.find_one_and_replace(
                "",
            )


class TestAsyncFindOneAndReplace:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_find_one_and_replace(self, async_client: AsyncVaif) -> None:
        find_one_and_replace = await async_client.mongodb.find_one_and_replace.find_one_and_replace(
            "collection",
        )
        assert find_one_and_replace is None

    @parametrize
    async def test_raw_response_find_one_and_replace(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.find_one_and_replace.with_raw_response.find_one_and_replace(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find_one_and_replace = await response.parse()
        assert find_one_and_replace is None

    @parametrize
    async def test_streaming_response_find_one_and_replace(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.find_one_and_replace.with_streaming_response.find_one_and_replace(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find_one_and_replace = await response.parse()
            assert find_one_and_replace is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_find_one_and_replace(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.find_one_and_replace.with_raw_response.find_one_and_replace(
                "",
            )
