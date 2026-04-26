# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploadURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upload_url(self, client: Vaif) -> None:
        upload_url = client.buckets.upload_url.upload_url(
            "bucketId",
        )
        assert upload_url is None

    @parametrize
    def test_raw_response_upload_url(self, client: Vaif) -> None:
        response = client.buckets.upload_url.with_raw_response.upload_url(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_url = response.parse()
        assert upload_url is None

    @parametrize
    def test_streaming_response_upload_url(self, client: Vaif) -> None:
        with client.buckets.upload_url.with_streaming_response.upload_url(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_url = response.parse()
            assert upload_url is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload_url(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.upload_url.with_raw_response.upload_url(
                "",
            )


class TestAsyncUploadURL:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_upload_url(self, async_client: AsyncVaif) -> None:
        upload_url = await async_client.buckets.upload_url.upload_url(
            "bucketId",
        )
        assert upload_url is None

    @parametrize
    async def test_raw_response_upload_url(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.upload_url.with_raw_response.upload_url(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_url = await response.parse()
        assert upload_url is None

    @parametrize
    async def test_streaming_response_upload_url(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.upload_url.with_streaming_response.upload_url(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_url = await response.parse()
            assert upload_url is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload_url(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.upload_url.with_raw_response.upload_url(
                "",
            )
