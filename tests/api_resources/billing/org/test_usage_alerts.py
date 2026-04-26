# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.billing.org import (
    UsageAlertUpdateResponse,
    UsageAlertUsageAlertsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.update(
            alert_id="alertId",
            org_id="orgId",
        )
        assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.update(
            alert_id="alertId",
            org_id="orgId",
            enabled=True,
            notify_email=True,
            threshold=1,
        )
        assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.billing.org.usage_alerts.with_raw_response.update(
            alert_id="alertId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = response.parse()
        assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.billing.org.usage_alerts.with_streaming_response.update(
            alert_id="alertId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = response.parse()
            assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.update(
                alert_id="alertId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.update(
                alert_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.delete(
            alert_id="alertId",
            org_id="orgId",
        )
        assert usage_alert is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.billing.org.usage_alerts.with_raw_response.delete(
            alert_id="alertId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = response.parse()
        assert usage_alert is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.billing.org.usage_alerts.with_streaming_response.delete(
            alert_id="alertId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.delete(
                alert_id="alertId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.delete(
                alert_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_get_configured(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.get_configured(
            "orgId",
        )
        assert usage_alert is None

    @parametrize
    def test_raw_response_get_configured(self, client: Vaif) -> None:
        response = client.billing.org.usage_alerts.with_raw_response.get_configured(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = response.parse()
        assert usage_alert is None

    @parametrize
    def test_streaming_response_get_configured(self, client: Vaif) -> None:
        with client.billing.org.usage_alerts.with_streaming_response.get_configured(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_configured(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.get_configured(
                "",
            )

    @parametrize
    def test_method_get_history(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.get_history(
            "orgId",
        )
        assert usage_alert is None

    @parametrize
    def test_raw_response_get_history(self, client: Vaif) -> None:
        response = client.billing.org.usage_alerts.with_raw_response.get_history(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = response.parse()
        assert usage_alert is None

    @parametrize
    def test_streaming_response_get_history(self, client: Vaif) -> None:
        with client.billing.org.usage_alerts.with_streaming_response.get_history(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_history(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.get_history(
                "",
            )

    @parametrize
    def test_method_get_usage_alerts(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.get_usage_alerts(
            "orgId",
        )
        assert usage_alert is None

    @parametrize
    def test_raw_response_get_usage_alerts(self, client: Vaif) -> None:
        response = client.billing.org.usage_alerts.with_raw_response.get_usage_alerts(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = response.parse()
        assert usage_alert is None

    @parametrize
    def test_streaming_response_get_usage_alerts(self, client: Vaif) -> None:
        with client.billing.org.usage_alerts.with_streaming_response.get_usage_alerts(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_usage_alerts(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.get_usage_alerts(
                "",
            )

    @parametrize
    def test_method_usage_alerts(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
        )
        assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

    @parametrize
    def test_method_usage_alerts_with_all_params(self, client: Vaif) -> None:
        usage_alert = client.billing.org.usage_alerts.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
            notify_email=True,
        )
        assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

    @parametrize
    def test_raw_response_usage_alerts(self, client: Vaif) -> None:
        response = client.billing.org.usage_alerts.with_raw_response.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = response.parse()
        assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

    @parametrize
    def test_streaming_response_usage_alerts(self, client: Vaif) -> None:
        with client.billing.org.usage_alerts.with_streaming_response.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = response.parse()
            assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_usage_alerts(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.usage_alerts.with_raw_response.usage_alerts(
                org_id="",
                metric="ai_credits",
                threshold=1,
            )


class TestAsyncUsageAlerts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.update(
            alert_id="alertId",
            org_id="orgId",
        )
        assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.update(
            alert_id="alertId",
            org_id="orgId",
            enabled=True,
            notify_email=True,
            threshold=1,
        )
        assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage_alerts.with_raw_response.update(
            alert_id="alertId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = await response.parse()
        assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage_alerts.with_streaming_response.update(
            alert_id="alertId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = await response.parse()
            assert_matches_type(UsageAlertUpdateResponse, usage_alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.update(
                alert_id="alertId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.update(
                alert_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.delete(
            alert_id="alertId",
            org_id="orgId",
        )
        assert usage_alert is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage_alerts.with_raw_response.delete(
            alert_id="alertId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = await response.parse()
        assert usage_alert is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage_alerts.with_streaming_response.delete(
            alert_id="alertId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = await response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.delete(
                alert_id="alertId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alert_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.delete(
                alert_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_get_configured(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.get_configured(
            "orgId",
        )
        assert usage_alert is None

    @parametrize
    async def test_raw_response_get_configured(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage_alerts.with_raw_response.get_configured(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = await response.parse()
        assert usage_alert is None

    @parametrize
    async def test_streaming_response_get_configured(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage_alerts.with_streaming_response.get_configured(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = await response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_configured(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.get_configured(
                "",
            )

    @parametrize
    async def test_method_get_history(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.get_history(
            "orgId",
        )
        assert usage_alert is None

    @parametrize
    async def test_raw_response_get_history(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage_alerts.with_raw_response.get_history(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = await response.parse()
        assert usage_alert is None

    @parametrize
    async def test_streaming_response_get_history(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage_alerts.with_streaming_response.get_history(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = await response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_history(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.get_history(
                "",
            )

    @parametrize
    async def test_method_get_usage_alerts(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.get_usage_alerts(
            "orgId",
        )
        assert usage_alert is None

    @parametrize
    async def test_raw_response_get_usage_alerts(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage_alerts.with_raw_response.get_usage_alerts(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = await response.parse()
        assert usage_alert is None

    @parametrize
    async def test_streaming_response_get_usage_alerts(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage_alerts.with_streaming_response.get_usage_alerts(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = await response.parse()
            assert usage_alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_usage_alerts(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.get_usage_alerts(
                "",
            )

    @parametrize
    async def test_method_usage_alerts(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
        )
        assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

    @parametrize
    async def test_method_usage_alerts_with_all_params(self, async_client: AsyncVaif) -> None:
        usage_alert = await async_client.billing.org.usage_alerts.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
            notify_email=True,
        )
        assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

    @parametrize
    async def test_raw_response_usage_alerts(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.usage_alerts.with_raw_response.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_alert = await response.parse()
        assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

    @parametrize
    async def test_streaming_response_usage_alerts(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.usage_alerts.with_streaming_response.usage_alerts(
            org_id="orgId",
            metric="ai_credits",
            threshold=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_alert = await response.parse()
            assert_matches_type(UsageAlertUsageAlertsResponse, usage_alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_usage_alerts(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.usage_alerts.with_raw_response.usage_alerts(
                org_id="",
                metric="ai_credits",
                threshold=1,
            )
