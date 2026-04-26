# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        chat = client.ai.copilot.chat.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        chat = client.ai.copilot.chat.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[
                {
                    "content": "content",
                    "type": "schema",
                    "name": "name",
                }
            ],
            generation_options={
                "api_style": "rest",
                "architecture": "mvc",
                "audit_logs": True,
                "auth_method": "vaif",
                "containerization": "docker",
                "database": "vaif",
                "db_migrations": True,
                "deploy_target": "railway",
                "email_verification": True,
                "feature_flags": True,
                "framework": "framework",
                "git_hooks": True,
                "health_checks": True,
                "include_api_collection": True,
                "include_sample_data": True,
                "include_sdk_client": True,
                "language": "typescript",
                "mfa": True,
                "mode": "opinionated",
                "multi_tenant": "single",
                "output_depth": "minimal",
                "rate_limiting": True,
                "rbac": "off",
                "realtime": "websockets",
                "scope": "schema-only",
                "security_headers": True,
                "storage": "vaif",
                "tests": ["unit"],
            },
            generation_types=["schema"],
            model_id="modelId",
            pinned_context={
                "bucket_ids": ["string"],
                "function_ids": ["string"],
                "table_ids": ["string"],
            },
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            stream=True,
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.ai.copilot.chat.with_raw_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.ai.copilot.chat.with_streaming_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        chat = await async_client.ai.copilot.chat.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        chat = await async_client.ai.copilot.chat.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments=[
                {
                    "content": "content",
                    "type": "schema",
                    "name": "name",
                }
            ],
            generation_options={
                "api_style": "rest",
                "architecture": "mvc",
                "audit_logs": True,
                "auth_method": "vaif",
                "containerization": "docker",
                "database": "vaif",
                "db_migrations": True,
                "deploy_target": "railway",
                "email_verification": True,
                "feature_flags": True,
                "framework": "framework",
                "git_hooks": True,
                "health_checks": True,
                "include_api_collection": True,
                "include_sample_data": True,
                "include_sdk_client": True,
                "language": "typescript",
                "mfa": True,
                "mode": "opinionated",
                "multi_tenant": "single",
                "output_depth": "minimal",
                "rate_limiting": True,
                "rbac": "off",
                "realtime": "websockets",
                "scope": "schema-only",
                "security_headers": True,
                "storage": "vaif",
                "tests": ["unit"],
            },
            generation_types=["schema"],
            model_id="modelId",
            pinned_context={
                "bucket_ids": ["string"],
                "function_ids": ["string"],
                "table_ids": ["string"],
            },
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            stream=True,
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.chat.with_raw_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.chat.with_streaming_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
