# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        invite = client.orgs.invites.delete(
            invite_id="inviteId",
            org_id="orgId",
        )
        assert invite is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.orgs.invites.with_raw_response.delete(
            invite_id="inviteId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert invite is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.orgs.invites.with_streaming_response.delete(
            invite_id="inviteId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert invite is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.invites.with_raw_response.delete(
                invite_id="inviteId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.orgs.invites.with_raw_response.delete(
                invite_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_get_invites(self, client: Vaif) -> None:
        invite = client.orgs.invites.get_invites(
            "orgId",
        )
        assert invite is None

    @parametrize
    def test_raw_response_get_invites(self, client: Vaif) -> None:
        response = client.orgs.invites.with_raw_response.get_invites(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert invite is None

    @parametrize
    def test_streaming_response_get_invites(self, client: Vaif) -> None:
        with client.orgs.invites.with_streaming_response.get_invites(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert invite is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_invites(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.invites.with_raw_response.get_invites(
                "",
            )


class TestAsyncInvites:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        invite = await async_client.orgs.invites.delete(
            invite_id="inviteId",
            org_id="orgId",
        )
        assert invite is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.invites.with_raw_response.delete(
            invite_id="inviteId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert invite is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.invites.with_streaming_response.delete(
            invite_id="inviteId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert invite is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.invites.with_raw_response.delete(
                invite_id="inviteId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.orgs.invites.with_raw_response.delete(
                invite_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_get_invites(self, async_client: AsyncVaif) -> None:
        invite = await async_client.orgs.invites.get_invites(
            "orgId",
        )
        assert invite is None

    @parametrize
    async def test_raw_response_get_invites(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.invites.with_raw_response.get_invites(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert invite is None

    @parametrize
    async def test_streaming_response_get_invites(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.invites.with_streaming_response.get_invites(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert invite is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_invites(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.invites.with_raw_response.get_invites(
                "",
            )
