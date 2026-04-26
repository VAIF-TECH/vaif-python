# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_events(self, client: Vaif) -> None:
        event = client.integrations.analytics.project.events.get_events(
            "projectId",
        )
        assert event is None

    @parametrize
    def test_raw_response_get_events(self, client: Vaif) -> None:
        response = client.integrations.analytics.project.events.with_raw_response.get_events(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert event is None

    @parametrize
    def test_streaming_response_get_events(self, client: Vaif) -> None:
        with client.integrations.analytics.project.events.with_streaming_response.get_events(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_events(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.integrations.analytics.project.events.with_raw_response.get_events(
                "",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_events(self, async_client: AsyncVaif) -> None:
        event = await async_client.integrations.analytics.project.events.get_events(
            "projectId",
        )
        assert event is None

    @parametrize
    async def test_raw_response_get_events(self, async_client: AsyncVaif) -> None:
        response = await async_client.integrations.analytics.project.events.with_raw_response.get_events(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert event is None

    @parametrize
    async def test_streaming_response_get_events(self, async_client: AsyncVaif) -> None:
        async with async_client.integrations.analytics.project.events.with_streaming_response.get_events(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert event is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_events(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.integrations.analytics.project.events.with_raw_response.get_events(
                "",
            )
