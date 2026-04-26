# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from .compare import (
    CompareResource,
    AsyncCompareResource,
    CompareResourceWithRawResponse,
    AsyncCompareResourceWithRawResponse,
    CompareResourceWithStreamingResponse,
    AsyncCompareResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .enterprise import (
    EnterpriseResource,
    AsyncEnterpriseResource,
    EnterpriseResourceWithRawResponse,
    AsyncEnterpriseResourceWithRawResponse,
    EnterpriseResourceWithStreamingResponse,
    AsyncEnterpriseResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .ai_features import (
    AIFeaturesResource,
    AsyncAIFeaturesResource,
    AIFeaturesResourceWithRawResponse,
    AsyncAIFeaturesResourceWithRawResponse,
    AIFeaturesResourceWithStreamingResponse,
    AsyncAIFeaturesResourceWithStreamingResponse,
)

__all__ = ["PricingResource", "AsyncPricingResource"]


class PricingResource(SyncAPIResource):
    @cached_property
    def ai_features(self) -> AIFeaturesResource:
        return AIFeaturesResource(self._client)

    @cached_property
    def compare(self) -> CompareResource:
        return CompareResource(self._client)

    @cached_property
    def enterprise(self) -> EnterpriseResource:
        return EnterpriseResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> PricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return PricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return PricingResourceWithStreamingResponse(self)


class AsyncPricingResource(AsyncAPIResource):
    @cached_property
    def ai_features(self) -> AsyncAIFeaturesResource:
        return AsyncAIFeaturesResource(self._client)

    @cached_property
    def compare(self) -> AsyncCompareResource:
        return AsyncCompareResource(self._client)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResource:
        return AsyncEnterpriseResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncPricingResourceWithStreamingResponse(self)


class PricingResourceWithRawResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def ai_features(self) -> AIFeaturesResourceWithRawResponse:
        return AIFeaturesResourceWithRawResponse(self._pricing.ai_features)

    @cached_property
    def compare(self) -> CompareResourceWithRawResponse:
        return CompareResourceWithRawResponse(self._pricing.compare)

    @cached_property
    def enterprise(self) -> EnterpriseResourceWithRawResponse:
        return EnterpriseResourceWithRawResponse(self._pricing.enterprise)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._pricing.plans)


class AsyncPricingResourceWithRawResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def ai_features(self) -> AsyncAIFeaturesResourceWithRawResponse:
        return AsyncAIFeaturesResourceWithRawResponse(self._pricing.ai_features)

    @cached_property
    def compare(self) -> AsyncCompareResourceWithRawResponse:
        return AsyncCompareResourceWithRawResponse(self._pricing.compare)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResourceWithRawResponse:
        return AsyncEnterpriseResourceWithRawResponse(self._pricing.enterprise)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._pricing.plans)


class PricingResourceWithStreamingResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def ai_features(self) -> AIFeaturesResourceWithStreamingResponse:
        return AIFeaturesResourceWithStreamingResponse(self._pricing.ai_features)

    @cached_property
    def compare(self) -> CompareResourceWithStreamingResponse:
        return CompareResourceWithStreamingResponse(self._pricing.compare)

    @cached_property
    def enterprise(self) -> EnterpriseResourceWithStreamingResponse:
        return EnterpriseResourceWithStreamingResponse(self._pricing.enterprise)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._pricing.plans)


class AsyncPricingResourceWithStreamingResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def ai_features(self) -> AsyncAIFeaturesResourceWithStreamingResponse:
        return AsyncAIFeaturesResourceWithStreamingResponse(self._pricing.ai_features)

    @cached_property
    def compare(self) -> AsyncCompareResourceWithStreamingResponse:
        return AsyncCompareResourceWithStreamingResponse(self._pricing.compare)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResourceWithStreamingResponse:
        return AsyncEnterpriseResourceWithStreamingResponse(self._pricing.enterprise)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._pricing.plans)
