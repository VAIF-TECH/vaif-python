# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cancel import (
    CancelResource,
    AsyncCancelResource,
    CancelResourceWithRawResponse,
    AsyncCancelResourceWithRawResponse,
    CancelResourceWithStreamingResponse,
    AsyncCancelResourceWithStreamingResponse,
)
from .resume import (
    ResumeResource,
    AsyncResumeResource,
    ResumeResourceWithRawResponse,
    AsyncResumeResourceWithRawResponse,
    ResumeResourceWithStreamingResponse,
    AsyncResumeResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GenerationResource", "AsyncGenerationResource"]


class GenerationResource(SyncAPIResource):
    @cached_property
    def cancel(self) -> CancelResource:
        return CancelResource(self._client)

    @cached_property
    def resume(self) -> ResumeResource:
        return ResumeResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return GenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return GenerationResourceWithStreamingResponse(self)


class AsyncGenerationResource(AsyncAPIResource):
    @cached_property
    def cancel(self) -> AsyncCancelResource:
        return AsyncCancelResource(self._client)

    @cached_property
    def resume(self) -> AsyncResumeResource:
        return AsyncResumeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncGenerationResourceWithStreamingResponse(self)


class GenerationResourceWithRawResponse:
    def __init__(self, generation: GenerationResource) -> None:
        self._generation = generation

    @cached_property
    def cancel(self) -> CancelResourceWithRawResponse:
        return CancelResourceWithRawResponse(self._generation.cancel)

    @cached_property
    def resume(self) -> ResumeResourceWithRawResponse:
        return ResumeResourceWithRawResponse(self._generation.resume)


class AsyncGenerationResourceWithRawResponse:
    def __init__(self, generation: AsyncGenerationResource) -> None:
        self._generation = generation

    @cached_property
    def cancel(self) -> AsyncCancelResourceWithRawResponse:
        return AsyncCancelResourceWithRawResponse(self._generation.cancel)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithRawResponse:
        return AsyncResumeResourceWithRawResponse(self._generation.resume)


class GenerationResourceWithStreamingResponse:
    def __init__(self, generation: GenerationResource) -> None:
        self._generation = generation

    @cached_property
    def cancel(self) -> CancelResourceWithStreamingResponse:
        return CancelResourceWithStreamingResponse(self._generation.cancel)

    @cached_property
    def resume(self) -> ResumeResourceWithStreamingResponse:
        return ResumeResourceWithStreamingResponse(self._generation.resume)


class AsyncGenerationResourceWithStreamingResponse:
    def __init__(self, generation: AsyncGenerationResource) -> None:
        self._generation = generation

    @cached_property
    def cancel(self) -> AsyncCancelResourceWithStreamingResponse:
        return AsyncCancelResourceWithStreamingResponse(self._generation.cancel)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithStreamingResponse:
        return AsyncResumeResourceWithStreamingResponse(self._generation.resume)
