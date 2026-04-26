# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProvisionSsl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_provision_ssl(self, client: Vaif) -> None:
        provision_ssl = client.projects.environments.provision_ssl.provision_ssl(
            env_id="envId",
            project_id="projectId",
        )
        assert provision_ssl is None

    @parametrize
    def test_raw_response_provision_ssl(self, client: Vaif) -> None:
        response = client.projects.environments.provision_ssl.with_raw_response.provision_ssl(
            env_id="envId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provision_ssl = response.parse()
        assert provision_ssl is None

    @parametrize
    def test_streaming_response_provision_ssl(self, client: Vaif) -> None:
        with client.projects.environments.provision_ssl.with_streaming_response.provision_ssl(
            env_id="envId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provision_ssl = response.parse()
            assert provision_ssl is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provision_ssl(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.provision_ssl.with_raw_response.provision_ssl(
                env_id="envId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            client.projects.environments.provision_ssl.with_raw_response.provision_ssl(
                env_id="",
                project_id="projectId",
            )


class TestAsyncProvisionSsl:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_provision_ssl(self, async_client: AsyncVaif) -> None:
        provision_ssl = await async_client.projects.environments.provision_ssl.provision_ssl(
            env_id="envId",
            project_id="projectId",
        )
        assert provision_ssl is None

    @parametrize
    async def test_raw_response_provision_ssl(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.provision_ssl.with_raw_response.provision_ssl(
            env_id="envId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provision_ssl = await response.parse()
        assert provision_ssl is None

    @parametrize
    async def test_streaming_response_provision_ssl(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.provision_ssl.with_streaming_response.provision_ssl(
            env_id="envId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provision_ssl = await response.parse()
            assert provision_ssl is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provision_ssl(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.provision_ssl.with_raw_response.provision_ssl(
                env_id="envId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            await async_client.projects.environments.provision_ssl.with_raw_response.provision_ssl(
                env_id="",
                project_id="projectId",
            )
