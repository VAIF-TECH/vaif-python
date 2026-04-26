# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types import BucketUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuckets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        bucket = client.buckets.retrieve(
            "bucketId",
        )
        assert bucket is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.buckets.with_raw_response.retrieve(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert bucket is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.buckets.with_streaming_response.retrieve(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        bucket = client.buckets.update(
            bucket_id="bucketId",
        )
        assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        bucket = client.buckets.update(
            bucket_id="bucketId",
            allowed_mime_types=["string"],
            cors_origins=["string"],
            file_size_limit=1,
            public=True,
        )
        assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.buckets.with_raw_response.update(
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.buckets.with_streaming_response.update(
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.with_raw_response.update(
                bucket_id="",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        bucket = client.buckets.delete(
            "bucketId",
        )
        assert bucket is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.buckets.with_raw_response.delete(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert bucket is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.buckets.with_streaming_response.delete(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.with_raw_response.delete(
                "",
            )


class TestAsyncBuckets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.buckets.retrieve(
            "bucketId",
        )
        assert bucket is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.with_raw_response.retrieve(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert bucket is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.with_streaming_response.retrieve(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.buckets.update(
            bucket_id="bucketId",
        )
        assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.buckets.update(
            bucket_id="bucketId",
            allowed_mime_types=["string"],
            cors_origins=["string"],
            file_size_limit=1,
            public=True,
        )
        assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.with_raw_response.update(
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.with_streaming_response.update(
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(BucketUpdateResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.with_raw_response.update(
                bucket_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.buckets.delete(
            "bucketId",
        )
        assert bucket is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.with_raw_response.delete(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert bucket is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.with_streaming_response.delete(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.with_raw_response.delete(
                "",
            )
