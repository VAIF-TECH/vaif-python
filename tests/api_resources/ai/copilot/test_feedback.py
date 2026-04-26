# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.ai.copilot import FeedbackCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        feedback = client.ai.copilot.feedback.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        feedback = client.ai.copilot.feedback.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            corrected_intent="correctedIntent",
            user_feedback="userFeedback",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.ai.copilot.feedback.with_raw_response.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.ai.copilot.feedback.with_streaming_response.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        feedback = await async_client.ai.copilot.feedback.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        feedback = await async_client.ai.copilot.feedback.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            corrected_intent="correctedIntent",
            user_feedback="userFeedback",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.feedback.with_raw_response.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.feedback.with_streaming_response.create(
            feedback_type="correct",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
