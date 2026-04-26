# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.billing.org import ContactContactsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        contact = client.billing.org.contacts.delete(
            contact_id="contactId",
            org_id="orgId",
        )
        assert contact is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.billing.org.contacts.with_raw_response.delete(
            contact_id="contactId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.billing.org.contacts.with_streaming_response.delete(
            contact_id="contactId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.contacts.with_raw_response.delete(
                contact_id="contactId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.billing.org.contacts.with_raw_response.delete(
                contact_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_contacts(self, client: Vaif) -> None:
        contact = client.billing.org.contacts.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
        )
        assert_matches_type(ContactContactsResponse, contact, path=["response"])

    @parametrize
    def test_method_contacts_with_all_params(self, client: Vaif) -> None:
        contact = client.billing.org.contacts.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
            phone="phone",
            receive_alerts=True,
            receive_invoices=True,
        )
        assert_matches_type(ContactContactsResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_contacts(self, client: Vaif) -> None:
        response = client.billing.org.contacts.with_raw_response.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactContactsResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_contacts(self, client: Vaif) -> None:
        with client.billing.org.contacts.with_streaming_response.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactContactsResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_contacts(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.contacts.with_raw_response.contacts(
                org_id="",
                email="dev@stainless.com",
                name="x",
            )

    @parametrize
    def test_method_get_contacts(self, client: Vaif) -> None:
        contact = client.billing.org.contacts.get_contacts(
            "orgId",
        )
        assert contact is None

    @parametrize
    def test_raw_response_get_contacts(self, client: Vaif) -> None:
        response = client.billing.org.contacts.with_raw_response.get_contacts(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @parametrize
    def test_streaming_response_get_contacts(self, client: Vaif) -> None:
        with client.billing.org.contacts.with_streaming_response.get_contacts(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_contacts(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.contacts.with_raw_response.get_contacts(
                "",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        contact = await async_client.billing.org.contacts.delete(
            contact_id="contactId",
            org_id="orgId",
        )
        assert contact is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.contacts.with_raw_response.delete(
            contact_id="contactId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.contacts.with_streaming_response.delete(
            contact_id="contactId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.contacts.with_raw_response.delete(
                contact_id="contactId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.billing.org.contacts.with_raw_response.delete(
                contact_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_contacts(self, async_client: AsyncVaif) -> None:
        contact = await async_client.billing.org.contacts.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
        )
        assert_matches_type(ContactContactsResponse, contact, path=["response"])

    @parametrize
    async def test_method_contacts_with_all_params(self, async_client: AsyncVaif) -> None:
        contact = await async_client.billing.org.contacts.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
            phone="phone",
            receive_alerts=True,
            receive_invoices=True,
        )
        assert_matches_type(ContactContactsResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_contacts(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.contacts.with_raw_response.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactContactsResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_contacts(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.contacts.with_streaming_response.contacts(
            org_id="orgId",
            email="dev@stainless.com",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactContactsResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_contacts(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.contacts.with_raw_response.contacts(
                org_id="",
                email="dev@stainless.com",
                name="x",
            )

    @parametrize
    async def test_method_get_contacts(self, async_client: AsyncVaif) -> None:
        contact = await async_client.billing.org.contacts.get_contacts(
            "orgId",
        )
        assert contact is None

    @parametrize
    async def test_raw_response_get_contacts(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.contacts.with_raw_response.get_contacts(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @parametrize
    async def test_streaming_response_get_contacts(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.contacts.with_streaming_response.get_contacts(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_contacts(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.contacts.with_raw_response.get_contacts(
                "",
            )
