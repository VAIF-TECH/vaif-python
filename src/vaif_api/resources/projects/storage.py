# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import storage_settings_params
from ...types.projects.storage_settings_response import StorageSettingsResponse

__all__ = ["StorageResource", "AsyncStorageResource"]


class StorageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return StorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return StorageResourceWithStreamingResponse(self)

    def get_settings(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/projects/{project_id}/storage/settings", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def settings(
        self,
        project_id: str,
        *,
        allowed_mime_types: Optional[SequenceNotStr[str]] | Omit = omit,
        allowed_transforms: SequenceNotStr[str] | Omit = omit,
        blocked_mime_types: SequenceNotStr[str] | Omit = omit,
        cdn_enabled: bool | Omit = omit,
        default_cache_ttl: int | Omit = omit,
        default_file_size_limit: int | Omit = omit,
        edge_caching_enabled: bool | Omit = omit,
        enable_image_transform: bool | Omit = omit,
        max_file_size_limit: int | Omit = omit,
        max_image_dimension: int | Omit = omit,
        signed_url_default_expiry: int | Omit = omit,
        signed_url_max_expiry: int | Omit = omit,
        webhook_enabled: bool | Omit = omit,
        webhook_events: SequenceNotStr[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StorageSettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._patch(
            path_template("/projects/{project_id}/storage/settings", project_id=project_id),
            body=maybe_transform(
                {
                    "allowed_mime_types": allowed_mime_types,
                    "allowed_transforms": allowed_transforms,
                    "blocked_mime_types": blocked_mime_types,
                    "cdn_enabled": cdn_enabled,
                    "default_cache_ttl": default_cache_ttl,
                    "default_file_size_limit": default_file_size_limit,
                    "edge_caching_enabled": edge_caching_enabled,
                    "enable_image_transform": enable_image_transform,
                    "max_file_size_limit": max_file_size_limit,
                    "max_image_dimension": max_image_dimension,
                    "signed_url_default_expiry": signed_url_default_expiry,
                    "signed_url_max_expiry": signed_url_max_expiry,
                    "webhook_enabled": webhook_enabled,
                    "webhook_events": webhook_events,
                    "webhook_url": webhook_url,
                },
                storage_settings_params.StorageSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StorageSettingsResponse,
        )


class AsyncStorageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncStorageResourceWithStreamingResponse(self)

    async def get_settings(
        self,
        project_id: str,
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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/projects/{project_id}/storage/settings", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def settings(
        self,
        project_id: str,
        *,
        allowed_mime_types: Optional[SequenceNotStr[str]] | Omit = omit,
        allowed_transforms: SequenceNotStr[str] | Omit = omit,
        blocked_mime_types: SequenceNotStr[str] | Omit = omit,
        cdn_enabled: bool | Omit = omit,
        default_cache_ttl: int | Omit = omit,
        default_file_size_limit: int | Omit = omit,
        edge_caching_enabled: bool | Omit = omit,
        enable_image_transform: bool | Omit = omit,
        max_file_size_limit: int | Omit = omit,
        max_image_dimension: int | Omit = omit,
        signed_url_default_expiry: int | Omit = omit,
        signed_url_max_expiry: int | Omit = omit,
        webhook_enabled: bool | Omit = omit,
        webhook_events: SequenceNotStr[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StorageSettingsResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._patch(
            path_template("/projects/{project_id}/storage/settings", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "allowed_mime_types": allowed_mime_types,
                    "allowed_transforms": allowed_transforms,
                    "blocked_mime_types": blocked_mime_types,
                    "cdn_enabled": cdn_enabled,
                    "default_cache_ttl": default_cache_ttl,
                    "default_file_size_limit": default_file_size_limit,
                    "edge_caching_enabled": edge_caching_enabled,
                    "enable_image_transform": enable_image_transform,
                    "max_file_size_limit": max_file_size_limit,
                    "max_image_dimension": max_image_dimension,
                    "signed_url_default_expiry": signed_url_default_expiry,
                    "signed_url_max_expiry": signed_url_max_expiry,
                    "webhook_enabled": webhook_enabled,
                    "webhook_events": webhook_events,
                    "webhook_url": webhook_url,
                },
                storage_settings_params.StorageSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StorageSettingsResponse,
        )


class StorageResourceWithRawResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

        self.get_settings = to_raw_response_wrapper(
            storage.get_settings,
        )
        self.settings = to_raw_response_wrapper(
            storage.settings,
        )


class AsyncStorageResourceWithRawResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

        self.get_settings = async_to_raw_response_wrapper(
            storage.get_settings,
        )
        self.settings = async_to_raw_response_wrapper(
            storage.settings,
        )


class StorageResourceWithStreamingResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

        self.get_settings = to_streamed_response_wrapper(
            storage.get_settings,
        )
        self.settings = to_streamed_response_wrapper(
            storage.settings,
        )


class AsyncStorageResourceWithStreamingResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

        self.get_settings = async_to_streamed_response_wrapper(
            storage.get_settings,
        )
        self.settings = async_to_streamed_response_wrapper(
            storage.settings,
        )
