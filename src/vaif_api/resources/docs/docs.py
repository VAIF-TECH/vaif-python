# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v2.v2 import (
    V2Resource,
    AsyncV2Resource,
    V2ResourceWithRawResponse,
    AsyncV2ResourceWithRawResponse,
    V2ResourceWithStreamingResponse,
    AsyncV2ResourceWithStreamingResponse,
)
from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from .examples import (
    ExamplesResource,
    AsyncExamplesResource,
    ExamplesResourceWithRawResponse,
    AsyncExamplesResourceWithRawResponse,
    ExamplesResourceWithStreamingResponse,
    AsyncExamplesResourceWithStreamingResponse,
)
from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .ai_answer import (
    AIAnswerResource,
    AsyncAIAnswerResource,
    AIAnswerResourceWithRawResponse,
    AsyncAIAnswerResourceWithRawResponse,
    AIAnswerResourceWithStreamingResponse,
    AsyncAIAnswerResourceWithStreamingResponse,
)
from .ai_search import (
    AISearchResource,
    AsyncAISearchResource,
    AISearchResourceWithRawResponse,
    AsyncAISearchResourceWithRawResponse,
    AISearchResourceWithStreamingResponse,
    AsyncAISearchResourceWithStreamingResponse,
)
from .changelog import (
    ChangelogResource,
    AsyncChangelogResource,
    ChangelogResourceWithRawResponse,
    AsyncChangelogResourceWithRawResponse,
    ChangelogResourceWithStreamingResponse,
    AsyncChangelogResourceWithStreamingResponse,
)
from .sdks.sdks import (
    SDKsResource,
    AsyncSDKsResource,
    SDKsResourceWithRawResponse,
    AsyncSDKsResourceWithRawResponse,
    SDKsResourceWithStreamingResponse,
    AsyncSDKsResourceWithStreamingResponse,
)
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .search_click import (
    SearchClickResource,
    AsyncSearchClickResource,
    SearchClickResourceWithRawResponse,
    AsyncSearchClickResourceWithRawResponse,
    SearchClickResourceWithStreamingResponse,
    AsyncSearchClickResourceWithStreamingResponse,
)
from .api_endpoints import (
    APIEndpointsResource,
    AsyncAPIEndpointsResource,
    APIEndpointsResourceWithRawResponse,
    AsyncAPIEndpointsResourceWithRawResponse,
    APIEndpointsResourceWithStreamingResponse,
    AsyncAPIEndpointsResourceWithStreamingResponse,
)
from .project.project import (
    ProjectResource,
    AsyncProjectResource,
    ProjectResourceWithRawResponse,
    AsyncProjectResourceWithRawResponse,
    ProjectResourceWithStreamingResponse,
    AsyncProjectResourceWithStreamingResponse,
)

__all__ = ["DocsResource", "AsyncDocsResource"]


class DocsResource(SyncAPIResource):
    @cached_property
    def ai_answer(self) -> AIAnswerResource:
        return AIAnswerResource(self._client)

    @cached_property
    def ai_search(self) -> AISearchResource:
        return AISearchResource(self._client)

    @cached_property
    def api_endpoints(self) -> APIEndpointsResource:
        return APIEndpointsResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def changelog(self) -> ChangelogResource:
        return ChangelogResource(self._client)

    @cached_property
    def examples(self) -> ExamplesResource:
        return ExamplesResource(self._client)

    @cached_property
    def feedback(self) -> FeedbackResource:
        return FeedbackResource(self._client)

    @cached_property
    def project(self) -> ProjectResource:
        return ProjectResource(self._client)

    @cached_property
    def sdks(self) -> SDKsResource:
        return SDKsResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)

    @cached_property
    def search_click(self) -> SearchClickResource:
        return SearchClickResource(self._client)

    @cached_property
    def v2(self) -> V2Resource:
        return V2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> DocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return DocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return DocsResourceWithStreamingResponse(self)


class AsyncDocsResource(AsyncAPIResource):
    @cached_property
    def ai_answer(self) -> AsyncAIAnswerResource:
        return AsyncAIAnswerResource(self._client)

    @cached_property
    def ai_search(self) -> AsyncAISearchResource:
        return AsyncAISearchResource(self._client)

    @cached_property
    def api_endpoints(self) -> AsyncAPIEndpointsResource:
        return AsyncAPIEndpointsResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def changelog(self) -> AsyncChangelogResource:
        return AsyncChangelogResource(self._client)

    @cached_property
    def examples(self) -> AsyncExamplesResource:
        return AsyncExamplesResource(self._client)

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        return AsyncFeedbackResource(self._client)

    @cached_property
    def project(self) -> AsyncProjectResource:
        return AsyncProjectResource(self._client)

    @cached_property
    def sdks(self) -> AsyncSDKsResource:
        return AsyncSDKsResource(self._client)

    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._client)

    @cached_property
    def search_click(self) -> AsyncSearchClickResource:
        return AsyncSearchClickResource(self._client)

    @cached_property
    def v2(self) -> AsyncV2Resource:
        return AsyncV2Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncDocsResourceWithStreamingResponse(self)


class DocsResourceWithRawResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

    @cached_property
    def ai_answer(self) -> AIAnswerResourceWithRawResponse:
        return AIAnswerResourceWithRawResponse(self._docs.ai_answer)

    @cached_property
    def ai_search(self) -> AISearchResourceWithRawResponse:
        return AISearchResourceWithRawResponse(self._docs.ai_search)

    @cached_property
    def api_endpoints(self) -> APIEndpointsResourceWithRawResponse:
        return APIEndpointsResourceWithRawResponse(self._docs.api_endpoints)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._docs.categories)

    @cached_property
    def changelog(self) -> ChangelogResourceWithRawResponse:
        return ChangelogResourceWithRawResponse(self._docs.changelog)

    @cached_property
    def examples(self) -> ExamplesResourceWithRawResponse:
        return ExamplesResourceWithRawResponse(self._docs.examples)

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self._docs.feedback)

    @cached_property
    def project(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self._docs.project)

    @cached_property
    def sdks(self) -> SDKsResourceWithRawResponse:
        return SDKsResourceWithRawResponse(self._docs.sdks)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._docs.search)

    @cached_property
    def search_click(self) -> SearchClickResourceWithRawResponse:
        return SearchClickResourceWithRawResponse(self._docs.search_click)

    @cached_property
    def v2(self) -> V2ResourceWithRawResponse:
        return V2ResourceWithRawResponse(self._docs.v2)


class AsyncDocsResourceWithRawResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

    @cached_property
    def ai_answer(self) -> AsyncAIAnswerResourceWithRawResponse:
        return AsyncAIAnswerResourceWithRawResponse(self._docs.ai_answer)

    @cached_property
    def ai_search(self) -> AsyncAISearchResourceWithRawResponse:
        return AsyncAISearchResourceWithRawResponse(self._docs.ai_search)

    @cached_property
    def api_endpoints(self) -> AsyncAPIEndpointsResourceWithRawResponse:
        return AsyncAPIEndpointsResourceWithRawResponse(self._docs.api_endpoints)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._docs.categories)

    @cached_property
    def changelog(self) -> AsyncChangelogResourceWithRawResponse:
        return AsyncChangelogResourceWithRawResponse(self._docs.changelog)

    @cached_property
    def examples(self) -> AsyncExamplesResourceWithRawResponse:
        return AsyncExamplesResourceWithRawResponse(self._docs.examples)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self._docs.feedback)

    @cached_property
    def project(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self._docs.project)

    @cached_property
    def sdks(self) -> AsyncSDKsResourceWithRawResponse:
        return AsyncSDKsResourceWithRawResponse(self._docs.sdks)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._docs.search)

    @cached_property
    def search_click(self) -> AsyncSearchClickResourceWithRawResponse:
        return AsyncSearchClickResourceWithRawResponse(self._docs.search_click)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithRawResponse:
        return AsyncV2ResourceWithRawResponse(self._docs.v2)


class DocsResourceWithStreamingResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

    @cached_property
    def ai_answer(self) -> AIAnswerResourceWithStreamingResponse:
        return AIAnswerResourceWithStreamingResponse(self._docs.ai_answer)

    @cached_property
    def ai_search(self) -> AISearchResourceWithStreamingResponse:
        return AISearchResourceWithStreamingResponse(self._docs.ai_search)

    @cached_property
    def api_endpoints(self) -> APIEndpointsResourceWithStreamingResponse:
        return APIEndpointsResourceWithStreamingResponse(self._docs.api_endpoints)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._docs.categories)

    @cached_property
    def changelog(self) -> ChangelogResourceWithStreamingResponse:
        return ChangelogResourceWithStreamingResponse(self._docs.changelog)

    @cached_property
    def examples(self) -> ExamplesResourceWithStreamingResponse:
        return ExamplesResourceWithStreamingResponse(self._docs.examples)

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self._docs.feedback)

    @cached_property
    def project(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self._docs.project)

    @cached_property
    def sdks(self) -> SDKsResourceWithStreamingResponse:
        return SDKsResourceWithStreamingResponse(self._docs.sdks)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._docs.search)

    @cached_property
    def search_click(self) -> SearchClickResourceWithStreamingResponse:
        return SearchClickResourceWithStreamingResponse(self._docs.search_click)

    @cached_property
    def v2(self) -> V2ResourceWithStreamingResponse:
        return V2ResourceWithStreamingResponse(self._docs.v2)


class AsyncDocsResourceWithStreamingResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

    @cached_property
    def ai_answer(self) -> AsyncAIAnswerResourceWithStreamingResponse:
        return AsyncAIAnswerResourceWithStreamingResponse(self._docs.ai_answer)

    @cached_property
    def ai_search(self) -> AsyncAISearchResourceWithStreamingResponse:
        return AsyncAISearchResourceWithStreamingResponse(self._docs.ai_search)

    @cached_property
    def api_endpoints(self) -> AsyncAPIEndpointsResourceWithStreamingResponse:
        return AsyncAPIEndpointsResourceWithStreamingResponse(self._docs.api_endpoints)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._docs.categories)

    @cached_property
    def changelog(self) -> AsyncChangelogResourceWithStreamingResponse:
        return AsyncChangelogResourceWithStreamingResponse(self._docs.changelog)

    @cached_property
    def examples(self) -> AsyncExamplesResourceWithStreamingResponse:
        return AsyncExamplesResourceWithStreamingResponse(self._docs.examples)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self._docs.feedback)

    @cached_property
    def project(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self._docs.project)

    @cached_property
    def sdks(self) -> AsyncSDKsResourceWithStreamingResponse:
        return AsyncSDKsResourceWithStreamingResponse(self._docs.sdks)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._docs.search)

    @cached_property
    def search_click(self) -> AsyncSearchClickResourceWithStreamingResponse:
        return AsyncSearchClickResourceWithStreamingResponse(self._docs.search_click)

    @cached_property
    def v2(self) -> AsyncV2ResourceWithStreamingResponse:
        return AsyncV2ResourceWithStreamingResponse(self._docs.v2)
