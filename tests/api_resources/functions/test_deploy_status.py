# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_deploy_status(self, client: Vaif) -> None:
        deploy_status = client.functions.deploy_status.get_deploy_status(
            "functionId",
        )
        assert deploy_status is None

    @parametrize
    def test_raw_response_get_deploy_status(self, client: Vaif) -> None:
        response = client.functions.deploy_status.with_raw_response.get_deploy_status(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deploy_status = response.parse()
        assert deploy_status is None

    @parametrize
    def test_streaming_response_get_deploy_status(self, client: Vaif) -> None:
        with client.functions.deploy_status.with_streaming_response.get_deploy_status(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deploy_status = response.parse()
            assert deploy_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_deploy_status(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.functions.deploy_status.with_raw_response.get_deploy_status(
                "",
            )


class TestAsyncDeployStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_deploy_status(self, async_client: AsyncVaif) -> None:
        deploy_status = await async_client.functions.deploy_status.get_deploy_status(
            "functionId",
        )
        assert deploy_status is None

    @parametrize
    async def test_raw_response_get_deploy_status(self, async_client: AsyncVaif) -> None:
        response = await async_client.functions.deploy_status.with_raw_response.get_deploy_status(
            "functionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deploy_status = await response.parse()
        assert deploy_status is None

    @parametrize
    async def test_streaming_response_get_deploy_status(self, async_client: AsyncVaif) -> None:
        async with async_client.functions.deploy_status.with_streaming_response.get_deploy_status(
            "functionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deploy_status = await response.parse()
            assert deploy_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_deploy_status(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.functions.deploy_status.with_raw_response.get_deploy_status(
                "",
            )
