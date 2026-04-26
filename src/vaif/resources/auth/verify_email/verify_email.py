# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .send import (
    SendResource,
    AsyncSendResource,
    SendResourceWithRawResponse,
    AsyncSendResourceWithRawResponse,
    SendResourceWithStreamingResponse,
    AsyncSendResourceWithStreamingResponse,
)
from .confirm import (
    ConfirmResource,
    AsyncConfirmResource,
    ConfirmResourceWithRawResponse,
    AsyncConfirmResourceWithRawResponse,
    ConfirmResourceWithStreamingResponse,
    AsyncConfirmResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VerifyEmailResource", "AsyncVerifyEmailResource"]


class VerifyEmailResource(SyncAPIResource):
    @cached_property
    def confirm(self) -> ConfirmResource:
        return ConfirmResource(self._client)

    @cached_property
    def send(self) -> SendResource:
        return SendResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerifyEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return VerifyEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifyEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return VerifyEmailResourceWithStreamingResponse(self)


class AsyncVerifyEmailResource(AsyncAPIResource):
    @cached_property
    def confirm(self) -> AsyncConfirmResource:
        return AsyncConfirmResource(self._client)

    @cached_property
    def send(self) -> AsyncSendResource:
        return AsyncSendResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerifyEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifyEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifyEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncVerifyEmailResourceWithStreamingResponse(self)


class VerifyEmailResourceWithRawResponse:
    def __init__(self, verify_email: VerifyEmailResource) -> None:
        self._verify_email = verify_email

    @cached_property
    def confirm(self) -> ConfirmResourceWithRawResponse:
        return ConfirmResourceWithRawResponse(self._verify_email.confirm)

    @cached_property
    def send(self) -> SendResourceWithRawResponse:
        return SendResourceWithRawResponse(self._verify_email.send)


class AsyncVerifyEmailResourceWithRawResponse:
    def __init__(self, verify_email: AsyncVerifyEmailResource) -> None:
        self._verify_email = verify_email

    @cached_property
    def confirm(self) -> AsyncConfirmResourceWithRawResponse:
        return AsyncConfirmResourceWithRawResponse(self._verify_email.confirm)

    @cached_property
    def send(self) -> AsyncSendResourceWithRawResponse:
        return AsyncSendResourceWithRawResponse(self._verify_email.send)


class VerifyEmailResourceWithStreamingResponse:
    def __init__(self, verify_email: VerifyEmailResource) -> None:
        self._verify_email = verify_email

    @cached_property
    def confirm(self) -> ConfirmResourceWithStreamingResponse:
        return ConfirmResourceWithStreamingResponse(self._verify_email.confirm)

    @cached_property
    def send(self) -> SendResourceWithStreamingResponse:
        return SendResourceWithStreamingResponse(self._verify_email.send)


class AsyncVerifyEmailResourceWithStreamingResponse:
    def __init__(self, verify_email: AsyncVerifyEmailResource) -> None:
        self._verify_email = verify_email

    @cached_property
    def confirm(self) -> AsyncConfirmResourceWithStreamingResponse:
        return AsyncConfirmResourceWithStreamingResponse(self._verify_email.confirm)

    @cached_property
    def send(self) -> AsyncSendResourceWithStreamingResponse:
        return AsyncSendResourceWithStreamingResponse(self._verify_email.send)
