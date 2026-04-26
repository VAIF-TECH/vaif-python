# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.storage import BucketCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuckets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        bucket = client.storage.buckets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BucketCreateResponse, bucket, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        bucket = client.storage.buckets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_mime_types=["string"],
            cors_origins=["string"],
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_size_limit=1,
            public=True,
        )
        assert_matches_type(BucketCreateResponse, bucket, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.storage.buckets.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert_matches_type(BucketCreateResponse, bucket, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.storage.buckets.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert_matches_type(BucketCreateResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        bucket = client.storage.buckets.list()
        assert bucket is None

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.storage.buckets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = response.parse()
        assert bucket is None

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.storage.buckets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBuckets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.storage.buckets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BucketCreateResponse, bucket, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.storage.buckets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_mime_types=["string"],
            cors_origins=["string"],
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_size_limit=1,
            public=True,
        )
        assert_matches_type(BucketCreateResponse, bucket, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert_matches_type(BucketCreateResponse, bucket, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert_matches_type(BucketCreateResponse, bucket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        bucket = await async_client.storage.buckets.list()
        assert bucket is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bucket = await response.parse()
        assert bucket is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bucket = await response.parse()
            assert bucket is None

        assert cast(Any, response.is_closed) is True
