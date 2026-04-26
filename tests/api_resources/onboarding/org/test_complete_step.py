# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompleteStep:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete_step(self, client: Vaif) -> None:
        complete_step = client.onboarding.org.complete_step.complete_step(
            "orgId",
        )
        assert complete_step is None

    @parametrize
    def test_raw_response_complete_step(self, client: Vaif) -> None:
        response = client.onboarding.org.complete_step.with_raw_response.complete_step(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        complete_step = response.parse()
        assert complete_step is None

    @parametrize
    def test_streaming_response_complete_step(self, client: Vaif) -> None:
        with client.onboarding.org.complete_step.with_streaming_response.complete_step(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            complete_step = response.parse()
            assert complete_step is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete_step(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.onboarding.org.complete_step.with_raw_response.complete_step(
                "",
            )


class TestAsyncCompleteStep:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_complete_step(self, async_client: AsyncVaif) -> None:
        complete_step = await async_client.onboarding.org.complete_step.complete_step(
            "orgId",
        )
        assert complete_step is None

    @parametrize
    async def test_raw_response_complete_step(self, async_client: AsyncVaif) -> None:
        response = await async_client.onboarding.org.complete_step.with_raw_response.complete_step(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        complete_step = await response.parse()
        assert complete_step is None

    @parametrize
    async def test_streaming_response_complete_step(self, async_client: AsyncVaif) -> None:
        async with async_client.onboarding.org.complete_step.with_streaming_response.complete_step(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            complete_step = await response.parse()
            assert complete_step is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete_step(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.onboarding.org.complete_step.with_raw_response.complete_step(
                "",
            )
