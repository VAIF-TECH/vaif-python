# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rate import (
    RateResource,
    AsyncRateResource,
    RateResourceWithRawResponse,
    AsyncRateResourceWithRawResponse,
    RateResourceWithStreamingResponse,
    AsyncRateResourceWithStreamingResponse,
)
from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from .execute import (
    ExecuteResource,
    AsyncExecuteResource,
    ExecuteResourceWithRawResponse,
    AsyncExecuteResourceWithRawResponse,
    ExecuteResourceWithStreamingResponse,
    AsyncExecuteResourceWithStreamingResponse,
)
from .git.git import (
    GitResource,
    AsyncGitResource,
    GitResourceWithRawResponse,
    AsyncGitResourceWithRawResponse,
    GitResourceWithStreamingResponse,
    AsyncGitResourceWithStreamingResponse,
)
from .job.job import (
    JobResource,
    AsyncJobResource,
    JobResourceWithRawResponse,
    AsyncJobResourceWithRawResponse,
    JobResourceWithStreamingResponse,
    AsyncJobResourceWithStreamingResponse,
)
from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from .chat.chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .usage_org import (
    UsageOrgResource,
    AsyncUsageOrgResource,
    UsageOrgResourceWithRawResponse,
    AsyncUsageOrgResourceWithRawResponse,
    UsageOrgResourceWithStreamingResponse,
    AsyncUsageOrgResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .credit_status import (
    CreditStatusResource,
    AsyncCreditStatusResource,
    CreditStatusResourceWithRawResponse,
    AsyncCreditStatusResourceWithRawResponse,
    CreditStatusResourceWithStreamingResponse,
    AsyncCreditStatusResourceWithStreamingResponse,
)
from .deploy.deploy import (
    DeployResource,
    AsyncDeployResource,
    DeployResourceWithRawResponse,
    AsyncDeployResourceWithRawResponse,
    DeployResourceWithStreamingResponse,
    AsyncDeployResourceWithStreamingResponse,
)
from .editor.editor import (
    EditorResource,
    AsyncEditorResource,
    EditorResourceWithRawResponse,
    AsyncEditorResourceWithRawResponse,
    EditorResourceWithStreamingResponse,
    AsyncEditorResourceWithStreamingResponse,
)
from .export.export import (
    ExportResource,
    AsyncExportResource,
    ExportResourceWithRawResponse,
    AsyncExportResourceWithRawResponse,
    ExportResourceWithStreamingResponse,
    AsyncExportResourceWithStreamingResponse,
)
from .context_summary import (
    ContextSummaryResource,
    AsyncContextSummaryResource,
    ContextSummaryResourceWithRawResponse,
    AsyncContextSummaryResourceWithRawResponse,
    ContextSummaryResourceWithStreamingResponse,
    AsyncContextSummaryResourceWithStreamingResponse,
)
from .metrics.metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from .training_consent import (
    TrainingConsentResource,
    AsyncTrainingConsentResource,
    TrainingConsentResourceWithRawResponse,
    AsyncTrainingConsentResourceWithRawResponse,
    TrainingConsentResourceWithStreamingResponse,
    AsyncTrainingConsentResourceWithStreamingResponse,
)
from .manifest.manifest import (
    ManifestResource,
    AsyncManifestResource,
    ManifestResourceWithRawResponse,
    AsyncManifestResourceWithRawResponse,
    ManifestResourceWithStreamingResponse,
    AsyncManifestResourceWithStreamingResponse,
)
from .memories.memories import (
    MemoriesResource,
    AsyncMemoriesResource,
    MemoriesResourceWithRawResponse,
    AsyncMemoriesResourceWithRawResponse,
    MemoriesResourceWithStreamingResponse,
    AsyncMemoriesResourceWithStreamingResponse,
)
from .versions.versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from .executions.executions import (
    ExecutionsResource,
    AsyncExecutionsResource,
    ExecutionsResourceWithRawResponse,
    AsyncExecutionsResourceWithRawResponse,
    ExecutionsResourceWithStreamingResponse,
    AsyncExecutionsResourceWithStreamingResponse,
)
from .generation.generation import (
    GenerationResource,
    AsyncGenerationResource,
    GenerationResourceWithRawResponse,
    AsyncGenerationResourceWithRawResponse,
    GenerationResourceWithStreamingResponse,
    AsyncGenerationResourceWithStreamingResponse,
)

__all__ = ["CopilotResource", "AsyncCopilotResource"]


class CopilotResource(SyncAPIResource):
    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def context_summary(self) -> ContextSummaryResource:
        return ContextSummaryResource(self._client)

    @cached_property
    def credit_status(self) -> CreditStatusResource:
        return CreditStatusResource(self._client)

    @cached_property
    def deploy(self) -> DeployResource:
        return DeployResource(self._client)

    @cached_property
    def editor(self) -> EditorResource:
        return EditorResource(self._client)

    @cached_property
    def execute(self) -> ExecuteResource:
        return ExecuteResource(self._client)

    @cached_property
    def executions(self) -> ExecutionsResource:
        return ExecutionsResource(self._client)

    @cached_property
    def export(self) -> ExportResource:
        return ExportResource(self._client)

    @cached_property
    def feedback(self) -> FeedbackResource:
        return FeedbackResource(self._client)

    @cached_property
    def generation(self) -> GenerationResource:
        return GenerationResource(self._client)

    @cached_property
    def git(self) -> GitResource:
        return GitResource(self._client)

    @cached_property
    def job(self) -> JobResource:
        return JobResource(self._client)

    @cached_property
    def manifest(self) -> ManifestResource:
        return ManifestResource(self._client)

    @cached_property
    def memories(self) -> MemoriesResource:
        return MemoriesResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def rate(self) -> RateResource:
        return RateResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def training_consent(self) -> TrainingConsentResource:
        return TrainingConsentResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def usage_org(self) -> UsageOrgResource:
        return UsageOrgResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CopilotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return CopilotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CopilotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return CopilotResourceWithStreamingResponse(self)


class AsyncCopilotResource(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def context_summary(self) -> AsyncContextSummaryResource:
        return AsyncContextSummaryResource(self._client)

    @cached_property
    def credit_status(self) -> AsyncCreditStatusResource:
        return AsyncCreditStatusResource(self._client)

    @cached_property
    def deploy(self) -> AsyncDeployResource:
        return AsyncDeployResource(self._client)

    @cached_property
    def editor(self) -> AsyncEditorResource:
        return AsyncEditorResource(self._client)

    @cached_property
    def execute(self) -> AsyncExecuteResource:
        return AsyncExecuteResource(self._client)

    @cached_property
    def executions(self) -> AsyncExecutionsResource:
        return AsyncExecutionsResource(self._client)

    @cached_property
    def export(self) -> AsyncExportResource:
        return AsyncExportResource(self._client)

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        return AsyncFeedbackResource(self._client)

    @cached_property
    def generation(self) -> AsyncGenerationResource:
        return AsyncGenerationResource(self._client)

    @cached_property
    def git(self) -> AsyncGitResource:
        return AsyncGitResource(self._client)

    @cached_property
    def job(self) -> AsyncJobResource:
        return AsyncJobResource(self._client)

    @cached_property
    def manifest(self) -> AsyncManifestResource:
        return AsyncManifestResource(self._client)

    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        return AsyncMemoriesResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def rate(self) -> AsyncRateResource:
        return AsyncRateResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def training_consent(self) -> AsyncTrainingConsentResource:
        return AsyncTrainingConsentResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def usage_org(self) -> AsyncUsageOrgResource:
        return AsyncUsageOrgResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCopilotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCopilotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCopilotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncCopilotResourceWithStreamingResponse(self)


class CopilotResourceWithRawResponse:
    def __init__(self, copilot: CopilotResource) -> None:
        self._copilot = copilot

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._copilot.chat)

    @cached_property
    def context_summary(self) -> ContextSummaryResourceWithRawResponse:
        return ContextSummaryResourceWithRawResponse(self._copilot.context_summary)

    @cached_property
    def credit_status(self) -> CreditStatusResourceWithRawResponse:
        return CreditStatusResourceWithRawResponse(self._copilot.credit_status)

    @cached_property
    def deploy(self) -> DeployResourceWithRawResponse:
        return DeployResourceWithRawResponse(self._copilot.deploy)

    @cached_property
    def editor(self) -> EditorResourceWithRawResponse:
        return EditorResourceWithRawResponse(self._copilot.editor)

    @cached_property
    def execute(self) -> ExecuteResourceWithRawResponse:
        return ExecuteResourceWithRawResponse(self._copilot.execute)

    @cached_property
    def executions(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self._copilot.executions)

    @cached_property
    def export(self) -> ExportResourceWithRawResponse:
        return ExportResourceWithRawResponse(self._copilot.export)

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self._copilot.feedback)

    @cached_property
    def generation(self) -> GenerationResourceWithRawResponse:
        return GenerationResourceWithRawResponse(self._copilot.generation)

    @cached_property
    def git(self) -> GitResourceWithRawResponse:
        return GitResourceWithRawResponse(self._copilot.git)

    @cached_property
    def job(self) -> JobResourceWithRawResponse:
        return JobResourceWithRawResponse(self._copilot.job)

    @cached_property
    def manifest(self) -> ManifestResourceWithRawResponse:
        return ManifestResourceWithRawResponse(self._copilot.manifest)

    @cached_property
    def memories(self) -> MemoriesResourceWithRawResponse:
        return MemoriesResourceWithRawResponse(self._copilot.memories)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._copilot.metrics)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._copilot.models)

    @cached_property
    def rate(self) -> RateResourceWithRawResponse:
        return RateResourceWithRawResponse(self._copilot.rate)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._copilot.sessions)

    @cached_property
    def training_consent(self) -> TrainingConsentResourceWithRawResponse:
        return TrainingConsentResourceWithRawResponse(self._copilot.training_consent)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._copilot.usage)

    @cached_property
    def usage_org(self) -> UsageOrgResourceWithRawResponse:
        return UsageOrgResourceWithRawResponse(self._copilot.usage_org)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._copilot.versions)


class AsyncCopilotResourceWithRawResponse:
    def __init__(self, copilot: AsyncCopilotResource) -> None:
        self._copilot = copilot

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._copilot.chat)

    @cached_property
    def context_summary(self) -> AsyncContextSummaryResourceWithRawResponse:
        return AsyncContextSummaryResourceWithRawResponse(self._copilot.context_summary)

    @cached_property
    def credit_status(self) -> AsyncCreditStatusResourceWithRawResponse:
        return AsyncCreditStatusResourceWithRawResponse(self._copilot.credit_status)

    @cached_property
    def deploy(self) -> AsyncDeployResourceWithRawResponse:
        return AsyncDeployResourceWithRawResponse(self._copilot.deploy)

    @cached_property
    def editor(self) -> AsyncEditorResourceWithRawResponse:
        return AsyncEditorResourceWithRawResponse(self._copilot.editor)

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithRawResponse:
        return AsyncExecuteResourceWithRawResponse(self._copilot.execute)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self._copilot.executions)

    @cached_property
    def export(self) -> AsyncExportResourceWithRawResponse:
        return AsyncExportResourceWithRawResponse(self._copilot.export)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self._copilot.feedback)

    @cached_property
    def generation(self) -> AsyncGenerationResourceWithRawResponse:
        return AsyncGenerationResourceWithRawResponse(self._copilot.generation)

    @cached_property
    def git(self) -> AsyncGitResourceWithRawResponse:
        return AsyncGitResourceWithRawResponse(self._copilot.git)

    @cached_property
    def job(self) -> AsyncJobResourceWithRawResponse:
        return AsyncJobResourceWithRawResponse(self._copilot.job)

    @cached_property
    def manifest(self) -> AsyncManifestResourceWithRawResponse:
        return AsyncManifestResourceWithRawResponse(self._copilot.manifest)

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithRawResponse:
        return AsyncMemoriesResourceWithRawResponse(self._copilot.memories)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._copilot.metrics)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._copilot.models)

    @cached_property
    def rate(self) -> AsyncRateResourceWithRawResponse:
        return AsyncRateResourceWithRawResponse(self._copilot.rate)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._copilot.sessions)

    @cached_property
    def training_consent(self) -> AsyncTrainingConsentResourceWithRawResponse:
        return AsyncTrainingConsentResourceWithRawResponse(self._copilot.training_consent)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._copilot.usage)

    @cached_property
    def usage_org(self) -> AsyncUsageOrgResourceWithRawResponse:
        return AsyncUsageOrgResourceWithRawResponse(self._copilot.usage_org)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._copilot.versions)


class CopilotResourceWithStreamingResponse:
    def __init__(self, copilot: CopilotResource) -> None:
        self._copilot = copilot

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._copilot.chat)

    @cached_property
    def context_summary(self) -> ContextSummaryResourceWithStreamingResponse:
        return ContextSummaryResourceWithStreamingResponse(self._copilot.context_summary)

    @cached_property
    def credit_status(self) -> CreditStatusResourceWithStreamingResponse:
        return CreditStatusResourceWithStreamingResponse(self._copilot.credit_status)

    @cached_property
    def deploy(self) -> DeployResourceWithStreamingResponse:
        return DeployResourceWithStreamingResponse(self._copilot.deploy)

    @cached_property
    def editor(self) -> EditorResourceWithStreamingResponse:
        return EditorResourceWithStreamingResponse(self._copilot.editor)

    @cached_property
    def execute(self) -> ExecuteResourceWithStreamingResponse:
        return ExecuteResourceWithStreamingResponse(self._copilot.execute)

    @cached_property
    def executions(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self._copilot.executions)

    @cached_property
    def export(self) -> ExportResourceWithStreamingResponse:
        return ExportResourceWithStreamingResponse(self._copilot.export)

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self._copilot.feedback)

    @cached_property
    def generation(self) -> GenerationResourceWithStreamingResponse:
        return GenerationResourceWithStreamingResponse(self._copilot.generation)

    @cached_property
    def git(self) -> GitResourceWithStreamingResponse:
        return GitResourceWithStreamingResponse(self._copilot.git)

    @cached_property
    def job(self) -> JobResourceWithStreamingResponse:
        return JobResourceWithStreamingResponse(self._copilot.job)

    @cached_property
    def manifest(self) -> ManifestResourceWithStreamingResponse:
        return ManifestResourceWithStreamingResponse(self._copilot.manifest)

    @cached_property
    def memories(self) -> MemoriesResourceWithStreamingResponse:
        return MemoriesResourceWithStreamingResponse(self._copilot.memories)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._copilot.metrics)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._copilot.models)

    @cached_property
    def rate(self) -> RateResourceWithStreamingResponse:
        return RateResourceWithStreamingResponse(self._copilot.rate)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._copilot.sessions)

    @cached_property
    def training_consent(self) -> TrainingConsentResourceWithStreamingResponse:
        return TrainingConsentResourceWithStreamingResponse(self._copilot.training_consent)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._copilot.usage)

    @cached_property
    def usage_org(self) -> UsageOrgResourceWithStreamingResponse:
        return UsageOrgResourceWithStreamingResponse(self._copilot.usage_org)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._copilot.versions)


class AsyncCopilotResourceWithStreamingResponse:
    def __init__(self, copilot: AsyncCopilotResource) -> None:
        self._copilot = copilot

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._copilot.chat)

    @cached_property
    def context_summary(self) -> AsyncContextSummaryResourceWithStreamingResponse:
        return AsyncContextSummaryResourceWithStreamingResponse(self._copilot.context_summary)

    @cached_property
    def credit_status(self) -> AsyncCreditStatusResourceWithStreamingResponse:
        return AsyncCreditStatusResourceWithStreamingResponse(self._copilot.credit_status)

    @cached_property
    def deploy(self) -> AsyncDeployResourceWithStreamingResponse:
        return AsyncDeployResourceWithStreamingResponse(self._copilot.deploy)

    @cached_property
    def editor(self) -> AsyncEditorResourceWithStreamingResponse:
        return AsyncEditorResourceWithStreamingResponse(self._copilot.editor)

    @cached_property
    def execute(self) -> AsyncExecuteResourceWithStreamingResponse:
        return AsyncExecuteResourceWithStreamingResponse(self._copilot.execute)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._copilot.executions)

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self._copilot.export)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self._copilot.feedback)

    @cached_property
    def generation(self) -> AsyncGenerationResourceWithStreamingResponse:
        return AsyncGenerationResourceWithStreamingResponse(self._copilot.generation)

    @cached_property
    def git(self) -> AsyncGitResourceWithStreamingResponse:
        return AsyncGitResourceWithStreamingResponse(self._copilot.git)

    @cached_property
    def job(self) -> AsyncJobResourceWithStreamingResponse:
        return AsyncJobResourceWithStreamingResponse(self._copilot.job)

    @cached_property
    def manifest(self) -> AsyncManifestResourceWithStreamingResponse:
        return AsyncManifestResourceWithStreamingResponse(self._copilot.manifest)

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithStreamingResponse:
        return AsyncMemoriesResourceWithStreamingResponse(self._copilot.memories)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._copilot.metrics)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._copilot.models)

    @cached_property
    def rate(self) -> AsyncRateResourceWithStreamingResponse:
        return AsyncRateResourceWithStreamingResponse(self._copilot.rate)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._copilot.sessions)

    @cached_property
    def training_consent(self) -> AsyncTrainingConsentResourceWithStreamingResponse:
        return AsyncTrainingConsentResourceWithStreamingResponse(self._copilot.training_consent)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._copilot.usage)

    @cached_property
    def usage_org(self) -> AsyncUsageOrgResourceWithStreamingResponse:
        return AsyncUsageOrgResourceWithStreamingResponse(self._copilot.usage_org)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._copilot.versions)
