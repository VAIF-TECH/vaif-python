# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stop(self, client: Vaif) -> None:
        stop = client.projects.infrastructure.stop.stop(
            instance_id="instanceId",
            project_id="projectId",
        )
        assert stop is None

    @parametrize
    def test_raw_response_stop(self, client: Vaif) -> None:
        response = client.projects.infrastructure.stop.with_raw_response.stop(
            instance_id="instanceId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stop = response.parse()
        assert stop is None

    @parametrize
    def test_streaming_response_stop(self, client: Vaif) -> None:
        with client.projects.infrastructure.stop.with_streaming_response.stop(
            instance_id="instanceId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stop = response.parse()
            assert stop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.stop.with_raw_response.stop(
                instance_id="instanceId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.projects.infrastructure.stop.with_raw_response.stop(
                instance_id="",
                project_id="projectId",
            )


class TestAsyncStop:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_stop(self, async_client: AsyncVaif) -> None:
        stop = await async_client.projects.infrastructure.stop.stop(
            instance_id="instanceId",
            project_id="projectId",
        )
        assert stop is None

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.stop.with_raw_response.stop(
            instance_id="instanceId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stop = await response.parse()
        assert stop is None

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.stop.with_streaming_response.stop(
            instance_id="instanceId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stop = await response.parse()
            assert stop is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.stop.with_raw_response.stop(
                instance_id="instanceId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.projects.infrastructure.stop.with_raw_response.stop(
                instance_id="",
                project_id="projectId",
            )
