# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.auth.me import LinkedAccountListResponse, LinkedAccountDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinkedAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Vaif) -> None:
        linked_account = client.auth.me.linked_accounts.list()
        assert_matches_type(LinkedAccountListResponse, linked_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Vaif) -> None:
        response = client.auth.me.linked_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linked_account = response.parse()
        assert_matches_type(LinkedAccountListResponse, linked_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Vaif) -> None:
        with client.auth.me.linked_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linked_account = response.parse()
            assert_matches_type(LinkedAccountListResponse, linked_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        linked_account = client.auth.me.linked_accounts.delete(
            "x",
        )
        assert_matches_type(LinkedAccountDeleteResponse, linked_account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.auth.me.linked_accounts.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linked_account = response.parse()
        assert_matches_type(LinkedAccountDeleteResponse, linked_account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.auth.me.linked_accounts.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linked_account = response.parse()
            assert_matches_type(LinkedAccountDeleteResponse, linked_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.auth.me.linked_accounts.with_raw_response.delete(
                "",
            )


class TestAsyncLinkedAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncVaif) -> None:
        linked_account = await async_client.auth.me.linked_accounts.list()
        assert_matches_type(LinkedAccountListResponse, linked_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.me.linked_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linked_account = await response.parse()
        assert_matches_type(LinkedAccountListResponse, linked_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.me.linked_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linked_account = await response.parse()
            assert_matches_type(LinkedAccountListResponse, linked_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        linked_account = await async_client.auth.me.linked_accounts.delete(
            "x",
        )
        assert_matches_type(LinkedAccountDeleteResponse, linked_account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.me.linked_accounts.with_raw_response.delete(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        linked_account = await response.parse()
        assert_matches_type(LinkedAccountDeleteResponse, linked_account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.me.linked_accounts.with_streaming_response.delete(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            linked_account = await response.parse()
            assert_matches_type(LinkedAccountDeleteResponse, linked_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.auth.me.linked_accounts.with_raw_response.delete(
                "",
            )
