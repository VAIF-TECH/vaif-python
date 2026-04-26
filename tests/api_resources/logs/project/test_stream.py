# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStream:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_stream(self, client: Vaif) -> None:
        stream = client.logs.project.stream.get_stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert stream is None

    @parametrize
    def test_raw_response_get_stream(self, client: Vaif) -> None:
        response = client.logs.project.stream.with_raw_response.get_stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert stream is None

    @parametrize
    def test_streaming_response_get_stream(self, client: Vaif) -> None:
        with client.logs.project.stream.with_streaming_response.get_stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_stream(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.logs.project.stream.with_raw_response.get_stream(
                "",
            )


class TestAsyncStream:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_stream(self, async_client: AsyncVaif) -> None:
        stream = await async_client.logs.project.stream.get_stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert stream is None

    @parametrize
    async def test_raw_response_get_stream(self, async_client: AsyncVaif) -> None:
        response = await async_client.logs.project.stream.with_raw_response.get_stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert stream is None

    @parametrize
    async def test_streaming_response_get_stream(self, async_client: AsyncVaif) -> None:
        async with async_client.logs.project.stream.with_streaming_response.get_stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_stream(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.logs.project.stream.with_raw_response.get_stream(
                "",
            )
