# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSignedURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_signed_url(self, client: Vaif) -> None:
        signed_url = client.buckets.signed_url.signed_url(
            "bucketId",
        )
        assert signed_url is None

    @parametrize
    def test_raw_response_signed_url(self, client: Vaif) -> None:
        response = client.buckets.signed_url.with_raw_response.signed_url(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signed_url = response.parse()
        assert signed_url is None

    @parametrize
    def test_streaming_response_signed_url(self, client: Vaif) -> None:
        with client.buckets.signed_url.with_streaming_response.signed_url(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signed_url = response.parse()
            assert signed_url is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_signed_url(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.buckets.signed_url.with_raw_response.signed_url(
                "",
            )


class TestAsyncSignedURL:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_signed_url(self, async_client: AsyncVaif) -> None:
        signed_url = await async_client.buckets.signed_url.signed_url(
            "bucketId",
        )
        assert signed_url is None

    @parametrize
    async def test_raw_response_signed_url(self, async_client: AsyncVaif) -> None:
        response = await async_client.buckets.signed_url.with_raw_response.signed_url(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signed_url = await response.parse()
        assert signed_url is None

    @parametrize
    async def test_streaming_response_signed_url(self, async_client: AsyncVaif) -> None:
        async with async_client.buckets.signed_url.with_streaming_response.signed_url(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signed_url = await response.parse()
            assert signed_url is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_signed_url(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.buckets.signed_url.with_raw_response.signed_url(
                "",
            )
