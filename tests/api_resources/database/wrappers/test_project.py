# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        project = client.database.wrappers.project.retrieve(
            "projectId",
        )
        assert project is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.database.wrappers.project.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.database.wrappers.project.with_streaming_response.retrieve(
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
            client.database.wrappers.project.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        project = client.database.wrappers.project.update(
            wrapper_id="wrapperId",
            project_id="projectId",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        project = client.database.wrappers.project.update(
            wrapper_id="wrapperId",
            project_id="projectId",
            config={"foo": "bar"},
            enabled_tables=["string"],
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.database.wrappers.project.with_raw_response.update(
            wrapper_id="wrapperId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.database.wrappers.project.with_streaming_response.update(
            wrapper_id="wrapperId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.database.wrappers.project.with_raw_response.update(
                wrapper_id="wrapperId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wrapper_id` but received ''"):
            client.database.wrappers.project.with_raw_response.update(
                wrapper_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        project = client.database.wrappers.project.delete(
            wrapper_id="wrapperId",
            project_id="projectId",
        )
        assert project is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.database.wrappers.project.with_raw_response.delete(
            wrapper_id="wrapperId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.database.wrappers.project.with_streaming_response.delete(
            wrapper_id="wrapperId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.database.wrappers.project.with_raw_response.delete(
                wrapper_id="wrapperId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wrapper_id` but received ''"):
            client.database.wrappers.project.with_raw_response.delete(
                wrapper_id="",
                project_id="projectId",
            )


class TestAsyncProject:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        project = await async_client.database.wrappers.project.retrieve(
            "projectId",
        )
        assert project is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.database.wrappers.project.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.database.wrappers.project.with_streaming_response.retrieve(
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
            await async_client.database.wrappers.project.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        project = await async_client.database.wrappers.project.update(
            wrapper_id="wrapperId",
            project_id="projectId",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        project = await async_client.database.wrappers.project.update(
            wrapper_id="wrapperId",
            project_id="projectId",
            config={"foo": "bar"},
            enabled_tables=["string"],
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.database.wrappers.project.with_raw_response.update(
            wrapper_id="wrapperId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.database.wrappers.project.with_streaming_response.update(
            wrapper_id="wrapperId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.database.wrappers.project.with_raw_response.update(
                wrapper_id="wrapperId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wrapper_id` but received ''"):
            await async_client.database.wrappers.project.with_raw_response.update(
                wrapper_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        project = await async_client.database.wrappers.project.delete(
            wrapper_id="wrapperId",
            project_id="projectId",
        )
        assert project is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.database.wrappers.project.with_raw_response.delete(
            wrapper_id="wrapperId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.database.wrappers.project.with_streaming_response.delete(
            wrapper_id="wrapperId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.database.wrappers.project.with_raw_response.delete(
                wrapper_id="wrapperId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wrapper_id` but received ''"):
            await async_client.database.wrappers.project.with_raw_response.delete(
                wrapper_id="",
                project_id="projectId",
            )
