# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.billing import CheckoutCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckout:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        checkout = client.billing.checkout.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
        )
        assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        checkout = client.billing.checkout.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
            cancel_url="https://example.com",
            interval="monthly",
            promo_code="promoCode",
            success_url="https://example.com",
        )
        assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.billing.checkout.with_raw_response.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout = response.parse()
        assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.billing.checkout.with_streaming_response.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout = response.parse()
            assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCheckout:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        checkout = await async_client.billing.checkout.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
        )
        assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        checkout = await async_client.billing.checkout.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
            cancel_url="https://example.com",
            interval="monthly",
            promo_code="promoCode",
            success_url="https://example.com",
        )
        assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.checkout.with_raw_response.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout = await response.parse()
        assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.checkout.with_streaming_response.create(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan="starter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout = await response.parse()
            assert_matches_type(CheckoutCreateResponse, checkout, path=["response"])

        assert cast(Any, response.is_closed) is True
