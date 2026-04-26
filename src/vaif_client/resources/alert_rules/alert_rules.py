# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["AlertRulesResource", "AsyncAlertRulesResource"]


class AlertRulesResource(SyncAPIResource):
    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlertRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AlertRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AlertRulesResourceWithStreamingResponse(self)

    def update(
        self,
        rule_id: str,
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
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/alert-rules/{rule_id}", rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        rule_id: str,
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
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/alert-rules/{rule_id}", rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAlertRulesResource(AsyncAPIResource):
    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlertRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncAlertRulesResourceWithStreamingResponse(self)

    async def update(
        self,
        rule_id: str,
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
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/alert-rules/{rule_id}", rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        rule_id: str,
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
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/alert-rules/{rule_id}", rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AlertRulesResourceWithRawResponse:
    def __init__(self, alert_rules: AlertRulesResource) -> None:
        self._alert_rules = alert_rules

        self.update = to_raw_response_wrapper(
            alert_rules.update,
        )
        self.delete = to_raw_response_wrapper(
            alert_rules.delete,
        )

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._alert_rules.project)


class AsyncAlertRulesResourceWithRawResponse:
    def __init__(self, alert_rules: AsyncAlertRulesResource) -> None:
        self._alert_rules = alert_rules

        self.update = async_to_raw_response_wrapper(
            alert_rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            alert_rules.delete,
        )

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._alert_rules.project)


class AlertRulesResourceWithStreamingResponse:
    def __init__(self, alert_rules: AlertRulesResource) -> None:
        self._alert_rules = alert_rules

        self.update = to_streamed_response_wrapper(
            alert_rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            alert_rules.delete,
        )

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._alert_rules.project)


class AsyncAlertRulesResourceWithStreamingResponse:
    def __init__(self, alert_rules: AsyncAlertRulesResource) -> None:
        self._alert_rules = alert_rules

        self.update = async_to_streamed_response_wrapper(
            alert_rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            alert_rules.delete,
        )

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._alert_rules.project)
