# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCostBreakdown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_cost_breakdown(self, client: Vaif) -> None:
        cost_breakdown = client.billing.org.cost_breakdown.get_cost_breakdown(
            "orgId",
        )
        assert cost_breakdown is None

    @parametrize
    def test_raw_response_get_cost_breakdown(self, client: Vaif) -> None:
        response = client.billing.org.cost_breakdown.with_raw_response.get_cost_breakdown(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_breakdown = response.parse()
        assert cost_breakdown is None

    @parametrize
    def test_streaming_response_get_cost_breakdown(self, client: Vaif) -> None:
        with client.billing.org.cost_breakdown.with_streaming_response.get_cost_breakdown(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_breakdown = response.parse()
            assert cost_breakdown is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_cost_breakdown(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.cost_breakdown.with_raw_response.get_cost_breakdown(
                "",
            )


class TestAsyncCostBreakdown:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_cost_breakdown(self, async_client: AsyncVaif) -> None:
        cost_breakdown = await async_client.billing.org.cost_breakdown.get_cost_breakdown(
            "orgId",
        )
        assert cost_breakdown is None

    @parametrize
    async def test_raw_response_get_cost_breakdown(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.cost_breakdown.with_raw_response.get_cost_breakdown(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost_breakdown = await response.parse()
        assert cost_breakdown is None

    @parametrize
    async def test_streaming_response_get_cost_breakdown(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.cost_breakdown.with_streaming_response.get_cost_breakdown(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost_breakdown = await response.parse()
            assert cost_breakdown is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_cost_breakdown(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.cost_breakdown.with_raw_response.get_cost_breakdown(
                "",
            )
