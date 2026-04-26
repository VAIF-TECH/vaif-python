# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.storage import UploadBase64CreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploadBase64:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        upload_base64 = client.storage.upload_base64.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        upload_base64 = client.storage.upload_base64.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_type="contentType",
        )
        assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.storage.upload_base64.with_raw_response.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_base64 = response.parse()
        assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.storage.upload_base64.with_streaming_response.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_base64 = response.parse()
            assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUploadBase64:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        upload_base64 = await async_client.storage.upload_base64.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        upload_base64 = await async_client.storage.upload_base64.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content_type="contentType",
        )
        assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.upload_base64.with_raw_response.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload_base64 = await response.parse()
        assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.upload_base64.with_streaming_response.create(
            bucket="x",
            data="x",
            path="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload_base64 = await response.parse()
            assert_matches_type(UploadBase64CreateResponse, upload_base64, path=["response"])

        assert cast(Any, response.is_closed) is True
