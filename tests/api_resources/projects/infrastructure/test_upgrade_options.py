# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpgradeOptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_upgrade_options(self, client: Vaif) -> None:
        upgrade_option = client.projects.infrastructure.upgrade_options.get_upgrade_options(
            instance_id="instanceId",
            project_id="projectId",
        )
        assert upgrade_option is None

    @parametrize
    def test_raw_response_get_upgrade_options(self, client: Vaif) -> None:
        response = client.projects.infrastructure.upgrade_options.with_raw_response.get_upgrade_options(
            instance_id="instanceId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upgrade_option = response.parse()
        assert upgrade_option is None

    @parametrize
    def test_streaming_response_get_upgrade_options(self, client: Vaif) -> None:
        with client.projects.infrastructure.upgrade_options.with_streaming_response.get_upgrade_options(
            instance_id="instanceId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upgrade_option = response.parse()
            assert upgrade_option is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_upgrade_options(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.upgrade_options.with_raw_response.get_upgrade_options(
                instance_id="instanceId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.projects.infrastructure.upgrade_options.with_raw_response.get_upgrade_options(
                instance_id="",
                project_id="projectId",
            )


class TestAsyncUpgradeOptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_upgrade_options(self, async_client: AsyncVaif) -> None:
        upgrade_option = await async_client.projects.infrastructure.upgrade_options.get_upgrade_options(
            instance_id="instanceId",
            project_id="projectId",
        )
        assert upgrade_option is None

    @parametrize
    async def test_raw_response_get_upgrade_options(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.upgrade_options.with_raw_response.get_upgrade_options(
            instance_id="instanceId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upgrade_option = await response.parse()
        assert upgrade_option is None

    @parametrize
    async def test_streaming_response_get_upgrade_options(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.upgrade_options.with_streaming_response.get_upgrade_options(
            instance_id="instanceId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upgrade_option = await response.parse()
            assert upgrade_option is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_upgrade_options(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.upgrade_options.with_raw_response.get_upgrade_options(
                instance_id="instanceId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.projects.infrastructure.upgrade_options.with_raw_response.get_upgrade_options(
                instance_id="",
                project_id="projectId",
            )
