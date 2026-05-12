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
from .portal import (
    PortalResource,
    AsyncPortalResource,
    PortalResourceWithRawResponse,
    AsyncPortalResourceWithRawResponse,
    PortalResourceWithStreamingResponse,
    AsyncPortalResourceWithStreamingResponse,
)
from .org.org import (
    OrgResource,
    AsyncOrgResource,
    OrgResourceWithRawResponse,
    AsyncOrgResourceWithRawResponse,
    OrgResourceWithStreamingResponse,
    AsyncOrgResourceWithStreamingResponse,
)
from .webhook import (
    WebhookResource,
    AsyncWebhookResource,
    WebhookResourceWithRawResponse,
    AsyncWebhookResourceWithRawResponse,
    WebhookResourceWithStreamingResponse,
    AsyncWebhookResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .redeem_promo import (
    RedeemPromoResource,
    AsyncRedeemPromoResource,
    RedeemPromoResourceWithRawResponse,
    AsyncRedeemPromoResourceWithRawResponse,
    RedeemPromoResourceWithStreamingResponse,
    AsyncRedeemPromoResourceWithStreamingResponse,
)
from .addons.addons import (
    AddonsResource,
    AsyncAddonsResource,
    AddonsResourceWithRawResponse,
    AsyncAddonsResourceWithRawResponse,
    AddonsResourceWithStreamingResponse,
    AsyncAddonsResourceWithStreamingResponse,
)
from .credits.credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from .checkout.checkout import (
    CheckoutResource,
    AsyncCheckoutResource,
    CheckoutResourceWithRawResponse,
    AsyncCheckoutResourceWithRawResponse,
    CheckoutResourceWithStreamingResponse,
    AsyncCheckoutResourceWithStreamingResponse,
)
from .enterprise.enterprise import (
    EnterpriseResource,
    AsyncEnterpriseResource,
    EnterpriseResourceWithRawResponse,
    AsyncEnterpriseResourceWithRawResponse,
    EnterpriseResourceWithStreamingResponse,
    AsyncEnterpriseResourceWithStreamingResponse,
)
from .promo_codes.promo_codes import (
    PromoCodesResource,
    AsyncPromoCodesResource,
    PromoCodesResourceWithRawResponse,
    AsyncPromoCodesResourceWithRawResponse,
    PromoCodesResourceWithStreamingResponse,
    AsyncPromoCodesResourceWithStreamingResponse,
)

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def addons(self) -> AddonsResource:
        return AddonsResource(self._client)

    @cached_property
    def checkout(self) -> CheckoutResource:
        return CheckoutResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def enterprise(self) -> EnterpriseResource:
        return EnterpriseResource(self._client)

    @cached_property
    def org(self) -> OrgResource:
        return OrgResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def portal(self) -> PortalResource:
        return PortalResource(self._client)

    @cached_property
    def promo_codes(self) -> PromoCodesResource:
        return PromoCodesResource(self._client)

    @cached_property
    def redeem_promo(self) -> RedeemPromoResource:
        return RedeemPromoResource(self._client)

    @cached_property
    def webhook(self) -> WebhookResource:
        return WebhookResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def addons(self) -> AsyncAddonsResource:
        return AsyncAddonsResource(self._client)

    @cached_property
    def checkout(self) -> AsyncCheckoutResource:
        return AsyncCheckoutResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResource:
        return AsyncEnterpriseResource(self._client)

    @cached_property
    def org(self) -> AsyncOrgResource:
        return AsyncOrgResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def portal(self) -> AsyncPortalResource:
        return AsyncPortalResource(self._client)

    @cached_property
    def promo_codes(self) -> AsyncPromoCodesResource:
        return AsyncPromoCodesResource(self._client)

    @cached_property
    def redeem_promo(self) -> AsyncRedeemPromoResource:
        return AsyncRedeemPromoResource(self._client)

    @cached_property
    def webhook(self) -> AsyncWebhookResource:
        return AsyncWebhookResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

    @cached_property
    def addons(self) -> AddonsResourceWithRawResponse:
        return AddonsResourceWithRawResponse(self._billing.addons)

    @cached_property
    def checkout(self) -> CheckoutResourceWithRawResponse:
        return CheckoutResourceWithRawResponse(self._billing.checkout)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._billing.credits)

    @cached_property
    def enterprise(self) -> EnterpriseResourceWithRawResponse:
        return EnterpriseResourceWithRawResponse(self._billing.enterprise)

    @cached_property
    def org(self) -> OrgResourceWithRawResponse:
        return OrgResourceWithRawResponse(self._billing.org)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._billing.plans)

    @cached_property
    def portal(self) -> PortalResourceWithRawResponse:
        return PortalResourceWithRawResponse(self._billing.portal)

    @cached_property
    def promo_codes(self) -> PromoCodesResourceWithRawResponse:
        return PromoCodesResourceWithRawResponse(self._billing.promo_codes)

    @cached_property
    def redeem_promo(self) -> RedeemPromoResourceWithRawResponse:
        return RedeemPromoResourceWithRawResponse(self._billing.redeem_promo)

    @cached_property
    def webhook(self) -> WebhookResourceWithRawResponse:
        return WebhookResourceWithRawResponse(self._billing.webhook)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithRawResponse:
        return AsyncAddonsResourceWithRawResponse(self._billing.addons)

    @cached_property
    def checkout(self) -> AsyncCheckoutResourceWithRawResponse:
        return AsyncCheckoutResourceWithRawResponse(self._billing.checkout)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._billing.credits)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResourceWithRawResponse:
        return AsyncEnterpriseResourceWithRawResponse(self._billing.enterprise)

    @cached_property
    def org(self) -> AsyncOrgResourceWithRawResponse:
        return AsyncOrgResourceWithRawResponse(self._billing.org)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._billing.plans)

    @cached_property
    def portal(self) -> AsyncPortalResourceWithRawResponse:
        return AsyncPortalResourceWithRawResponse(self._billing.portal)

    @cached_property
    def promo_codes(self) -> AsyncPromoCodesResourceWithRawResponse:
        return AsyncPromoCodesResourceWithRawResponse(self._billing.promo_codes)

    @cached_property
    def redeem_promo(self) -> AsyncRedeemPromoResourceWithRawResponse:
        return AsyncRedeemPromoResourceWithRawResponse(self._billing.redeem_promo)

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithRawResponse:
        return AsyncWebhookResourceWithRawResponse(self._billing.webhook)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

    @cached_property
    def addons(self) -> AddonsResourceWithStreamingResponse:
        return AddonsResourceWithStreamingResponse(self._billing.addons)

    @cached_property
    def checkout(self) -> CheckoutResourceWithStreamingResponse:
        return CheckoutResourceWithStreamingResponse(self._billing.checkout)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._billing.credits)

    @cached_property
    def enterprise(self) -> EnterpriseResourceWithStreamingResponse:
        return EnterpriseResourceWithStreamingResponse(self._billing.enterprise)

    @cached_property
    def org(self) -> OrgResourceWithStreamingResponse:
        return OrgResourceWithStreamingResponse(self._billing.org)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._billing.plans)

    @cached_property
    def portal(self) -> PortalResourceWithStreamingResponse:
        return PortalResourceWithStreamingResponse(self._billing.portal)

    @cached_property
    def promo_codes(self) -> PromoCodesResourceWithStreamingResponse:
        return PromoCodesResourceWithStreamingResponse(self._billing.promo_codes)

    @cached_property
    def redeem_promo(self) -> RedeemPromoResourceWithStreamingResponse:
        return RedeemPromoResourceWithStreamingResponse(self._billing.redeem_promo)

    @cached_property
    def webhook(self) -> WebhookResourceWithStreamingResponse:
        return WebhookResourceWithStreamingResponse(self._billing.webhook)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithStreamingResponse:
        return AsyncAddonsResourceWithStreamingResponse(self._billing.addons)

    @cached_property
    def checkout(self) -> AsyncCheckoutResourceWithStreamingResponse:
        return AsyncCheckoutResourceWithStreamingResponse(self._billing.checkout)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._billing.credits)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResourceWithStreamingResponse:
        return AsyncEnterpriseResourceWithStreamingResponse(self._billing.enterprise)

    @cached_property
    def org(self) -> AsyncOrgResourceWithStreamingResponse:
        return AsyncOrgResourceWithStreamingResponse(self._billing.org)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._billing.plans)

    @cached_property
    def portal(self) -> AsyncPortalResourceWithStreamingResponse:
        return AsyncPortalResourceWithStreamingResponse(self._billing.portal)

    @cached_property
    def promo_codes(self) -> AsyncPromoCodesResourceWithStreamingResponse:
        return AsyncPromoCodesResourceWithStreamingResponse(self._billing.promo_codes)

    @cached_property
    def redeem_promo(self) -> AsyncRedeemPromoResourceWithStreamingResponse:
        return AsyncRedeemPromoResourceWithStreamingResponse(self._billing.redeem_promo)

    @cached_property
    def webhook(self) -> AsyncWebhookResourceWithStreamingResponse:
        return AsyncWebhookResourceWithStreamingResponse(self._billing.webhook)
