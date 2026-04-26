# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.orgs import (
    BillingContactDeleteResponse,
    BillingContactBillingContactsResponse,
    BillingContactGetBillingContactsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        billing_contact = client.orgs.billing_contacts.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingContactDeleteResponse, billing_contact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.orgs.billing_contacts.with_raw_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_contact = response.parse()
        assert_matches_type(BillingContactDeleteResponse, billing_contact, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.orgs.billing_contacts.with_streaming_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_contact = response.parse()
            assert_matches_type(BillingContactDeleteResponse, billing_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.billing_contacts.with_raw_response.delete(
                contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.orgs.billing_contacts.with_raw_response.delete(
                contact_id="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_billing_contacts(self, client: Vaif) -> None:
        billing_contact = client.orgs.billing_contacts.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
        )
        assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    def test_method_billing_contacts_with_all_params(self, client: Vaif) -> None:
        billing_contact = client.orgs.billing_contacts.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
            label="label",
        )
        assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    def test_raw_response_billing_contacts(self, client: Vaif) -> None:
        response = client.orgs.billing_contacts.with_raw_response.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_contact = response.parse()
        assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    def test_streaming_response_billing_contacts(self, client: Vaif) -> None:
        with client.orgs.billing_contacts.with_streaming_response.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_contact = response.parse()
            assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_billing_contacts(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.billing_contacts.with_raw_response.billing_contacts(
                org_id="",
                email="dev@stainless.com",
            )

    @parametrize
    def test_method_get_billing_contacts(self, client: Vaif) -> None:
        billing_contact = client.orgs.billing_contacts.get_billing_contacts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingContactGetBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    def test_raw_response_get_billing_contacts(self, client: Vaif) -> None:
        response = client.orgs.billing_contacts.with_raw_response.get_billing_contacts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_contact = response.parse()
        assert_matches_type(BillingContactGetBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    def test_streaming_response_get_billing_contacts(self, client: Vaif) -> None:
        with client.orgs.billing_contacts.with_streaming_response.get_billing_contacts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_contact = response.parse()
            assert_matches_type(BillingContactGetBillingContactsResponse, billing_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_billing_contacts(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.billing_contacts.with_raw_response.get_billing_contacts(
                "",
            )


class TestAsyncBillingContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        billing_contact = await async_client.orgs.billing_contacts.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingContactDeleteResponse, billing_contact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.billing_contacts.with_raw_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_contact = await response.parse()
        assert_matches_type(BillingContactDeleteResponse, billing_contact, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.billing_contacts.with_streaming_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_contact = await response.parse()
            assert_matches_type(BillingContactDeleteResponse, billing_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.billing_contacts.with_raw_response.delete(
                contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.orgs.billing_contacts.with_raw_response.delete(
                contact_id="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_billing_contacts(self, async_client: AsyncVaif) -> None:
        billing_contact = await async_client.orgs.billing_contacts.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
        )
        assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    async def test_method_billing_contacts_with_all_params(self, async_client: AsyncVaif) -> None:
        billing_contact = await async_client.orgs.billing_contacts.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
            label="label",
        )
        assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    async def test_raw_response_billing_contacts(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.billing_contacts.with_raw_response.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_contact = await response.parse()
        assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    async def test_streaming_response_billing_contacts(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.billing_contacts.with_streaming_response.billing_contacts(
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_contact = await response.parse()
            assert_matches_type(BillingContactBillingContactsResponse, billing_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_billing_contacts(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.billing_contacts.with_raw_response.billing_contacts(
                org_id="",
                email="dev@stainless.com",
            )

    @parametrize
    async def test_method_get_billing_contacts(self, async_client: AsyncVaif) -> None:
        billing_contact = await async_client.orgs.billing_contacts.get_billing_contacts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BillingContactGetBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    async def test_raw_response_get_billing_contacts(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.billing_contacts.with_raw_response.get_billing_contacts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_contact = await response.parse()
        assert_matches_type(BillingContactGetBillingContactsResponse, billing_contact, path=["response"])

    @parametrize
    async def test_streaming_response_get_billing_contacts(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.billing_contacts.with_streaming_response.get_billing_contacts(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_contact = await response.parse()
            assert_matches_type(BillingContactGetBillingContactsResponse, billing_contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_billing_contacts(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.billing_contacts.with_raw_response.get_billing_contacts(
                "",
            )
