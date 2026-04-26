# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_configure(self, client: Vaif) -> None:
        configure = client.sso.org.configure.configure(
            "orgId",
        )
        assert configure is None

    @parametrize
    def test_raw_response_configure(self, client: Vaif) -> None:
        response = client.sso.org.configure.with_raw_response.configure(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configure = response.parse()
        assert configure is None

    @parametrize
    def test_streaming_response_configure(self, client: Vaif) -> None:
        with client.sso.org.configure.with_streaming_response.configure(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configure = response.parse()
            assert configure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_configure(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.sso.org.configure.with_raw_response.configure(
                "",
            )


class TestAsyncConfigure:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_configure(self, async_client: AsyncVaif) -> None:
        configure = await async_client.sso.org.configure.configure(
            "orgId",
        )
        assert configure is None

    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncVaif) -> None:
        response = await async_client.sso.org.configure.with_raw_response.configure(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configure = await response.parse()
        assert configure is None

    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncVaif) -> None:
        async with async_client.sso.org.configure.with_streaming_response.configure(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configure = await response.parse()
            assert configure is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_configure(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.sso.org.configure.with_raw_response.configure(
                "",
            )
