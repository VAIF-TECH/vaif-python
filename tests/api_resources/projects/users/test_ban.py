# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.projects.users import BanBanResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBan:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ban(self, client: Vaif) -> None:
        ban = client.projects.users.ban.ban(
            user_id="userId",
            project_id="projectId",
        )
        assert_matches_type(BanBanResponse, ban, path=["response"])

    @parametrize
    def test_method_ban_with_all_params(self, client: Vaif) -> None:
        ban = client.projects.users.ban.ban(
            user_id="userId",
            project_id="projectId",
            reason="reason",
        )
        assert_matches_type(BanBanResponse, ban, path=["response"])

    @parametrize
    def test_raw_response_ban(self, client: Vaif) -> None:
        response = client.projects.users.ban.with_raw_response.ban(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = response.parse()
        assert_matches_type(BanBanResponse, ban, path=["response"])

    @parametrize
    def test_streaming_response_ban(self, client: Vaif) -> None:
        with client.projects.users.ban.with_streaming_response.ban(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = response.parse()
            assert_matches_type(BanBanResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_ban(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.ban.with_raw_response.ban(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.ban.with_raw_response.ban(
                user_id="",
                project_id="projectId",
            )


class TestAsyncBan:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_ban(self, async_client: AsyncVaif) -> None:
        ban = await async_client.projects.users.ban.ban(
            user_id="userId",
            project_id="projectId",
        )
        assert_matches_type(BanBanResponse, ban, path=["response"])

    @parametrize
    async def test_method_ban_with_all_params(self, async_client: AsyncVaif) -> None:
        ban = await async_client.projects.users.ban.ban(
            user_id="userId",
            project_id="projectId",
            reason="reason",
        )
        assert_matches_type(BanBanResponse, ban, path=["response"])

    @parametrize
    async def test_raw_response_ban(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.ban.with_raw_response.ban(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ban = await response.parse()
        assert_matches_type(BanBanResponse, ban, path=["response"])

    @parametrize
    async def test_streaming_response_ban(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.ban.with_streaming_response.ban(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ban = await response.parse()
            assert_matches_type(BanBanResponse, ban, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_ban(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.ban.with_raw_response.ban(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.ban.with_raw_response.ban(
                user_id="",
                project_id="projectId",
            )
