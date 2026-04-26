# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.enterprise.org import OnboardingOnboardingResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnboarding:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_onboarding(self, client: Vaif) -> None:
        onboarding = client.enterprise.org.onboarding.get_onboarding(
            "orgId",
        )
        assert onboarding is None

    @parametrize
    def test_raw_response_get_onboarding(self, client: Vaif) -> None:
        response = client.enterprise.org.onboarding.with_raw_response.get_onboarding(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = response.parse()
        assert onboarding is None

    @parametrize
    def test_streaming_response_get_onboarding(self, client: Vaif) -> None:
        with client.enterprise.org.onboarding.with_streaming_response.get_onboarding(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = response.parse()
            assert onboarding is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_onboarding(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.org.onboarding.with_raw_response.get_onboarding(
                "",
            )

    @parametrize
    def test_method_onboarding(self, client: Vaif) -> None:
        onboarding = client.enterprise.org.onboarding.onboarding(
            org_id="orgId",
        )
        assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

    @parametrize
    def test_method_onboarding_with_all_params(self, client: Vaif) -> None:
        onboarding = client.enterprise.org.onboarding.onboarding(
            org_id="orgId",
            dismissed=True,
            steps={"foo": True},
        )
        assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

    @parametrize
    def test_raw_response_onboarding(self, client: Vaif) -> None:
        response = client.enterprise.org.onboarding.with_raw_response.onboarding(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = response.parse()
        assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

    @parametrize
    def test_streaming_response_onboarding(self, client: Vaif) -> None:
        with client.enterprise.org.onboarding.with_streaming_response.onboarding(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = response.parse()
            assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_onboarding(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.enterprise.org.onboarding.with_raw_response.onboarding(
                org_id="",
            )


class TestAsyncOnboarding:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_onboarding(self, async_client: AsyncVaif) -> None:
        onboarding = await async_client.enterprise.org.onboarding.get_onboarding(
            "orgId",
        )
        assert onboarding is None

    @parametrize
    async def test_raw_response_get_onboarding(self, async_client: AsyncVaif) -> None:
        response = await async_client.enterprise.org.onboarding.with_raw_response.get_onboarding(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = await response.parse()
        assert onboarding is None

    @parametrize
    async def test_streaming_response_get_onboarding(self, async_client: AsyncVaif) -> None:
        async with async_client.enterprise.org.onboarding.with_streaming_response.get_onboarding(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = await response.parse()
            assert onboarding is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_onboarding(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.org.onboarding.with_raw_response.get_onboarding(
                "",
            )

    @parametrize
    async def test_method_onboarding(self, async_client: AsyncVaif) -> None:
        onboarding = await async_client.enterprise.org.onboarding.onboarding(
            org_id="orgId",
        )
        assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

    @parametrize
    async def test_method_onboarding_with_all_params(self, async_client: AsyncVaif) -> None:
        onboarding = await async_client.enterprise.org.onboarding.onboarding(
            org_id="orgId",
            dismissed=True,
            steps={"foo": True},
        )
        assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

    @parametrize
    async def test_raw_response_onboarding(self, async_client: AsyncVaif) -> None:
        response = await async_client.enterprise.org.onboarding.with_raw_response.onboarding(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = await response.parse()
        assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

    @parametrize
    async def test_streaming_response_onboarding(self, async_client: AsyncVaif) -> None:
        async with async_client.enterprise.org.onboarding.with_streaming_response.onboarding(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = await response.parse()
            assert_matches_type(OnboardingOnboardingResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_onboarding(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.enterprise.org.onboarding.with_raw_response.onboarding(
                org_id="",
            )
