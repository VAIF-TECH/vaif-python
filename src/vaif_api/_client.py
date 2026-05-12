# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        ai,
        v1,
        cms,
        rls,
        sdk,
        sso,
        auth,
        docs,
        jobs,
        logs,
        orgs,
        audit,
        oauth,
        plans,
        users,
        github,
        status,
        billing,
        buckets,
        contact,
        credits,
        metrics,
        mongodb,
        openapi,
        pricing,
        refunds,
        regions,
        schemas,
        storage,
        ai_usage,
        database,
        projects,
        realtime,
        security,
        bootstrap,
        functions,
        generated,
        incidents,
        templates,
        activation,
        enterprise,
        onboarding,
        quickstart,
        alert_rules,
        deployments,
        maintenance,
        entitlements,
        integrations,
        announcements,
        schema_engine,
        infrastructure,
    )
    from .resources.ai.ai import AIResource, AsyncAIResource
    from .resources.v1.v1 import V1Resource, AsyncV1Resource
    from .resources.cms.cms import CmsResource, AsyncCmsResource
    from .resources.contact import ContactResource, AsyncContactResource
    from .resources.rls.rls import RlsResource, AsyncRlsResource
    from .resources.sdk.sdk import SDKResource, AsyncSDKResource
    from .resources.sso.sso import SSOResource, AsyncSSOResource
    from .resources.auth.auth import AuthResource, AsyncAuthResource
    from .resources.bootstrap import BootstrapResource, AsyncBootstrapResource
    from .resources.docs.docs import DocsResource, AsyncDocsResource
    from .resources.jobs.jobs import JobsResource, AsyncJobsResource
    from .resources.logs.logs import LogsResource, AsyncLogsResource
    from .resources.orgs.orgs import OrgsResource, AsyncOrgsResource
    from .resources.audit.audit import AuditResource, AsyncAuditResource
    from .resources.maintenance import MaintenanceResource, AsyncMaintenanceResource
    from .resources.oauth.oauth import OAuthResource, AsyncOAuthResource
    from .resources.plans.plans import PlansResource, AsyncPlansResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.announcements import AnnouncementsResource, AsyncAnnouncementsResource
    from .resources.github.github import GitHubResource, AsyncGitHubResource
    from .resources.status.status import StatusResource, AsyncStatusResource
    from .resources.billing.billing import BillingResource, AsyncBillingResource
    from .resources.buckets.buckets import BucketsResource, AsyncBucketsResource
    from .resources.credits.credits import CreditsResource, AsyncCreditsResource
    from .resources.metrics.metrics import MetricsResource, AsyncMetricsResource
    from .resources.mongodb.mongodb import MongoDBResource, AsyncMongoDBResource
    from .resources.openapi.openapi import OpenAPIResource, AsyncOpenAPIResource
    from .resources.pricing.pricing import PricingResource, AsyncPricingResource
    from .resources.refunds.refunds import RefundsResource, AsyncRefundsResource
    from .resources.regions.regions import RegionsResource, AsyncRegionsResource
    from .resources.schemas.schemas import SchemasResource, AsyncSchemasResource
    from .resources.storage.storage import StorageResource, AsyncStorageResource
    from .resources.ai_usage.ai_usage import AIUsageResource, AsyncAIUsageResource
    from .resources.database.database import DatabaseResource, AsyncDatabaseResource
    from .resources.projects.projects import ProjectsResource, AsyncProjectsResource
    from .resources.realtime.realtime import RealtimeResource, AsyncRealtimeResource
    from .resources.security.security import SecurityResource, AsyncSecurityResource
    from .resources.functions.functions import FunctionsResource, AsyncFunctionsResource
    from .resources.generated.generated import GeneratedResource, AsyncGeneratedResource
    from .resources.incidents.incidents import IncidentsResource, AsyncIncidentsResource
    from .resources.templates.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.activation.activation import ActivationResource, AsyncActivationResource
    from .resources.enterprise.enterprise import EnterpriseResource, AsyncEnterpriseResource
    from .resources.onboarding.onboarding import OnboardingResource, AsyncOnboardingResource
    from .resources.quickstart.quickstart import QuickstartResource, AsyncQuickstartResource
    from .resources.alert_rules.alert_rules import AlertRulesResource, AsyncAlertRulesResource
    from .resources.deployments.deployments import DeploymentsResource, AsyncDeploymentsResource
    from .resources.entitlements.entitlements import EntitlementsResource, AsyncEntitlementsResource
    from .resources.integrations.integrations import IntegrationsResource, AsyncIntegrationsResource
    from .resources.schema_engine.schema_engine import SchemaEngineResource, AsyncSchemaEngineResource
    from .resources.infrastructure.infrastructure import InfrastructureResource, AsyncInfrastructureResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Vaif", "AsyncVaif", "Client", "AsyncClient"]


class Vaif(SyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Vaif client instance."""
        self.api_key = api_key

        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("VAIF_BASE_URL")
        if base_url is None:
            base_url = f"https://api.vaif.studio"

        custom_headers_env = os.environ.get("VAIF_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def activation(self) -> ActivationResource:
        from .resources.activation import ActivationResource

        return ActivationResource(self)

    @cached_property
    def ai(self) -> AIResource:
        from .resources.ai import AIResource

        return AIResource(self)

    @cached_property
    def ai_usage(self) -> AIUsageResource:
        from .resources.ai_usage import AIUsageResource

        return AIUsageResource(self)

    @cached_property
    def alert_rules(self) -> AlertRulesResource:
        from .resources.alert_rules import AlertRulesResource

        return AlertRulesResource(self)

    @cached_property
    def announcements(self) -> AnnouncementsResource:
        from .resources.announcements import AnnouncementsResource

        return AnnouncementsResource(self)

    @cached_property
    def audit(self) -> AuditResource:
        from .resources.audit import AuditResource

        return AuditResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def billing(self) -> BillingResource:
        from .resources.billing import BillingResource

        return BillingResource(self)

    @cached_property
    def bootstrap(self) -> BootstrapResource:
        from .resources.bootstrap import BootstrapResource

        return BootstrapResource(self)

    @cached_property
    def buckets(self) -> BucketsResource:
        from .resources.buckets import BucketsResource

        return BucketsResource(self)

    @cached_property
    def cms(self) -> CmsResource:
        from .resources.cms import CmsResource

        return CmsResource(self)

    @cached_property
    def contact(self) -> ContactResource:
        from .resources.contact import ContactResource

        return ContactResource(self)

    @cached_property
    def credits(self) -> CreditsResource:
        from .resources.credits import CreditsResource

        return CreditsResource(self)

    @cached_property
    def database(self) -> DatabaseResource:
        from .resources.database import DatabaseResource

        return DatabaseResource(self)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        from .resources.deployments import DeploymentsResource

        return DeploymentsResource(self)

    @cached_property
    def docs(self) -> DocsResource:
        from .resources.docs import DocsResource

        return DocsResource(self)

    @cached_property
    def enterprise(self) -> EnterpriseResource:
        from .resources.enterprise import EnterpriseResource

        return EnterpriseResource(self)

    @cached_property
    def entitlements(self) -> EntitlementsResource:
        from .resources.entitlements import EntitlementsResource

        return EntitlementsResource(self)

    @cached_property
    def functions(self) -> FunctionsResource:
        from .resources.functions import FunctionsResource

        return FunctionsResource(self)

    @cached_property
    def generated(self) -> GeneratedResource:
        from .resources.generated import GeneratedResource

        return GeneratedResource(self)

    @cached_property
    def github(self) -> GitHubResource:
        from .resources.github import GitHubResource

        return GitHubResource(self)

    @cached_property
    def incidents(self) -> IncidentsResource:
        from .resources.incidents import IncidentsResource

        return IncidentsResource(self)

    @cached_property
    def infrastructure(self) -> InfrastructureResource:
        from .resources.infrastructure import InfrastructureResource

        return InfrastructureResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def jobs(self) -> JobsResource:
        from .resources.jobs import JobsResource

        return JobsResource(self)

    @cached_property
    def logs(self) -> LogsResource:
        from .resources.logs import LogsResource

        return LogsResource(self)

    @cached_property
    def maintenance(self) -> MaintenanceResource:
        from .resources.maintenance import MaintenanceResource

        return MaintenanceResource(self)

    @cached_property
    def metrics(self) -> MetricsResource:
        from .resources.metrics import MetricsResource

        return MetricsResource(self)

    @cached_property
    def mongodb(self) -> MongoDBResource:
        from .resources.mongodb import MongoDBResource

        return MongoDBResource(self)

    @cached_property
    def oauth(self) -> OAuthResource:
        from .resources.oauth import OAuthResource

        return OAuthResource(self)

    @cached_property
    def onboarding(self) -> OnboardingResource:
        from .resources.onboarding import OnboardingResource

        return OnboardingResource(self)

    @cached_property
    def openapi(self) -> OpenAPIResource:
        from .resources.openapi import OpenAPIResource

        return OpenAPIResource(self)

    @cached_property
    def orgs(self) -> OrgsResource:
        from .resources.orgs import OrgsResource

        return OrgsResource(self)

    @cached_property
    def plans(self) -> PlansResource:
        from .resources.plans import PlansResource

        return PlansResource(self)

    @cached_property
    def pricing(self) -> PricingResource:
        from .resources.pricing import PricingResource

        return PricingResource(self)

    @cached_property
    def projects(self) -> ProjectsResource:
        from .resources.projects import ProjectsResource

        return ProjectsResource(self)

    @cached_property
    def quickstart(self) -> QuickstartResource:
        from .resources.quickstart import QuickstartResource

        return QuickstartResource(self)

    @cached_property
    def realtime(self) -> RealtimeResource:
        from .resources.realtime import RealtimeResource

        return RealtimeResource(self)

    @cached_property
    def refunds(self) -> RefundsResource:
        from .resources.refunds import RefundsResource

        return RefundsResource(self)

    @cached_property
    def regions(self) -> RegionsResource:
        from .resources.regions import RegionsResource

        return RegionsResource(self)

    @cached_property
    def rls(self) -> RlsResource:
        from .resources.rls import RlsResource

        return RlsResource(self)

    @cached_property
    def schema_engine(self) -> SchemaEngineResource:
        from .resources.schema_engine import SchemaEngineResource

        return SchemaEngineResource(self)

    @cached_property
    def schemas(self) -> SchemasResource:
        from .resources.schemas import SchemasResource

        return SchemasResource(self)

    @cached_property
    def sdk(self) -> SDKResource:
        from .resources.sdk import SDKResource

        return SDKResource(self)

    @cached_property
    def security(self) -> SecurityResource:
        from .resources.security import SecurityResource

        return SecurityResource(self)

    @cached_property
    def sso(self) -> SSOResource:
        from .resources.sso import SSOResource

        return SSOResource(self)

    @cached_property
    def status(self) -> StatusResource:
        from .resources.status import StatusResource

        return StatusResource(self)

    @cached_property
    def storage(self) -> StorageResource:
        from .resources.storage import StorageResource

        return StorageResource(self)

    @cached_property
    def templates(self) -> TemplatesResource:
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def v1(self) -> V1Resource:
        from .resources.v1 import V1Resource

        return V1Resource(self)

    @cached_property
    def with_raw_response(self) -> VaifWithRawResponse:
        return VaifWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VaifWithStreamedResponse:
        return VaifWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._bearer_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"x-vaif-key": api_key}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("x-vaif-key") or isinstance(custom_headers.get("x-vaif-key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `x-vaif-key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncVaif(AsyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncVaif client instance."""
        self.api_key = api_key

        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("VAIF_BASE_URL")
        if base_url is None:
            base_url = f"https://api.vaif.studio"

        custom_headers_env = os.environ.get("VAIF_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def activation(self) -> AsyncActivationResource:
        from .resources.activation import AsyncActivationResource

        return AsyncActivationResource(self)

    @cached_property
    def ai(self) -> AsyncAIResource:
        from .resources.ai import AsyncAIResource

        return AsyncAIResource(self)

    @cached_property
    def ai_usage(self) -> AsyncAIUsageResource:
        from .resources.ai_usage import AsyncAIUsageResource

        return AsyncAIUsageResource(self)

    @cached_property
    def alert_rules(self) -> AsyncAlertRulesResource:
        from .resources.alert_rules import AsyncAlertRulesResource

        return AsyncAlertRulesResource(self)

    @cached_property
    def announcements(self) -> AsyncAnnouncementsResource:
        from .resources.announcements import AsyncAnnouncementsResource

        return AsyncAnnouncementsResource(self)

    @cached_property
    def audit(self) -> AsyncAuditResource:
        from .resources.audit import AsyncAuditResource

        return AsyncAuditResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        from .resources.billing import AsyncBillingResource

        return AsyncBillingResource(self)

    @cached_property
    def bootstrap(self) -> AsyncBootstrapResource:
        from .resources.bootstrap import AsyncBootstrapResource

        return AsyncBootstrapResource(self)

    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        from .resources.buckets import AsyncBucketsResource

        return AsyncBucketsResource(self)

    @cached_property
    def cms(self) -> AsyncCmsResource:
        from .resources.cms import AsyncCmsResource

        return AsyncCmsResource(self)

    @cached_property
    def contact(self) -> AsyncContactResource:
        from .resources.contact import AsyncContactResource

        return AsyncContactResource(self)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        from .resources.credits import AsyncCreditsResource

        return AsyncCreditsResource(self)

    @cached_property
    def database(self) -> AsyncDatabaseResource:
        from .resources.database import AsyncDatabaseResource

        return AsyncDatabaseResource(self)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        from .resources.deployments import AsyncDeploymentsResource

        return AsyncDeploymentsResource(self)

    @cached_property
    def docs(self) -> AsyncDocsResource:
        from .resources.docs import AsyncDocsResource

        return AsyncDocsResource(self)

    @cached_property
    def enterprise(self) -> AsyncEnterpriseResource:
        from .resources.enterprise import AsyncEnterpriseResource

        return AsyncEnterpriseResource(self)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        from .resources.entitlements import AsyncEntitlementsResource

        return AsyncEntitlementsResource(self)

    @cached_property
    def functions(self) -> AsyncFunctionsResource:
        from .resources.functions import AsyncFunctionsResource

        return AsyncFunctionsResource(self)

    @cached_property
    def generated(self) -> AsyncGeneratedResource:
        from .resources.generated import AsyncGeneratedResource

        return AsyncGeneratedResource(self)

    @cached_property
    def github(self) -> AsyncGitHubResource:
        from .resources.github import AsyncGitHubResource

        return AsyncGitHubResource(self)

    @cached_property
    def incidents(self) -> AsyncIncidentsResource:
        from .resources.incidents import AsyncIncidentsResource

        return AsyncIncidentsResource(self)

    @cached_property
    def infrastructure(self) -> AsyncInfrastructureResource:
        from .resources.infrastructure import AsyncInfrastructureResource

        return AsyncInfrastructureResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        from .resources.jobs import AsyncJobsResource

        return AsyncJobsResource(self)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        from .resources.logs import AsyncLogsResource

        return AsyncLogsResource(self)

    @cached_property
    def maintenance(self) -> AsyncMaintenanceResource:
        from .resources.maintenance import AsyncMaintenanceResource

        return AsyncMaintenanceResource(self)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        from .resources.metrics import AsyncMetricsResource

        return AsyncMetricsResource(self)

    @cached_property
    def mongodb(self) -> AsyncMongoDBResource:
        from .resources.mongodb import AsyncMongoDBResource

        return AsyncMongoDBResource(self)

    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        from .resources.oauth import AsyncOAuthResource

        return AsyncOAuthResource(self)

    @cached_property
    def onboarding(self) -> AsyncOnboardingResource:
        from .resources.onboarding import AsyncOnboardingResource

        return AsyncOnboardingResource(self)

    @cached_property
    def openapi(self) -> AsyncOpenAPIResource:
        from .resources.openapi import AsyncOpenAPIResource

        return AsyncOpenAPIResource(self)

    @cached_property
    def orgs(self) -> AsyncOrgsResource:
        from .resources.orgs import AsyncOrgsResource

        return AsyncOrgsResource(self)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        from .resources.plans import AsyncPlansResource

        return AsyncPlansResource(self)

    @cached_property
    def pricing(self) -> AsyncPricingResource:
        from .resources.pricing import AsyncPricingResource

        return AsyncPricingResource(self)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        from .resources.projects import AsyncProjectsResource

        return AsyncProjectsResource(self)

    @cached_property
    def quickstart(self) -> AsyncQuickstartResource:
        from .resources.quickstart import AsyncQuickstartResource

        return AsyncQuickstartResource(self)

    @cached_property
    def realtime(self) -> AsyncRealtimeResource:
        from .resources.realtime import AsyncRealtimeResource

        return AsyncRealtimeResource(self)

    @cached_property
    def refunds(self) -> AsyncRefundsResource:
        from .resources.refunds import AsyncRefundsResource

        return AsyncRefundsResource(self)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        from .resources.regions import AsyncRegionsResource

        return AsyncRegionsResource(self)

    @cached_property
    def rls(self) -> AsyncRlsResource:
        from .resources.rls import AsyncRlsResource

        return AsyncRlsResource(self)

    @cached_property
    def schema_engine(self) -> AsyncSchemaEngineResource:
        from .resources.schema_engine import AsyncSchemaEngineResource

        return AsyncSchemaEngineResource(self)

    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        from .resources.schemas import AsyncSchemasResource

        return AsyncSchemasResource(self)

    @cached_property
    def sdk(self) -> AsyncSDKResource:
        from .resources.sdk import AsyncSDKResource

        return AsyncSDKResource(self)

    @cached_property
    def security(self) -> AsyncSecurityResource:
        from .resources.security import AsyncSecurityResource

        return AsyncSecurityResource(self)

    @cached_property
    def sso(self) -> AsyncSSOResource:
        from .resources.sso import AsyncSSOResource

        return AsyncSSOResource(self)

    @cached_property
    def status(self) -> AsyncStatusResource:
        from .resources.status import AsyncStatusResource

        return AsyncStatusResource(self)

    @cached_property
    def storage(self) -> AsyncStorageResource:
        from .resources.storage import AsyncStorageResource

        return AsyncStorageResource(self)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def v1(self) -> AsyncV1Resource:
        from .resources.v1 import AsyncV1Resource

        return AsyncV1Resource(self)

    @cached_property
    def with_raw_response(self) -> AsyncVaifWithRawResponse:
        return AsyncVaifWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVaifWithStreamedResponse:
        return AsyncVaifWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._bearer_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"x-vaif-key": api_key}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("x-vaif-key") or isinstance(custom_headers.get("x-vaif-key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `x-vaif-key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class VaifWithRawResponse:
    _client: Vaif

    def __init__(self, client: Vaif) -> None:
        self._client = client

    @cached_property
    def activation(self) -> activation.ActivationResourceWithRawResponse:
        from .resources.activation import ActivationResourceWithRawResponse

        return ActivationResourceWithRawResponse(self._client.activation)

    @cached_property
    def ai(self) -> ai.AIResourceWithRawResponse:
        from .resources.ai import AIResourceWithRawResponse

        return AIResourceWithRawResponse(self._client.ai)

    @cached_property
    def ai_usage(self) -> ai_usage.AIUsageResourceWithRawResponse:
        from .resources.ai_usage import AIUsageResourceWithRawResponse

        return AIUsageResourceWithRawResponse(self._client.ai_usage)

    @cached_property
    def alert_rules(self) -> alert_rules.AlertRulesResourceWithRawResponse:
        from .resources.alert_rules import AlertRulesResourceWithRawResponse

        return AlertRulesResourceWithRawResponse(self._client.alert_rules)

    @cached_property
    def announcements(self) -> announcements.AnnouncementsResourceWithRawResponse:
        from .resources.announcements import AnnouncementsResourceWithRawResponse

        return AnnouncementsResourceWithRawResponse(self._client.announcements)

    @cached_property
    def audit(self) -> audit.AuditResourceWithRawResponse:
        from .resources.audit import AuditResourceWithRawResponse

        return AuditResourceWithRawResponse(self._client.audit)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def billing(self) -> billing.BillingResourceWithRawResponse:
        from .resources.billing import BillingResourceWithRawResponse

        return BillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def bootstrap(self) -> bootstrap.BootstrapResourceWithRawResponse:
        from .resources.bootstrap import BootstrapResourceWithRawResponse

        return BootstrapResourceWithRawResponse(self._client.bootstrap)

    @cached_property
    def buckets(self) -> buckets.BucketsResourceWithRawResponse:
        from .resources.buckets import BucketsResourceWithRawResponse

        return BucketsResourceWithRawResponse(self._client.buckets)

    @cached_property
    def cms(self) -> cms.CmsResourceWithRawResponse:
        from .resources.cms import CmsResourceWithRawResponse

        return CmsResourceWithRawResponse(self._client.cms)

    @cached_property
    def contact(self) -> contact.ContactResourceWithRawResponse:
        from .resources.contact import ContactResourceWithRawResponse

        return ContactResourceWithRawResponse(self._client.contact)

    @cached_property
    def credits(self) -> credits.CreditsResourceWithRawResponse:
        from .resources.credits import CreditsResourceWithRawResponse

        return CreditsResourceWithRawResponse(self._client.credits)

    @cached_property
    def database(self) -> database.DatabaseResourceWithRawResponse:
        from .resources.database import DatabaseResourceWithRawResponse

        return DatabaseResourceWithRawResponse(self._client.database)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithRawResponse:
        from .resources.deployments import DeploymentsResourceWithRawResponse

        return DeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def docs(self) -> docs.DocsResourceWithRawResponse:
        from .resources.docs import DocsResourceWithRawResponse

        return DocsResourceWithRawResponse(self._client.docs)

    @cached_property
    def enterprise(self) -> enterprise.EnterpriseResourceWithRawResponse:
        from .resources.enterprise import EnterpriseResourceWithRawResponse

        return EnterpriseResourceWithRawResponse(self._client.enterprise)

    @cached_property
    def entitlements(self) -> entitlements.EntitlementsResourceWithRawResponse:
        from .resources.entitlements import EntitlementsResourceWithRawResponse

        return EntitlementsResourceWithRawResponse(self._client.entitlements)

    @cached_property
    def functions(self) -> functions.FunctionsResourceWithRawResponse:
        from .resources.functions import FunctionsResourceWithRawResponse

        return FunctionsResourceWithRawResponse(self._client.functions)

    @cached_property
    def generated(self) -> generated.GeneratedResourceWithRawResponse:
        from .resources.generated import GeneratedResourceWithRawResponse

        return GeneratedResourceWithRawResponse(self._client.generated)

    @cached_property
    def github(self) -> github.GitHubResourceWithRawResponse:
        from .resources.github import GitHubResourceWithRawResponse

        return GitHubResourceWithRawResponse(self._client.github)

    @cached_property
    def incidents(self) -> incidents.IncidentsResourceWithRawResponse:
        from .resources.incidents import IncidentsResourceWithRawResponse

        return IncidentsResourceWithRawResponse(self._client.incidents)

    @cached_property
    def infrastructure(self) -> infrastructure.InfrastructureResourceWithRawResponse:
        from .resources.infrastructure import InfrastructureResourceWithRawResponse

        return InfrastructureResourceWithRawResponse(self._client.infrastructure)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def jobs(self) -> jobs.JobsResourceWithRawResponse:
        from .resources.jobs import JobsResourceWithRawResponse

        return JobsResourceWithRawResponse(self._client.jobs)

    @cached_property
    def logs(self) -> logs.LogsResourceWithRawResponse:
        from .resources.logs import LogsResourceWithRawResponse

        return LogsResourceWithRawResponse(self._client.logs)

    @cached_property
    def maintenance(self) -> maintenance.MaintenanceResourceWithRawResponse:
        from .resources.maintenance import MaintenanceResourceWithRawResponse

        return MaintenanceResourceWithRawResponse(self._client.maintenance)

    @cached_property
    def metrics(self) -> metrics.MetricsResourceWithRawResponse:
        from .resources.metrics import MetricsResourceWithRawResponse

        return MetricsResourceWithRawResponse(self._client.metrics)

    @cached_property
    def mongodb(self) -> mongodb.MongoDBResourceWithRawResponse:
        from .resources.mongodb import MongoDBResourceWithRawResponse

        return MongoDBResourceWithRawResponse(self._client.mongodb)

    @cached_property
    def oauth(self) -> oauth.OAuthResourceWithRawResponse:
        from .resources.oauth import OAuthResourceWithRawResponse

        return OAuthResourceWithRawResponse(self._client.oauth)

    @cached_property
    def onboarding(self) -> onboarding.OnboardingResourceWithRawResponse:
        from .resources.onboarding import OnboardingResourceWithRawResponse

        return OnboardingResourceWithRawResponse(self._client.onboarding)

    @cached_property
    def openapi(self) -> openapi.OpenAPIResourceWithRawResponse:
        from .resources.openapi import OpenAPIResourceWithRawResponse

        return OpenAPIResourceWithRawResponse(self._client.openapi)

    @cached_property
    def orgs(self) -> orgs.OrgsResourceWithRawResponse:
        from .resources.orgs import OrgsResourceWithRawResponse

        return OrgsResourceWithRawResponse(self._client.orgs)

    @cached_property
    def plans(self) -> plans.PlansResourceWithRawResponse:
        from .resources.plans import PlansResourceWithRawResponse

        return PlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def pricing(self) -> pricing.PricingResourceWithRawResponse:
        from .resources.pricing import PricingResourceWithRawResponse

        return PricingResourceWithRawResponse(self._client.pricing)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithRawResponse:
        from .resources.projects import ProjectsResourceWithRawResponse

        return ProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def quickstart(self) -> quickstart.QuickstartResourceWithRawResponse:
        from .resources.quickstart import QuickstartResourceWithRawResponse

        return QuickstartResourceWithRawResponse(self._client.quickstart)

    @cached_property
    def realtime(self) -> realtime.RealtimeResourceWithRawResponse:
        from .resources.realtime import RealtimeResourceWithRawResponse

        return RealtimeResourceWithRawResponse(self._client.realtime)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithRawResponse:
        from .resources.refunds import RefundsResourceWithRawResponse

        return RefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithRawResponse:
        from .resources.regions import RegionsResourceWithRawResponse

        return RegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def rls(self) -> rls.RlsResourceWithRawResponse:
        from .resources.rls import RlsResourceWithRawResponse

        return RlsResourceWithRawResponse(self._client.rls)

    @cached_property
    def schema_engine(self) -> schema_engine.SchemaEngineResourceWithRawResponse:
        from .resources.schema_engine import SchemaEngineResourceWithRawResponse

        return SchemaEngineResourceWithRawResponse(self._client.schema_engine)

    @cached_property
    def schemas(self) -> schemas.SchemasResourceWithRawResponse:
        from .resources.schemas import SchemasResourceWithRawResponse

        return SchemasResourceWithRawResponse(self._client.schemas)

    @cached_property
    def sdk(self) -> sdk.SDKResourceWithRawResponse:
        from .resources.sdk import SDKResourceWithRawResponse

        return SDKResourceWithRawResponse(self._client.sdk)

    @cached_property
    def security(self) -> security.SecurityResourceWithRawResponse:
        from .resources.security import SecurityResourceWithRawResponse

        return SecurityResourceWithRawResponse(self._client.security)

    @cached_property
    def sso(self) -> sso.SSOResourceWithRawResponse:
        from .resources.sso import SSOResourceWithRawResponse

        return SSOResourceWithRawResponse(self._client.sso)

    @cached_property
    def status(self) -> status.StatusResourceWithRawResponse:
        from .resources.status import StatusResourceWithRawResponse

        return StatusResourceWithRawResponse(self._client.status)

    @cached_property
    def storage(self) -> storage.StorageResourceWithRawResponse:
        from .resources.storage import StorageResourceWithRawResponse

        return StorageResourceWithRawResponse(self._client.storage)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def v1(self) -> v1.V1ResourceWithRawResponse:
        from .resources.v1 import V1ResourceWithRawResponse

        return V1ResourceWithRawResponse(self._client.v1)


class AsyncVaifWithRawResponse:
    _client: AsyncVaif

    def __init__(self, client: AsyncVaif) -> None:
        self._client = client

    @cached_property
    def activation(self) -> activation.AsyncActivationResourceWithRawResponse:
        from .resources.activation import AsyncActivationResourceWithRawResponse

        return AsyncActivationResourceWithRawResponse(self._client.activation)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithRawResponse:
        from .resources.ai import AsyncAIResourceWithRawResponse

        return AsyncAIResourceWithRawResponse(self._client.ai)

    @cached_property
    def ai_usage(self) -> ai_usage.AsyncAIUsageResourceWithRawResponse:
        from .resources.ai_usage import AsyncAIUsageResourceWithRawResponse

        return AsyncAIUsageResourceWithRawResponse(self._client.ai_usage)

    @cached_property
    def alert_rules(self) -> alert_rules.AsyncAlertRulesResourceWithRawResponse:
        from .resources.alert_rules import AsyncAlertRulesResourceWithRawResponse

        return AsyncAlertRulesResourceWithRawResponse(self._client.alert_rules)

    @cached_property
    def announcements(self) -> announcements.AsyncAnnouncementsResourceWithRawResponse:
        from .resources.announcements import AsyncAnnouncementsResourceWithRawResponse

        return AsyncAnnouncementsResourceWithRawResponse(self._client.announcements)

    @cached_property
    def audit(self) -> audit.AsyncAuditResourceWithRawResponse:
        from .resources.audit import AsyncAuditResourceWithRawResponse

        return AsyncAuditResourceWithRawResponse(self._client.audit)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithRawResponse:
        from .resources.billing import AsyncBillingResourceWithRawResponse

        return AsyncBillingResourceWithRawResponse(self._client.billing)

    @cached_property
    def bootstrap(self) -> bootstrap.AsyncBootstrapResourceWithRawResponse:
        from .resources.bootstrap import AsyncBootstrapResourceWithRawResponse

        return AsyncBootstrapResourceWithRawResponse(self._client.bootstrap)

    @cached_property
    def buckets(self) -> buckets.AsyncBucketsResourceWithRawResponse:
        from .resources.buckets import AsyncBucketsResourceWithRawResponse

        return AsyncBucketsResourceWithRawResponse(self._client.buckets)

    @cached_property
    def cms(self) -> cms.AsyncCmsResourceWithRawResponse:
        from .resources.cms import AsyncCmsResourceWithRawResponse

        return AsyncCmsResourceWithRawResponse(self._client.cms)

    @cached_property
    def contact(self) -> contact.AsyncContactResourceWithRawResponse:
        from .resources.contact import AsyncContactResourceWithRawResponse

        return AsyncContactResourceWithRawResponse(self._client.contact)

    @cached_property
    def credits(self) -> credits.AsyncCreditsResourceWithRawResponse:
        from .resources.credits import AsyncCreditsResourceWithRawResponse

        return AsyncCreditsResourceWithRawResponse(self._client.credits)

    @cached_property
    def database(self) -> database.AsyncDatabaseResourceWithRawResponse:
        from .resources.database import AsyncDatabaseResourceWithRawResponse

        return AsyncDatabaseResourceWithRawResponse(self._client.database)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithRawResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithRawResponse

        return AsyncDeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def docs(self) -> docs.AsyncDocsResourceWithRawResponse:
        from .resources.docs import AsyncDocsResourceWithRawResponse

        return AsyncDocsResourceWithRawResponse(self._client.docs)

    @cached_property
    def enterprise(self) -> enterprise.AsyncEnterpriseResourceWithRawResponse:
        from .resources.enterprise import AsyncEnterpriseResourceWithRawResponse

        return AsyncEnterpriseResourceWithRawResponse(self._client.enterprise)

    @cached_property
    def entitlements(self) -> entitlements.AsyncEntitlementsResourceWithRawResponse:
        from .resources.entitlements import AsyncEntitlementsResourceWithRawResponse

        return AsyncEntitlementsResourceWithRawResponse(self._client.entitlements)

    @cached_property
    def functions(self) -> functions.AsyncFunctionsResourceWithRawResponse:
        from .resources.functions import AsyncFunctionsResourceWithRawResponse

        return AsyncFunctionsResourceWithRawResponse(self._client.functions)

    @cached_property
    def generated(self) -> generated.AsyncGeneratedResourceWithRawResponse:
        from .resources.generated import AsyncGeneratedResourceWithRawResponse

        return AsyncGeneratedResourceWithRawResponse(self._client.generated)

    @cached_property
    def github(self) -> github.AsyncGitHubResourceWithRawResponse:
        from .resources.github import AsyncGitHubResourceWithRawResponse

        return AsyncGitHubResourceWithRawResponse(self._client.github)

    @cached_property
    def incidents(self) -> incidents.AsyncIncidentsResourceWithRawResponse:
        from .resources.incidents import AsyncIncidentsResourceWithRawResponse

        return AsyncIncidentsResourceWithRawResponse(self._client.incidents)

    @cached_property
    def infrastructure(self) -> infrastructure.AsyncInfrastructureResourceWithRawResponse:
        from .resources.infrastructure import AsyncInfrastructureResourceWithRawResponse

        return AsyncInfrastructureResourceWithRawResponse(self._client.infrastructure)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def jobs(self) -> jobs.AsyncJobsResourceWithRawResponse:
        from .resources.jobs import AsyncJobsResourceWithRawResponse

        return AsyncJobsResourceWithRawResponse(self._client.jobs)

    @cached_property
    def logs(self) -> logs.AsyncLogsResourceWithRawResponse:
        from .resources.logs import AsyncLogsResourceWithRawResponse

        return AsyncLogsResourceWithRawResponse(self._client.logs)

    @cached_property
    def maintenance(self) -> maintenance.AsyncMaintenanceResourceWithRawResponse:
        from .resources.maintenance import AsyncMaintenanceResourceWithRawResponse

        return AsyncMaintenanceResourceWithRawResponse(self._client.maintenance)

    @cached_property
    def metrics(self) -> metrics.AsyncMetricsResourceWithRawResponse:
        from .resources.metrics import AsyncMetricsResourceWithRawResponse

        return AsyncMetricsResourceWithRawResponse(self._client.metrics)

    @cached_property
    def mongodb(self) -> mongodb.AsyncMongoDBResourceWithRawResponse:
        from .resources.mongodb import AsyncMongoDBResourceWithRawResponse

        return AsyncMongoDBResourceWithRawResponse(self._client.mongodb)

    @cached_property
    def oauth(self) -> oauth.AsyncOAuthResourceWithRawResponse:
        from .resources.oauth import AsyncOAuthResourceWithRawResponse

        return AsyncOAuthResourceWithRawResponse(self._client.oauth)

    @cached_property
    def onboarding(self) -> onboarding.AsyncOnboardingResourceWithRawResponse:
        from .resources.onboarding import AsyncOnboardingResourceWithRawResponse

        return AsyncOnboardingResourceWithRawResponse(self._client.onboarding)

    @cached_property
    def openapi(self) -> openapi.AsyncOpenAPIResourceWithRawResponse:
        from .resources.openapi import AsyncOpenAPIResourceWithRawResponse

        return AsyncOpenAPIResourceWithRawResponse(self._client.openapi)

    @cached_property
    def orgs(self) -> orgs.AsyncOrgsResourceWithRawResponse:
        from .resources.orgs import AsyncOrgsResourceWithRawResponse

        return AsyncOrgsResourceWithRawResponse(self._client.orgs)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithRawResponse:
        from .resources.plans import AsyncPlansResourceWithRawResponse

        return AsyncPlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def pricing(self) -> pricing.AsyncPricingResourceWithRawResponse:
        from .resources.pricing import AsyncPricingResourceWithRawResponse

        return AsyncPricingResourceWithRawResponse(self._client.pricing)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithRawResponse:
        from .resources.projects import AsyncProjectsResourceWithRawResponse

        return AsyncProjectsResourceWithRawResponse(self._client.projects)

    @cached_property
    def quickstart(self) -> quickstart.AsyncQuickstartResourceWithRawResponse:
        from .resources.quickstart import AsyncQuickstartResourceWithRawResponse

        return AsyncQuickstartResourceWithRawResponse(self._client.quickstart)

    @cached_property
    def realtime(self) -> realtime.AsyncRealtimeResourceWithRawResponse:
        from .resources.realtime import AsyncRealtimeResourceWithRawResponse

        return AsyncRealtimeResourceWithRawResponse(self._client.realtime)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithRawResponse:
        from .resources.refunds import AsyncRefundsResourceWithRawResponse

        return AsyncRefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithRawResponse:
        from .resources.regions import AsyncRegionsResourceWithRawResponse

        return AsyncRegionsResourceWithRawResponse(self._client.regions)

    @cached_property
    def rls(self) -> rls.AsyncRlsResourceWithRawResponse:
        from .resources.rls import AsyncRlsResourceWithRawResponse

        return AsyncRlsResourceWithRawResponse(self._client.rls)

    @cached_property
    def schema_engine(self) -> schema_engine.AsyncSchemaEngineResourceWithRawResponse:
        from .resources.schema_engine import AsyncSchemaEngineResourceWithRawResponse

        return AsyncSchemaEngineResourceWithRawResponse(self._client.schema_engine)

    @cached_property
    def schemas(self) -> schemas.AsyncSchemasResourceWithRawResponse:
        from .resources.schemas import AsyncSchemasResourceWithRawResponse

        return AsyncSchemasResourceWithRawResponse(self._client.schemas)

    @cached_property
    def sdk(self) -> sdk.AsyncSDKResourceWithRawResponse:
        from .resources.sdk import AsyncSDKResourceWithRawResponse

        return AsyncSDKResourceWithRawResponse(self._client.sdk)

    @cached_property
    def security(self) -> security.AsyncSecurityResourceWithRawResponse:
        from .resources.security import AsyncSecurityResourceWithRawResponse

        return AsyncSecurityResourceWithRawResponse(self._client.security)

    @cached_property
    def sso(self) -> sso.AsyncSSOResourceWithRawResponse:
        from .resources.sso import AsyncSSOResourceWithRawResponse

        return AsyncSSOResourceWithRawResponse(self._client.sso)

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithRawResponse:
        from .resources.status import AsyncStatusResourceWithRawResponse

        return AsyncStatusResourceWithRawResponse(self._client.status)

    @cached_property
    def storage(self) -> storage.AsyncStorageResourceWithRawResponse:
        from .resources.storage import AsyncStorageResourceWithRawResponse

        return AsyncStorageResourceWithRawResponse(self._client.storage)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def v1(self) -> v1.AsyncV1ResourceWithRawResponse:
        from .resources.v1 import AsyncV1ResourceWithRawResponse

        return AsyncV1ResourceWithRawResponse(self._client.v1)


class VaifWithStreamedResponse:
    _client: Vaif

    def __init__(self, client: Vaif) -> None:
        self._client = client

    @cached_property
    def activation(self) -> activation.ActivationResourceWithStreamingResponse:
        from .resources.activation import ActivationResourceWithStreamingResponse

        return ActivationResourceWithStreamingResponse(self._client.activation)

    @cached_property
    def ai(self) -> ai.AIResourceWithStreamingResponse:
        from .resources.ai import AIResourceWithStreamingResponse

        return AIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def ai_usage(self) -> ai_usage.AIUsageResourceWithStreamingResponse:
        from .resources.ai_usage import AIUsageResourceWithStreamingResponse

        return AIUsageResourceWithStreamingResponse(self._client.ai_usage)

    @cached_property
    def alert_rules(self) -> alert_rules.AlertRulesResourceWithStreamingResponse:
        from .resources.alert_rules import AlertRulesResourceWithStreamingResponse

        return AlertRulesResourceWithStreamingResponse(self._client.alert_rules)

    @cached_property
    def announcements(self) -> announcements.AnnouncementsResourceWithStreamingResponse:
        from .resources.announcements import AnnouncementsResourceWithStreamingResponse

        return AnnouncementsResourceWithStreamingResponse(self._client.announcements)

    @cached_property
    def audit(self) -> audit.AuditResourceWithStreamingResponse:
        from .resources.audit import AuditResourceWithStreamingResponse

        return AuditResourceWithStreamingResponse(self._client.audit)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def billing(self) -> billing.BillingResourceWithStreamingResponse:
        from .resources.billing import BillingResourceWithStreamingResponse

        return BillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def bootstrap(self) -> bootstrap.BootstrapResourceWithStreamingResponse:
        from .resources.bootstrap import BootstrapResourceWithStreamingResponse

        return BootstrapResourceWithStreamingResponse(self._client.bootstrap)

    @cached_property
    def buckets(self) -> buckets.BucketsResourceWithStreamingResponse:
        from .resources.buckets import BucketsResourceWithStreamingResponse

        return BucketsResourceWithStreamingResponse(self._client.buckets)

    @cached_property
    def cms(self) -> cms.CmsResourceWithStreamingResponse:
        from .resources.cms import CmsResourceWithStreamingResponse

        return CmsResourceWithStreamingResponse(self._client.cms)

    @cached_property
    def contact(self) -> contact.ContactResourceWithStreamingResponse:
        from .resources.contact import ContactResourceWithStreamingResponse

        return ContactResourceWithStreamingResponse(self._client.contact)

    @cached_property
    def credits(self) -> credits.CreditsResourceWithStreamingResponse:
        from .resources.credits import CreditsResourceWithStreamingResponse

        return CreditsResourceWithStreamingResponse(self._client.credits)

    @cached_property
    def database(self) -> database.DatabaseResourceWithStreamingResponse:
        from .resources.database import DatabaseResourceWithStreamingResponse

        return DatabaseResourceWithStreamingResponse(self._client.database)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithStreamingResponse:
        from .resources.deployments import DeploymentsResourceWithStreamingResponse

        return DeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def docs(self) -> docs.DocsResourceWithStreamingResponse:
        from .resources.docs import DocsResourceWithStreamingResponse

        return DocsResourceWithStreamingResponse(self._client.docs)

    @cached_property
    def enterprise(self) -> enterprise.EnterpriseResourceWithStreamingResponse:
        from .resources.enterprise import EnterpriseResourceWithStreamingResponse

        return EnterpriseResourceWithStreamingResponse(self._client.enterprise)

    @cached_property
    def entitlements(self) -> entitlements.EntitlementsResourceWithStreamingResponse:
        from .resources.entitlements import EntitlementsResourceWithStreamingResponse

        return EntitlementsResourceWithStreamingResponse(self._client.entitlements)

    @cached_property
    def functions(self) -> functions.FunctionsResourceWithStreamingResponse:
        from .resources.functions import FunctionsResourceWithStreamingResponse

        return FunctionsResourceWithStreamingResponse(self._client.functions)

    @cached_property
    def generated(self) -> generated.GeneratedResourceWithStreamingResponse:
        from .resources.generated import GeneratedResourceWithStreamingResponse

        return GeneratedResourceWithStreamingResponse(self._client.generated)

    @cached_property
    def github(self) -> github.GitHubResourceWithStreamingResponse:
        from .resources.github import GitHubResourceWithStreamingResponse

        return GitHubResourceWithStreamingResponse(self._client.github)

    @cached_property
    def incidents(self) -> incidents.IncidentsResourceWithStreamingResponse:
        from .resources.incidents import IncidentsResourceWithStreamingResponse

        return IncidentsResourceWithStreamingResponse(self._client.incidents)

    @cached_property
    def infrastructure(self) -> infrastructure.InfrastructureResourceWithStreamingResponse:
        from .resources.infrastructure import InfrastructureResourceWithStreamingResponse

        return InfrastructureResourceWithStreamingResponse(self._client.infrastructure)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def jobs(self) -> jobs.JobsResourceWithStreamingResponse:
        from .resources.jobs import JobsResourceWithStreamingResponse

        return JobsResourceWithStreamingResponse(self._client.jobs)

    @cached_property
    def logs(self) -> logs.LogsResourceWithStreamingResponse:
        from .resources.logs import LogsResourceWithStreamingResponse

        return LogsResourceWithStreamingResponse(self._client.logs)

    @cached_property
    def maintenance(self) -> maintenance.MaintenanceResourceWithStreamingResponse:
        from .resources.maintenance import MaintenanceResourceWithStreamingResponse

        return MaintenanceResourceWithStreamingResponse(self._client.maintenance)

    @cached_property
    def metrics(self) -> metrics.MetricsResourceWithStreamingResponse:
        from .resources.metrics import MetricsResourceWithStreamingResponse

        return MetricsResourceWithStreamingResponse(self._client.metrics)

    @cached_property
    def mongodb(self) -> mongodb.MongoDBResourceWithStreamingResponse:
        from .resources.mongodb import MongoDBResourceWithStreamingResponse

        return MongoDBResourceWithStreamingResponse(self._client.mongodb)

    @cached_property
    def oauth(self) -> oauth.OAuthResourceWithStreamingResponse:
        from .resources.oauth import OAuthResourceWithStreamingResponse

        return OAuthResourceWithStreamingResponse(self._client.oauth)

    @cached_property
    def onboarding(self) -> onboarding.OnboardingResourceWithStreamingResponse:
        from .resources.onboarding import OnboardingResourceWithStreamingResponse

        return OnboardingResourceWithStreamingResponse(self._client.onboarding)

    @cached_property
    def openapi(self) -> openapi.OpenAPIResourceWithStreamingResponse:
        from .resources.openapi import OpenAPIResourceWithStreamingResponse

        return OpenAPIResourceWithStreamingResponse(self._client.openapi)

    @cached_property
    def orgs(self) -> orgs.OrgsResourceWithStreamingResponse:
        from .resources.orgs import OrgsResourceWithStreamingResponse

        return OrgsResourceWithStreamingResponse(self._client.orgs)

    @cached_property
    def plans(self) -> plans.PlansResourceWithStreamingResponse:
        from .resources.plans import PlansResourceWithStreamingResponse

        return PlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def pricing(self) -> pricing.PricingResourceWithStreamingResponse:
        from .resources.pricing import PricingResourceWithStreamingResponse

        return PricingResourceWithStreamingResponse(self._client.pricing)

    @cached_property
    def projects(self) -> projects.ProjectsResourceWithStreamingResponse:
        from .resources.projects import ProjectsResourceWithStreamingResponse

        return ProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def quickstart(self) -> quickstart.QuickstartResourceWithStreamingResponse:
        from .resources.quickstart import QuickstartResourceWithStreamingResponse

        return QuickstartResourceWithStreamingResponse(self._client.quickstart)

    @cached_property
    def realtime(self) -> realtime.RealtimeResourceWithStreamingResponse:
        from .resources.realtime import RealtimeResourceWithStreamingResponse

        return RealtimeResourceWithStreamingResponse(self._client.realtime)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithStreamingResponse:
        from .resources.refunds import RefundsResourceWithStreamingResponse

        return RefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def regions(self) -> regions.RegionsResourceWithStreamingResponse:
        from .resources.regions import RegionsResourceWithStreamingResponse

        return RegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def rls(self) -> rls.RlsResourceWithStreamingResponse:
        from .resources.rls import RlsResourceWithStreamingResponse

        return RlsResourceWithStreamingResponse(self._client.rls)

    @cached_property
    def schema_engine(self) -> schema_engine.SchemaEngineResourceWithStreamingResponse:
        from .resources.schema_engine import SchemaEngineResourceWithStreamingResponse

        return SchemaEngineResourceWithStreamingResponse(self._client.schema_engine)

    @cached_property
    def schemas(self) -> schemas.SchemasResourceWithStreamingResponse:
        from .resources.schemas import SchemasResourceWithStreamingResponse

        return SchemasResourceWithStreamingResponse(self._client.schemas)

    @cached_property
    def sdk(self) -> sdk.SDKResourceWithStreamingResponse:
        from .resources.sdk import SDKResourceWithStreamingResponse

        return SDKResourceWithStreamingResponse(self._client.sdk)

    @cached_property
    def security(self) -> security.SecurityResourceWithStreamingResponse:
        from .resources.security import SecurityResourceWithStreamingResponse

        return SecurityResourceWithStreamingResponse(self._client.security)

    @cached_property
    def sso(self) -> sso.SSOResourceWithStreamingResponse:
        from .resources.sso import SSOResourceWithStreamingResponse

        return SSOResourceWithStreamingResponse(self._client.sso)

    @cached_property
    def status(self) -> status.StatusResourceWithStreamingResponse:
        from .resources.status import StatusResourceWithStreamingResponse

        return StatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def storage(self) -> storage.StorageResourceWithStreamingResponse:
        from .resources.storage import StorageResourceWithStreamingResponse

        return StorageResourceWithStreamingResponse(self._client.storage)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def v1(self) -> v1.V1ResourceWithStreamingResponse:
        from .resources.v1 import V1ResourceWithStreamingResponse

        return V1ResourceWithStreamingResponse(self._client.v1)


class AsyncVaifWithStreamedResponse:
    _client: AsyncVaif

    def __init__(self, client: AsyncVaif) -> None:
        self._client = client

    @cached_property
    def activation(self) -> activation.AsyncActivationResourceWithStreamingResponse:
        from .resources.activation import AsyncActivationResourceWithStreamingResponse

        return AsyncActivationResourceWithStreamingResponse(self._client.activation)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithStreamingResponse:
        from .resources.ai import AsyncAIResourceWithStreamingResponse

        return AsyncAIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def ai_usage(self) -> ai_usage.AsyncAIUsageResourceWithStreamingResponse:
        from .resources.ai_usage import AsyncAIUsageResourceWithStreamingResponse

        return AsyncAIUsageResourceWithStreamingResponse(self._client.ai_usage)

    @cached_property
    def alert_rules(self) -> alert_rules.AsyncAlertRulesResourceWithStreamingResponse:
        from .resources.alert_rules import AsyncAlertRulesResourceWithStreamingResponse

        return AsyncAlertRulesResourceWithStreamingResponse(self._client.alert_rules)

    @cached_property
    def announcements(self) -> announcements.AsyncAnnouncementsResourceWithStreamingResponse:
        from .resources.announcements import AsyncAnnouncementsResourceWithStreamingResponse

        return AsyncAnnouncementsResourceWithStreamingResponse(self._client.announcements)

    @cached_property
    def audit(self) -> audit.AsyncAuditResourceWithStreamingResponse:
        from .resources.audit import AsyncAuditResourceWithStreamingResponse

        return AsyncAuditResourceWithStreamingResponse(self._client.audit)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithStreamingResponse:
        from .resources.billing import AsyncBillingResourceWithStreamingResponse

        return AsyncBillingResourceWithStreamingResponse(self._client.billing)

    @cached_property
    def bootstrap(self) -> bootstrap.AsyncBootstrapResourceWithStreamingResponse:
        from .resources.bootstrap import AsyncBootstrapResourceWithStreamingResponse

        return AsyncBootstrapResourceWithStreamingResponse(self._client.bootstrap)

    @cached_property
    def buckets(self) -> buckets.AsyncBucketsResourceWithStreamingResponse:
        from .resources.buckets import AsyncBucketsResourceWithStreamingResponse

        return AsyncBucketsResourceWithStreamingResponse(self._client.buckets)

    @cached_property
    def cms(self) -> cms.AsyncCmsResourceWithStreamingResponse:
        from .resources.cms import AsyncCmsResourceWithStreamingResponse

        return AsyncCmsResourceWithStreamingResponse(self._client.cms)

    @cached_property
    def contact(self) -> contact.AsyncContactResourceWithStreamingResponse:
        from .resources.contact import AsyncContactResourceWithStreamingResponse

        return AsyncContactResourceWithStreamingResponse(self._client.contact)

    @cached_property
    def credits(self) -> credits.AsyncCreditsResourceWithStreamingResponse:
        from .resources.credits import AsyncCreditsResourceWithStreamingResponse

        return AsyncCreditsResourceWithStreamingResponse(self._client.credits)

    @cached_property
    def database(self) -> database.AsyncDatabaseResourceWithStreamingResponse:
        from .resources.database import AsyncDatabaseResourceWithStreamingResponse

        return AsyncDatabaseResourceWithStreamingResponse(self._client.database)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithStreamingResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithStreamingResponse

        return AsyncDeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def docs(self) -> docs.AsyncDocsResourceWithStreamingResponse:
        from .resources.docs import AsyncDocsResourceWithStreamingResponse

        return AsyncDocsResourceWithStreamingResponse(self._client.docs)

    @cached_property
    def enterprise(self) -> enterprise.AsyncEnterpriseResourceWithStreamingResponse:
        from .resources.enterprise import AsyncEnterpriseResourceWithStreamingResponse

        return AsyncEnterpriseResourceWithStreamingResponse(self._client.enterprise)

    @cached_property
    def entitlements(self) -> entitlements.AsyncEntitlementsResourceWithStreamingResponse:
        from .resources.entitlements import AsyncEntitlementsResourceWithStreamingResponse

        return AsyncEntitlementsResourceWithStreamingResponse(self._client.entitlements)

    @cached_property
    def functions(self) -> functions.AsyncFunctionsResourceWithStreamingResponse:
        from .resources.functions import AsyncFunctionsResourceWithStreamingResponse

        return AsyncFunctionsResourceWithStreamingResponse(self._client.functions)

    @cached_property
    def generated(self) -> generated.AsyncGeneratedResourceWithStreamingResponse:
        from .resources.generated import AsyncGeneratedResourceWithStreamingResponse

        return AsyncGeneratedResourceWithStreamingResponse(self._client.generated)

    @cached_property
    def github(self) -> github.AsyncGitHubResourceWithStreamingResponse:
        from .resources.github import AsyncGitHubResourceWithStreamingResponse

        return AsyncGitHubResourceWithStreamingResponse(self._client.github)

    @cached_property
    def incidents(self) -> incidents.AsyncIncidentsResourceWithStreamingResponse:
        from .resources.incidents import AsyncIncidentsResourceWithStreamingResponse

        return AsyncIncidentsResourceWithStreamingResponse(self._client.incidents)

    @cached_property
    def infrastructure(self) -> infrastructure.AsyncInfrastructureResourceWithStreamingResponse:
        from .resources.infrastructure import AsyncInfrastructureResourceWithStreamingResponse

        return AsyncInfrastructureResourceWithStreamingResponse(self._client.infrastructure)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def jobs(self) -> jobs.AsyncJobsResourceWithStreamingResponse:
        from .resources.jobs import AsyncJobsResourceWithStreamingResponse

        return AsyncJobsResourceWithStreamingResponse(self._client.jobs)

    @cached_property
    def logs(self) -> logs.AsyncLogsResourceWithStreamingResponse:
        from .resources.logs import AsyncLogsResourceWithStreamingResponse

        return AsyncLogsResourceWithStreamingResponse(self._client.logs)

    @cached_property
    def maintenance(self) -> maintenance.AsyncMaintenanceResourceWithStreamingResponse:
        from .resources.maintenance import AsyncMaintenanceResourceWithStreamingResponse

        return AsyncMaintenanceResourceWithStreamingResponse(self._client.maintenance)

    @cached_property
    def metrics(self) -> metrics.AsyncMetricsResourceWithStreamingResponse:
        from .resources.metrics import AsyncMetricsResourceWithStreamingResponse

        return AsyncMetricsResourceWithStreamingResponse(self._client.metrics)

    @cached_property
    def mongodb(self) -> mongodb.AsyncMongoDBResourceWithStreamingResponse:
        from .resources.mongodb import AsyncMongoDBResourceWithStreamingResponse

        return AsyncMongoDBResourceWithStreamingResponse(self._client.mongodb)

    @cached_property
    def oauth(self) -> oauth.AsyncOAuthResourceWithStreamingResponse:
        from .resources.oauth import AsyncOAuthResourceWithStreamingResponse

        return AsyncOAuthResourceWithStreamingResponse(self._client.oauth)

    @cached_property
    def onboarding(self) -> onboarding.AsyncOnboardingResourceWithStreamingResponse:
        from .resources.onboarding import AsyncOnboardingResourceWithStreamingResponse

        return AsyncOnboardingResourceWithStreamingResponse(self._client.onboarding)

    @cached_property
    def openapi(self) -> openapi.AsyncOpenAPIResourceWithStreamingResponse:
        from .resources.openapi import AsyncOpenAPIResourceWithStreamingResponse

        return AsyncOpenAPIResourceWithStreamingResponse(self._client.openapi)

    @cached_property
    def orgs(self) -> orgs.AsyncOrgsResourceWithStreamingResponse:
        from .resources.orgs import AsyncOrgsResourceWithStreamingResponse

        return AsyncOrgsResourceWithStreamingResponse(self._client.orgs)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithStreamingResponse:
        from .resources.plans import AsyncPlansResourceWithStreamingResponse

        return AsyncPlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def pricing(self) -> pricing.AsyncPricingResourceWithStreamingResponse:
        from .resources.pricing import AsyncPricingResourceWithStreamingResponse

        return AsyncPricingResourceWithStreamingResponse(self._client.pricing)

    @cached_property
    def projects(self) -> projects.AsyncProjectsResourceWithStreamingResponse:
        from .resources.projects import AsyncProjectsResourceWithStreamingResponse

        return AsyncProjectsResourceWithStreamingResponse(self._client.projects)

    @cached_property
    def quickstart(self) -> quickstart.AsyncQuickstartResourceWithStreamingResponse:
        from .resources.quickstart import AsyncQuickstartResourceWithStreamingResponse

        return AsyncQuickstartResourceWithStreamingResponse(self._client.quickstart)

    @cached_property
    def realtime(self) -> realtime.AsyncRealtimeResourceWithStreamingResponse:
        from .resources.realtime import AsyncRealtimeResourceWithStreamingResponse

        return AsyncRealtimeResourceWithStreamingResponse(self._client.realtime)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithStreamingResponse:
        from .resources.refunds import AsyncRefundsResourceWithStreamingResponse

        return AsyncRefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def regions(self) -> regions.AsyncRegionsResourceWithStreamingResponse:
        from .resources.regions import AsyncRegionsResourceWithStreamingResponse

        return AsyncRegionsResourceWithStreamingResponse(self._client.regions)

    @cached_property
    def rls(self) -> rls.AsyncRlsResourceWithStreamingResponse:
        from .resources.rls import AsyncRlsResourceWithStreamingResponse

        return AsyncRlsResourceWithStreamingResponse(self._client.rls)

    @cached_property
    def schema_engine(self) -> schema_engine.AsyncSchemaEngineResourceWithStreamingResponse:
        from .resources.schema_engine import AsyncSchemaEngineResourceWithStreamingResponse

        return AsyncSchemaEngineResourceWithStreamingResponse(self._client.schema_engine)

    @cached_property
    def schemas(self) -> schemas.AsyncSchemasResourceWithStreamingResponse:
        from .resources.schemas import AsyncSchemasResourceWithStreamingResponse

        return AsyncSchemasResourceWithStreamingResponse(self._client.schemas)

    @cached_property
    def sdk(self) -> sdk.AsyncSDKResourceWithStreamingResponse:
        from .resources.sdk import AsyncSDKResourceWithStreamingResponse

        return AsyncSDKResourceWithStreamingResponse(self._client.sdk)

    @cached_property
    def security(self) -> security.AsyncSecurityResourceWithStreamingResponse:
        from .resources.security import AsyncSecurityResourceWithStreamingResponse

        return AsyncSecurityResourceWithStreamingResponse(self._client.security)

    @cached_property
    def sso(self) -> sso.AsyncSSOResourceWithStreamingResponse:
        from .resources.sso import AsyncSSOResourceWithStreamingResponse

        return AsyncSSOResourceWithStreamingResponse(self._client.sso)

    @cached_property
    def status(self) -> status.AsyncStatusResourceWithStreamingResponse:
        from .resources.status import AsyncStatusResourceWithStreamingResponse

        return AsyncStatusResourceWithStreamingResponse(self._client.status)

    @cached_property
    def storage(self) -> storage.AsyncStorageResourceWithStreamingResponse:
        from .resources.storage import AsyncStorageResourceWithStreamingResponse

        return AsyncStorageResourceWithStreamingResponse(self._client.storage)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def v1(self) -> v1.AsyncV1ResourceWithStreamingResponse:
        from .resources.v1 import AsyncV1ResourceWithStreamingResponse

        return AsyncV1ResourceWithStreamingResponse(self._client.v1)


Client = Vaif

AsyncClient = AsyncVaif
