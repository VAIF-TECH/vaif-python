# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClose:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_close(self, client: Vaif) -> None:
        close = client.mongodb.cursor.close.close(
            cursor_id="cursorId",
            collection="collection",
        )
        assert close is None

    @parametrize
    def test_raw_response_close(self, client: Vaif) -> None:
        response = client.mongodb.cursor.close.with_raw_response.close(
            cursor_id="cursorId",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        close = response.parse()
        assert close is None

    @parametrize
    def test_streaming_response_close(self, client: Vaif) -> None:
        with client.mongodb.cursor.close.with_streaming_response.close(
            cursor_id="cursorId",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            close = response.parse()
            assert close is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.cursor.close.with_raw_response.close(
                cursor_id="cursorId",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cursor_id` but received ''"):
            client.mongodb.cursor.close.with_raw_response.close(
                cursor_id="",
                collection="collection",
            )


class TestAsyncClose:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_close(self, async_client: AsyncVaif) -> None:
        close = await async_client.mongodb.cursor.close.close(
            cursor_id="cursorId",
            collection="collection",
        )
        assert close is None

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.cursor.close.with_raw_response.close(
            cursor_id="cursorId",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        close = await response.parse()
        assert close is None

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.cursor.close.with_streaming_response.close(
            cursor_id="cursorId",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            close = await response.parse()
            assert close is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.cursor.close.with_raw_response.close(
                cursor_id="cursorId",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cursor_id` but received ''"):
            await async_client.mongodb.cursor.close.with_raw_response.close(
                cursor_id="",
                collection="collection",
            )
