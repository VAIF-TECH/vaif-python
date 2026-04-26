# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        metric = client.ai.copilot.metrics.retrieve(
            "projectId",
        )
        assert metric is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.ai.copilot.metrics.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert metric is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.ai.copilot.metrics.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert metric is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.ai.copilot.metrics.with_raw_response.retrieve(
                "",
            )


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        metric = await async_client.ai.copilot.metrics.retrieve(
            "projectId",
        )
        assert metric is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.metrics.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert metric is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.metrics.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert metric is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.ai.copilot.metrics.with_raw_response.retrieve(
                "",
            )
