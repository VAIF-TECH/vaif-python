# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_query(self, client: Vaif) -> None:
        query = client.database.connector.query.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Vaif) -> None:
        query = client.database.connector.query.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
            filters={"foo": "bar"},
            limit=1,
            offset=0,
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Vaif) -> None:
        response = client.database.connector.query.with_raw_response.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(object, query, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Vaif) -> None:
        with client.database.connector.query.with_streaming_response.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(object, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.database.connector.query.with_raw_response.query(
                project_id="",
                table="x",
                wrapper_id="x",
            )


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_query(self, async_client: AsyncVaif) -> None:
        query = await async_client.database.connector.query.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncVaif) -> None:
        query = await async_client.database.connector.query.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
            filters={"foo": "bar"},
            limit=1,
            offset=0,
        )
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncVaif) -> None:
        response = await async_client.database.connector.query.with_raw_response.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(object, query, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncVaif) -> None:
        async with async_client.database.connector.query.with_streaming_response.query(
            project_id="projectId",
            table="x",
            wrapper_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(object, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.database.connector.query.with_raw_response.query(
                project_id="",
                table="x",
                wrapper_id="x",
            )
