# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_steps(self, client: Vaif) -> None:
        step = client.deployments.steps.get_steps(
            "deploymentId",
        )
        assert step is None

    @parametrize
    def test_raw_response_get_steps(self, client: Vaif) -> None:
        response = client.deployments.steps.with_raw_response.get_steps(
            "deploymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert step is None

    @parametrize
    def test_streaming_response_get_steps(self, client: Vaif) -> None:
        with client.deployments.steps.with_streaming_response.get_steps(
            "deploymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert step is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_steps(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.deployments.steps.with_raw_response.get_steps(
                "",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_steps(self, async_client: AsyncVaif) -> None:
        step = await async_client.deployments.steps.get_steps(
            "deploymentId",
        )
        assert step is None

    @parametrize
    async def test_raw_response_get_steps(self, async_client: AsyncVaif) -> None:
        response = await async_client.deployments.steps.with_raw_response.get_steps(
            "deploymentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert step is None

    @parametrize
    async def test_streaming_response_get_steps(self, async_client: AsyncVaif) -> None:
        async with async_client.deployments.steps.with_streaming_response.get_steps(
            "deploymentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert step is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_steps(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.deployments.steps.with_raw_response.get_steps(
                "",
            )
