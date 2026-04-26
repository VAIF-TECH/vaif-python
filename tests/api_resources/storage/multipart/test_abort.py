# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.storage.multipart import AbortAbortResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbort:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_abort(self, client: Vaif) -> None:
        abort = client.storage.multipart.abort.abort(
            upload_id="x",
            bucket_id="x",
            key="x",
        )
        assert_matches_type(AbortAbortResponse, abort, path=["response"])

    @parametrize
    def test_raw_response_abort(self, client: Vaif) -> None:
        response = client.storage.multipart.abort.with_raw_response.abort(
            upload_id="x",
            bucket_id="x",
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abort = response.parse()
        assert_matches_type(AbortAbortResponse, abort, path=["response"])

    @parametrize
    def test_streaming_response_abort(self, client: Vaif) -> None:
        with client.storage.multipart.abort.with_streaming_response.abort(
            upload_id="x",
            bucket_id="x",
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abort = response.parse()
            assert_matches_type(AbortAbortResponse, abort, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_abort(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.storage.multipart.abort.with_raw_response.abort(
                upload_id="",
                bucket_id="x",
                key="x",
            )


class TestAsyncAbort:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_abort(self, async_client: AsyncVaif) -> None:
        abort = await async_client.storage.multipart.abort.abort(
            upload_id="x",
            bucket_id="x",
            key="x",
        )
        assert_matches_type(AbortAbortResponse, abort, path=["response"])

    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.multipart.abort.with_raw_response.abort(
            upload_id="x",
            bucket_id="x",
            key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abort = await response.parse()
        assert_matches_type(AbortAbortResponse, abort, path=["response"])

    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.multipart.abort.with_streaming_response.abort(
            upload_id="x",
            bucket_id="x",
            key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abort = await response.parse()
            assert_matches_type(AbortAbortResponse, abort, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_abort(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.storage.multipart.abort.with_raw_response.abort(
                upload_id="",
                bucket_id="x",
                key="x",
            )
