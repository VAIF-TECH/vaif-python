# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.schema_engine import PreviewCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        preview = client.schema_engine.preview.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                            }
                        ],
                        "name": "x",
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        preview = client.schema_engine.preview.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                                "default": "string",
                                "nullable": True,
                                "primary_key": True,
                                "references": {
                                    "table": "table",
                                    "column": "column",
                                    "on_delete": "CASCADE",
                                    "on_update": "CASCADE",
                                },
                                "unique": True,
                            }
                        ],
                        "name": "x",
                        "indexes": [
                            {
                                "columns": ["x"],
                                "name": "x",
                                "unique": True,
                            }
                        ],
                        "unique": [
                            {
                                "columns": ["x"],
                                "name": "x",
                            }
                        ],
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_destructive=True,
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.schema_engine.preview.with_raw_response.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                            }
                        ],
                        "name": "x",
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.schema_engine.preview.with_streaming_response.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                            }
                        ],
                        "name": "x",
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewCreateResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreview:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        preview = await async_client.schema_engine.preview.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                            }
                        ],
                        "name": "x",
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        preview = await async_client.schema_engine.preview.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                                "default": "string",
                                "nullable": True,
                                "primary_key": True,
                                "references": {
                                    "table": "table",
                                    "column": "column",
                                    "on_delete": "CASCADE",
                                    "on_update": "CASCADE",
                                },
                                "unique": True,
                            }
                        ],
                        "name": "x",
                        "indexes": [
                            {
                                "columns": ["x"],
                                "name": "x",
                                "unique": True,
                            }
                        ],
                        "unique": [
                            {
                                "columns": ["x"],
                                "name": "x",
                            }
                        ],
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_destructive=True,
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.schema_engine.preview.with_raw_response.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                            }
                        ],
                        "name": "x",
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.schema_engine.preview.with_streaming_response.create(
            definition={
                "schema_version": "1.0",
                "tables": [
                    {
                        "columns": [
                            {
                                "name": "x",
                                "type": "uuid",
                            }
                        ],
                        "name": "x",
                    }
                ],
            },
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewCreateResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True
