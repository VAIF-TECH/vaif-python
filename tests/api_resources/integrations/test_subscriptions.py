# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.integrations import (
    SubscriptionCreateResponse,
    SubscriptionDeleteResponse,
    SubscriptionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        subscription = client.integrations.subscriptions.create(
            config={},
            event_filter={},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        subscription = client.integrations.subscriptions.create(
            config={
                "api_key": "apiKey",
                "api_secret": "apiSecret",
                "headers": {"foo": "string"},
                "measurement_id": "measurementId",
                "project_id": "projectId",
                "provider": "provider",
                "secret": "secret",
                "url": "https://example.com",
            },
            event_filter={"allow": ["string"]},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.integrations.subscriptions.with_raw_response.create(
            config={},
            event_filter={},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.integrations.subscriptions.with_streaming_response.create(
            config={},
            event_filter={},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        subscription = client.integrations.subscriptions.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.integrations.subscriptions.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.integrations.subscriptions.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integrations.subscriptions.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        subscription = client.integrations.subscriptions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.integrations.subscriptions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.integrations.subscriptions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integrations.subscriptions.with_raw_response.delete(
                "",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        subscription = await async_client.integrations.subscriptions.create(
            config={},
            event_filter={},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        subscription = await async_client.integrations.subscriptions.create(
            config={
                "api_key": "apiKey",
                "api_secret": "apiSecret",
                "headers": {"foo": "string"},
                "measurement_id": "measurementId",
                "project_id": "projectId",
                "provider": "provider",
                "secret": "secret",
                "url": "https://example.com",
            },
            event_filter={"allow": ["string"]},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.integrations.subscriptions.with_raw_response.create(
            config={},
            event_filter={},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.integrations.subscriptions.with_streaming_response.create(
            config={},
            event_filter={},
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        subscription = await async_client.integrations.subscriptions.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.integrations.subscriptions.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.integrations.subscriptions.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integrations.subscriptions.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        subscription = await async_client.integrations.subscriptions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.integrations.subscriptions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.integrations.subscriptions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integrations.subscriptions.with_raw_response.delete(
                "",
            )
