# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.enterprise import InquireCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInquire:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        inquire = client.enterprise.inquire.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
        )
        assert_matches_type(InquireCreateResponse, inquire, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        inquire = client.enterprise.inquire.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
            company_size="1-10",
            contact_phone="contactPhone",
            current_plan="free",
            estimated_projects=1,
            requirements={
                "bedrock_routing": True,
                "custom_retention": True,
                "custom_sla": True,
                "dedicated_db": True,
                "dedicated_support": True,
                "hipaa_compliance": True,
                "saml": True,
                "soc2_compliance": True,
                "sso": True,
                "vertex_routing": True,
            },
            source="source",
            use_case="useCase",
        )
        assert_matches_type(InquireCreateResponse, inquire, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.enterprise.inquire.with_raw_response.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inquire = response.parse()
        assert_matches_type(InquireCreateResponse, inquire, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.enterprise.inquire.with_streaming_response.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inquire = response.parse()
            assert_matches_type(InquireCreateResponse, inquire, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInquire:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        inquire = await async_client.enterprise.inquire.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
        )
        assert_matches_type(InquireCreateResponse, inquire, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        inquire = await async_client.enterprise.inquire.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
            company_size="1-10",
            contact_phone="contactPhone",
            current_plan="free",
            estimated_projects=1,
            requirements={
                "bedrock_routing": True,
                "custom_retention": True,
                "custom_sla": True,
                "dedicated_db": True,
                "dedicated_support": True,
                "hipaa_compliance": True,
                "saml": True,
                "soc2_compliance": True,
                "sso": True,
                "vertex_routing": True,
            },
            source="source",
            use_case="useCase",
        )
        assert_matches_type(InquireCreateResponse, inquire, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.enterprise.inquire.with_raw_response.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inquire = await response.parse()
        assert_matches_type(InquireCreateResponse, inquire, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.enterprise.inquire.with_streaming_response.create(
            company_name="x",
            contact_email="dev@stainless.com",
            contact_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inquire = await response.parse()
            assert_matches_type(InquireCreateResponse, inquire, path=["response"])

        assert cast(Any, response.is_closed) is True
