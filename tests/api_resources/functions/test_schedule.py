# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_schedule(self, client: Vaif) -> None:
        schedule = client.functions.schedule.get_schedule(
            "functionId",
        )
        assert schedule is None

    @parametrize
    def test_raw_response_get_schedule(self, client: Vaif) -> None:
        response = client.functions.schedule.with_raw_response.get_schedule(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert schedule is None

    @parametrize
    def test_streaming_response_get_schedule(self, client: Vaif) -> None:
        with client.functions.schedule.with_streaming_response.get_schedule(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_schedule(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.schedule.with_raw_response.get_schedule(
                "",
            )

    @parametrize
    def test_method_schedule(self, client: Vaif) -> None:
        schedule = client.functions.schedule.schedule(
            function_id="functionId",
            cron="x",
        )
        assert_matches_type(object, schedule, path=["response"])

    @parametrize
    def test_method_schedule_with_all_params(self, client: Vaif) -> None:
        schedule = client.functions.schedule.schedule(
            function_id="functionId",
            cron="x",
            enabled=True,
        )
        assert_matches_type(object, schedule, path=["response"])

    @parametrize
    def test_raw_response_schedule(self, client: Vaif) -> None:
        response = client.functions.schedule.with_raw_response.schedule(
            function_id="functionId",
            cron="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(object, schedule, path=["response"])

    @parametrize
    def test_streaming_response_schedule(self, client: Vaif) -> None:
        with client.functions.schedule.with_streaming_response.schedule(
            function_id="functionId",
            cron="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(object, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_schedule(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.schedule.with_raw_response.schedule(
                function_id="",
                cron="x",
            )

    @parametrize
    def test_method_schedule2(self, client: Vaif) -> None:
        schedule = client.functions.schedule.schedule2(
            "functionId",
        )
        assert schedule is None

    @parametrize
    def test_raw_response_schedule2(self, client: Vaif) -> None:
        response = client.functions.schedule.with_raw_response.schedule2(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert schedule is None

    @parametrize
    def test_streaming_response_schedule2(self, client: Vaif) -> None:
        with client.functions.schedule.with_streaming_response.schedule2(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_schedule2(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.schedule.with_raw_response.schedule2(
                "",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_schedule(self, async_client: AsyncVaif) -> None:
        schedule = await async_client.functions.schedule.get_schedule(
            "functionId",
        )
        assert schedule is None

    @parametrize
    async def test_raw_response_get_schedule(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.schedule.with_raw_response.get_schedule(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert schedule is None

    @parametrize
    async def test_streaming_response_get_schedule(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.schedule.with_streaming_response.get_schedule(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_schedule(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.schedule.with_raw_response.get_schedule(
                "",
            )

    @parametrize
    async def test_method_schedule(self, async_client: AsyncVaif) -> None:
        schedule = await async_client.functions.schedule.schedule(
            function_id="functionId",
            cron="x",
        )
        assert_matches_type(object, schedule, path=["response"])

    @parametrize
    async def test_method_schedule_with_all_params(self, async_client: AsyncVaif) -> None:
        schedule = await async_client.functions.schedule.schedule(
            function_id="functionId",
            cron="x",
            enabled=True,
        )
        assert_matches_type(object, schedule, path=["response"])

    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.schedule.with_raw_response.schedule(
            function_id="functionId",
            cron="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(object, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.schedule.with_streaming_response.schedule(
            function_id="functionId",
            cron="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(object, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_schedule(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.schedule.with_raw_response.schedule(
                function_id="",
                cron="x",
            )

    @parametrize
    async def test_method_schedule2(self, async_client: AsyncVaif) -> None:
        schedule = await async_client.functions.schedule.schedule2(
            "functionId",
        )
        assert schedule is None

    @parametrize
    async def test_raw_response_schedule2(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.schedule.with_raw_response.schedule2(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert schedule is None

    @parametrize
    async def test_streaming_response_schedule2(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.schedule.with_streaming_response.schedule2(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_schedule2(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.schedule.with_raw_response.schedule2(
                "",
            )
