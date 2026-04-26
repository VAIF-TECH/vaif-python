# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        index = client.mongodb.indexes.delete(
            index_name="indexName",
            collection="collection",
        )
        assert index is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.mongodb.indexes.with_raw_response.delete(
            index_name="indexName",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert index is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.mongodb.indexes.with_streaming_response.delete(
            index_name="indexName",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.indexes.with_raw_response.delete(
                index_name="indexName",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.mongodb.indexes.with_raw_response.delete(
                index_name="",
                collection="collection",
            )

    @parametrize
    def test_method_get_indexes(self, client: Vaif) -> None:
        index = client.mongodb.indexes.get_indexes(
            "collection",
        )
        assert index is None

    @parametrize
    def test_raw_response_get_indexes(self, client: Vaif) -> None:
        response = client.mongodb.indexes.with_raw_response.get_indexes(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert index is None

    @parametrize
    def test_streaming_response_get_indexes(self, client: Vaif) -> None:
        with client.mongodb.indexes.with_streaming_response.get_indexes(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_indexes(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.indexes.with_raw_response.get_indexes(
                "",
            )

    @parametrize
    def test_method_indexes(self, client: Vaif) -> None:
        index = client.mongodb.indexes.indexes(
            "collection",
        )
        assert index is None

    @parametrize
    def test_raw_response_indexes(self, client: Vaif) -> None:
        response = client.mongodb.indexes.with_raw_response.indexes(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert index is None

    @parametrize
    def test_streaming_response_indexes(self, client: Vaif) -> None:
        with client.mongodb.indexes.with_streaming_response.indexes(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_indexes(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.mongodb.indexes.with_raw_response.indexes(
                "",
            )


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        index = await async_client.mongodb.indexes.delete(
            index_name="indexName",
            collection="collection",
        )
        assert index is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.indexes.with_raw_response.delete(
            index_name="indexName",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert index is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.indexes.with_streaming_response.delete(
            index_name="indexName",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.indexes.with_raw_response.delete(
                index_name="indexName",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.mongodb.indexes.with_raw_response.delete(
                index_name="",
                collection="collection",
            )

    @parametrize
    async def test_method_get_indexes(self, async_client: AsyncVaif) -> None:
        index = await async_client.mongodb.indexes.get_indexes(
            "collection",
        )
        assert index is None

    @parametrize
    async def test_raw_response_get_indexes(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.indexes.with_raw_response.get_indexes(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert index is None

    @parametrize
    async def test_streaming_response_get_indexes(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.indexes.with_streaming_response.get_indexes(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_indexes(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.indexes.with_raw_response.get_indexes(
                "",
            )

    @parametrize
    async def test_method_indexes(self, async_client: AsyncVaif) -> None:
        index = await async_client.mongodb.indexes.indexes(
            "collection",
        )
        assert index is None

    @parametrize
    async def test_raw_response_indexes(self, async_client: AsyncVaif) -> None:
        response = await async_client.mongodb.indexes.with_raw_response.indexes(
            "collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert index is None

    @parametrize
    async def test_streaming_response_indexes(self, async_client: AsyncVaif) -> None:
        async with async_client.mongodb.indexes.with_streaming_response.indexes(
            "collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_indexes(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.mongodb.indexes.with_raw_response.indexes(
                "",
            )
