# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from vaif.types import ProjectCreateResponse, ProjectUpdateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        project = client.projects.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        project = client.projects.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            features={
                "ai": True,
                "analytics": True,
                "auth": True,
                "database": True,
                "functions": True,
                "realtime": True,
                "scheduling": True,
                "storage": True,
            },
            region_key="x",
            slug="x",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.projects.with_raw_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.projects.with_streaming_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        project = client.projects.retrieve(
            "projectId",
        )
        assert project is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.projects.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.projects.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        project = client.projects.update(
            project_id="projectId",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        project = client.projects.update(
            project_id="projectId",
            default_environment="development",
            description="description",
            features={"foo": True},
            name="x",
            timezone="timezone",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.projects.with_raw_response.update(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.projects.with_streaming_response.update(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.update(
                project_id="",
            )

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        project = client.projects.list()
        assert project is None

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        project = client.projects.delete(
            "projectId",
        )
        assert project is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.with_raw_response.delete(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.with_streaming_response.delete(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.with_raw_response.delete(
                "",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            features={
                "ai": True,
                "analytics": True,
                "auth": True,
                "database": True,
                "functions": True,
                "realtime": True,
                "scheduling": True,
                "storage": True,
            },
            region_key="x",
            slug="x",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.with_raw_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.with_streaming_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.retrieve(
            "projectId",
        )
        assert project is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.update(
            project_id="projectId",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.update(
            project_id="projectId",
            default_environment="development",
            description="description",
            features={"foo": True},
            name="x",
            timezone="timezone",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.with_raw_response.update(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.with_streaming_response.update(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.update(
                project_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.list()
        assert project is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        project = await async_client.projects.delete(
            "projectId",
        )
        assert project is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.with_raw_response.delete(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.with_streaming_response.delete(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.with_raw_response.delete(
                "",
            )
