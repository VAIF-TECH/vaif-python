# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        function = client.functions.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        function = client.functions.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            entrypoint="entrypoint",
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runtime="runtime",
            schedule="schedule",
            timeout_ms=1000,
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.functions.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.functions.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(object, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        function = client.functions.retrieve(
            "functionId",
        )
        assert function is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.functions.with_raw_response.retrieve(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert function is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.functions.with_streaming_response.retrieve(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        function = client.functions.update(
            function_id="functionId",
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        function = client.functions.update(
            function_id="functionId",
            description="description",
            enabled=True,
            entrypoint="entrypoint",
            name="name",
            schedule="schedule",
            timeout_ms=1000,
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.functions.with_raw_response.update(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(object, function, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.functions.with_streaming_response.update(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(object, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.update(
                function_id="",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        function = client.functions.delete(
            "functionId",
        )
        assert function is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.functions.with_raw_response.delete(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert function is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.functions.with_streaming_response.delete(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.with_raw_response.delete(
                "",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        function = await async_client.functions.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        function = await async_client.functions.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            entrypoint="entrypoint",
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runtime="runtime",
            schedule="schedule",
            timeout_ms=1000,
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(object, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        function = await async_client.functions.retrieve(
            "functionId",
        )
        assert function is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.with_raw_response.retrieve(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert function is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.with_streaming_response.retrieve(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        function = await async_client.functions.update(
            function_id="functionId",
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        function = await async_client.functions.update(
            function_id="functionId",
            description="description",
            enabled=True,
            entrypoint="entrypoint",
            name="name",
            schedule="schedule",
            timeout_ms=1000,
        )
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.with_raw_response.update(
            function_id="functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(object, function, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.with_streaming_response.update(
            function_id="functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(object, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.update(
                function_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        function = await async_client.functions.delete(
            "functionId",
        )
        assert function is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.with_raw_response.delete(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert function is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.with_streaming_response.delete(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.with_raw_response.delete(
                "",
            )
