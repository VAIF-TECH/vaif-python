# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.ai.copilot.executions import ResumeResumeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResume:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_resume(self, client: Vaif) -> None:
        resume = client.ai.copilot.executions.resume.resume(
            execution_id="executionId",
        )
        assert_matches_type(ResumeResumeResponse, resume, path=["response"])

    @parametrize
    def test_method_resume_with_all_params(self, client: Vaif) -> None:
        resume = client.ai.copilot.executions.resume.resume(
            execution_id="executionId",
            from_checkpoint="fromCheckpoint",
        )
        assert_matches_type(ResumeResumeResponse, resume, path=["response"])

    @parametrize
    def test_raw_response_resume(self, client: Vaif) -> None:
        response = client.ai.copilot.executions.resume.with_raw_response.resume(
            execution_id="executionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = response.parse()
        assert_matches_type(ResumeResumeResponse, resume, path=["response"])

    @parametrize
    def test_streaming_response_resume(self, client: Vaif) -> None:
        with client.ai.copilot.executions.resume.with_streaming_response.resume(
            execution_id="executionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = response.parse()
            assert_matches_type(ResumeResumeResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resume(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.ai.copilot.executions.resume.with_raw_response.resume(
                execution_id="",
            )


class TestAsyncResume:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_resume(self, async_client: AsyncVaif) -> None:
        resume = await async_client.ai.copilot.executions.resume.resume(
            execution_id="executionId",
        )
        assert_matches_type(ResumeResumeResponse, resume, path=["response"])

    @parametrize
    async def test_method_resume_with_all_params(self, async_client: AsyncVaif) -> None:
        resume = await async_client.ai.copilot.executions.resume.resume(
            execution_id="executionId",
            from_checkpoint="fromCheckpoint",
        )
        assert_matches_type(ResumeResumeResponse, resume, path=["response"])

    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.executions.resume.with_raw_response.resume(
            execution_id="executionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resume = await response.parse()
        assert_matches_type(ResumeResumeResponse, resume, path=["response"])

    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.executions.resume.with_streaming_response.resume(
            execution_id="executionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resume = await response.parse()
            assert_matches_type(ResumeResumeResponse, resume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resume(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.ai.copilot.executions.resume.with_raw_response.resume(
                execution_id="",
            )
