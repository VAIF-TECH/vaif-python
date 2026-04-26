# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .validate import (
    ValidateResource,
    AsyncValidateResource,
    ValidateResourceWithRawResponse,
    AsyncValidateResourceWithRawResponse,
    ValidateResourceWithStreamingResponse,
    AsyncValidateResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PromoCodesResource", "AsyncPromoCodesResource"]


class PromoCodesResource(SyncAPIResource):
    @cached_property
    def validate(self) -> ValidateResource:
        return ValidateResource(self._client)

    @cached_property
    def with_raw_response(self) -> PromoCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return PromoCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromoCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return PromoCodesResourceWithStreamingResponse(self)


class AsyncPromoCodesResource(AsyncAPIResource):
    @cached_property
    def validate(self) -> AsyncValidateResource:
        return AsyncValidateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPromoCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromoCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromoCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncPromoCodesResourceWithStreamingResponse(self)


class PromoCodesResourceWithRawResponse:
    def __init__(self, promo_codes: PromoCodesResource) -> None:
        self._promo_codes = promo_codes

    @cached_property
    def validate(self) -> ValidateResourceWithRawResponse:
        return ValidateResourceWithRawResponse(self._promo_codes.validate)


class AsyncPromoCodesResourceWithRawResponse:
    def __init__(self, promo_codes: AsyncPromoCodesResource) -> None:
        self._promo_codes = promo_codes

    @cached_property
    def validate(self) -> AsyncValidateResourceWithRawResponse:
        return AsyncValidateResourceWithRawResponse(self._promo_codes.validate)


class PromoCodesResourceWithStreamingResponse:
    def __init__(self, promo_codes: PromoCodesResource) -> None:
        self._promo_codes = promo_codes

    @cached_property
    def validate(self) -> ValidateResourceWithStreamingResponse:
        return ValidateResourceWithStreamingResponse(self._promo_codes.validate)


class AsyncPromoCodesResourceWithStreamingResponse:
    def __init__(self, promo_codes: AsyncPromoCodesResource) -> None:
        self._promo_codes = promo_codes

    @cached_property
    def validate(self) -> AsyncValidateResourceWithStreamingResponse:
        return AsyncValidateResourceWithStreamingResponse(self._promo_codes.validate)
