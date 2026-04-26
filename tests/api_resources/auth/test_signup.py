# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.auth import SignupCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSignup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        signup = client.auth.signup.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
        )
        assert_matches_type(SignupCreateResponse, signup, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        signup = client.auth.signup.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
            name="name",
        )
        assert_matches_type(SignupCreateResponse, signup, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.auth.signup.with_raw_response.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signup = response.parse()
        assert_matches_type(SignupCreateResponse, signup, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.auth.signup.with_streaming_response.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signup = response.parse()
            assert_matches_type(SignupCreateResponse, signup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSignup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        signup = await async_client.auth.signup.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
        )
        assert_matches_type(SignupCreateResponse, signup, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        signup = await async_client.auth.signup.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
            name="name",
        )
        assert_matches_type(SignupCreateResponse, signup, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.auth.signup.with_raw_response.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        signup = await response.parse()
        assert_matches_type(SignupCreateResponse, signup, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.auth.signup.with_streaming_response.create(
            email="dev@stainless.com",
            password="xxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            signup = await response.parse()
            assert_matches_type(SignupCreateResponse, signup, path=["response"])

        assert cast(Any, response.is_closed) is True
