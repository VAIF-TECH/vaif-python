# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_files(self, client: Vaif) -> None:
        file = client.buckets.files.files(
            "bucketId",
        )
        assert file is None

    @parametrize
    def test_raw_response_files(self, client: Vaif) -> None:
        response = client.buckets.files.with_raw_response.files(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_files(self, client: Vaif) -> None:
        with client.buckets.files.with_streaming_response.files(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_files(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.files.with_raw_response.files(
                "",
            )

    @parametrize
    def test_method_get_files(self, client: Vaif) -> None:
        file = client.buckets.files.get_files(
            "bucketId",
        )
        assert file is None

    @parametrize
    def test_raw_response_get_files(self, client: Vaif) -> None:
        response = client.buckets.files.with_raw_response.get_files(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_get_files(self, client: Vaif) -> None:
        with client.buckets.files.with_streaming_response.get_files(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_files(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.files.with_raw_response.get_files(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_files(self, async_client: AsyncVaif) -> None:
        file = await async_client.buckets.files.files(
            "bucketId",
        )
        assert file is None

    @parametrize
    async def test_raw_response_files(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.files.with_raw_response.files(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_files(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.files.with_streaming_response.files(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_files(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.files.with_raw_response.files(
                "",
            )

    @parametrize
    async def test_method_get_files(self, async_client: AsyncVaif) -> None:
        file = await async_client.buckets.files.get_files(
            "bucketId",
        )
        assert file is None

    @parametrize
    async def test_raw_response_get_files(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.files.with_raw_response.get_files(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_get_files(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.files.with_streaming_response.get_files(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_files(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.files.with_raw_response.get_files(
                "",
            )
