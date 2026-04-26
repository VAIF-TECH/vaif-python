# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResume:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_resume(self, client: Vaif) -> None:
        resume = client.billing.org.resume.resume(
            "orgId",
        )
        assert resume is None

    @parametrize
    def test_raw_response_resume(self, client: Vaif) -> None:
        response = client.billing.org.resume.with_raw_response.resume(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert resume is None

    @parametrize
    def test_streaming_response_resume(self, client: Vaif) -> None:
        with client.billing.org.resume.with_streaming_response.resume(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert resume is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resume(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.resume.with_raw_response.resume(
                "",
            )


class TestAsyncResume:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_resume(self, async_client: AsyncVaif) -> None:
        resume = await async_client.billing.org.resume.resume(
            "orgId",
        )
        assert resume is None

    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.resume.with_raw_response.resume(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert resume is None

    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.resume.with_streaming_response.resume(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert resume is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resume(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.resume.with_raw_response.resume(
                "",
            )
