# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.storage import DownloadURLCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloadURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        download_url = client.storage.download_url.create(
            key="x",
        )
        assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        download_url = client.storage.download_url.create(
            key="x",
            bucket="x",
        )
        assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.storage.download_url.with_raw_response.create(
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download_url = response.parse()
        assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.storage.download_url.with_streaming_response.create(
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download_url = response.parse()
            assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDownloadURL:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        download_url = await async_client.storage.download_url.create(
            key="x",
        )
        assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        download_url = await async_client.storage.download_url.create(
            key="x",
            bucket="x",
        )
        assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.download_url.with_raw_response.create(
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download_url = await response.parse()
        assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.download_url.with_streaming_response.create(
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download_url = await response.parse()
            assert_matches_type(DownloadURLCreateResponse, download_url, path=["response"])

        assert cast(Any, response.is_closed) is True
