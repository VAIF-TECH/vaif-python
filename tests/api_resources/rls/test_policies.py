# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        policy = client.rls.policies.create(
            "projectId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.rls.policies.with_raw_response.create(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.rls.policies.with_streaming_response.create(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.rls.policies.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        policy = client.rls.policies.retrieve(
            "projectId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.rls.policies.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.rls.policies.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.rls.policies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        policy = client.rls.policies.update(
            "policyId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.rls.policies.with_raw_response.update(
            "policyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.rls.policies.with_streaming_response.update(
            "policyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.rls.policies.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        policy = client.rls.policies.delete(
            "policyId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.rls.policies.with_raw_response.delete(
            "policyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.rls.policies.with_streaming_response.delete(
            "policyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.rls.policies.with_raw_response.delete(
                "",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        policy = await async_client.rls.policies.create(
            "projectId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.rls.policies.with_raw_response.create(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.rls.policies.with_streaming_response.create(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.rls.policies.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        policy = await async_client.rls.policies.retrieve(
            "projectId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.rls.policies.with_raw_response.retrieve(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.rls.policies.with_streaming_response.retrieve(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.rls.policies.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        policy = await async_client.rls.policies.update(
            "policyId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.rls.policies.with_raw_response.update(
            "policyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.rls.policies.with_streaming_response.update(
            "policyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.rls.policies.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        policy = await async_client.rls.policies.delete(
            "policyId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.rls.policies.with_raw_response.delete(
            "policyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.rls.policies.with_streaming_response.delete(
            "policyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.rls.policies.with_raw_response.delete(
                "",
            )
