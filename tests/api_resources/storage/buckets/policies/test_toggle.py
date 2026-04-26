# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToggle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_toggle(self, client: Vaif) -> None:
        toggle = client.storage.buckets.policies.toggle.toggle(
            policy_id="policyId",
            bucket_id="bucketId",
        )
        assert toggle is None

    @parametrize
    def test_raw_response_toggle(self, client: Vaif) -> None:
        response = client.storage.buckets.policies.toggle.with_raw_response.toggle(
            policy_id="policyId",
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toggle = response.parse()
        assert toggle is None

    @parametrize
    def test_streaming_response_toggle(self, client: Vaif) -> None:
        with client.storage.buckets.policies.toggle.with_streaming_response.toggle(
            policy_id="policyId",
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toggle = response.parse()
            assert toggle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_toggle(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            client.storage.buckets.policies.toggle.with_raw_response.toggle(
                policy_id="policyId",
                bucket_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.storage.buckets.policies.toggle.with_raw_response.toggle(
                policy_id="",
                bucket_id="bucketId",
            )


class TestAsyncToggle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_toggle(self, async_client: AsyncVaif) -> None:
        toggle = await async_client.storage.buckets.policies.toggle.toggle(
            policy_id="policyId",
            bucket_id="bucketId",
        )
        assert toggle is None

    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncVaif) -> None:
        response = await async_client.storage.buckets.policies.toggle.with_raw_response.toggle(
            policy_id="policyId",
            bucket_id="bucketId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toggle = await response.parse()
        assert toggle is None

    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncVaif) -> None:
        async with async_client.storage.buckets.policies.toggle.with_streaming_response.toggle(
            policy_id="policyId",
            bucket_id="bucketId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toggle = await response.parse()
            assert toggle is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_toggle(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_id` but received ''"):
            await async_client.storage.buckets.policies.toggle.with_raw_response.toggle(
                policy_id="policyId",
                bucket_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.storage.buckets.policies.toggle.with_raw_response.toggle(
                policy_id="",
                bucket_id="bucketId",
            )
