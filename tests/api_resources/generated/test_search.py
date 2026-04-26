# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_search(self, client: Vaif) -> None:
        search = client.generated.search.get_search(
            "table",
        )
        assert search is None

    @parametrize
    def test_raw_response_get_search(self, client: Vaif) -> None:
        response = client.generated.search.with_raw_response.get_search(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert search is None

    @parametrize
    def test_streaming_response_get_search(self, client: Vaif) -> None:
        with client.generated.search.with_streaming_response.get_search(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert search is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_search(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.search.with_raw_response.get_search(
                "",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_search(self, async_client: AsyncVaif) -> None:
        search = await async_client.generated.search.get_search(
            "table",
        )
        assert search is None

    @parametrize
    async def test_raw_response_get_search(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.search.with_raw_response.get_search(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert search is None

    @parametrize
    async def test_streaming_response_get_search(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.search.with_streaming_response.get_search(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert search is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_search(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.search.with_raw_response.get_search(
                "",
            )
