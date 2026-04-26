# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_check(self, client: Vaif) -> None:
        check = client.entitlements.org.check.check(
            "orgId",
        )
        assert check is None

    @parametrize
    def test_raw_response_check(self, client: Vaif) -> None:
        response = client.entitlements.org.check.with_raw_response.check(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert check is None

    @parametrize
    def test_streaming_response_check(self, client: Vaif) -> None:
        with client.entitlements.org.check.with_streaming_response.check(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert check is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_check(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.entitlements.org.check.with_raw_response.check(
                "",
            )


class TestAsyncCheck:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_check(self, async_client: AsyncVaif) -> None:
        check = await async_client.entitlements.org.check.check(
            "orgId",
        )
        assert check is None

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncVaif) -> None:
        response = await async_client.entitlements.org.check.with_raw_response.check(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert check is None

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncVaif) -> None:
        async with async_client.entitlements.org.check.with_streaming_response.check(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert check is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_check(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.entitlements.org.check.with_raw_response.check(
                "",
            )
