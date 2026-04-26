# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        environment = client.projects.environments.update(
            env_id="envId",
            project_id="projectId",
        )
        assert environment is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.projects.environments.with_raw_response.update(
            env_id="envId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.projects.environments.with_streaming_response.update(
            env_id="envId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.with_raw_response.update(
                env_id="envId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            client.projects.environments.with_raw_response.update(
                env_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        environment = client.projects.environments.delete(
            env_id="envId",
            project_id="projectId",
        )
        assert environment is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.environments.with_raw_response.delete(
            env_id="envId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.environments.with_streaming_response.delete(
            env_id="envId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.with_raw_response.delete(
                env_id="envId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            client.projects.environments.with_raw_response.delete(
                env_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_backfill_urls(self, client: Vaif) -> None:
        environment = client.projects.environments.backfill_urls(
            "projectId",
        )
        assert environment is None

    @parametrize
    def test_raw_response_backfill_urls(self, client: Vaif) -> None:
        response = client.projects.environments.with_raw_response.backfill_urls(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_backfill_urls(self, client: Vaif) -> None:
        with client.projects.environments.with_streaming_response.backfill_urls(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_backfill_urls(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.with_raw_response.backfill_urls(
                "",
            )

    @parametrize
    def test_method_bootstrap(self, client: Vaif) -> None:
        environment = client.projects.environments.bootstrap(
            "projectId",
        )
        assert environment is None

    @parametrize
    def test_raw_response_bootstrap(self, client: Vaif) -> None:
        response = client.projects.environments.with_raw_response.bootstrap(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_bootstrap(self, client: Vaif) -> None:
        with client.projects.environments.with_streaming_response.bootstrap(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bootstrap(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.with_raw_response.bootstrap(
                "",
            )

    @parametrize
    def test_method_environments(self, client: Vaif) -> None:
        environment = client.projects.environments.environments(
            "projectId",
        )
        assert environment is None

    @parametrize
    def test_raw_response_environments(self, client: Vaif) -> None:
        response = client.projects.environments.with_raw_response.environments(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_environments(self, client: Vaif) -> None:
        with client.projects.environments.with_streaming_response.environments(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_environments(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.with_raw_response.environments(
                "",
            )

    @parametrize
    def test_method_get_environments(self, client: Vaif) -> None:
        environment = client.projects.environments.get_environments(
            "projectId",
        )
        assert environment is None

    @parametrize
    def test_raw_response_get_environments(self, client: Vaif) -> None:
        response = client.projects.environments.with_raw_response.get_environments(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert environment is None

    @parametrize
    def test_streaming_response_get_environments(self, client: Vaif) -> None:
        with client.projects.environments.with_streaming_response.get_environments(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_environments(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.environments.with_raw_response.get_environments(
                "",
            )


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        environment = await async_client.projects.environments.update(
            env_id="envId",
            project_id="projectId",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.with_raw_response.update(
            env_id="envId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.with_streaming_response.update(
            env_id="envId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.with_raw_response.update(
                env_id="envId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            await async_client.projects.environments.with_raw_response.update(
                env_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        environment = await async_client.projects.environments.delete(
            env_id="envId",
            project_id="projectId",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.with_raw_response.delete(
            env_id="envId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.with_streaming_response.delete(
            env_id="envId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.with_raw_response.delete(
                env_id="envId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_id` but received ''"):
            await async_client.projects.environments.with_raw_response.delete(
                env_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_backfill_urls(self, async_client: AsyncVaif) -> None:
        environment = await async_client.projects.environments.backfill_urls(
            "projectId",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_backfill_urls(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.with_raw_response.backfill_urls(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_backfill_urls(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.with_streaming_response.backfill_urls(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_backfill_urls(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.with_raw_response.backfill_urls(
                "",
            )

    @parametrize
    async def test_method_bootstrap(self, async_client: AsyncVaif) -> None:
        environment = await async_client.projects.environments.bootstrap(
            "projectId",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_bootstrap(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.with_raw_response.bootstrap(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_bootstrap(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.with_streaming_response.bootstrap(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bootstrap(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.with_raw_response.bootstrap(
                "",
            )

    @parametrize
    async def test_method_environments(self, async_client: AsyncVaif) -> None:
        environment = await async_client.projects.environments.environments(
            "projectId",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_environments(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.with_raw_response.environments(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_environments(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.with_streaming_response.environments(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_environments(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.with_raw_response.environments(
                "",
            )

    @parametrize
    async def test_method_get_environments(self, async_client: AsyncVaif) -> None:
        environment = await async_client.projects.environments.get_environments(
            "projectId",
        )
        assert environment is None

    @parametrize
    async def test_raw_response_get_environments(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.environments.with_raw_response.get_environments(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert environment is None

    @parametrize
    async def test_streaming_response_get_environments(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.environments.with_streaming_response.get_environments(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert environment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_environments(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.environments.with_raw_response.get_environments(
                "",
            )
