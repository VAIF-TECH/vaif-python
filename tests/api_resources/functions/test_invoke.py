# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoke:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_invoke(self, client: Vaif) -> None:
        invoke = client.functions.invoke.invoke(
            "functionIdOrName",
        )
        assert invoke is None

    @parametrize
    def test_raw_response_invoke(self, client: Vaif) -> None:
        response = client.functions.invoke.with_raw_response.invoke(
            "functionIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoke = response.parse()
        assert invoke is None

    @parametrize
    def test_streaming_response_invoke(self, client: Vaif) -> None:
        with client.functions.invoke.with_streaming_response.invoke(
            "functionIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoke = response.parse()
            assert invoke is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invoke(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id_or_name` but received ''"):
            client.functions.invoke.with_raw_response.invoke(
                "",
            )


class TestAsyncInvoke:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_invoke(self, async_client: AsyncVaif) -> None:
        invoke = await async_client.functions.invoke.invoke(
            "functionIdOrName",
        )
        assert invoke is None

    @parametrize
    async def test_raw_response_invoke(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.invoke.with_raw_response.invoke(
            "functionIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoke = await response.parse()
        assert invoke is None

    @parametrize
    async def test_streaming_response_invoke(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.invoke.with_streaming_response.invoke(
            "functionIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoke = await response.parse()
            assert invoke is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invoke(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id_or_name` but received ''"):
            await async_client.functions.invoke.with_raw_response.invoke(
                "",
            )
