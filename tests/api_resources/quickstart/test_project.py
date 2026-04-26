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
        project = client.quickstart.project.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, project, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Vaif) -> None:
        project = client.quickstart.project.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            env="env",
            platform="web",
        )
        assert_matches_type(str, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.quickstart.project.with_raw_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(str, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.quickstart.project.with_streaming_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(str, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.quickstart.project.with_raw_response.retrieve(
                project_id="",
            )


class TestAsyncProject:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        project = await async_client.quickstart.project.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, project, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncVaif) -> None:
        project = await async_client.quickstart.project.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            env="env",
            platform="web",
        )
        assert_matches_type(str, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.quickstart.project.with_raw_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(str, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.quickstart.project.with_streaming_response.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(str, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.quickstart.project.with_raw_response.retrieve(
                project_id="",
            )
