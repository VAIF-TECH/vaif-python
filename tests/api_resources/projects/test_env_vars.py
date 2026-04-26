# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvVars:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        env_var = client.projects.env_vars.update(
            env_var_id="envVarId",
            project_id="projectId",
        )
        assert env_var is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.projects.env_vars.with_raw_response.update(
            env_var_id="envVarId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert env_var is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.projects.env_vars.with_streaming_response.update(
            env_var_id="envVarId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.env_vars.with_raw_response.update(
                env_var_id="envVarId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            client.projects.env_vars.with_raw_response.update(
                env_var_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        env_var = client.projects.env_vars.delete(
            env_var_id="envVarId",
            project_id="projectId",
        )
        assert env_var is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.env_vars.with_raw_response.delete(
            env_var_id="envVarId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert env_var is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.env_vars.with_streaming_response.delete(
            env_var_id="envVarId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.env_vars.with_raw_response.delete(
                env_var_id="envVarId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            client.projects.env_vars.with_raw_response.delete(
                env_var_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_env_vars(self, client: Vaif) -> None:
        env_var = client.projects.env_vars.env_vars(
            "projectId",
        )
        assert env_var is None

    @parametrize
    def test_raw_response_env_vars(self, client: Vaif) -> None:
        response = client.projects.env_vars.with_raw_response.env_vars(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert env_var is None

    @parametrize
    def test_streaming_response_env_vars(self, client: Vaif) -> None:
        with client.projects.env_vars.with_streaming_response.env_vars(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_env_vars(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.env_vars.with_raw_response.env_vars(
                "",
            )

    @parametrize
    def test_method_get_env_vars(self, client: Vaif) -> None:
        env_var = client.projects.env_vars.get_env_vars(
            "projectId",
        )
        assert env_var is None

    @parametrize
    def test_raw_response_get_env_vars(self, client: Vaif) -> None:
        response = client.projects.env_vars.with_raw_response.get_env_vars(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert env_var is None

    @parametrize
    def test_streaming_response_get_env_vars(self, client: Vaif) -> None:
        with client.projects.env_vars.with_streaming_response.get_env_vars(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_env_vars(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.env_vars.with_raw_response.get_env_vars(
                "",
            )


class TestAsyncEnvVars:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        env_var = await async_client.projects.env_vars.update(
            env_var_id="envVarId",
            project_id="projectId",
        )
        assert env_var is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.env_vars.with_raw_response.update(
            env_var_id="envVarId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert env_var is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.env_vars.with_streaming_response.update(
            env_var_id="envVarId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.env_vars.with_raw_response.update(
                env_var_id="envVarId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            await async_client.projects.env_vars.with_raw_response.update(
                env_var_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        env_var = await async_client.projects.env_vars.delete(
            env_var_id="envVarId",
            project_id="projectId",
        )
        assert env_var is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.env_vars.with_raw_response.delete(
            env_var_id="envVarId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert env_var is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.env_vars.with_streaming_response.delete(
            env_var_id="envVarId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.env_vars.with_raw_response.delete(
                env_var_id="envVarId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            await async_client.projects.env_vars.with_raw_response.delete(
                env_var_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_env_vars(self, async_client: AsyncVaif) -> None:
        env_var = await async_client.projects.env_vars.env_vars(
            "projectId",
        )
        assert env_var is None

    @parametrize
    async def test_raw_response_env_vars(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.env_vars.with_raw_response.env_vars(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert env_var is None

    @parametrize
    async def test_streaming_response_env_vars(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.env_vars.with_streaming_response.env_vars(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_env_vars(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.env_vars.with_raw_response.env_vars(
                "",
            )

    @parametrize
    async def test_method_get_env_vars(self, async_client: AsyncVaif) -> None:
        env_var = await async_client.projects.env_vars.get_env_vars(
            "projectId",
        )
        assert env_var is None

    @parametrize
    async def test_raw_response_get_env_vars(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.env_vars.with_raw_response.get_env_vars(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert env_var is None

    @parametrize
    async def test_streaming_response_get_env_vars(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.env_vars.with_streaming_response.get_env_vars(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert env_var is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_env_vars(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.env_vars.with_raw_response.get_env_vars(
                "",
            )
