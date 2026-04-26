# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_profile(self, client: Vaif) -> None:
        profile = client.orgs.profile.get_profile(
            "orgId",
        )
        assert profile is None

    @parametrize
    def test_raw_response_get_profile(self, client: Vaif) -> None:
        response = client.orgs.profile.with_raw_response.get_profile(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @parametrize
    def test_streaming_response_get_profile(self, client: Vaif) -> None:
        with client.orgs.profile.with_streaming_response.get_profile(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_profile(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.profile.with_raw_response.get_profile(
                "",
            )

    @parametrize
    def test_method_profile(self, client: Vaif) -> None:
        profile = client.orgs.profile.profile(
            "orgId",
        )
        assert profile is None

    @parametrize
    def test_raw_response_profile(self, client: Vaif) -> None:
        response = client.orgs.profile.with_raw_response.profile(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @parametrize
    def test_streaming_response_profile(self, client: Vaif) -> None:
        with client.orgs.profile.with_streaming_response.profile(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_profile(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.profile.with_raw_response.profile(
                "",
            )


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_profile(self, async_client: AsyncVaif) -> None:
        profile = await async_client.orgs.profile.get_profile(
            "orgId",
        )
        assert profile is None

    @parametrize
    async def test_raw_response_get_profile(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.profile.with_raw_response.get_profile(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @parametrize
    async def test_streaming_response_get_profile(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.profile.with_streaming_response.get_profile(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_profile(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.profile.with_raw_response.get_profile(
                "",
            )

    @parametrize
    async def test_method_profile(self, async_client: AsyncVaif) -> None:
        profile = await async_client.orgs.profile.profile(
            "orgId",
        )
        assert profile is None

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncVaif) -> None:
        response = await async_client.orgs.profile.with_raw_response.profile(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncVaif) -> None:
        async with async_client.orgs.profile.with_streaming_response.profile(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_profile(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.profile.with_raw_response.profile(
                "",
            )
