# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ChatCreateParams", "Attachment", "GenerationOptions", "PinnedContext"]


class ChatCreateParams(TypedDict, total=False):
    message: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    attachments: Iterable[Attachment]

    generation_options: Annotated[GenerationOptions, PropertyInfo(alias="generationOptions")]

    generation_types: Annotated[
        List[Literal["schema", "storage", "functions", "backend", "fullstack"]], PropertyInfo(alias="generationTypes")
    ]

    model_id: Annotated[str, PropertyInfo(alias="modelId")]

    pinned_context: Annotated[PinnedContext, PropertyInfo(alias="pinnedContext")]

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]

    stream: bool


class Attachment(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["schema", "function", "file", "context"]]

    name: str


class GenerationOptions(TypedDict, total=False):
    api_style: Annotated[Literal["rest", "graphql", "trpc"], PropertyInfo(alias="apiStyle")]

    architecture: Literal["mvc", "clean", "hexagonal", "feature-sliced"]

    audit_logs: Annotated[bool, PropertyInfo(alias="auditLogs")]

    auth_method: Annotated[Literal["vaif", "jwt", "session", "oauth", "sso"], PropertyInfo(alias="authMethod")]

    containerization: Literal["docker", "none"]

    database: Literal["vaif", "postgresql", "mysql", "mongodb"]

    db_migrations: Annotated[bool, PropertyInfo(alias="dbMigrations")]

    deploy_target: Annotated[
        Literal["railway", "fly-io", "render", "cloud-run", "aws-ecs"], PropertyInfo(alias="deployTarget")
    ]

    email_verification: Annotated[bool, PropertyInfo(alias="emailVerification")]

    feature_flags: Annotated[bool, PropertyInfo(alias="featureFlags")]

    framework: str

    git_hooks: Annotated[bool, PropertyInfo(alias="gitHooks")]

    health_checks: Annotated[bool, PropertyInfo(alias="healthChecks")]

    include_api_collection: Annotated[bool, PropertyInfo(alias="includeApiCollection")]

    include_sample_data: Annotated[bool, PropertyInfo(alias="includeSampleData")]

    include_sdk_client: Annotated[bool, PropertyInfo(alias="includeSdkClient")]

    language: Literal["typescript", "python", "go"]

    mfa: bool

    mode: Literal["opinionated", "minimal", "custom"]

    multi_tenant: Annotated[Literal["single", "org-based", "project-based"], PropertyInfo(alias="multiTenant")]

    output_depth: Annotated[Literal["minimal", "standard", "enterprise"], PropertyInfo(alias="outputDepth")]

    rate_limiting: Annotated[bool, PropertyInfo(alias="rateLimiting")]

    rbac: Literal["off", "basic", "advanced"]

    realtime: Literal["websockets", "sse", "pubsub", "none"]

    scope: Literal["schema-only", "functions-only", "full-backend"]

    security_headers: Annotated[bool, PropertyInfo(alias="securityHeaders")]

    storage: Literal["vaif", "s3", "gcs", "local"]

    tests: List[Literal["unit", "integration", "e2e"]]


class PinnedContext(TypedDict, total=False):
    bucket_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="bucketIds")]

    function_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="functionIds")]

    table_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="tableIds")]
