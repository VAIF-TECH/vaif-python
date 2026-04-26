# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExamples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_examples(self, client: Vaif) -> None:
        example = client.docs.sdks.examples.get_examples(
            "sdkId",
        )
        assert example is None

    @parametrize
    def test_raw_response_get_examples(self, client: Vaif) -> None:
        response = client.docs.sdks.examples.with_raw_response.get_examples(
            "sdkId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert example is None

    @parametrize
    def test_streaming_response_get_examples(self, client: Vaif) -> None:
        with client.docs.sdks.examples.with_streaming_response.get_examples(
            "sdkId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert example is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_examples(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sdk_id` but received ''"):
            client.docs.sdks.examples.with_raw_response.get_examples(
                "",
            )


class TestAsyncExamples:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_examples(self, async_client: AsyncVaif) -> None:
        example = await async_client.docs.sdks.examples.get_examples(
            "sdkId",
        )
        assert example is None

    @parametrize
    async def test_raw_response_get_examples(self, async_client: AsyncVaif) -> None:
        response = await async_client.docs.sdks.examples.with_raw_response.get_examples(
            "sdkId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert example is None

    @parametrize
    async def test_streaming_response_get_examples(self, async_client: AsyncVaif) -> None:
        async with async_client.docs.sdks.examples.with_streaming_response.get_examples(
            "sdkId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert example is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_examples(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sdk_id` but received ''"):
            await async_client.docs.sdks.examples.with_raw_response.get_examples(
                "",
            )
