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
    def test_method_update(self, client: Vaif) -> None:
        policy = client.storage.buckets.policies.update(
            policy_id="policyId",
            bucket_id="bucketId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.storage.buckets.policies.with_raw_response.update(
            policy_id="policyId",
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.storage.buckets.policies.with_streaming_response.update(
            policy_id="policyId",
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.buckets.policies.with_raw_response.update(
                policy_id="policyId",
                bucket_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.storage.buckets.policies.with_raw_response.update(
                policy_id="",
                bucket_id="bucketId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        policy = client.storage.buckets.policies.delete(
            policy_id="policyId",
            bucket_id="bucketId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.storage.buckets.policies.with_raw_response.delete(
            policy_id="policyId",
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.storage.buckets.policies.with_streaming_response.delete(
            policy_id="policyId",
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.buckets.policies.with_raw_response.delete(
                policy_id="policyId",
                bucket_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.storage.buckets.policies.with_raw_response.delete(
                policy_id="",
                bucket_id="bucketId",
            )

    @parametrize
    def test_method_get_policies(self, client: Vaif) -> None:
        policy = client.storage.buckets.policies.get_policies(
            "bucketId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_get_policies(self, client: Vaif) -> None:
        response = client.storage.buckets.policies.with_raw_response.get_policies(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_get_policies(self, client: Vaif) -> None:
        with client.storage.buckets.policies.with_streaming_response.get_policies(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_policies(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.buckets.policies.with_raw_response.get_policies(
                "",
            )

    @parametrize
    def test_method_policies(self, client: Vaif) -> None:
        policy = client.storage.buckets.policies.policies(
            "bucketId",
        )
        assert policy is None

    @parametrize
    def test_raw_response_policies(self, client: Vaif) -> None:
        response = client.storage.buckets.policies.with_raw_response.policies(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert policy is None

    @parametrize
    def test_streaming_response_policies(self, client: Vaif) -> None:
        with client.storage.buckets.policies.with_streaming_response.policies(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_policies(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.buckets.policies.with_raw_response.policies(
                "",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        policy = await async_client.storage.buckets.policies.update(
            policy_id="policyId",
            bucket_id="bucketId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.policies.with_raw_response.update(
            policy_id="policyId",
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.policies.with_streaming_response.update(
            policy_id="policyId",
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.buckets.policies.with_raw_response.update(
                policy_id="policyId",
                bucket_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.storage.buckets.policies.with_raw_response.update(
                policy_id="",
                bucket_id="bucketId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        policy = await async_client.storage.buckets.policies.delete(
            policy_id="policyId",
            bucket_id="bucketId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.policies.with_raw_response.delete(
            policy_id="policyId",
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.policies.with_streaming_response.delete(
            policy_id="policyId",
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.buckets.policies.with_raw_response.delete(
                policy_id="policyId",
                bucket_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.storage.buckets.policies.with_raw_response.delete(
                policy_id="",
                bucket_id="bucketId",
            )

    @parametrize
    async def test_method_get_policies(self, async_client: AsyncVaif) -> None:
        policy = await async_client.storage.buckets.policies.get_policies(
            "bucketId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_get_policies(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.policies.with_raw_response.get_policies(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_get_policies(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.policies.with_streaming_response.get_policies(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_policies(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.buckets.policies.with_raw_response.get_policies(
                "",
            )

    @parametrize
    async def test_method_policies(self, async_client: AsyncVaif) -> None:
        policy = await async_client.storage.buckets.policies.policies(
            "bucketId",
        )
        assert policy is None

    @parametrize
    async def test_raw_response_policies(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.policies.with_raw_response.policies(
            "bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert policy is None

    @parametrize
    async def test_streaming_response_policies(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.policies.with_streaming_response.policies(
            "bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert policy is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_policies(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.buckets.policies.with_raw_response.policies(
                "",
            )
