# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .aws import (
    AwsResource,
    AsyncAwsResource,
    AwsResourceWithRawResponse,
    AsyncAwsResourceWithRawResponse,
    AwsResourceWithStreamingResponse,
    AsyncAwsResourceWithStreamingResponse,
)
from .gcp import (
    GcpResource,
    AsyncGcpResource,
    GcpResourceWithRawResponse,
    AsyncGcpResourceWithRawResponse,
    GcpResourceWithStreamingResponse,
    AsyncGcpResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TerraformResource", "AsyncTerraformResource"]


class TerraformResource(SyncAPIResource):
    @cached_property
    def aws(self) -> AwsResource:
        return AwsResource(self._client)

    @cached_property
    def gcp(self) -> GcpResource:
        return GcpResource(self._client)

    @cached_property
    def with_raw_response(self) -> TerraformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return TerraformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TerraformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return TerraformResourceWithStreamingResponse(self)


class AsyncTerraformResource(AsyncAPIResource):
    @cached_property
    def aws(self) -> AsyncAwsResource:
        return AsyncAwsResource(self._client)

    @cached_property
    def gcp(self) -> AsyncGcpResource:
        return AsyncGcpResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTerraformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTerraformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTerraformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncTerraformResourceWithStreamingResponse(self)


class TerraformResourceWithRawResponse:
    def __init__(self, terraform: TerraformResource) -> None:
        self._terraform = terraform

    @cached_property
    def aws(self) -> AwsResourceWithRawResponse:
        return AwsResourceWithRawResponse(self._terraform.aws)

    @cached_property
    def gcp(self) -> GcpResourceWithRawResponse:
        return GcpResourceWithRawResponse(self._terraform.gcp)


class AsyncTerraformResourceWithRawResponse:
    def __init__(self, terraform: AsyncTerraformResource) -> None:
        self._terraform = terraform

    @cached_property
    def aws(self) -> AsyncAwsResourceWithRawResponse:
        return AsyncAwsResourceWithRawResponse(self._terraform.aws)

    @cached_property
    def gcp(self) -> AsyncGcpResourceWithRawResponse:
        return AsyncGcpResourceWithRawResponse(self._terraform.gcp)


class TerraformResourceWithStreamingResponse:
    def __init__(self, terraform: TerraformResource) -> None:
        self._terraform = terraform

    @cached_property
    def aws(self) -> AwsResourceWithStreamingResponse:
        return AwsResourceWithStreamingResponse(self._terraform.aws)

    @cached_property
    def gcp(self) -> GcpResourceWithStreamingResponse:
        return GcpResourceWithStreamingResponse(self._terraform.gcp)


class AsyncTerraformResourceWithStreamingResponse:
    def __init__(self, terraform: AsyncTerraformResource) -> None:
        self._terraform = terraform

    @cached_property
    def aws(self) -> AsyncAwsResourceWithStreamingResponse:
        return AsyncAwsResourceWithStreamingResponse(self._terraform.aws)

    @cached_property
    def gcp(self) -> AsyncGcpResourceWithStreamingResponse:
        return AsyncGcpResourceWithStreamingResponse(self._terraform.gcp)
