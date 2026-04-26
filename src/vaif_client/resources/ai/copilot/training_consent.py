# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.ai.copilot import training_consent_create_params
from ....types.ai.copilot.training_consent_create_response import TrainingConsentCreateResponse

__all__ = ["TrainingConsentResource", "AsyncTrainingConsentResource"]


class TrainingConsentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrainingConsentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return TrainingConsentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingConsentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return TrainingConsentResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        consent: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingConsentCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/ai/copilot/training-consent/{session_id}", session_id=session_id),
            body=maybe_transform({"consent": consent}, training_consent_create_params.TrainingConsentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingConsentCreateResponse,
        )


class AsyncTrainingConsentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrainingConsentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingConsentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingConsentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncTrainingConsentResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        consent: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingConsentCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/ai/copilot/training-consent/{session_id}", session_id=session_id),
            body=await async_maybe_transform(
                {"consent": consent}, training_consent_create_params.TrainingConsentCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingConsentCreateResponse,
        )


class TrainingConsentResourceWithRawResponse:
    def __init__(self, training_consent: TrainingConsentResource) -> None:
        self._training_consent = training_consent

        self.create = to_raw_response_wrapper(
            training_consent.create,
        )


class AsyncTrainingConsentResourceWithRawResponse:
    def __init__(self, training_consent: AsyncTrainingConsentResource) -> None:
        self._training_consent = training_consent

        self.create = async_to_raw_response_wrapper(
            training_consent.create,
        )


class TrainingConsentResourceWithStreamingResponse:
    def __init__(self, training_consent: TrainingConsentResource) -> None:
        self._training_consent = training_consent

        self.create = to_streamed_response_wrapper(
            training_consent.create,
        )


class AsyncTrainingConsentResourceWithStreamingResponse:
    def __init__(self, training_consent: AsyncTrainingConsentResource) -> None:
        self._training_consent = training_consent

        self.create = async_to_streamed_response_wrapper(
            training_consent.create,
        )
