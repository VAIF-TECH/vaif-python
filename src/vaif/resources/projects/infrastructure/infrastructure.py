# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .stop import (
    StopResource,
    AsyncStopResource,
    StopResourceWithRawResponse,
    AsyncStopResourceWithRawResponse,
    StopResourceWithStreamingResponse,
    AsyncStopResourceWithStreamingResponse,
)
from .start import (
    StartResource,
    AsyncStartResource,
    StartResourceWithRawResponse,
    AsyncStartResourceWithRawResponse,
    StartResourceWithStreamingResponse,
    AsyncStartResourceWithStreamingResponse,
)
from .resize import (
    ResizeResource,
    AsyncResizeResource,
    ResizeResourceWithRawResponse,
    AsyncResizeResourceWithRawResponse,
    ResizeResourceWithStreamingResponse,
    AsyncResizeResourceWithStreamingResponse,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from .replicas import (
    ReplicasResource,
    AsyncReplicasResource,
    ReplicasResourceWithRawResponse,
    AsyncReplicasResourceWithRawResponse,
    ReplicasResourceWithStreamingResponse,
    AsyncReplicasResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from .migrate_now import (
    MigrateNowResource,
    AsyncMigrateNowResource,
    MigrateNowResourceWithRawResponse,
    AsyncMigrateNowResourceWithRawResponse,
    MigrateNowResourceWithStreamingResponse,
    AsyncMigrateNowResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resize_custom import (
    ResizeCustomResource,
    AsyncResizeCustomResource,
    ResizeCustomResourceWithRawResponse,
    AsyncResizeCustomResourceWithRawResponse,
    ResizeCustomResourceWithStreamingResponse,
    AsyncResizeCustomResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .upgrade_options import (
    UpgradeOptionsResource,
    AsyncUpgradeOptionsResource,
    UpgradeOptionsResourceWithRawResponse,
    AsyncUpgradeOptionsResourceWithRawResponse,
    UpgradeOptionsResourceWithStreamingResponse,
    AsyncUpgradeOptionsResourceWithStreamingResponse,
)

__all__ = ["InfrastructureResource", "AsyncInfrastructureResource"]


class InfrastructureResource(SyncAPIResource):
    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def migrate_now(self) -> MigrateNowResource:
        return MigrateNowResource(self._client)

    @cached_property
    def replicas(self) -> ReplicasResource:
        return ReplicasResource(self._client)

    @cached_property
    def resize(self) -> ResizeResource:
        return ResizeResource(self._client)

    @cached_property
    def resize_custom(self) -> ResizeCustomResource:
        return ResizeCustomResource(self._client)

    @cached_property
    def start(self) -> StartResource:
        return StartResource(self._client)

    @cached_property
    def stop(self) -> StopResource:
        return StopResource(self._client)

    @cached_property
    def upgrade_options(self) -> UpgradeOptionsResource:
        return UpgradeOptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InfrastructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return InfrastructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfrastructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return InfrastructureResourceWithStreamingResponse(self)

    def delete(
        self,
        instance_id: str,
        *,
        project_id: str,
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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/projects/{project_id}/infrastructure/{instance_id}", project_id=project_id, instance_id=instance_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_infrastructure(
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
            path_template("/projects/{project_id}/infrastructure", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_migration_status(
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
            path_template("/projects/{project_id}/infrastructure/migration-status", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_progress(
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
            path_template("/projects/{project_id}/infrastructure/migration/progress", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def provision(
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
        return self._post(
            path_template("/projects/{project_id}/infrastructure/provision", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def provision_custom(
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
        return self._post(
            path_template("/projects/{project_id}/infrastructure/provision-custom", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retry(
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
        return self._post(
            path_template("/projects/{project_id}/infrastructure/migration/retry", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rollback(
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
        return self._post(
            path_template("/projects/{project_id}/infrastructure/migration/rollback", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInfrastructureResource(AsyncAPIResource):
    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def migrate_now(self) -> AsyncMigrateNowResource:
        return AsyncMigrateNowResource(self._client)

    @cached_property
    def replicas(self) -> AsyncReplicasResource:
        return AsyncReplicasResource(self._client)

    @cached_property
    def resize(self) -> AsyncResizeResource:
        return AsyncResizeResource(self._client)

    @cached_property
    def resize_custom(self) -> AsyncResizeCustomResource:
        return AsyncResizeCustomResource(self._client)

    @cached_property
    def start(self) -> AsyncStartResource:
        return AsyncStartResource(self._client)

    @cached_property
    def stop(self) -> AsyncStopResource:
        return AsyncStopResource(self._client)

    @cached_property
    def upgrade_options(self) -> AsyncUpgradeOptionsResource:
        return AsyncUpgradeOptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInfrastructureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfrastructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfrastructureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncInfrastructureResourceWithStreamingResponse(self)

    async def delete(
        self,
        instance_id: str,
        *,
        project_id: str,
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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/projects/{project_id}/infrastructure/{instance_id}", project_id=project_id, instance_id=instance_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_infrastructure(
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
            path_template("/projects/{project_id}/infrastructure", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_migration_status(
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
            path_template("/projects/{project_id}/infrastructure/migration-status", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_progress(
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
            path_template("/projects/{project_id}/infrastructure/migration/progress", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def provision(
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
        return await self._post(
            path_template("/projects/{project_id}/infrastructure/provision", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def provision_custom(
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
        return await self._post(
            path_template("/projects/{project_id}/infrastructure/provision-custom", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retry(
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
        return await self._post(
            path_template("/projects/{project_id}/infrastructure/migration/retry", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rollback(
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
        return await self._post(
            path_template("/projects/{project_id}/infrastructure/migration/rollback", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InfrastructureResourceWithRawResponse:
    def __init__(self, infrastructure: InfrastructureResource) -> None:
        self._infrastructure = infrastructure

        self.delete = to_raw_response_wrapper(
            infrastructure.delete,
        )
        self.get_infrastructure = to_raw_response_wrapper(
            infrastructure.get_infrastructure,
        )
        self.get_migration_status = to_raw_response_wrapper(
            infrastructure.get_migration_status,
        )
        self.get_progress = to_raw_response_wrapper(
            infrastructure.get_progress,
        )
        self.provision = to_raw_response_wrapper(
            infrastructure.provision,
        )
        self.provision_custom = to_raw_response_wrapper(
            infrastructure.provision_custom,
        )
        self.retry = to_raw_response_wrapper(
            infrastructure.retry,
        )
        self.rollback = to_raw_response_wrapper(
            infrastructure.rollback,
        )

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._infrastructure.metrics)

    @cached_property
    def migrate_now(self) -> MigrateNowResourceWithRawResponse:
        return MigrateNowResourceWithRawResponse(self._infrastructure.migrate_now)

    @cached_property
    def replicas(self) -> ReplicasResourceWithRawResponse:
        return ReplicasResourceWithRawResponse(self._infrastructure.replicas)

    @cached_property
    def resize(self) -> ResizeResourceWithRawResponse:
        return ResizeResourceWithRawResponse(self._infrastructure.resize)

    @cached_property
    def resize_custom(self) -> ResizeCustomResourceWithRawResponse:
        return ResizeCustomResourceWithRawResponse(self._infrastructure.resize_custom)

    @cached_property
    def start(self) -> StartResourceWithRawResponse:
        return StartResourceWithRawResponse(self._infrastructure.start)

    @cached_property
    def stop(self) -> StopResourceWithRawResponse:
        return StopResourceWithRawResponse(self._infrastructure.stop)

    @cached_property
    def upgrade_options(self) -> UpgradeOptionsResourceWithRawResponse:
        return UpgradeOptionsResourceWithRawResponse(self._infrastructure.upgrade_options)


class AsyncInfrastructureResourceWithRawResponse:
    def __init__(self, infrastructure: AsyncInfrastructureResource) -> None:
        self._infrastructure = infrastructure

        self.delete = async_to_raw_response_wrapper(
            infrastructure.delete,
        )
        self.get_infrastructure = async_to_raw_response_wrapper(
            infrastructure.get_infrastructure,
        )
        self.get_migration_status = async_to_raw_response_wrapper(
            infrastructure.get_migration_status,
        )
        self.get_progress = async_to_raw_response_wrapper(
            infrastructure.get_progress,
        )
        self.provision = async_to_raw_response_wrapper(
            infrastructure.provision,
        )
        self.provision_custom = async_to_raw_response_wrapper(
            infrastructure.provision_custom,
        )
        self.retry = async_to_raw_response_wrapper(
            infrastructure.retry,
        )
        self.rollback = async_to_raw_response_wrapper(
            infrastructure.rollback,
        )

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._infrastructure.metrics)

    @cached_property
    def migrate_now(self) -> AsyncMigrateNowResourceWithRawResponse:
        return AsyncMigrateNowResourceWithRawResponse(self._infrastructure.migrate_now)

    @cached_property
    def replicas(self) -> AsyncReplicasResourceWithRawResponse:
        return AsyncReplicasResourceWithRawResponse(self._infrastructure.replicas)

    @cached_property
    def resize(self) -> AsyncResizeResourceWithRawResponse:
        return AsyncResizeResourceWithRawResponse(self._infrastructure.resize)

    @cached_property
    def resize_custom(self) -> AsyncResizeCustomResourceWithRawResponse:
        return AsyncResizeCustomResourceWithRawResponse(self._infrastructure.resize_custom)

    @cached_property
    def start(self) -> AsyncStartResourceWithRawResponse:
        return AsyncStartResourceWithRawResponse(self._infrastructure.start)

    @cached_property
    def stop(self) -> AsyncStopResourceWithRawResponse:
        return AsyncStopResourceWithRawResponse(self._infrastructure.stop)

    @cached_property
    def upgrade_options(self) -> AsyncUpgradeOptionsResourceWithRawResponse:
        return AsyncUpgradeOptionsResourceWithRawResponse(self._infrastructure.upgrade_options)


class InfrastructureResourceWithStreamingResponse:
    def __init__(self, infrastructure: InfrastructureResource) -> None:
        self._infrastructure = infrastructure

        self.delete = to_streamed_response_wrapper(
            infrastructure.delete,
        )
        self.get_infrastructure = to_streamed_response_wrapper(
            infrastructure.get_infrastructure,
        )
        self.get_migration_status = to_streamed_response_wrapper(
            infrastructure.get_migration_status,
        )
        self.get_progress = to_streamed_response_wrapper(
            infrastructure.get_progress,
        )
        self.provision = to_streamed_response_wrapper(
            infrastructure.provision,
        )
        self.provision_custom = to_streamed_response_wrapper(
            infrastructure.provision_custom,
        )
        self.retry = to_streamed_response_wrapper(
            infrastructure.retry,
        )
        self.rollback = to_streamed_response_wrapper(
            infrastructure.rollback,
        )

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._infrastructure.metrics)

    @cached_property
    def migrate_now(self) -> MigrateNowResourceWithStreamingResponse:
        return MigrateNowResourceWithStreamingResponse(self._infrastructure.migrate_now)

    @cached_property
    def replicas(self) -> ReplicasResourceWithStreamingResponse:
        return ReplicasResourceWithStreamingResponse(self._infrastructure.replicas)

    @cached_property
    def resize(self) -> ResizeResourceWithStreamingResponse:
        return ResizeResourceWithStreamingResponse(self._infrastructure.resize)

    @cached_property
    def resize_custom(self) -> ResizeCustomResourceWithStreamingResponse:
        return ResizeCustomResourceWithStreamingResponse(self._infrastructure.resize_custom)

    @cached_property
    def start(self) -> StartResourceWithStreamingResponse:
        return StartResourceWithStreamingResponse(self._infrastructure.start)

    @cached_property
    def stop(self) -> StopResourceWithStreamingResponse:
        return StopResourceWithStreamingResponse(self._infrastructure.stop)

    @cached_property
    def upgrade_options(self) -> UpgradeOptionsResourceWithStreamingResponse:
        return UpgradeOptionsResourceWithStreamingResponse(self._infrastructure.upgrade_options)


class AsyncInfrastructureResourceWithStreamingResponse:
    def __init__(self, infrastructure: AsyncInfrastructureResource) -> None:
        self._infrastructure = infrastructure

        self.delete = async_to_streamed_response_wrapper(
            infrastructure.delete,
        )
        self.get_infrastructure = async_to_streamed_response_wrapper(
            infrastructure.get_infrastructure,
        )
        self.get_migration_status = async_to_streamed_response_wrapper(
            infrastructure.get_migration_status,
        )
        self.get_progress = async_to_streamed_response_wrapper(
            infrastructure.get_progress,
        )
        self.provision = async_to_streamed_response_wrapper(
            infrastructure.provision,
        )
        self.provision_custom = async_to_streamed_response_wrapper(
            infrastructure.provision_custom,
        )
        self.retry = async_to_streamed_response_wrapper(
            infrastructure.retry,
        )
        self.rollback = async_to_streamed_response_wrapper(
            infrastructure.rollback,
        )

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._infrastructure.metrics)

    @cached_property
    def migrate_now(self) -> AsyncMigrateNowResourceWithStreamingResponse:
        return AsyncMigrateNowResourceWithStreamingResponse(self._infrastructure.migrate_now)

    @cached_property
    def replicas(self) -> AsyncReplicasResourceWithStreamingResponse:
        return AsyncReplicasResourceWithStreamingResponse(self._infrastructure.replicas)

    @cached_property
    def resize(self) -> AsyncResizeResourceWithStreamingResponse:
        return AsyncResizeResourceWithStreamingResponse(self._infrastructure.resize)

    @cached_property
    def resize_custom(self) -> AsyncResizeCustomResourceWithStreamingResponse:
        return AsyncResizeCustomResourceWithStreamingResponse(self._infrastructure.resize_custom)

    @cached_property
    def start(self) -> AsyncStartResourceWithStreamingResponse:
        return AsyncStartResourceWithStreamingResponse(self._infrastructure.start)

    @cached_property
    def stop(self) -> AsyncStopResourceWithStreamingResponse:
        return AsyncStopResourceWithStreamingResponse(self._infrastructure.stop)

    @cached_property
    def upgrade_options(self) -> AsyncUpgradeOptionsResourceWithStreamingResponse:
        return AsyncUpgradeOptionsResourceWithStreamingResponse(self._infrastructure.upgrade_options)
