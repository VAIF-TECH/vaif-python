# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_members(self, client: Vaif) -> None:
        member = client.orgs.members.get_members(
            "orgId",
        )
        assert member is None

    @parametrize
    def test_raw_response_get_members(self, client: Vaif) -> None:
        response = client.orgs.members.with_raw_response.get_members(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert member is None

    @parametrize
    def test_streaming_response_get_members(self, client: Vaif) -> None:
        with client.orgs.members.with_streaming_response.get_members(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_members(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.members.with_raw_response.get_members(
                "",
            )

    @parametrize
    def test_method_invite(self, client: Vaif) -> None:
        member = client.orgs.members.invite(
            "orgId",
        )
        assert member is None

    @parametrize
    def test_raw_response_invite(self, client: Vaif) -> None:
        response = client.orgs.members.with_raw_response.invite(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert member is None

    @parametrize
    def test_streaming_response_invite(self, client: Vaif) -> None:
        with client.orgs.members.with_streaming_response.invite(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invite(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.members.with_raw_response.invite(
                "",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_members(self, async_client: AsyncVaif) -> None:
        member = await async_client.orgs.members.get_members(
            "orgId",
        )
        assert member is None

    @parametrize
    async def test_raw_response_get_members(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.members.with_raw_response.get_members(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert member is None

    @parametrize
    async def test_streaming_response_get_members(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.members.with_streaming_response.get_members(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_members(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.members.with_raw_response.get_members(
                "",
            )

    @parametrize
    async def test_method_invite(self, async_client: AsyncVaif) -> None:
        member = await async_client.orgs.members.invite(
            "orgId",
        )
        assert member is None

    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.members.with_raw_response.invite(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert member is None

    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.members.with_streaming_response.invite(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invite(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.members.with_raw_response.invite(
                "",
            )
