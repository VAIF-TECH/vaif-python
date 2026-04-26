# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.incidents import ResolveResolveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResolve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_resolve(self, client: Vaif) -> None:
        resolve = client.incidents.resolve.resolve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResolveResolveResponse, resolve, path=["response"])

    @parametrize
    def test_raw_response_resolve(self, client: Vaif) -> None:
        response = client.incidents.resolve.with_raw_response.resolve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = response.parse()
        assert_matches_type(ResolveResolveResponse, resolve, path=["response"])

    @parametrize
    def test_streaming_response_resolve(self, client: Vaif) -> None:
        with client.incidents.resolve.with_streaming_response.resolve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = response.parse()
            assert_matches_type(ResolveResolveResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resolve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `incident_id` but received ''"):
            client.incidents.resolve.with_raw_response.resolve(
                "",
            )


class TestAsyncResolve:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_resolve(self, async_client: AsyncVaif) -> None:
        resolve = await async_client.incidents.resolve.resolve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResolveResolveResponse, resolve, path=["response"])

    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncVaif) -> None:
        response = await async_client.incidents.resolve.with_raw_response.resolve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = await response.parse()
        assert_matches_type(ResolveResolveResponse, resolve, path=["response"])

    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncVaif) -> None:
        async with async_client.incidents.resolve.with_streaming_response.resolve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = await response.parse()
            assert_matches_type(ResolveResolveResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resolve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `incident_id` but received ''"):
            await async_client.incidents.resolve.with_raw_response.resolve(
                "",
            )
