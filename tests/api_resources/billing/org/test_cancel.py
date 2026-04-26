# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.billing.org import CancelCancelResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCancel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel(self, client: Vaif) -> None:
        cancel = client.billing.org.cancel.cancel(
            org_id="orgId",
        )
        assert_matches_type(CancelCancelResponse, cancel, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Vaif) -> None:
        cancel = client.billing.org.cancel.cancel(
            org_id="orgId",
            cancel_immediately=True,
        )
        assert_matches_type(CancelCancelResponse, cancel, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Vaif) -> None:
        response = client.billing.org.cancel.with_raw_response.cancel(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancel = response.parse()
        assert_matches_type(CancelCancelResponse, cancel, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Vaif) -> None:
        with client.billing.org.cancel.with_streaming_response.cancel(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancel = response.parse()
            assert_matches_type(CancelCancelResponse, cancel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.cancel.with_raw_response.cancel(
                org_id="",
            )


class TestAsyncCancel:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncVaif) -> None:
        cancel = await async_client.billing.org.cancel.cancel(
            org_id="orgId",
        )
        assert_matches_type(CancelCancelResponse, cancel, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncVaif) -> None:
        cancel = await async_client.billing.org.cancel.cancel(
            org_id="orgId",
            cancel_immediately=True,
        )
        assert_matches_type(CancelCancelResponse, cancel, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.cancel.with_raw_response.cancel(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cancel = await response.parse()
        assert_matches_type(CancelCancelResponse, cancel, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.cancel.with_streaming_response.cancel(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cancel = await response.parse()
            assert_matches_type(CancelCancelResponse, cancel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.cancel.with_raw_response.cancel(
                org_id="",
            )
