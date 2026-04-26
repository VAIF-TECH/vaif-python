# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bulk(self, client: Vaif) -> None:
        bulk = client.generated.bulk.bulk(
            "table",
        )
        assert bulk is None

    @parametrize
    def test_raw_response_bulk(self, client: Vaif) -> None:
        response = client.generated.bulk.with_raw_response.bulk(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert bulk is None

    @parametrize
    def test_streaming_response_bulk(self, client: Vaif) -> None:
        with client.generated.bulk.with_streaming_response.bulk(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.bulk.with_raw_response.bulk(
                "",
            )

    @parametrize
    def test_method_bulk2(self, client: Vaif) -> None:
        bulk = client.generated.bulk.bulk2(
            "table",
        )
        assert bulk is None

    @parametrize
    def test_raw_response_bulk2(self, client: Vaif) -> None:
        response = client.generated.bulk.with_raw_response.bulk2(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert bulk is None

    @parametrize
    def test_streaming_response_bulk2(self, client: Vaif) -> None:
        with client.generated.bulk.with_streaming_response.bulk2(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk2(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.bulk.with_raw_response.bulk2(
                "",
            )

    @parametrize
    def test_method_bulk3(self, client: Vaif) -> None:
        bulk = client.generated.bulk.bulk3(
            "table",
        )
        assert bulk is None

    @parametrize
    def test_raw_response_bulk3(self, client: Vaif) -> None:
        response = client.generated.bulk.with_raw_response.bulk3(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert bulk is None

    @parametrize
    def test_streaming_response_bulk3(self, client: Vaif) -> None:
        with client.generated.bulk.with_streaming_response.bulk3(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk3(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.bulk.with_raw_response.bulk3(
                "",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_bulk(self, async_client: AsyncVaif) -> None:
        bulk = await async_client.generated.bulk.bulk(
            "table",
        )
        assert bulk is None

    @parametrize
    async def test_raw_response_bulk(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.bulk.with_raw_response.bulk(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert bulk is None

    @parametrize
    async def test_streaming_response_bulk(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.bulk.with_streaming_response.bulk(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.bulk.with_raw_response.bulk(
                "",
            )

    @parametrize
    async def test_method_bulk2(self, async_client: AsyncVaif) -> None:
        bulk = await async_client.generated.bulk.bulk2(
            "table",
        )
        assert bulk is None

    @parametrize
    async def test_raw_response_bulk2(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.bulk.with_raw_response.bulk2(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert bulk is None

    @parametrize
    async def test_streaming_response_bulk2(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.bulk.with_streaming_response.bulk2(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk2(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.bulk.with_raw_response.bulk2(
                "",
            )

    @parametrize
    async def test_method_bulk3(self, async_client: AsyncVaif) -> None:
        bulk = await async_client.generated.bulk.bulk3(
            "table",
        )
        assert bulk is None

    @parametrize
    async def test_raw_response_bulk3(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.bulk.with_raw_response.bulk3(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert bulk is None

    @parametrize
    async def test_streaming_response_bulk3(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.bulk.with_streaming_response.bulk3(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert bulk is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk3(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.bulk.with_raw_response.bulk3(
                "",
            )
