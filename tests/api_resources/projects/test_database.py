# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatabase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_dedicated(self, client: Vaif) -> None:
        database = client.projects.database.dedicated(
            project_id="projectId",
            tier="micro",
        )
        assert_matches_type(object, database, path=["response"])

    @parametrize
    def test_method_dedicated_with_all_params(self, client: Vaif) -> None:
        database = client.projects.database.dedicated(
            project_id="projectId",
            tier="micro",
            custom_ram_gb=0.6,
            custom_storage_gb=10,
            custom_vcpus=1,
            postgres_version="postgresVersion",
            region="region",
        )
        assert_matches_type(object, database, path=["response"])

    @parametrize
    def test_raw_response_dedicated(self, client: Vaif) -> None:
        response = client.projects.database.with_raw_response.dedicated(
            project_id="projectId",
            tier="micro",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert_matches_type(object, database, path=["response"])

    @parametrize
    def test_streaming_response_dedicated(self, client: Vaif) -> None:
        with client.projects.database.with_streaming_response.dedicated(
            project_id="projectId",
            tier="micro",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert_matches_type(object, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dedicated(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.database.with_raw_response.dedicated(
                project_id="",
                tier="micro",
            )

    @parametrize
    def test_method_dedicated2(self, client: Vaif) -> None:
        database = client.projects.database.dedicated2(
            "projectId",
        )
        assert database is None

    @parametrize
    def test_raw_response_dedicated2(self, client: Vaif) -> None:
        response = client.projects.database.with_raw_response.dedicated2(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert database is None

    @parametrize
    def test_streaming_response_dedicated2(self, client: Vaif) -> None:
        with client.projects.database.with_streaming_response.dedicated2(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dedicated2(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.database.with_raw_response.dedicated2(
                "",
            )

    @parametrize
    def test_method_get_connection(self, client: Vaif) -> None:
        database = client.projects.database.get_connection(
            "projectId",
        )
        assert database is None

    @parametrize
    def test_raw_response_get_connection(self, client: Vaif) -> None:
        response = client.projects.database.with_raw_response.get_connection(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert database is None

    @parametrize
    def test_streaming_response_get_connection(self, client: Vaif) -> None:
        with client.projects.database.with_streaming_response.get_connection(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_connection(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.database.with_raw_response.get_connection(
                "",
            )

    @parametrize
    def test_method_get_dedicated(self, client: Vaif) -> None:
        database = client.projects.database.get_dedicated(
            "projectId",
        )
        assert database is None

    @parametrize
    def test_raw_response_get_dedicated(self, client: Vaif) -> None:
        response = client.projects.database.with_raw_response.get_dedicated(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert database is None

    @parametrize
    def test_streaming_response_get_dedicated(self, client: Vaif) -> None:
        with client.projects.database.with_streaming_response.get_dedicated(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_dedicated(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.database.with_raw_response.get_dedicated(
                "",
            )

    @parametrize
    def test_method_get_status(self, client: Vaif) -> None:
        database = client.projects.database.get_status(
            "projectId",
        )
        assert database is None

    @parametrize
    def test_raw_response_get_status(self, client: Vaif) -> None:
        response = client.projects.database.with_raw_response.get_status(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert database is None

    @parametrize
    def test_streaming_response_get_status(self, client: Vaif) -> None:
        with client.projects.database.with_streaming_response.get_status(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_status(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.database.with_raw_response.get_status(
                "",
            )

    @parametrize
    def test_method_restart(self, client: Vaif) -> None:
        database = client.projects.database.restart(
            "projectId",
        )
        assert database is None

    @parametrize
    def test_raw_response_restart(self, client: Vaif) -> None:
        response = client.projects.database.with_raw_response.restart(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = response.parse()
        assert database is None

    @parametrize
    def test_streaming_response_restart(self, client: Vaif) -> None:
        with client.projects.database.with_streaming_response.restart(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_restart(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.database.with_raw_response.restart(
                "",
            )


class TestAsyncDatabase:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_dedicated(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.dedicated(
            project_id="projectId",
            tier="micro",
        )
        assert_matches_type(object, database, path=["response"])

    @parametrize
    async def test_method_dedicated_with_all_params(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.dedicated(
            project_id="projectId",
            tier="micro",
            custom_ram_gb=0.6,
            custom_storage_gb=10,
            custom_vcpus=1,
            postgres_version="postgresVersion",
            region="region",
        )
        assert_matches_type(object, database, path=["response"])

    @parametrize
    async def test_raw_response_dedicated(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.database.with_raw_response.dedicated(
            project_id="projectId",
            tier="micro",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert_matches_type(object, database, path=["response"])

    @parametrize
    async def test_streaming_response_dedicated(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.database.with_streaming_response.dedicated(
            project_id="projectId",
            tier="micro",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert_matches_type(object, database, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dedicated(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.database.with_raw_response.dedicated(
                project_id="",
                tier="micro",
            )

    @parametrize
    async def test_method_dedicated2(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.dedicated2(
            "projectId",
        )
        assert database is None

    @parametrize
    async def test_raw_response_dedicated2(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.database.with_raw_response.dedicated2(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert database is None

    @parametrize
    async def test_streaming_response_dedicated2(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.database.with_streaming_response.dedicated2(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dedicated2(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.database.with_raw_response.dedicated2(
                "",
            )

    @parametrize
    async def test_method_get_connection(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.get_connection(
            "projectId",
        )
        assert database is None

    @parametrize
    async def test_raw_response_get_connection(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.database.with_raw_response.get_connection(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert database is None

    @parametrize
    async def test_streaming_response_get_connection(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.database.with_streaming_response.get_connection(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_connection(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.database.with_raw_response.get_connection(
                "",
            )

    @parametrize
    async def test_method_get_dedicated(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.get_dedicated(
            "projectId",
        )
        assert database is None

    @parametrize
    async def test_raw_response_get_dedicated(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.database.with_raw_response.get_dedicated(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert database is None

    @parametrize
    async def test_streaming_response_get_dedicated(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.database.with_streaming_response.get_dedicated(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_dedicated(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.database.with_raw_response.get_dedicated(
                "",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.get_status(
            "projectId",
        )
        assert database is None

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.database.with_raw_response.get_status(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert database is None

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.database.with_streaming_response.get_status(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.database.with_raw_response.get_status(
                "",
            )

    @parametrize
    async def test_method_restart(self, async_client: AsyncVaif) -> None:
        database = await async_client.projects.database.restart(
            "projectId",
        )
        assert database is None

    @parametrize
    async def test_raw_response_restart(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.database.with_raw_response.restart(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        database = await response.parse()
        assert database is None

    @parametrize
    async def test_streaming_response_restart(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.database.with_streaming_response.restart(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            database = await response.parse()
            assert database is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_restart(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.database.with_raw_response.restart(
                "",
            )
