# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pause import (
    PauseResource,
    AsyncPauseResource,
    PauseResourceWithRawResponse,
    AsyncPauseResourceWithRawResponse,
    PauseResourceWithStreamingResponse,
    AsyncPauseResourceWithStreamingResponse,
)
from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .addons import (
    AddonsResource,
    AsyncAddonsResource,
    AddonsResourceWithRawResponse,
    AsyncAddonsResourceWithRawResponse,
    AddonsResourceWithStreamingResponse,
    AsyncAddonsResourceWithStreamingResponse,
)
from .cancel import (
    CancelResource,
    AsyncCancelResource,
    CancelResourceWithRawResponse,
    AsyncCancelResourceWithRawResponse,
    CancelResourceWithStreamingResponse,
    AsyncCancelResourceWithStreamingResponse,
)
from .portal import (
    PortalResource,
    AsyncPortalResource,
    PortalResourceWithRawResponse,
    AsyncPortalResourceWithRawResponse,
    PortalResourceWithStreamingResponse,
    AsyncPortalResourceWithStreamingResponse,
)
from .resume import (
    ResumeResource,
    AsyncResumeResource,
    ResumeResourceWithRawResponse,
    AsyncResumeResourceWithRawResponse,
    ResumeResourceWithStreamingResponse,
    AsyncResumeResourceWithStreamingResponse,
)
from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from .overages import (
    OveragesResource,
    AsyncOveragesResource,
    OveragesResourceWithRawResponse,
    AsyncOveragesResourceWithRawResponse,
    OveragesResourceWithStreamingResponse,
    AsyncOveragesResourceWithStreamingResponse,
)
from .tax_info import (
    TaxInfoResource,
    AsyncTaxInfoResource,
    TaxInfoResourceWithRawResponse,
    AsyncTaxInfoResourceWithRawResponse,
    TaxInfoResourceWithStreamingResponse,
    AsyncTaxInfoResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .reactivate import (
    ReactivateResource,
    AsyncReactivateResource,
    ReactivateResourceWithRawResponse,
    AsyncReactivateResourceWithRawResponse,
    ReactivateResourceWithStreamingResponse,
    AsyncReactivateResourceWithStreamingResponse,
)
from .change_plan import (
    ChangePlanResource,
    AsyncChangePlanResource,
    ChangePlanResourceWithRawResponse,
    AsyncChangePlanResourceWithRawResponse,
    ChangePlanResourceWithStreamingResponse,
    AsyncChangePlanResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .usage_alerts import (
    UsageAlertsResource,
    AsyncUsageAlertsResource,
    UsageAlertsResourceWithRawResponse,
    AsyncUsageAlertsResourceWithRawResponse,
    UsageAlertsResourceWithStreamingResponse,
    AsyncUsageAlertsResourceWithStreamingResponse,
)
from .cost_breakdown import (
    CostBreakdownResource,
    AsyncCostBreakdownResource,
    CostBreakdownResourceWithRawResponse,
    AsyncCostBreakdownResourceWithRawResponse,
    CostBreakdownResourceWithStreamingResponse,
    AsyncCostBreakdownResourceWithStreamingResponse,
)
from .invoices.invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def addons(self) -> AddonsResource:
        return AddonsResource(self._client)

    @cached_property
    def cancel(self) -> CancelResource:
        return CancelResource(self._client)

    @cached_property
    def change_plan(self) -> ChangePlanResource:
        return ChangePlanResource(self._client)

    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def cost_breakdown(self) -> CostBreakdownResource:
        return CostBreakdownResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def overages(self) -> OveragesResource:
        return OveragesResource(self._client)

    @cached_property
    def pause(self) -> PauseResource:
        return PauseResource(self._client)

    @cached_property
    def portal(self) -> PortalResource:
        return PortalResource(self._client)

    @cached_property
    def reactivate(self) -> ReactivateResource:
        return ReactivateResource(self._client)

    @cached_property
    def resume(self) -> ResumeResource:
        return ResumeResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def tax_info(self) -> TaxInfoResource:
        return TaxInfoResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def usage_alerts(self) -> UsageAlertsResource:
        return UsageAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def addons(self) -> AsyncAddonsResource:
        return AsyncAddonsResource(self._client)

    @cached_property
    def cancel(self) -> AsyncCancelResource:
        return AsyncCancelResource(self._client)

    @cached_property
    def change_plan(self) -> AsyncChangePlanResource:
        return AsyncChangePlanResource(self._client)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def cost_breakdown(self) -> AsyncCostBreakdownResource:
        return AsyncCostBreakdownResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def overages(self) -> AsyncOveragesResource:
        return AsyncOveragesResource(self._client)

    @cached_property
    def pause(self) -> AsyncPauseResource:
        return AsyncPauseResource(self._client)

    @cached_property
    def portal(self) -> AsyncPortalResource:
        return AsyncPortalResource(self._client)

    @cached_property
    def reactivate(self) -> AsyncReactivateResource:
        return AsyncReactivateResource(self._client)

    @cached_property
    def resume(self) -> AsyncResumeResource:
        return AsyncResumeResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def tax_info(self) -> AsyncTaxInfoResource:
        return AsyncTaxInfoResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def usage_alerts(self) -> AsyncUsageAlertsResource:
        return AsyncUsageAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def addons(self) -> AddonsResourceWithRawResponse:
        return AddonsResourceWithRawResponse(self._org.addons)

    @cached_property
    def cancel(self) -> CancelResourceWithRawResponse:
        return CancelResourceWithRawResponse(self._org.cancel)

    @cached_property
    def change_plan(self) -> ChangePlanResourceWithRawResponse:
        return ChangePlanResourceWithRawResponse(self._org.change_plan)

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._org.contacts)

    @cached_property
    def cost_breakdown(self) -> CostBreakdownResourceWithRawResponse:
        return CostBreakdownResourceWithRawResponse(self._org.cost_breakdown)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._org.credits)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._org.invoices)

    @cached_property
    def overages(self) -> OveragesResourceWithRawResponse:
        return OveragesResourceWithRawResponse(self._org.overages)

    @cached_property
    def pause(self) -> PauseResourceWithRawResponse:
        return PauseResourceWithRawResponse(self._org.pause)

    @cached_property
    def portal(self) -> PortalResourceWithRawResponse:
        return PortalResourceWithRawResponse(self._org.portal)

    @cached_property
    def reactivate(self) -> ReactivateResourceWithRawResponse:
        return ReactivateResourceWithRawResponse(self._org.reactivate)

    @cached_property
    def resume(self) -> ResumeResourceWithRawResponse:
        return ResumeResourceWithRawResponse(self._org.resume)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._org.summary)

    @cached_property
    def tax_info(self) -> TaxInfoResourceWithRawResponse:
        return TaxInfoResourceWithRawResponse(self._org.tax_info)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._org.usage)

    @cached_property
    def usage_alerts(self) -> UsageAlertsResourceWithRawResponse:
        return UsageAlertsResourceWithRawResponse(self._org.usage_alerts)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithRawResponse:
        return AsyncAddonsResourceWithRawResponse(self._org.addons)

    @cached_property
    def cancel(self) -> AsyncCancelResourceWithRawResponse:
        return AsyncCancelResourceWithRawResponse(self._org.cancel)

    @cached_property
    def change_plan(self) -> AsyncChangePlanResourceWithRawResponse:
        return AsyncChangePlanResourceWithRawResponse(self._org.change_plan)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._org.contacts)

    @cached_property
    def cost_breakdown(self) -> AsyncCostBreakdownResourceWithRawResponse:
        return AsyncCostBreakdownResourceWithRawResponse(self._org.cost_breakdown)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._org.credits)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._org.invoices)

    @cached_property
    def overages(self) -> AsyncOveragesResourceWithRawResponse:
        return AsyncOveragesResourceWithRawResponse(self._org.overages)

    @cached_property
    def pause(self) -> AsyncPauseResourceWithRawResponse:
        return AsyncPauseResourceWithRawResponse(self._org.pause)

    @cached_property
    def portal(self) -> AsyncPortalResourceWithRawResponse:
        return AsyncPortalResourceWithRawResponse(self._org.portal)

    @cached_property
    def reactivate(self) -> AsyncReactivateResourceWithRawResponse:
        return AsyncReactivateResourceWithRawResponse(self._org.reactivate)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithRawResponse:
        return AsyncResumeResourceWithRawResponse(self._org.resume)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._org.summary)

    @cached_property
    def tax_info(self) -> AsyncTaxInfoResourceWithRawResponse:
        return AsyncTaxInfoResourceWithRawResponse(self._org.tax_info)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._org.usage)

    @cached_property
    def usage_alerts(self) -> AsyncUsageAlertsResourceWithRawResponse:
        return AsyncUsageAlertsResourceWithRawResponse(self._org.usage_alerts)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

    @cached_property
    def addons(self) -> AddonsResourceWithStreamingResponse:
        return AddonsResourceWithStreamingResponse(self._org.addons)

    @cached_property
    def cancel(self) -> CancelResourceWithStreamingResponse:
        return CancelResourceWithStreamingResponse(self._org.cancel)

    @cached_property
    def change_plan(self) -> ChangePlanResourceWithStreamingResponse:
        return ChangePlanResourceWithStreamingResponse(self._org.change_plan)

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._org.contacts)

    @cached_property
    def cost_breakdown(self) -> CostBreakdownResourceWithStreamingResponse:
        return CostBreakdownResourceWithStreamingResponse(self._org.cost_breakdown)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._org.credits)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._org.invoices)

    @cached_property
    def overages(self) -> OveragesResourceWithStreamingResponse:
        return OveragesResourceWithStreamingResponse(self._org.overages)

    @cached_property
    def pause(self) -> PauseResourceWithStreamingResponse:
        return PauseResourceWithStreamingResponse(self._org.pause)

    @cached_property
    def portal(self) -> PortalResourceWithStreamingResponse:
        return PortalResourceWithStreamingResponse(self._org.portal)

    @cached_property
    def reactivate(self) -> ReactivateResourceWithStreamingResponse:
        return ReactivateResourceWithStreamingResponse(self._org.reactivate)

    @cached_property
    def resume(self) -> ResumeResourceWithStreamingResponse:
        return ResumeResourceWithStreamingResponse(self._org.resume)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._org.summary)

    @cached_property
    def tax_info(self) -> TaxInfoResourceWithStreamingResponse:
        return TaxInfoResourceWithStreamingResponse(self._org.tax_info)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._org.usage)

    @cached_property
    def usage_alerts(self) -> UsageAlertsResourceWithStreamingResponse:
        return UsageAlertsResourceWithStreamingResponse(self._org.usage_alerts)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithStreamingResponse:
        return AsyncAddonsResourceWithStreamingResponse(self._org.addons)

    @cached_property
    def cancel(self) -> AsyncCancelResourceWithStreamingResponse:
        return AsyncCancelResourceWithStreamingResponse(self._org.cancel)

    @cached_property
    def change_plan(self) -> AsyncChangePlanResourceWithStreamingResponse:
        return AsyncChangePlanResourceWithStreamingResponse(self._org.change_plan)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._org.contacts)

    @cached_property
    def cost_breakdown(self) -> AsyncCostBreakdownResourceWithStreamingResponse:
        return AsyncCostBreakdownResourceWithStreamingResponse(self._org.cost_breakdown)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._org.credits)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._org.invoices)

    @cached_property
    def overages(self) -> AsyncOveragesResourceWithStreamingResponse:
        return AsyncOveragesResourceWithStreamingResponse(self._org.overages)

    @cached_property
    def pause(self) -> AsyncPauseResourceWithStreamingResponse:
        return AsyncPauseResourceWithStreamingResponse(self._org.pause)

    @cached_property
    def portal(self) -> AsyncPortalResourceWithStreamingResponse:
        return AsyncPortalResourceWithStreamingResponse(self._org.portal)

    @cached_property
    def reactivate(self) -> AsyncReactivateResourceWithStreamingResponse:
        return AsyncReactivateResourceWithStreamingResponse(self._org.reactivate)

    @cached_property
    def resume(self) -> AsyncResumeResourceWithStreamingResponse:
        return AsyncResumeResourceWithStreamingResponse(self._org.resume)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._org.summary)

    @cached_property
    def tax_info(self) -> AsyncTaxInfoResourceWithStreamingResponse:
        return AsyncTaxInfoResourceWithStreamingResponse(self._org.tax_info)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._org.usage)

    @cached_property
    def usage_alerts(self) -> AsyncUsageAlertsResourceWithStreamingResponse:
        return AsyncUsageAlertsResourceWithStreamingResponse(self._org.usage_alerts)
