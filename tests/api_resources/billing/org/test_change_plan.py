# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.billing.org import ChangePlanChangePlanResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChangePlan:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_change_plan(self, client: Vaif) -> None:
        change_plan = client.billing.org.change_plan.change_plan(
            org_id="orgId",
            plan="starter",
        )
        assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

    @parametrize
    def test_method_change_plan_with_all_params(self, client: Vaif) -> None:
        change_plan = client.billing.org.change_plan.change_plan(
            org_id="orgId",
            plan="starter",
            interval="monthly",
        )
        assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

    @parametrize
    def test_raw_response_change_plan(self, client: Vaif) -> None:
        response = client.billing.org.change_plan.with_raw_response.change_plan(
            org_id="orgId",
            plan="starter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change_plan = response.parse()
        assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

    @parametrize
    def test_streaming_response_change_plan(self, client: Vaif) -> None:
        with client.billing.org.change_plan.with_streaming_response.change_plan(
            org_id="orgId",
            plan="starter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change_plan = response.parse()
            assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_plan(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.change_plan.with_raw_response.change_plan(
                org_id="",
                plan="starter",
            )


class TestAsyncChangePlan:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_change_plan(self, async_client: AsyncVaif) -> None:
        change_plan = await async_client.billing.org.change_plan.change_plan(
            org_id="orgId",
            plan="starter",
        )
        assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

    @parametrize
    async def test_method_change_plan_with_all_params(self, async_client: AsyncVaif) -> None:
        change_plan = await async_client.billing.org.change_plan.change_plan(
            org_id="orgId",
            plan="starter",
            interval="monthly",
        )
        assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

    @parametrize
    async def test_raw_response_change_plan(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.change_plan.with_raw_response.change_plan(
            org_id="orgId",
            plan="starter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change_plan = await response.parse()
        assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

    @parametrize
    async def test_streaming_response_change_plan(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.change_plan.with_streaming_response.change_plan(
            org_id="orgId",
            plan="starter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change_plan = await response.parse()
            assert_matches_type(ChangePlanChangePlanResponse, change_plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_plan(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.change_plan.with_raw_response.change_plan(
                org_id="",
                plan="starter",
            )
