# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.integrations.deliveries import RetryRetryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retry(self, client: Vaif) -> None:
        retry = client.integrations.deliveries.retry.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RetryRetryResponse, retry, path=["response"])

    @parametrize
    def test_raw_response_retry(self, client: Vaif) -> None:
        response = client.integrations.deliveries.retry.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retry = response.parse()
        assert_matches_type(RetryRetryResponse, retry, path=["response"])

    @parametrize
    def test_streaming_response_retry(self, client: Vaif) -> None:
        with client.integrations.deliveries.retry.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retry = response.parse()
            assert_matches_type(RetryRetryResponse, retry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.integrations.deliveries.retry.with_raw_response.retry(
                "",
            )


class TestAsyncRetry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retry(self, async_client: AsyncVaif) -> None:
        retry = await async_client.integrations.deliveries.retry.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RetryRetryResponse, retry, path=["response"])

    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncVaif) -> None:
        response = await async_client.integrations.deliveries.retry.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retry = await response.parse()
        assert_matches_type(RetryRetryResponse, retry, path=["response"])

    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncVaif) -> None:
        async with async_client.integrations.deliveries.retry.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retry = await response.parse()
            assert_matches_type(RetryRetryResponse, retry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.integrations.deliveries.retry.with_raw_response.retry(
                "",
            )
