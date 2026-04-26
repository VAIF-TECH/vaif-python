# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.billing.org import CreditPurchaseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_transactions(self, client: Vaif) -> None:
        credit = client.billing.org.credits.get_transactions(
            "orgId",
        )
        assert credit is None

    @parametrize
    def test_raw_response_get_transactions(self, client: Vaif) -> None:
        response = client.billing.org.credits.with_raw_response.get_transactions(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert credit is None

    @parametrize
    def test_streaming_response_get_transactions(self, client: Vaif) -> None:
        with client.billing.org.credits.with_streaming_response.get_transactions(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert credit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_transactions(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.credits.with_raw_response.get_transactions(
                "",
            )

    @parametrize
    def test_method_purchase(self, client: Vaif) -> None:
        credit = client.billing.org.credits.purchase(
            org_id="orgId",
            package_id="credits_10",
        )
        assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

    @parametrize
    def test_method_purchase_with_all_params(self, client: Vaif) -> None:
        credit = client.billing.org.credits.purchase(
            org_id="orgId",
            package_id="credits_10",
            cancel_url="https://example.com",
            success_url="https://example.com",
        )
        assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

    @parametrize
    def test_raw_response_purchase(self, client: Vaif) -> None:
        response = client.billing.org.credits.with_raw_response.purchase(
            org_id="orgId",
            package_id="credits_10",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

    @parametrize
    def test_streaming_response_purchase(self, client: Vaif) -> None:
        with client.billing.org.credits.with_streaming_response.purchase(
            org_id="orgId",
            package_id="credits_10",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purchase(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.credits.with_raw_response.purchase(
                org_id="",
                package_id="credits_10",
            )


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_transactions(self, async_client: AsyncVaif) -> None:
        credit = await async_client.billing.org.credits.get_transactions(
            "orgId",
        )
        assert credit is None

    @parametrize
    async def test_raw_response_get_transactions(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.credits.with_raw_response.get_transactions(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert credit is None

    @parametrize
    async def test_streaming_response_get_transactions(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.credits.with_streaming_response.get_transactions(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert credit is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_transactions(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.credits.with_raw_response.get_transactions(
                "",
            )

    @parametrize
    async def test_method_purchase(self, async_client: AsyncVaif) -> None:
        credit = await async_client.billing.org.credits.purchase(
            org_id="orgId",
            package_id="credits_10",
        )
        assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

    @parametrize
    async def test_method_purchase_with_all_params(self, async_client: AsyncVaif) -> None:
        credit = await async_client.billing.org.credits.purchase(
            org_id="orgId",
            package_id="credits_10",
            cancel_url="https://example.com",
            success_url="https://example.com",
        )
        assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

    @parametrize
    async def test_raw_response_purchase(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.credits.with_raw_response.purchase(
            org_id="orgId",
            package_id="credits_10",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

    @parametrize
    async def test_streaming_response_purchase(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.credits.with_streaming_response.purchase(
            org_id="orgId",
            package_id="credits_10",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditPurchaseResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purchase(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.credits.with_raw_response.purchase(
                org_id="",
                package_id="credits_10",
            )
