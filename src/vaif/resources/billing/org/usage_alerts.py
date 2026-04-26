# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.billing.org import usage_alert_update_params, usage_alert_usage_alerts_params
from ....types.billing.org.usage_alert_update_response import UsageAlertUpdateResponse
from ....types.billing.org.usage_alert_usage_alerts_response import UsageAlertUsageAlertsResponse

__all__ = ["UsageAlertsResource", "AsyncUsageAlertsResource"]


class UsageAlertsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return UsageAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return UsageAlertsResourceWithStreamingResponse(self)

    def update(
        self,
        alert_id: str,
        *,
        org_id: str,
        enabled: bool | Omit = omit,
        notify_email: bool | Omit = omit,
        threshold: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageAlertUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        return self._patch(
            path_template("/billing/org/{org_id}/usage-alerts/{alert_id}", org_id=org_id, alert_id=alert_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "notify_email": notify_email,
                    "threshold": threshold,
                },
                usage_alert_update_params.UsageAlertUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageAlertUpdateResponse,
        )

    def delete(
        self,
        alert_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/billing/org/{org_id}/usage-alerts/{alert_id}", org_id=org_id, alert_id=alert_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_configured(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/billing/org/{org_id}/usage-alerts/configured", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_history(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/billing/org/{org_id}/usage-alerts/history", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_usage_alerts(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/billing/org/{org_id}/usage-alerts", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def usage_alerts(
        self,
        org_id: str,
        *,
        metric: Literal[
            "ai_credits", "api_requests", "storage", "realtime_connections", "function_invocations", "bandwidth"
        ],
        threshold: float,
        notify_email: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageAlertUsageAlertsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/billing/org/{org_id}/usage-alerts", org_id=org_id),
            body=maybe_transform(
                {
                    "metric": metric,
                    "threshold": threshold,
                    "notify_email": notify_email,
                },
                usage_alert_usage_alerts_params.UsageAlertUsageAlertsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageAlertUsageAlertsResponse,
        )


class AsyncUsageAlertsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncUsageAlertsResourceWithStreamingResponse(self)

    async def update(
        self,
        alert_id: str,
        *,
        org_id: str,
        enabled: bool | Omit = omit,
        notify_email: bool | Omit = omit,
        threshold: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageAlertUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        return await self._patch(
            path_template("/billing/org/{org_id}/usage-alerts/{alert_id}", org_id=org_id, alert_id=alert_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "notify_email": notify_email,
                    "threshold": threshold,
                },
                usage_alert_update_params.UsageAlertUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageAlertUpdateResponse,
        )

    async def delete(
        self,
        alert_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/billing/org/{org_id}/usage-alerts/{alert_id}", org_id=org_id, alert_id=alert_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_configured(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/billing/org/{org_id}/usage-alerts/configured", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_history(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/billing/org/{org_id}/usage-alerts/history", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_usage_alerts(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/billing/org/{org_id}/usage-alerts", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def usage_alerts(
        self,
        org_id: str,
        *,
        metric: Literal[
            "ai_credits", "api_requests", "storage", "realtime_connections", "function_invocations", "bandwidth"
        ],
        threshold: float,
        notify_email: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageAlertUsageAlertsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/billing/org/{org_id}/usage-alerts", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "metric": metric,
                    "threshold": threshold,
                    "notify_email": notify_email,
                },
                usage_alert_usage_alerts_params.UsageAlertUsageAlertsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageAlertUsageAlertsResponse,
        )


class UsageAlertsResourceWithRawResponse:
    def __init__(self, usage_alerts: UsageAlertsResource) -> None:
        self._usage_alerts = usage_alerts

        self.update = to_raw_response_wrapper(
            usage_alerts.update,
        )
        self.delete = to_raw_response_wrapper(
            usage_alerts.delete,
        )
        self.get_configured = to_raw_response_wrapper(
            usage_alerts.get_configured,
        )
        self.get_history = to_raw_response_wrapper(
            usage_alerts.get_history,
        )
        self.get_usage_alerts = to_raw_response_wrapper(
            usage_alerts.get_usage_alerts,
        )
        self.usage_alerts = to_raw_response_wrapper(
            usage_alerts.usage_alerts,
        )


class AsyncUsageAlertsResourceWithRawResponse:
    def __init__(self, usage_alerts: AsyncUsageAlertsResource) -> None:
        self._usage_alerts = usage_alerts

        self.update = async_to_raw_response_wrapper(
            usage_alerts.update,
        )
        self.delete = async_to_raw_response_wrapper(
            usage_alerts.delete,
        )
        self.get_configured = async_to_raw_response_wrapper(
            usage_alerts.get_configured,
        )
        self.get_history = async_to_raw_response_wrapper(
            usage_alerts.get_history,
        )
        self.get_usage_alerts = async_to_raw_response_wrapper(
            usage_alerts.get_usage_alerts,
        )
        self.usage_alerts = async_to_raw_response_wrapper(
            usage_alerts.usage_alerts,
        )


class UsageAlertsResourceWithStreamingResponse:
    def __init__(self, usage_alerts: UsageAlertsResource) -> None:
        self._usage_alerts = usage_alerts

        self.update = to_streamed_response_wrapper(
            usage_alerts.update,
        )
        self.delete = to_streamed_response_wrapper(
            usage_alerts.delete,
        )
        self.get_configured = to_streamed_response_wrapper(
            usage_alerts.get_configured,
        )
        self.get_history = to_streamed_response_wrapper(
            usage_alerts.get_history,
        )
        self.get_usage_alerts = to_streamed_response_wrapper(
            usage_alerts.get_usage_alerts,
        )
        self.usage_alerts = to_streamed_response_wrapper(
            usage_alerts.usage_alerts,
        )


class AsyncUsageAlertsResourceWithStreamingResponse:
    def __init__(self, usage_alerts: AsyncUsageAlertsResource) -> None:
        self._usage_alerts = usage_alerts

        self.update = async_to_streamed_response_wrapper(
            usage_alerts.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            usage_alerts.delete,
        )
        self.get_configured = async_to_streamed_response_wrapper(
            usage_alerts.get_configured,
        )
        self.get_history = async_to_streamed_response_wrapper(
            usage_alerts.get_history,
        )
        self.get_usage_alerts = async_to_streamed_response_wrapper(
            usage_alerts.get_usage_alerts,
        )
        self.usage_alerts = async_to_streamed_response_wrapper(
            usage_alerts.usage_alerts,
        )
