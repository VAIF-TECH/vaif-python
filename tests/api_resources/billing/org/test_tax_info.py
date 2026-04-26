# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.billing.org import TaxInfoTaxInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaxInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_tax_info(self, client: Vaif) -> None:
        tax_info = client.billing.org.tax_info.get_tax_info(
            "orgId",
        )
        assert tax_info is None

    @parametrize
    def test_raw_response_get_tax_info(self, client: Vaif) -> None:
        response = client.billing.org.tax_info.with_raw_response.get_tax_info(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_info = response.parse()
        assert tax_info is None

    @parametrize
    def test_streaming_response_get_tax_info(self, client: Vaif) -> None:
        with client.billing.org.tax_info.with_streaming_response.get_tax_info(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_info = response.parse()
            assert tax_info is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_tax_info(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.tax_info.with_raw_response.get_tax_info(
                "",
            )

    @parametrize
    def test_method_tax_info(self, client: Vaif) -> None:
        tax_info = client.billing.org.tax_info.tax_info(
            org_id="orgId",
        )
        assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

    @parametrize
    def test_method_tax_info_with_all_params(self, client: Vaif) -> None:
        tax_info = client.billing.org.tax_info.tax_info(
            org_id="orgId",
            address={
                "city": "city",
                "country": "xx",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postalCode",
                "state": "state",
            },
            business_name="businessName",
            tax_id="taxId",
            tax_id_type="taxIdType",
        )
        assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

    @parametrize
    def test_raw_response_tax_info(self, client: Vaif) -> None:
        response = client.billing.org.tax_info.with_raw_response.tax_info(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_info = response.parse()
        assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

    @parametrize
    def test_streaming_response_tax_info(self, client: Vaif) -> None:
        with client.billing.org.tax_info.with_streaming_response.tax_info(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_info = response.parse()
            assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tax_info(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.tax_info.with_raw_response.tax_info(
                org_id="",
            )


class TestAsyncTaxInfo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_tax_info(self, async_client: AsyncVaif) -> None:
        tax_info = await async_client.billing.org.tax_info.get_tax_info(
            "orgId",
        )
        assert tax_info is None

    @parametrize
    async def test_raw_response_get_tax_info(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.tax_info.with_raw_response.get_tax_info(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_info = await response.parse()
        assert tax_info is None

    @parametrize
    async def test_streaming_response_get_tax_info(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.tax_info.with_streaming_response.get_tax_info(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_info = await response.parse()
            assert tax_info is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_tax_info(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.tax_info.with_raw_response.get_tax_info(
                "",
            )

    @parametrize
    async def test_method_tax_info(self, async_client: AsyncVaif) -> None:
        tax_info = await async_client.billing.org.tax_info.tax_info(
            org_id="orgId",
        )
        assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

    @parametrize
    async def test_method_tax_info_with_all_params(self, async_client: AsyncVaif) -> None:
        tax_info = await async_client.billing.org.tax_info.tax_info(
            org_id="orgId",
            address={
                "city": "city",
                "country": "xx",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postalCode",
                "state": "state",
            },
            business_name="businessName",
            tax_id="taxId",
            tax_id_type="taxIdType",
        )
        assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

    @parametrize
    async def test_raw_response_tax_info(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.tax_info.with_raw_response.tax_info(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax_info = await response.parse()
        assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

    @parametrize
    async def test_streaming_response_tax_info(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.tax_info.with_streaming_response.tax_info(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax_info = await response.parse()
            assert_matches_type(TaxInfoTaxInfoResponse, tax_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tax_info(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.tax_info.with_raw_response.tax_info(
                org_id="",
            )
