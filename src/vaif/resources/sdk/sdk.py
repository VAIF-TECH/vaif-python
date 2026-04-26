# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .generate import (
    GenerateResource,
    AsyncGenerateResource,
    GenerateResourceWithRawResponse,
    AsyncGenerateResourceWithRawResponse,
    GenerateResourceWithStreamingResponse,
    AsyncGenerateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SDKResource", "AsyncSDKResource"]


class SDKResource(SyncAPIResource):
    @cached_property
    def generate(self) -> GenerateResource:
        return GenerateResource(self._client)

    @cached_property
    def with_raw_response(self) -> SDKResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return SDKResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SDKResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return SDKResourceWithStreamingResponse(self)


class AsyncSDKResource(AsyncAPIResource):
    @cached_property
    def generate(self) -> AsyncGenerateResource:
        return AsyncGenerateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSDKResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSDKResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSDKResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncSDKResourceWithStreamingResponse(self)


class SDKResourceWithRawResponse:
    def __init__(self, sdk: SDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        return GenerateResourceWithRawResponse(self._sdk.generate)


class AsyncSDKResourceWithRawResponse:
    def __init__(self, sdk: AsyncSDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        return AsyncGenerateResourceWithRawResponse(self._sdk.generate)


class SDKResourceWithStreamingResponse:
    def __init__(self, sdk: SDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        return GenerateResourceWithStreamingResponse(self._sdk.generate)


class AsyncSDKResourceWithStreamingResponse:
    def __init__(self, sdk: AsyncSDKResource) -> None:
        self._sdk = sdk

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        return AsyncGenerateResourceWithStreamingResponse(self._sdk.generate)
