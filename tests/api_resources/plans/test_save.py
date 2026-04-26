# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.plans import SaveCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSave:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        save = client.plans.save.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [{"action": "x"}],
                "version": "x",
            },
            task_type="x",
        )
        assert_matches_type(SaveCreateResponse, save, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Vaif) -> None:
        save = client.plans.save.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [
                    {
                        "action": "x",
                        "args": {"foo": "bar"},
                    }
                ],
                "version": "x",
                "warnings": ["string"],
            },
            task_type="x",
            description="description",
            visibility="public",
        )
        assert_matches_type(SaveCreateResponse, save, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.plans.save.with_raw_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [{"action": "x"}],
                "version": "x",
            },
            task_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        save = response.parse()
        assert_matches_type(SaveCreateResponse, save, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.plans.save.with_streaming_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [{"action": "x"}],
                "version": "x",
            },
            task_type="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            save = response.parse()
            assert_matches_type(SaveCreateResponse, save, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSave:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        save = await async_client.plans.save.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [{"action": "x"}],
                "version": "x",
            },
            task_type="x",
        )
        assert_matches_type(SaveCreateResponse, save, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncVaif) -> None:
        save = await async_client.plans.save.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [
                    {
                        "action": "x",
                        "args": {"foo": "bar"},
                    }
                ],
                "version": "x",
                "warnings": ["string"],
            },
            task_type="x",
            description="description",
            visibility="public",
        )
        assert_matches_type(SaveCreateResponse, save, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.plans.save.with_raw_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [{"action": "x"}],
                "version": "x",
            },
            task_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        save = await response.parse()
        assert_matches_type(SaveCreateResponse, save, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.plans.save.with_streaming_response.create(
            name="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            plan={
                "intent": "x",
                "steps": [{"action": "x"}],
                "version": "x",
            },
            task_type="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            save = await response.parse()
            assert_matches_type(SaveCreateResponse, save, path=["response"])

        assert cast(Any, response.is_closed) is True
