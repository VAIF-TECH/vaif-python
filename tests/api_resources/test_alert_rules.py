# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlertRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        alert_rule = client.alert_rules.update(
            "ruleId",
        )
        assert alert_rule is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.alert_rules.with_raw_response.update(
            "ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert_rule = response.parse()
        assert alert_rule is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.alert_rules.with_streaming_response.update(
            "ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert_rule = response.parse()
            assert alert_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.alert_rules.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        alert_rule = client.alert_rules.delete(
            "ruleId",
        )
        assert alert_rule is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.alert_rules.with_raw_response.delete(
            "ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert_rule = response.parse()
        assert alert_rule is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.alert_rules.with_streaming_response.delete(
            "ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert_rule = response.parse()
            assert alert_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.alert_rules.with_raw_response.delete(
                "",
            )


class TestAsyncAlertRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        alert_rule = await async_client.alert_rules.update(
            "ruleId",
        )
        assert alert_rule is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.alert_rules.with_raw_response.update(
            "ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert_rule = await response.parse()
        assert alert_rule is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.alert_rules.with_streaming_response.update(
            "ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert_rule = await response.parse()
            assert alert_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.alert_rules.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        alert_rule = await async_client.alert_rules.delete(
            "ruleId",
        )
        assert alert_rule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.alert_rules.with_raw_response.delete(
            "ruleId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert_rule = await response.parse()
        assert alert_rule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.alert_rules.with_streaming_response.delete(
            "ruleId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert_rule = await response.parse()
            assert alert_rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.alert_rules.with_raw_response.delete(
                "",
            )
