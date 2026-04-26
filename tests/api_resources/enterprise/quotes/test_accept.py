# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccept:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_accept(self, client: Vaif) -> None:
        accept = client.enterprise.quotes.accept.accept(
            "quoteId",
        )
        assert accept is None

    @parametrize
    def test_raw_response_accept(self, client: Vaif) -> None:
        response = client.enterprise.quotes.accept.with_raw_response.accept(
            "quoteId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accept = response.parse()
        assert accept is None

    @parametrize
    def test_streaming_response_accept(self, client: Vaif) -> None:
        with client.enterprise.quotes.accept.with_streaming_response.accept(
            "quoteId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accept = response.parse()
            assert accept is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_accept(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            client.enterprise.quotes.accept.with_raw_response.accept(
                "",
            )


class TestAsyncAccept:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_accept(self, async_client: AsyncVaif) -> None:
        accept = await async_client.enterprise.quotes.accept.accept(
            "quoteId",
        )
        assert accept is None

    @parametrize
    async def test_raw_response_accept(self, async_client: AsyncVaif) -> None:
        response = await async_client.enterprise.quotes.accept.with_raw_response.accept(
            "quoteId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accept = await response.parse()
        assert accept is None

    @parametrize
    async def test_streaming_response_accept(self, async_client: AsyncVaif) -> None:
        async with async_client.enterprise.quotes.accept.with_streaming_response.accept(
            "quoteId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accept = await response.parse()
            assert accept is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_accept(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            await async_client.enterprise.quotes.accept.with_raw_response.accept(
                "",
            )
