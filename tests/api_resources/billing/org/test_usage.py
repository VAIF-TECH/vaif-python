# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_history(self, client: Vaif) -> None:
        usage = client.billing.org.usage.get_history(
            "orgId",
        )
        assert usage is None

    @parametrize
    def test_raw_response_get_history(self, client: Vaif) -> None:
        response = client.billing.org.usage.with_raw_response.get_history(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert usage is None

    @parametrize
    def test_streaming_response_get_history(self, client: Vaif) -> None:
        with client.billing.org.usage.with_streaming_response.get_history(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_history(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage.with_raw_response.get_history(
                "",
            )

    @parametrize
    def test_method_get_realtime(self, client: Vaif) -> None:
        usage = client.billing.org.usage.get_realtime(
            "orgId",
        )
        assert usage is None

    @parametrize
    def test_raw_response_get_realtime(self, client: Vaif) -> None:
        response = client.billing.org.usage.with_raw_response.get_realtime(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert usage is None

    @parametrize
    def test_streaming_response_get_realtime(self, client: Vaif) -> None:
        with client.billing.org.usage.with_streaming_response.get_realtime(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_realtime(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage.with_raw_response.get_realtime(
                "",
            )

    @parametrize
    def test_method_get_usage(self, client: Vaif) -> None:
        usage = client.billing.org.usage.get_usage(
            "orgId",
        )
        assert usage is None

    @parametrize
    def test_raw_response_get_usage(self, client: Vaif) -> None:
        response = client.billing.org.usage.with_raw_response.get_usage(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert usage is None

    @parametrize
    def test_streaming_response_get_usage(self, client: Vaif) -> None:
        with client.billing.org.usage.with_streaming_response.get_usage(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_usage(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage.with_raw_response.get_usage(
                "",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_history(self, async_client: AsyncVaif) -> None:
        usage = await async_client.billing.org.usage.get_history(
            "orgId",
        )
        assert usage is None

    @parametrize
    async def test_raw_response_get_history(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage.with_raw_response.get_history(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert usage is None

    @parametrize
    async def test_streaming_response_get_history(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage.with_streaming_response.get_history(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_history(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage.with_raw_response.get_history(
                "",
            )

    @parametrize
    async def test_method_get_realtime(self, async_client: AsyncVaif) -> None:
        usage = await async_client.billing.org.usage.get_realtime(
            "orgId",
        )
        assert usage is None

    @parametrize
    async def test_raw_response_get_realtime(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage.with_raw_response.get_realtime(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert usage is None

    @parametrize
    async def test_streaming_response_get_realtime(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage.with_streaming_response.get_realtime(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_realtime(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage.with_raw_response.get_realtime(
                "",
            )

    @parametrize
    async def test_method_get_usage(self, async_client: AsyncVaif) -> None:
        usage = await async_client.billing.org.usage.get_usage(
            "orgId",
        )
        assert usage is None

    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage.with_raw_response.get_usage(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert usage is None

    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage.with_streaming_response.get_usage(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_usage(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage.with_raw_response.get_usage(
                "",
            )
