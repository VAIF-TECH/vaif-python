# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        name = client.functions.project.name.retrieve(
            function_name="functionName",
            project_id="projectId",
        )
        assert name is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.functions.project.name.with_raw_response.retrieve(
            function_name="functionName",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert name is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.functions.project.name.with_streaming_response.retrieve(
            function_name="functionName",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert name is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.functions.project.name.with_raw_response.retrieve(
                function_name="functionName",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.functions.project.name.with_raw_response.retrieve(
                function_name="",
                project_id="projectId",
            )


class TestAsyncName:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        name = await async_client.functions.project.name.retrieve(
            function_name="functionName",
            project_id="projectId",
        )
        assert name is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.project.name.with_raw_response.retrieve(
            function_name="functionName",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert name is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.project.name.with_streaming_response.retrieve(
            function_name="functionName",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert name is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.functions.project.name.with_raw_response.retrieve(
                function_name="functionName",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.functions.project.name.with_raw_response.retrieve(
                function_name="",
                project_id="projectId",
            )
