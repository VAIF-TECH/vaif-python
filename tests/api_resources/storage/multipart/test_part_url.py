# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.storage.multipart import PartURLPartURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPartURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_part_url(self, client: Vaif) -> None:
        part_url = client.storage.multipart.part_url.part_url(
            upload_id="x",
            bucket_id="x",
            key="x",
            part_number=1,
        )
        assert_matches_type(PartURLPartURLResponse, part_url, path=["response"])

    @parametrize
    def test_raw_response_part_url(self, client: Vaif) -> None:
        response = client.storage.multipart.part_url.with_raw_response.part_url(
            upload_id="x",
            bucket_id="x",
            key="x",
            part_number=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part_url = response.parse()
        assert_matches_type(PartURLPartURLResponse, part_url, path=["response"])

    @parametrize
    def test_streaming_response_part_url(self, client: Vaif) -> None:
        with client.storage.multipart.part_url.with_streaming_response.part_url(
            upload_id="x",
            bucket_id="x",
            key="x",
            part_number=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part_url = response.parse()
            assert_matches_type(PartURLPartURLResponse, part_url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_part_url(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.storage.multipart.part_url.with_raw_response.part_url(
                upload_id="",
                bucket_id="x",
                key="x",
                part_number=1,
            )


class TestAsyncPartURL:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_part_url(self, async_client: AsyncVaif) -> None:
        part_url = await async_client.storage.multipart.part_url.part_url(
            upload_id="x",
            bucket_id="x",
            key="x",
            part_number=1,
        )
        assert_matches_type(PartURLPartURLResponse, part_url, path=["response"])

    @parametrize
    async def test_raw_response_part_url(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.multipart.part_url.with_raw_response.part_url(
            upload_id="x",
            bucket_id="x",
            key="x",
            part_number=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part_url = await response.parse()
        assert_matches_type(PartURLPartURLResponse, part_url, path=["response"])

    @parametrize
    async def test_streaming_response_part_url(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.multipart.part_url.with_streaming_response.part_url(
            upload_id="x",
            bucket_id="x",
            key="x",
            part_number=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part_url = await response.parse()
            assert_matches_type(PartURLPartURLResponse, part_url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_part_url(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.storage.multipart.part_url.with_raw_response.part_url(
                upload_id="",
                bucket_id="x",
                key="x",
                part_number=1,
            )
