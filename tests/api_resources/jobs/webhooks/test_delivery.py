# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDelivery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        delivery = client.jobs.webhooks.delivery.retrieve(
            "deliveryId",
        )
        assert delivery is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.jobs.webhooks.delivery.with_raw_response.retrieve(
            "deliveryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert delivery is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.jobs.webhooks.delivery.with_streaming_response.retrieve(
            "deliveryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.jobs.webhooks.delivery.with_raw_response.retrieve(
                "",
            )


class TestAsyncDelivery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        delivery = await async_client.jobs.webhooks.delivery.retrieve(
            "deliveryId",
        )
        assert delivery is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.jobs.webhooks.delivery.with_raw_response.retrieve(
            "deliveryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert delivery is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.jobs.webhooks.delivery.with_streaming_response.retrieve(
            "deliveryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert delivery is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.jobs.webhooks.delivery.with_raw_response.retrieve(
                "",
            )
