# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .zip import (
    ZipResource,
    AsyncZipResource,
    ZipResourceWithRawResponse,
    AsyncZipResourceWithRawResponse,
    ZipResourceWithStreamingResponse,
    AsyncZipResourceWithStreamingResponse,
)
from .docker import (
    DockerResource,
    AsyncDockerResource,
    DockerResourceWithRawResponse,
    AsyncDockerResourceWithRawResponse,
    DockerResourceWithStreamingResponse,
    AsyncDockerResourceWithStreamingResponse,
)
from .github import (
    GitHubResource,
    AsyncGitHubResource,
    GitHubResourceWithRawResponse,
    AsyncGitHubResourceWithRawResponse,
    GitHubResourceWithStreamingResponse,
    AsyncGitHubResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .terraform.terraform import (
    TerraformResource,
    AsyncTerraformResource,
    TerraformResourceWithRawResponse,
    AsyncTerraformResourceWithRawResponse,
    TerraformResourceWithStreamingResponse,
    AsyncTerraformResourceWithStreamingResponse,
)

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def docker(self) -> DockerResource:
        return DockerResource(self._client)

    @cached_property
    def github(self) -> GitHubResource:
        return GitHubResource(self._client)

    @cached_property
    def terraform(self) -> TerraformResource:
        return TerraformResource(self._client)

    @cached_property
    def zip(self) -> ZipResource:
        return ZipResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def create(
        self,
        version_id: str,
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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/ai/copilot/export/{version_id}", version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def docker(self) -> AsyncDockerResource:
        return AsyncDockerResource(self._client)

    @cached_property
    def github(self) -> AsyncGitHubResource:
        return AsyncGitHubResource(self._client)

    @cached_property
    def terraform(self) -> AsyncTerraformResource:
        return AsyncTerraformResource(self._client)

    @cached_property
    def zip(self) -> AsyncZipResource:
        return AsyncZipResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def create(
        self,
        version_id: str,
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
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/ai/copilot/export/{version_id}", version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_raw_response_wrapper(
            export.create,
        )

    @cached_property
    def docker(self) -> DockerResourceWithRawResponse:
        return DockerResourceWithRawResponse(self._export.docker)

    @cached_property
    def github(self) -> GitHubResourceWithRawResponse:
        return GitHubResourceWithRawResponse(self._export.github)

    @cached_property
    def terraform(self) -> TerraformResourceWithRawResponse:
        return TerraformResourceWithRawResponse(self._export.terraform)

    @cached_property
    def zip(self) -> ZipResourceWithRawResponse:
        return ZipResourceWithRawResponse(self._export.zip)


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_raw_response_wrapper(
            export.create,
        )

    @cached_property
    def docker(self) -> AsyncDockerResourceWithRawResponse:
        return AsyncDockerResourceWithRawResponse(self._export.docker)

    @cached_property
    def github(self) -> AsyncGitHubResourceWithRawResponse:
        return AsyncGitHubResourceWithRawResponse(self._export.github)

    @cached_property
    def terraform(self) -> AsyncTerraformResourceWithRawResponse:
        return AsyncTerraformResourceWithRawResponse(self._export.terraform)

    @cached_property
    def zip(self) -> AsyncZipResourceWithRawResponse:
        return AsyncZipResourceWithRawResponse(self._export.zip)


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_streamed_response_wrapper(
            export.create,
        )

    @cached_property
    def docker(self) -> DockerResourceWithStreamingResponse:
        return DockerResourceWithStreamingResponse(self._export.docker)

    @cached_property
    def github(self) -> GitHubResourceWithStreamingResponse:
        return GitHubResourceWithStreamingResponse(self._export.github)

    @cached_property
    def terraform(self) -> TerraformResourceWithStreamingResponse:
        return TerraformResourceWithStreamingResponse(self._export.terraform)

    @cached_property
    def zip(self) -> ZipResourceWithStreamingResponse:
        return ZipResourceWithStreamingResponse(self._export.zip)


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_streamed_response_wrapper(
            export.create,
        )

    @cached_property
    def docker(self) -> AsyncDockerResourceWithStreamingResponse:
        return AsyncDockerResourceWithStreamingResponse(self._export.docker)

    @cached_property
    def github(self) -> AsyncGitHubResourceWithStreamingResponse:
        return AsyncGitHubResourceWithStreamingResponse(self._export.github)

    @cached_property
    def terraform(self) -> AsyncTerraformResourceWithStreamingResponse:
        return AsyncTerraformResourceWithStreamingResponse(self._export.terraform)

    @cached_property
    def zip(self) -> AsyncZipResourceWithStreamingResponse:
        return AsyncZipResourceWithStreamingResponse(self._export.zip)
