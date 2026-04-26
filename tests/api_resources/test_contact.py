# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types import ContactCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        contact = client.contact.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        contact = client.contact.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
            company="company",
            website="website",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.contact.with_raw_response.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.contact.with_streaming_response.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContact:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        contact = await async_client.contact.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        contact = await async_client.contact.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
            company="company",
            website="website",
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.contact.with_raw_response.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.contact.with_streaming_response.create(
            email="dev@stainless.com",
            message="x",
            name="x",
            subject="Sales Inquiry",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
