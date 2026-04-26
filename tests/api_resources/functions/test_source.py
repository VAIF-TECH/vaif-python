# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.functions import SourceSourceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSource:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_source(self, client: Vaif) -> None:
        source = client.functions.source.source(
            function_id="functionId",
            source_code="x",
        )
        assert_matches_type(SourceSourceResponse, source, path=["response"])

    @parametrize
    def test_raw_response_source(self, client: Vaif) -> None:
        response = client.functions.source.with_raw_response.source(
            function_id="functionId",
            source_code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceSourceResponse, source, path=["response"])

    @parametrize
    def test_streaming_response_source(self, client: Vaif) -> None:
        with client.functions.source.with_streaming_response.source(
            function_id="functionId",
            source_code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceSourceResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_source(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.source.with_raw_response.source(
                function_id="",
                source_code="x",
            )


class TestAsyncSource:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_source(self, async_client: AsyncVaif) -> None:
        source = await async_client.functions.source.source(
            function_id="functionId",
            source_code="x",
        )
        assert_matches_type(SourceSourceResponse, source, path=["response"])

    @parametrize
    async def test_raw_response_source(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.source.with_raw_response.source(
            function_id="functionId",
            source_code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceSourceResponse, source, path=["response"])

    @parametrize
    async def test_streaming_response_source(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.source.with_streaming_response.source(
            function_id="functionId",
            source_code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceSourceResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_source(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.source.with_raw_response.source(
                function_id="",
                source_code="x",
            )
