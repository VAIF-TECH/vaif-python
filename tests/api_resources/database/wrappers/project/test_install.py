# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_install(self, client: Vaif) -> None:
        install = client.database.wrappers.project.install.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
        )
        assert_matches_type(object, install, path=["response"])

    @parametrize
    def test_method_install_with_all_params(self, client: Vaif) -> None:
        install = client.database.wrappers.project.install.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
            enabled_tables=["string"],
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, install, path=["response"])

    @parametrize
    def test_raw_response_install(self, client: Vaif) -> None:
        response = client.database.wrappers.project.install.with_raw_response.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = response.parse()
        assert_matches_type(object, install, path=["response"])

    @parametrize
    def test_streaming_response_install(self, client: Vaif) -> None:
        with client.database.wrappers.project.install.with_streaming_response.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = response.parse()
            assert_matches_type(object, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_install(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.database.wrappers.project.install.with_raw_response.install(
                project_id="",
                config={"foo": "bar"},
                wrapper_id="x",
            )


class TestAsyncInstall:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_install(self, async_client: AsyncVaif) -> None:
        install = await async_client.database.wrappers.project.install.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
        )
        assert_matches_type(object, install, path=["response"])

    @parametrize
    async def test_method_install_with_all_params(self, async_client: AsyncVaif) -> None:
        install = await async_client.database.wrappers.project.install.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
            enabled_tables=["string"],
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, install, path=["response"])

    @parametrize
    async def test_raw_response_install(self, async_client: AsyncVaif) -> None:
        response = await async_client.database.wrappers.project.install.with_raw_response.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        install = await response.parse()
        assert_matches_type(object, install, path=["response"])

    @parametrize
    async def test_streaming_response_install(self, async_client: AsyncVaif) -> None:
        async with async_client.database.wrappers.project.install.with_streaming_response.install(
            project_id="projectId",
            config={"foo": "bar"},
            wrapper_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            install = await response.parse()
            assert_matches_type(object, install, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_install(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.database.wrappers.project.install.with_raw_response.install(
                project_id="",
                config={"foo": "bar"},
                wrapper_id="x",
            )
