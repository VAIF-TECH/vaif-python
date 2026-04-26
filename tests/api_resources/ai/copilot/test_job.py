# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.ai.copilot import JobCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        job = client.ai.copilot.job.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        job = client.ai.copilot.job.create(
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
            resume_from_checkpoint="resumeFromCheckpoint",
            resume_from_execution="resumeFromExecution",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.ai.copilot.job.with_raw_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.ai.copilot.job.with_streaming_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        job = client.ai.copilot.job.retrieve(
            "jobId",
        )
        assert job is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.ai.copilot.job.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.ai.copilot.job.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.ai.copilot.job.with_raw_response.retrieve(
                "",
            )


class TestAsyncJob:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        job = await async_client.ai.copilot.job.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        job = await async_client.ai.copilot.job.create(
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
            resume_from_checkpoint="resumeFromCheckpoint",
            resume_from_execution="resumeFromExecution",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.job.with_raw_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.job.with_streaming_response.create(
            message="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        job = await async_client.ai.copilot.job.retrieve(
            "jobId",
        )
        assert job is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.job.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.job.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.ai.copilot.job.with_raw_response.retrieve(
                "",
            )
