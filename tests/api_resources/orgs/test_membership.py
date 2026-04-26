# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembership:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_membership(self, client: Vaif) -> None:
        membership = client.orgs.membership.get_membership(
            "orgId",
        )
        assert membership is None

    @parametrize
    def test_raw_response_get_membership(self, client: Vaif) -> None:
        response = client.orgs.membership.with_raw_response.get_membership(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert membership is None

    @parametrize
    def test_streaming_response_get_membership(self, client: Vaif) -> None:
        with client.orgs.membership.with_streaming_response.get_membership(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert membership is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_membership(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.membership.with_raw_response.get_membership(
                "",
            )


class TestAsyncMembership:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_membership(self, async_client: AsyncVaif) -> None:
        membership = await async_client.orgs.membership.get_membership(
            "orgId",
        )
        assert membership is None

    @parametrize
    async def test_raw_response_get_membership(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.membership.with_raw_response.get_membership(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert membership is None

    @parametrize
    async def test_streaming_response_get_membership(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.membership.with_streaming_response.get_membership(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert membership is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_membership(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.membership.with_raw_response.get_membership(
                "",
            )
