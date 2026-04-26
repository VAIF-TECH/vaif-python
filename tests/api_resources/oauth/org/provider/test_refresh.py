# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.oauth.org.provider import RefreshRefreshResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRefresh:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_refresh(self, client: Vaif) -> None:
        refresh = client.oauth.org.provider.refresh.refresh(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RefreshRefreshResponse, refresh, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Vaif) -> None:
        response = client.oauth.org.provider.refresh.with_raw_response.refresh(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refresh = response.parse()
        assert_matches_type(RefreshRefreshResponse, refresh, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Vaif) -> None:
        with client.oauth.org.provider.refresh.with_streaming_response.refresh(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refresh = response.parse()
            assert_matches_type(RefreshRefreshResponse, refresh, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refresh(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.oauth.org.provider.refresh.with_raw_response.refresh(
                provider="x",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.oauth.org.provider.refresh.with_raw_response.refresh(
                provider="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRefresh:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_refresh(self, async_client: AsyncVaif) -> None:
        refresh = await async_client.oauth.org.provider.refresh.refresh(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RefreshRefreshResponse, refresh, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncVaif) -> None:
        response = await async_client.oauth.org.provider.refresh.with_raw_response.refresh(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refresh = await response.parse()
        assert_matches_type(RefreshRefreshResponse, refresh, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncVaif) -> None:
        async with async_client.oauth.org.provider.refresh.with_streaming_response.refresh(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refresh = await response.parse()
            assert_matches_type(RefreshRefreshResponse, refresh, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.oauth.org.provider.refresh.with_raw_response.refresh(
                provider="x",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.oauth.org.provider.refresh.with_raw_response.refresh(
                provider="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
