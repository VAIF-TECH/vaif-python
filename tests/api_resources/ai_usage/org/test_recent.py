# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_recent(self, client: Vaif) -> None:
        recent = client.ai_usage.org.recent.get_recent(
            "orgId",
        )
        assert recent is None

    @parametrize
    def test_raw_response_get_recent(self, client: Vaif) -> None:
        response = client.ai_usage.org.recent.with_raw_response.get_recent(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recent = response.parse()
        assert recent is None

    @parametrize
    def test_streaming_response_get_recent(self, client: Vaif) -> None:
        with client.ai_usage.org.recent.with_streaming_response.get_recent(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recent = response.parse()
            assert recent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_recent(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.ai_usage.org.recent.with_raw_response.get_recent(
                "",
            )


class TestAsyncRecent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_recent(self, async_client: AsyncVaif) -> None:
        recent = await async_client.ai_usage.org.recent.get_recent(
            "orgId",
        )
        assert recent is None

    @parametrize
    async def test_raw_response_get_recent(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai_usage.org.recent.with_raw_response.get_recent(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recent = await response.parse()
        assert recent is None

    @parametrize
    async def test_streaming_response_get_recent(self, async_client: AsyncVaif) -> None:
        async with async_client.ai_usage.org.recent.with_streaming_response.get_recent(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recent = await response.parse()
            assert recent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_recent(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.ai_usage.org.recent.with_raw_response.get_recent(
                "",
            )
