# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.schema_engine import ChangeGetChangesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_changes(self, client: Vaif) -> None:
        change = client.schema_engine.changes.get_changes(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChangeGetChangesResponse, change, path=["response"])

    @parametrize
    def test_raw_response_get_changes(self, client: Vaif) -> None:
        response = client.schema_engine.changes.with_raw_response.get_changes(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = response.parse()
        assert_matches_type(ChangeGetChangesResponse, change, path=["response"])

    @parametrize
    def test_streaming_response_get_changes(self, client: Vaif) -> None:
        with client.schema_engine.changes.with_streaming_response.get_changes(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = response.parse()
            assert_matches_type(ChangeGetChangesResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_changes(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.schema_engine.changes.with_raw_response.get_changes(
                "",
            )


class TestAsyncChanges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_changes(self, async_client: AsyncVaif) -> None:
        change = await async_client.schema_engine.changes.get_changes(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChangeGetChangesResponse, change, path=["response"])

    @parametrize
    async def test_raw_response_get_changes(self, async_client: AsyncVaif) -> None:
        response = await async_client.schema_engine.changes.with_raw_response.get_changes(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = await response.parse()
        assert_matches_type(ChangeGetChangesResponse, change, path=["response"])

    @parametrize
    async def test_streaming_response_get_changes(self, async_client: AsyncVaif) -> None:
        async with async_client.schema_engine.changes.with_streaming_response.get_changes(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = await response.parse()
            assert_matches_type(ChangeGetChangesResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_changes(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.schema_engine.changes.with_raw_response.get_changes(
                "",
            )
