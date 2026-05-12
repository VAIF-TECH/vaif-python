# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .faqs import (
    FaqsResource,
    AsyncFaqsResource,
    FaqsResourceWithRawResponse,
    AsyncFaqsResourceWithRawResponse,
    FaqsResourceWithStreamingResponse,
    AsyncFaqsResourceWithStreamingResponse,
)
from .team import (
    TeamResource,
    AsyncTeamResource,
    TeamResourceWithRawResponse,
    AsyncTeamResourceWithRawResponse,
    TeamResourceWithStreamingResponse,
    AsyncTeamResourceWithStreamingResponse,
)
from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from .careers import (
    CareersResource,
    AsyncCareersResource,
    CareersResourceWithRawResponse,
    AsyncCareersResourceWithRawResponse,
    CareersResourceWithStreamingResponse,
    AsyncCareersResourceWithStreamingResponse,
)
from .partners import (
    PartnersResource,
    AsyncPartnersResource,
    PartnersResourceWithRawResponse,
    AsyncPartnersResourceWithRawResponse,
    PartnersResourceWithStreamingResponse,
    AsyncPartnersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .testimonials import (
    TestimonialsResource,
    AsyncTestimonialsResource,
    TestimonialsResourceWithRawResponse,
    AsyncTestimonialsResourceWithRawResponse,
    TestimonialsResourceWithStreamingResponse,
    AsyncTestimonialsResourceWithStreamingResponse,
)

__all__ = ["CmsResource", "AsyncCmsResource"]


class CmsResource(SyncAPIResource):
    @cached_property
    def careers(self) -> CareersResource:
        return CareersResource(self._client)

    @cached_property
    def faqs(self) -> FaqsResource:
        return FaqsResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def partners(self) -> PartnersResource:
        return PartnersResource(self._client)

    @cached_property
    def team(self) -> TeamResource:
        return TeamResource(self._client)

    @cached_property
    def testimonials(self) -> TestimonialsResource:
        return TestimonialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CmsResourceWithStreamingResponse(self)


class AsyncCmsResource(AsyncAPIResource):
    @cached_property
    def careers(self) -> AsyncCareersResource:
        return AsyncCareersResource(self._client)

    @cached_property
    def faqs(self) -> AsyncFaqsResource:
        return AsyncFaqsResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def partners(self) -> AsyncPartnersResource:
        return AsyncPartnersResource(self._client)

    @cached_property
    def team(self) -> AsyncTeamResource:
        return AsyncTeamResource(self._client)

    @cached_property
    def testimonials(self) -> AsyncTestimonialsResource:
        return AsyncTestimonialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCmsResourceWithStreamingResponse(self)


class CmsResourceWithRawResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def careers(self) -> CareersResourceWithRawResponse:
        return CareersResourceWithRawResponse(self._cms.careers)

    @cached_property
    def faqs(self) -> FaqsResourceWithRawResponse:
        return FaqsResourceWithRawResponse(self._cms.faqs)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._cms.pages)

    @cached_property
    def partners(self) -> PartnersResourceWithRawResponse:
        return PartnersResourceWithRawResponse(self._cms.partners)

    @cached_property
    def team(self) -> TeamResourceWithRawResponse:
        return TeamResourceWithRawResponse(self._cms.team)

    @cached_property
    def testimonials(self) -> TestimonialsResourceWithRawResponse:
        return TestimonialsResourceWithRawResponse(self._cms.testimonials)


class AsyncCmsResourceWithRawResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def careers(self) -> AsyncCareersResourceWithRawResponse:
        return AsyncCareersResourceWithRawResponse(self._cms.careers)

    @cached_property
    def faqs(self) -> AsyncFaqsResourceWithRawResponse:
        return AsyncFaqsResourceWithRawResponse(self._cms.faqs)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._cms.pages)

    @cached_property
    def partners(self) -> AsyncPartnersResourceWithRawResponse:
        return AsyncPartnersResourceWithRawResponse(self._cms.partners)

    @cached_property
    def team(self) -> AsyncTeamResourceWithRawResponse:
        return AsyncTeamResourceWithRawResponse(self._cms.team)

    @cached_property
    def testimonials(self) -> AsyncTestimonialsResourceWithRawResponse:
        return AsyncTestimonialsResourceWithRawResponse(self._cms.testimonials)


class CmsResourceWithStreamingResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def careers(self) -> CareersResourceWithStreamingResponse:
        return CareersResourceWithStreamingResponse(self._cms.careers)

    @cached_property
    def faqs(self) -> FaqsResourceWithStreamingResponse:
        return FaqsResourceWithStreamingResponse(self._cms.faqs)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._cms.pages)

    @cached_property
    def partners(self) -> PartnersResourceWithStreamingResponse:
        return PartnersResourceWithStreamingResponse(self._cms.partners)

    @cached_property
    def team(self) -> TeamResourceWithStreamingResponse:
        return TeamResourceWithStreamingResponse(self._cms.team)

    @cached_property
    def testimonials(self) -> TestimonialsResourceWithStreamingResponse:
        return TestimonialsResourceWithStreamingResponse(self._cms.testimonials)


class AsyncCmsResourceWithStreamingResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def careers(self) -> AsyncCareersResourceWithStreamingResponse:
        return AsyncCareersResourceWithStreamingResponse(self._cms.careers)

    @cached_property
    def faqs(self) -> AsyncFaqsResourceWithStreamingResponse:
        return AsyncFaqsResourceWithStreamingResponse(self._cms.faqs)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._cms.pages)

    @cached_property
    def partners(self) -> AsyncPartnersResourceWithStreamingResponse:
        return AsyncPartnersResourceWithStreamingResponse(self._cms.partners)

    @cached_property
    def team(self) -> AsyncTeamResourceWithStreamingResponse:
        return AsyncTeamResourceWithStreamingResponse(self._cms.team)

    @cached_property
    def testimonials(self) -> AsyncTestimonialsResourceWithStreamingResponse:
        return AsyncTestimonialsResourceWithStreamingResponse(self._cms.testimonials)
