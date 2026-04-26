# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_metadata(self, client: Vaif) -> None:
        metadata = client.storage.files.metadata.get_metadata(
            "bucketId",
        )
        assert metadata is None

    @parametrize
    def test_raw_response_get_metadata(self, client: Vaif) -> None:
        response = client.storage.files.metadata.with_raw_response.get_metadata(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert metadata is None

    @parametrize
    def test_streaming_response_get_metadata(self, client: Vaif) -> None:
        with client.storage.files.metadata.with_streaming_response.get_metadata(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert metadata is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_metadata(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.files.metadata.with_raw_response.get_metadata(
                "",
            )

    @parametrize
    def test_method_metadata(self, client: Vaif) -> None:
        metadata = client.storage.files.metadata.metadata(
            "bucketId",
        )
        assert metadata is None

    @parametrize
    def test_raw_response_metadata(self, client: Vaif) -> None:
        response = client.storage.files.metadata.with_raw_response.metadata(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert metadata is None

    @parametrize
    def test_streaming_response_metadata(self, client: Vaif) -> None:
        with client.storage.files.metadata.with_streaming_response.metadata(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert metadata is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_metadata(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.files.metadata.with_raw_response.metadata(
                "",
            )


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_metadata(self, async_client: AsyncVaif) -> None:
        metadata = await async_client.storage.files.metadata.get_metadata(
            "bucketId",
        )
        assert metadata is None

    @parametrize
    async def test_raw_response_get_metadata(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.files.metadata.with_raw_response.get_metadata(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert metadata is None

    @parametrize
    async def test_streaming_response_get_metadata(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.files.metadata.with_streaming_response.get_metadata(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert metadata is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_metadata(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.files.metadata.with_raw_response.get_metadata(
                "",
            )

    @parametrize
    async def test_method_metadata(self, async_client: AsyncVaif) -> None:
        metadata = await async_client.storage.files.metadata.metadata(
            "bucketId",
        )
        assert metadata is None

    @parametrize
    async def test_raw_response_metadata(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.files.metadata.with_raw_response.metadata(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert metadata is None

    @parametrize
    async def test_streaming_response_metadata(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.files.metadata.with_streaming_response.metadata(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert metadata is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_metadata(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.files.metadata.with_raw_response.metadata(
                "",
            )
