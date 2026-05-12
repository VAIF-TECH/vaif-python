# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.database.extensions.project import install_install_params

__all__ = ["InstallResource", "AsyncInstallResource"]


class InstallResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return InstallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return InstallResourceWithStreamingResponse(self)

    def install(
        self,
        project_id: str,
        *,
        extension_id: str,
        config: Dict[str, object] | Omit = omit,
        env_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/database/extensions/project/{project_id}/install", project_id=project_id),
            body=maybe_transform(
                {
                    "extension_id": extension_id,
                    "config": config,
                    "env_id": env_id,
                },
                install_install_params.InstallInstallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncInstallResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncInstallResourceWithStreamingResponse(self)

    async def install(
        self,
        project_id: str,
        *,
        extension_id: str,
        config: Dict[str, object] | Omit = omit,
        env_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/database/extensions/project/{project_id}/install", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "extension_id": extension_id,
                    "config": config,
                    "env_id": env_id,
                },
                install_install_params.InstallInstallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class InstallResourceWithRawResponse:
    def __init__(self, install: InstallResource) -> None:
        self._install = install

        self.install = to_raw_response_wrapper(
            install.install,
        )


class AsyncInstallResourceWithRawResponse:
    def __init__(self, install: AsyncInstallResource) -> None:
        self._install = install

        self.install = async_to_raw_response_wrapper(
            install.install,
        )


class InstallResourceWithStreamingResponse:
    def __init__(self, install: InstallResource) -> None:
        self._install = install

        self.install = to_streamed_response_wrapper(
            install.install,
        )


class AsyncInstallResourceWithStreamingResponse:
    def __init__(self, install: AsyncInstallResource) -> None:
        self._install = install

        self.install = async_to_streamed_response_wrapper(
            install.install,
        )
