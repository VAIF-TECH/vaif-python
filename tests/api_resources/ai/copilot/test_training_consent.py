# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.ai.copilot import TrainingConsentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrainingConsent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        training_consent = client.ai.copilot.training_consent.create(
            session_id="sessionId",
            consent=True,
        )
        assert_matches_type(TrainingConsentCreateResponse, training_consent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.ai.copilot.training_consent.with_raw_response.create(
            session_id="sessionId",
            consent=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_consent = response.parse()
        assert_matches_type(TrainingConsentCreateResponse, training_consent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.ai.copilot.training_consent.with_streaming_response.create(
            session_id="sessionId",
            consent=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_consent = response.parse()
            assert_matches_type(TrainingConsentCreateResponse, training_consent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.ai.copilot.training_consent.with_raw_response.create(
                session_id="",
                consent=True,
            )


class TestAsyncTrainingConsent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        training_consent = await async_client.ai.copilot.training_consent.create(
            session_id="sessionId",
            consent=True,
        )
        assert_matches_type(TrainingConsentCreateResponse, training_consent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.ai.copilot.training_consent.with_raw_response.create(
            session_id="sessionId",
            consent=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_consent = await response.parse()
        assert_matches_type(TrainingConsentCreateResponse, training_consent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.ai.copilot.training_consent.with_streaming_response.create(
            session_id="sessionId",
            consent=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_consent = await response.parse()
            assert_matches_type(TrainingConsentCreateResponse, training_consent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.ai.copilot.training_consent.with_raw_response.create(
                session_id="",
                consent=True,
            )
