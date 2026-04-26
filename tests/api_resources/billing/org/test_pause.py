# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPause:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_pause(self, client: Vaif) -> None:
        pause = client.billing.org.pause.pause(
            "orgId",
        )
        assert pause is None

    @parametrize
    def test_raw_response_pause(self, client: Vaif) -> None:
        response = client.billing.org.pause.with_raw_response.pause(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pause = response.parse()
        assert pause is None

    @parametrize
    def test_streaming_response_pause(self, client: Vaif) -> None:
        with client.billing.org.pause.with_streaming_response.pause(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pause = response.parse()
            assert pause is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pause(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.pause.with_raw_response.pause(
                "",
            )


class TestAsyncPause:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_pause(self, async_client: AsyncVaif) -> None:
        pause = await async_client.billing.org.pause.pause(
            "orgId",
        )
        assert pause is None

    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.pause.with_raw_response.pause(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pause = await response.parse()
        assert pause is None

    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.pause.with_streaming_response.pause(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pause = await response.parse()
            assert pause is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pause(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.pause.with_raw_response.pause(
                "",
            )
