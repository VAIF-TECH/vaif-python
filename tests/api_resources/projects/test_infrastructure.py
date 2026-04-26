# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInfrastructure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.delete(
            instance_id="instanceId",
            project_id="projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.delete(
            instance_id="instanceId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.delete(
            instance_id="instanceId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.delete(
                instance_id="instanceId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.projects.infrastructure.with_raw_response.delete(
                instance_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_get_infrastructure(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.get_infrastructure(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_get_infrastructure(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.get_infrastructure(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_get_infrastructure(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.get_infrastructure(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_infrastructure(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.get_infrastructure(
                "",
            )

    @parametrize
    def test_method_get_migration_status(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.get_migration_status(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_get_migration_status(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.get_migration_status(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_get_migration_status(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.get_migration_status(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_migration_status(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.get_migration_status(
                "",
            )

    @parametrize
    def test_method_get_progress(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.get_progress(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_get_progress(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.get_progress(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_get_progress(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.get_progress(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_progress(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.get_progress(
                "",
            )

    @parametrize
    def test_method_provision(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.provision(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_provision(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.provision(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_provision(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.provision(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provision(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.provision(
                "",
            )

    @parametrize
    def test_method_provision_custom(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.provision_custom(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_provision_custom(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.provision_custom(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_provision_custom(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.provision_custom(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provision_custom(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.provision_custom(
                "",
            )

    @parametrize
    def test_method_retry(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.retry(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_retry(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.retry(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_retry(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.retry(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.retry(
                "",
            )

    @parametrize
    def test_method_rollback(self, client: Vaif) -> None:
        infrastructure = client.projects.infrastructure.rollback(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    def test_raw_response_rollback(self, client: Vaif) -> None:
        response = client.projects.infrastructure.with_raw_response.rollback(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = response.parse()
        assert infrastructure is None

    @parametrize
    def test_streaming_response_rollback(self, client: Vaif) -> None:
        with client.projects.infrastructure.with_streaming_response.rollback(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rollback(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.infrastructure.with_raw_response.rollback(
                "",
            )


class TestAsyncInfrastructure:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.delete(
            instance_id="instanceId",
            project_id="projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.delete(
            instance_id="instanceId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.delete(
            instance_id="instanceId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.delete(
                instance_id="instanceId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.delete(
                instance_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_get_infrastructure(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.get_infrastructure(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_get_infrastructure(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.get_infrastructure(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_get_infrastructure(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.get_infrastructure(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_infrastructure(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.get_infrastructure(
                "",
            )

    @parametrize
    async def test_method_get_migration_status(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.get_migration_status(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_get_migration_status(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.get_migration_status(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_get_migration_status(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.get_migration_status(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_migration_status(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.get_migration_status(
                "",
            )

    @parametrize
    async def test_method_get_progress(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.get_progress(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_get_progress(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.get_progress(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_get_progress(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.get_progress(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_progress(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.get_progress(
                "",
            )

    @parametrize
    async def test_method_provision(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.provision(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_provision(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.provision(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_provision(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.provision(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provision(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.provision(
                "",
            )

    @parametrize
    async def test_method_provision_custom(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.provision_custom(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_provision_custom(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.provision_custom(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_provision_custom(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.provision_custom(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provision_custom(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.provision_custom(
                "",
            )

    @parametrize
    async def test_method_retry(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.retry(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.retry(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.retry(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.retry(
                "",
            )

    @parametrize
    async def test_method_rollback(self, async_client: AsyncVaif) -> None:
        infrastructure = await async_client.projects.infrastructure.rollback(
            "projectId",
        )
        assert infrastructure is None

    @parametrize
    async def test_raw_response_rollback(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.infrastructure.with_raw_response.rollback(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infrastructure = await response.parse()
        assert infrastructure is None

    @parametrize
    async def test_streaming_response_rollback(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.infrastructure.with_streaming_response.rollback(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infrastructure = await response.parse()
            assert infrastructure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rollback(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.infrastructure.with_raw_response.rollback(
                "",
            )
