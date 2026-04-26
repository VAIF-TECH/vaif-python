# Activation

## Org

Methods:

- <code title="get /activation/org/{orgId}">client.activation.org.<a href="./src/vaif_client/resources/activation/org.py">retrieve</a>(org_id) -> None</code>

# AI

## Copilot

### Chat

Methods:

- <code title="post /ai/copilot/chat">client.ai.copilot.chat.<a href="./src/vaif_client/resources/ai/copilot/chat/chat.py">create</a>(\*\*<a href="src/vaif_client/types/ai/copilot/chat_create_params.py">params</a>) -> object</code>

#### Stream

Methods:

- <code title="post /ai/copilot/chat/stream">client.ai.copilot.chat.stream.<a href="./src/vaif_client/resources/ai/copilot/chat/stream.py">create</a>() -> None</code>

### ContextSummary

Methods:

- <code title="get /ai/copilot/context-summary/{projectId}">client.ai.copilot.context_summary.<a href="./src/vaif_client/resources/ai/copilot/context_summary.py">retrieve</a>(project_id) -> None</code>

### CreditStatus

Methods:

- <code title="get /ai/copilot/credit-status/{projectId}">client.ai.copilot.credit_status.<a href="./src/vaif_client/resources/ai/copilot/credit_status.py">retrieve</a>(project_id) -> None</code>

### Deploy

Methods:

- <code title="post /ai/copilot/deploy">client.ai.copilot.deploy.<a href="./src/vaif_client/resources/ai/copilot/deploy/deploy.py">create</a>(\*\*<a href="src/vaif_client/types/ai/copilot/deploy_create_params.py">params</a>) -> None</code>
- <code title="get /ai/copilot/deploy/{deployId}">client.ai.copilot.deploy.<a href="./src/vaif_client/resources/ai/copilot/deploy/deploy.py">retrieve</a>(deploy_id) -> object</code>

#### History

Types:

```python
from vaif_client.types.ai.copilot.deploy import HistoryRetrieveResponse
```

Methods:

- <code title="get /ai/copilot/deploy/history/{projectId}">client.ai.copilot.deploy.history.<a href="./src/vaif_client/resources/ai/copilot/deploy/history.py">retrieve</a>(project_id, \*\*<a href="src/vaif_client/types/ai/copilot/deploy/history_retrieve_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/deploy/history_retrieve_response.py">HistoryRetrieveResponse</a></code>

#### Rollback

Methods:

- <code title="post /ai/copilot/deploy/{deployId}/rollback">client.ai.copilot.deploy.rollback.<a href="./src/vaif_client/resources/ai/copilot/deploy/rollback.py">rollback</a>(deploy_id) -> None</code>

### Editor

#### Chat

Methods:

- <code title="post /ai/copilot/editor/chat">client.ai.copilot.editor.chat.<a href="./src/vaif_client/resources/ai/copilot/editor/chat.py">create</a>(\*\*<a href="src/vaif_client/types/ai/copilot/editor/chat_create_params.py">params</a>) -> None</code>

### Execute

Types:

```python
from vaif_client.types.ai.copilot import ExecuteCreateResponse
```

Methods:

- <code title="post /ai/copilot/execute">client.ai.copilot.execute.<a href="./src/vaif_client/resources/ai/copilot/execute.py">create</a>(\*\*<a href="src/vaif_client/types/ai/copilot/execute_create_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/execute_create_response.py">ExecuteCreateResponse</a></code>

### Executions

Methods:

- <code title="get /ai/copilot/execution/{executionId}">client.ai.copilot.executions.<a href="./src/vaif_client/resources/ai/copilot/executions/executions.py">retrieve</a>(execution_id) -> None</code>
- <code title="get /ai/copilot/executions/{sessionId}">client.ai.copilot.executions.<a href="./src/vaif_client/resources/ai/copilot/executions/executions.py">retrieve2</a>(session_id) -> None</code>

#### Pause

Methods:

- <code title="post /ai/copilot/execution/{executionId}/pause">client.ai.copilot.executions.pause.<a href="./src/vaif_client/resources/ai/copilot/executions/pause.py">pause</a>(execution_id) -> None</code>

#### Resume

Types:

```python
from vaif_client.types.ai.copilot.executions import ResumeResumeResponse
```

Methods:

- <code title="post /ai/copilot/execution/{executionId}/resume">client.ai.copilot.executions.resume.<a href="./src/vaif_client/resources/ai/copilot/executions/resume.py">resume</a>(execution_id, \*\*<a href="src/vaif_client/types/ai/copilot/executions/resume_resume_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/executions/resume_resume_response.py">ResumeResumeResponse</a></code>

#### Rollback

Types:

```python
from vaif_client.types.ai.copilot.executions import RollbackRollbackResponse
```

Methods:

- <code title="post /ai/copilot/execution/{executionId}/rollback">client.ai.copilot.executions.rollback.<a href="./src/vaif_client/resources/ai/copilot/executions/rollback.py">rollback</a>(execution_id, \*\*<a href="src/vaif_client/types/ai/copilot/executions/rollback_rollback_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/executions/rollback_rollback_response.py">RollbackRollbackResponse</a></code>

### Export

Methods:

- <code title="post /ai/copilot/export/{versionId}">client.ai.copilot.export.<a href="./src/vaif_client/resources/ai/copilot/export/export.py">create</a>(version_id) -> None</code>

#### Docker

Methods:

- <code title="post /ai/copilot/export/docker">client.ai.copilot.export.docker.<a href="./src/vaif_client/resources/ai/copilot/export/docker.py">create</a>() -> None</code>

#### GitHub

Methods:

- <code title="post /ai/copilot/export/github">client.ai.copilot.export.github.<a href="./src/vaif_client/resources/ai/copilot/export/github.py">create</a>() -> None</code>

#### Terraform

##### Aws

Methods:

- <code title="post /ai/copilot/export/terraform/aws">client.ai.copilot.export.terraform.aws.<a href="./src/vaif_client/resources/ai/copilot/export/terraform/aws.py">create</a>() -> None</code>

##### Gcp

Methods:

- <code title="post /ai/copilot/export/terraform/gcp">client.ai.copilot.export.terraform.gcp.<a href="./src/vaif_client/resources/ai/copilot/export/terraform/gcp.py">create</a>() -> None</code>

#### Zip

Methods:

- <code title="post /ai/copilot/export/zip">client.ai.copilot.export.zip.<a href="./src/vaif_client/resources/ai/copilot/export/zip.py">create</a>() -> None</code>

### Feedback

Types:

```python
from vaif_client.types.ai.copilot import FeedbackCreateResponse
```

Methods:

- <code title="post /ai/copilot/feedback">client.ai.copilot.feedback.<a href="./src/vaif_client/resources/ai/copilot/feedback.py">create</a>(\*\*<a href="src/vaif_client/types/ai/copilot/feedback_create_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/feedback_create_response.py">FeedbackCreateResponse</a></code>

### Generation

#### Cancel

Methods:

- <code title="post /ai/copilot/generation/{manifestId}/cancel">client.ai.copilot.generation.cancel.<a href="./src/vaif_client/resources/ai/copilot/generation/cancel.py">cancel</a>(manifest_id) -> None</code>

#### Resume

Methods:

- <code title="post /ai/copilot/generation/resume">client.ai.copilot.generation.resume.<a href="./src/vaif_client/resources/ai/copilot/generation/resume.py">create</a>() -> None</code>

### Git

#### Branches

Methods:

- <code title="post /ai/copilot/git/branch">client.ai.copilot.git.branches.<a href="./src/vaif_client/resources/ai/copilot/git/branches.py">create</a>() -> None</code>
- <code title="get /ai/copilot/git/branches/{sessionId}">client.ai.copilot.git.branches.<a href="./src/vaif_client/resources/ai/copilot/git/branches.py">retrieve</a>(session_id) -> None</code>

#### Clone

Methods:

- <code title="post /ai/copilot/git/clone">client.ai.copilot.git.clone.<a href="./src/vaif_client/resources/ai/copilot/git/clone.py">create</a>() -> None</code>

#### Commit

Methods:

- <code title="post /ai/copilot/git/commit">client.ai.copilot.git.commit.<a href="./src/vaif_client/resources/ai/copilot/git/commit.py">create</a>() -> None</code>

#### Files

Methods:

- <code title="get /ai/copilot/git/files/{sessionId}">client.ai.copilot.git.files.<a href="./src/vaif_client/resources/ai/copilot/git/files.py">retrieve</a>(session_id) -> None</code>

#### Init

Methods:

- <code title="post /ai/copilot/git/init">client.ai.copilot.git.init.<a href="./src/vaif_client/resources/ai/copilot/git/init.py">create</a>() -> None</code>

#### Log

Methods:

- <code title="get /ai/copilot/git/log/{sessionId}">client.ai.copilot.git.log.<a href="./src/vaif_client/resources/ai/copilot/git/log.py">retrieve</a>(session_id) -> None</code>

#### Pull

Methods:

- <code title="post /ai/copilot/git/pull">client.ai.copilot.git.pull.<a href="./src/vaif_client/resources/ai/copilot/git/pull.py">create</a>() -> None</code>

#### Push

Methods:

- <code title="post /ai/copilot/git/push">client.ai.copilot.git.push.<a href="./src/vaif_client/resources/ai/copilot/git/push.py">create</a>() -> None</code>

#### Status

Methods:

- <code title="get /ai/copilot/git/status/{sessionId}">client.ai.copilot.git.status.<a href="./src/vaif_client/resources/ai/copilot/git/status.py">retrieve</a>(session_id) -> None</code>

#### Write

Methods:

- <code title="post /ai/copilot/git/write">client.ai.copilot.git.write.<a href="./src/vaif_client/resources/ai/copilot/git/write.py">create</a>() -> None</code>

### Job

Types:

```python
from vaif_client.types.ai.copilot import JobCreateResponse
```

Methods:

- <code title="post /ai/copilot/job">client.ai.copilot.job.<a href="./src/vaif_client/resources/ai/copilot/job/job.py">create</a>(\*\*<a href="src/vaif_client/types/ai/copilot/job_create_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/job_create_response.py">JobCreateResponse</a></code>
- <code title="get /ai/copilot/job/{jobId}">client.ai.copilot.job.<a href="./src/vaif_client/resources/ai/copilot/job/job.py">retrieve</a>(job_id) -> None</code>

#### Cancel

Methods:

- <code title="post /ai/copilot/job/{jobId}/cancel">client.ai.copilot.job.cancel.<a href="./src/vaif_client/resources/ai/copilot/job/cancel.py">cancel</a>(job_id) -> None</code>

#### Events

Methods:

- <code title="get /ai/copilot/job/{jobId}/events">client.ai.copilot.job.events.<a href="./src/vaif_client/resources/ai/copilot/job/events.py">get_events</a>(job_id) -> None</code>

#### Retry

Methods:

- <code title="post /ai/copilot/job/{jobId}/retry">client.ai.copilot.job.retry.<a href="./src/vaif_client/resources/ai/copilot/job/retry.py">retry</a>(job_id) -> None</code>

### Manifest

Methods:

- <code title="get /ai/copilot/manifest/{manifestId}">client.ai.copilot.manifest.<a href="./src/vaif_client/resources/ai/copilot/manifest/manifest.py">retrieve</a>(manifest_id) -> None</code>

#### Pause

Methods:

- <code title="post /ai/copilot/manifest/{manifestId}/pause">client.ai.copilot.manifest.pause.<a href="./src/vaif_client/resources/ai/copilot/manifest/pause.py">pause</a>(manifest_id) -> None</code>

### Memories

#### Promote

Methods:

- <code title="post /ai/copilot/memories/{memoryId}/promote">client.ai.copilot.memories.promote.<a href="./src/vaif_client/resources/ai/copilot/memories/promote.py">promote</a>(memory_id) -> None</code>

### Metrics

Methods:

- <code title="get /ai/copilot/metrics/{projectId}">client.ai.copilot.metrics.<a href="./src/vaif_client/resources/ai/copilot/metrics/metrics.py">retrieve</a>(project_id) -> None</code>

#### Org

Methods:

- <code title="get /ai/copilot/metrics/org/{orgId}">client.ai.copilot.metrics.org.<a href="./src/vaif_client/resources/ai/copilot/metrics/org.py">retrieve</a>(org_id) -> None</code>

### Models

Methods:

- <code title="get /ai/copilot/models/{projectId}">client.ai.copilot.models.<a href="./src/vaif_client/resources/ai/copilot/models.py">retrieve</a>(project_id) -> None</code>

### Rate

Types:

```python
from vaif_client.types.ai.copilot import RateCreateResponse
```

Methods:

- <code title="post /ai/copilot/rate/{messageId}">client.ai.copilot.rate.<a href="./src/vaif_client/resources/ai/copilot/rate.py">create</a>(message_id, \*\*<a href="src/vaif_client/types/ai/copilot/rate_create_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/rate_create_response.py">RateCreateResponse</a></code>

### Sessions

Types:

```python
from vaif_client.types.ai.copilot import SessionUpdateResponse
```

Methods:

- <code title="get /ai/copilot/sessions/{projectId}">client.ai.copilot.sessions.<a href="./src/vaif_client/resources/ai/copilot/sessions.py">retrieve</a>(project_id) -> None</code>
- <code title="patch /ai/copilot/session/{sessionId}">client.ai.copilot.sessions.<a href="./src/vaif_client/resources/ai/copilot/sessions.py">update</a>(session_id, \*\*<a href="src/vaif_client/types/ai/copilot/session_update_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/session_update_response.py">SessionUpdateResponse</a></code>
- <code title="delete /ai/copilot/session/{sessionId}">client.ai.copilot.sessions.<a href="./src/vaif_client/resources/ai/copilot/sessions.py">delete</a>(session_id) -> None</code>
- <code title="get /ai/copilot/session/{sessionId}">client.ai.copilot.sessions.<a href="./src/vaif_client/resources/ai/copilot/sessions.py">retrieve2</a>(session_id) -> None</code>

### TrainingConsent

Types:

```python
from vaif_client.types.ai.copilot import TrainingConsentCreateResponse
```

Methods:

- <code title="post /ai/copilot/training-consent/{sessionId}">client.ai.copilot.training_consent.<a href="./src/vaif_client/resources/ai/copilot/training_consent.py">create</a>(session_id, \*\*<a href="src/vaif_client/types/ai/copilot/training_consent_create_params.py">params</a>) -> <a href="./src/vaif_client/types/ai/copilot/training_consent_create_response.py">TrainingConsentCreateResponse</a></code>

### Usage

Methods:

- <code title="get /ai/copilot/usage/{projectId}">client.ai.copilot.usage.<a href="./src/vaif_client/resources/ai/copilot/usage.py">retrieve</a>(project_id) -> None</code>

### UsageOrg

Methods:

- <code title="get /ai/copilot/usage-org/{orgId}">client.ai.copilot.usage_org.<a href="./src/vaif_client/resources/ai/copilot/usage_org.py">retrieve</a>(org_id) -> None</code>

### Versions

Methods:

- <code title="get /ai/copilot/versions/{sessionId}">client.ai.copilot.versions.<a href="./src/vaif_client/resources/ai/copilot/versions/versions.py">retrieve</a>(session_id) -> None</code>
- <code title="get /ai/copilot/version/{versionId}">client.ai.copilot.versions.<a href="./src/vaif_client/resources/ai/copilot/versions/versions.py">retrieve2</a>(version_id) -> None</code>

#### Diff

Methods:

- <code title="get /ai/copilot/version/{versionId}/diff/{compareVersionId}">client.ai.copilot.versions.diff.<a href="./src/vaif_client/resources/ai/copilot/versions/diff.py">retrieve</a>(compare_version_id, \*, version_id) -> None</code>

# AIUsage

## Org

### Breakdown

Methods:

- <code title="get /ai-usage/org/{orgId}/breakdown">client.ai_usage.org.breakdown.<a href="./src/vaif_client/resources/ai_usage/org/breakdown.py">get_breakdown</a>(org_id) -> None</code>

### ExhaustionEvents

Methods:

- <code title="get /ai-usage/org/{orgId}/exhaustion-events">client.ai_usage.org.exhaustion_events.<a href="./src/vaif_client/resources/ai_usage/org/exhaustion_events.py">get_exhaustion_events</a>(org_id) -> None</code>

### History

Methods:

- <code title="get /ai-usage/org/{orgId}/history">client.ai_usage.org.history.<a href="./src/vaif_client/resources/ai_usage/org/history.py">get_history</a>(org_id) -> None</code>

### Recent

Methods:

- <code title="get /ai-usage/org/{orgId}/recent">client.ai_usage.org.recent.<a href="./src/vaif_client/resources/ai_usage/org/recent.py">get_recent</a>(org_id) -> None</code>

### Rollups

Methods:

- <code title="get /ai-usage/org/{orgId}/rollups">client.ai_usage.org.rollups.<a href="./src/vaif_client/resources/ai_usage/org/rollups.py">get_rollups</a>(org_id) -> None</code>

### Summary

Methods:

- <code title="get /ai-usage/org/{orgId}/summary">client.ai_usage.org.summary.<a href="./src/vaif_client/resources/ai_usage/org/summary.py">get_summary</a>(org_id) -> None</code>

# AlertRules

Methods:

- <code title="put /alert-rules/{ruleId}">client.alert_rules.<a href="./src/vaif_client/resources/alert_rules/alert_rules.py">update</a>(rule_id) -> None</code>
- <code title="delete /alert-rules/{ruleId}">client.alert_rules.<a href="./src/vaif_client/resources/alert_rules/alert_rules.py">delete</a>(rule_id) -> None</code>

## Project

Methods:

- <code title="post /alert-rules/project/{projectId}">client.alert_rules.project.<a href="./src/vaif_client/resources/alert_rules/project.py">create</a>(project_id) -> None</code>
- <code title="get /alert-rules/project/{projectId}">client.alert_rules.project.<a href="./src/vaif_client/resources/alert_rules/project.py">retrieve</a>(project_id) -> None</code>

# Announcements

Methods:

- <code title="get /announcements">client.announcements.<a href="./src/vaif_client/resources/announcements.py">list</a>() -> None</code>

# Audit

## Org

Methods:

- <code title="get /audit/org/{orgId}">client.audit.org.<a href="./src/vaif_client/resources/audit/org.py">retrieve</a>(org_id) -> None</code>

## Project

Methods:

- <code title="get /audit/project/{projectId}">client.audit.project.<a href="./src/vaif_client/resources/audit/project.py">retrieve</a>(project_id) -> None</code>

# Auth

## Cli

### Authorize

Types:

```python
from vaif_client.types.auth.cli import AuthorizeCreateResponse
```

Methods:

- <code title="post /auth/cli/authorize">client.auth.cli.authorize.<a href="./src/vaif_client/resources/auth/cli/authorize.py">create</a>() -> <a href="./src/vaif_client/types/auth/cli/authorize_create_response.py">AuthorizeCreateResponse</a></code>

### Callback

Types:

```python
from vaif_client.types.auth.cli import CallbackCreateResponse
```

Methods:

- <code title="post /auth/cli/callback">client.auth.cli.callback.<a href="./src/vaif_client/resources/auth/cli/callback.py">create</a>(\*\*<a href="src/vaif_client/types/auth/cli/callback_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/cli/callback_create_response.py">CallbackCreateResponse</a></code>

### Login

Types:

```python
from vaif_client.types.auth.cli import LoginCreateResponse
```

Methods:

- <code title="post /auth/cli/login">client.auth.cli.login.<a href="./src/vaif_client/resources/auth/cli/login.py">create</a>(\*\*<a href="src/vaif_client/types/auth/cli/login_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/cli/login_create_response.py">LoginCreateResponse</a></code>

### Token

Types:

```python
from vaif_client.types.auth.cli import TokenCreateResponse
```

Methods:

- <code title="post /auth/cli/token">client.auth.cli.token.<a href="./src/vaif_client/resources/auth/cli/token.py">create</a>(\*\*<a href="src/vaif_client/types/auth/cli/token_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/cli/token_create_response.py">TokenCreateResponse</a></code>

## ForgotPassword

Types:

```python
from vaif_client.types.auth import ForgotPasswordCreateResponse
```

Methods:

- <code title="post /auth/forgot-password">client.auth.forgot_password.<a href="./src/vaif_client/resources/auth/forgot_password.py">create</a>(\*\*<a href="src/vaif_client/types/auth/forgot_password_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/forgot_password_create_response.py">ForgotPasswordCreateResponse</a></code>

## Login

Types:

```python
from vaif_client.types.auth import LoginCreateResponse
```

Methods:

- <code title="post /auth/login">client.auth.login.<a href="./src/vaif_client/resources/auth/login.py">create</a>(\*\*<a href="src/vaif_client/types/auth/login_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/login_create_response.py">LoginCreateResponse</a></code>

## Logout

Types:

```python
from vaif_client.types.auth import LogoutCreateResponse
```

Methods:

- <code title="post /auth/logout">client.auth.logout.<a href="./src/vaif_client/resources/auth/logout.py">create</a>() -> <a href="./src/vaif_client/types/auth/logout_create_response.py">LogoutCreateResponse</a></code>

## Me

Types:

```python
from vaif_client.types.auth import MeUpdateResponse, MeListResponse
```

Methods:

- <code title="patch /auth/me">client.auth.me.<a href="./src/vaif_client/resources/auth/me/me.py">update</a>(\*\*<a href="src/vaif_client/types/auth/me_update_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/me_update_response.py">MeUpdateResponse</a></code>
- <code title="get /auth/me">client.auth.me.<a href="./src/vaif_client/resources/auth/me/me.py">list</a>() -> <a href="./src/vaif_client/types/auth/me_list_response.py">MeListResponse</a></code>

### Admin

Types:

```python
from vaif_client.types.auth.me import AdminListResponse
```

Methods:

- <code title="get /auth/me/admin">client.auth.me.admin.<a href="./src/vaif_client/resources/auth/me/admin.py">list</a>() -> <a href="./src/vaif_client/types/auth/me/admin_list_response.py">AdminListResponse</a></code>

### Context

Types:

```python
from vaif_client.types.auth.me import ContextListResponse
```

Methods:

- <code title="get /auth/me/context">client.auth.me.context.<a href="./src/vaif_client/resources/auth/me/context.py">list</a>() -> <a href="./src/vaif_client/types/auth/me/context_list_response.py">ContextListResponse</a></code>

### LinkedAccounts

Types:

```python
from vaif_client.types.auth.me import LinkedAccountListResponse, LinkedAccountDeleteResponse
```

Methods:

- <code title="get /auth/me/linked-accounts">client.auth.me.linked_accounts.<a href="./src/vaif_client/resources/auth/me/linked_accounts.py">list</a>() -> <a href="./src/vaif_client/types/auth/me/linked_account_list_response.py">LinkedAccountListResponse</a></code>
- <code title="delete /auth/me/linked-accounts/{provider}">client.auth.me.linked_accounts.<a href="./src/vaif_client/resources/auth/me/linked_accounts.py">delete</a>(provider) -> <a href="./src/vaif_client/types/auth/me/linked_account_delete_response.py">LinkedAccountDeleteResponse</a></code>

## OAuth

Methods:

- <code title="get /auth/oauth/{provider}">client.auth.oauth.<a href="./src/vaif_client/resources/auth/oauth/oauth.py">retrieve</a>(provider, \*\*<a href="src/vaif_client/types/auth/oauth_retrieve_params.py">params</a>) -> None</code>

### Callback

Methods:

- <code title="get /auth/oauth/{provider}/callback">client.auth.oauth.callback.<a href="./src/vaif_client/resources/auth/oauth/callback.py">get_callback</a>(provider, \*\*<a href="src/vaif_client/types/auth/oauth/callback_get_callback_params.py">params</a>) -> None</code>

### Providers

Types:

```python
from vaif_client.types.auth.oauth import ProviderListResponse
```

Methods:

- <code title="get /auth/oauth/providers">client.auth.oauth.providers.<a href="./src/vaif_client/resources/auth/oauth/providers.py">list</a>() -> <a href="./src/vaif_client/types/auth/oauth/provider_list_response.py">ProviderListResponse</a></code>

## Refresh

Types:

```python
from vaif_client.types.auth import RefreshCreateResponse
```

Methods:

- <code title="post /auth/refresh">client.auth.refresh.<a href="./src/vaif_client/resources/auth/refresh.py">create</a>() -> <a href="./src/vaif_client/types/auth/refresh_create_response.py">RefreshCreateResponse</a></code>

## ResetPassword

Types:

```python
from vaif_client.types.auth import ResetPasswordCreateResponse
```

Methods:

- <code title="post /auth/reset-password">client.auth.reset_password.<a href="./src/vaif_client/resources/auth/reset_password.py">create</a>(\*\*<a href="src/vaif_client/types/auth/reset_password_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/reset_password_create_response.py">ResetPasswordCreateResponse</a></code>

## Signup

Types:

```python
from vaif_client.types.auth import SignupCreateResponse
```

Methods:

- <code title="post /auth/signup">client.auth.signup.<a href="./src/vaif_client/resources/auth/signup.py">create</a>(\*\*<a href="src/vaif_client/types/auth/signup_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/signup_create_response.py">SignupCreateResponse</a></code>

## VerifyEmail

### Confirm

Types:

```python
from vaif_client.types.auth.verify_email import ConfirmCreateResponse
```

Methods:

- <code title="post /auth/verify-email/confirm">client.auth.verify_email.confirm.<a href="./src/vaif_client/resources/auth/verify_email/confirm.py">create</a>(\*\*<a href="src/vaif_client/types/auth/verify_email/confirm_create_params.py">params</a>) -> <a href="./src/vaif_client/types/auth/verify_email/confirm_create_response.py">ConfirmCreateResponse</a></code>

### Send

Types:

```python
from vaif_client.types.auth.verify_email import SendCreateResponse
```

Methods:

- <code title="post /auth/verify-email/send">client.auth.verify_email.send.<a href="./src/vaif_client/resources/auth/verify_email/send.py">create</a>() -> <a href="./src/vaif_client/types/auth/verify_email/send_create_response.py">SendCreateResponse</a></code>

# Billing

## Addons

### Catalog

Methods:

- <code title="get /billing/addons/catalog">client.billing.addons.catalog.<a href="./src/vaif_client/resources/billing/addons/catalog.py">list</a>() -> None</code>

## Checkout

Types:

```python
from vaif_client.types.billing import CheckoutCreateResponse
```

Methods:

- <code title="post /billing/checkout">client.billing.checkout.<a href="./src/vaif_client/resources/billing/checkout/checkout.py">create</a>(\*\*<a href="src/vaif_client/types/billing/checkout_create_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/checkout_create_response.py">CheckoutCreateResponse</a></code>

### Verify

Methods:

- <code title="get /billing/checkout/verify/{sessionId}">client.billing.checkout.verify.<a href="./src/vaif_client/resources/billing/checkout/verify.py">retrieve</a>(session_id) -> None</code>

## Credits

### Packages

Methods:

- <code title="get /billing/credits/packages">client.billing.credits.packages.<a href="./src/vaif_client/resources/billing/credits/packages.py">list</a>() -> None</code>

## Enterprise

### Inquiry

Types:

```python
from vaif_client.types.billing.enterprise import InquiryCreateResponse
```

Methods:

- <code title="post /billing/enterprise/inquiry">client.billing.enterprise.inquiry.<a href="./src/vaif_client/resources/billing/enterprise/inquiry.py">create</a>(\*\*<a href="src/vaif_client/types/billing/enterprise/inquiry_create_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/enterprise/inquiry_create_response.py">InquiryCreateResponse</a></code>

## Org

### Addons

Methods:

- <code title="patch /billing/org/{orgId}/addons/{addonId}">client.billing.org.addons.<a href="./src/vaif_client/resources/billing/org/addons.py">update</a>(addon_id, \*, org_id) -> None</code>
- <code title="delete /billing/org/{orgId}/addons/{addonId}">client.billing.org.addons.<a href="./src/vaif_client/resources/billing/org/addons.py">delete</a>(addon_id, \*, org_id) -> None</code>
- <code title="post /billing/org/{orgId}/addons">client.billing.org.addons.<a href="./src/vaif_client/resources/billing/org/addons.py">addons</a>(org_id) -> None</code>
- <code title="get /billing/org/{orgId}/addons">client.billing.org.addons.<a href="./src/vaif_client/resources/billing/org/addons.py">get_addons</a>(org_id) -> None</code>

### Cancel

Types:

```python
from vaif_client.types.billing.org import CancelCancelResponse
```

Methods:

- <code title="post /billing/org/{orgId}/cancel">client.billing.org.cancel.<a href="./src/vaif_client/resources/billing/org/cancel.py">cancel</a>(org_id, \*\*<a href="src/vaif_client/types/billing/org/cancel_cancel_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/cancel_cancel_response.py">CancelCancelResponse</a></code>

### ChangePlan

Types:

```python
from vaif_client.types.billing.org import ChangePlanChangePlanResponse
```

Methods:

- <code title="post /billing/org/{orgId}/change-plan">client.billing.org.change_plan.<a href="./src/vaif_client/resources/billing/org/change_plan.py">change_plan</a>(org_id, \*\*<a href="src/vaif_client/types/billing/org/change_plan_change_plan_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/change_plan_change_plan_response.py">ChangePlanChangePlanResponse</a></code>

### Contacts

Types:

```python
from vaif_client.types.billing.org import ContactContactsResponse
```

Methods:

- <code title="delete /billing/org/{orgId}/contacts/{contactId}">client.billing.org.contacts.<a href="./src/vaif_client/resources/billing/org/contacts.py">delete</a>(contact_id, \*, org_id) -> None</code>
- <code title="post /billing/org/{orgId}/contacts">client.billing.org.contacts.<a href="./src/vaif_client/resources/billing/org/contacts.py">contacts</a>(org_id, \*\*<a href="src/vaif_client/types/billing/org/contact_contacts_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/contact_contacts_response.py">ContactContactsResponse</a></code>
- <code title="get /billing/org/{orgId}/contacts">client.billing.org.contacts.<a href="./src/vaif_client/resources/billing/org/contacts.py">get_contacts</a>(org_id) -> None</code>

### CostBreakdown

Methods:

- <code title="get /billing/org/{orgId}/cost-breakdown">client.billing.org.cost_breakdown.<a href="./src/vaif_client/resources/billing/org/cost_breakdown.py">get_cost_breakdown</a>(org_id) -> None</code>

### Credits

Types:

```python
from vaif_client.types.billing.org import CreditPurchaseResponse
```

Methods:

- <code title="get /billing/org/{orgId}/credits/transactions">client.billing.org.credits.<a href="./src/vaif_client/resources/billing/org/credits.py">get_transactions</a>(org_id) -> None</code>
- <code title="post /billing/org/{orgId}/credits/purchase">client.billing.org.credits.<a href="./src/vaif_client/resources/billing/org/credits.py">purchase</a>(org_id, \*\*<a href="src/vaif_client/types/billing/org/credit_purchase_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/credit_purchase_response.py">CreditPurchaseResponse</a></code>

### Invoices

Methods:

- <code title="get /billing/org/{orgId}/invoices">client.billing.org.invoices.<a href="./src/vaif_client/resources/billing/org/invoices/invoices.py">get_invoices</a>(org_id) -> None</code>

#### Pdf

Methods:

- <code title="get /billing/org/{orgId}/invoices/{invoiceId}/pdf">client.billing.org.invoices.pdf.<a href="./src/vaif_client/resources/billing/org/invoices/pdf.py">get_pdf</a>(invoice_id, \*, org_id) -> None</code>

### Overages

Methods:

- <code title="get /billing/org/{orgId}/overages/history">client.billing.org.overages.<a href="./src/vaif_client/resources/billing/org/overages.py">get_history</a>(org_id) -> None</code>
- <code title="get /billing/org/{orgId}/overages">client.billing.org.overages.<a href="./src/vaif_client/resources/billing/org/overages.py">get_overages</a>(org_id) -> None</code>

### Pause

Methods:

- <code title="post /billing/org/{orgId}/pause">client.billing.org.pause.<a href="./src/vaif_client/resources/billing/org/pause.py">pause</a>(org_id) -> None</code>

### Portal

Methods:

- <code title="post /billing/org/{orgId}/portal">client.billing.org.portal.<a href="./src/vaif_client/resources/billing/org/portal.py">portal</a>(org_id) -> None</code>

### Reactivate

Methods:

- <code title="post /billing/org/{orgId}/reactivate">client.billing.org.reactivate.<a href="./src/vaif_client/resources/billing/org/reactivate.py">reactivate</a>(org_id) -> None</code>

### Resume

Methods:

- <code title="post /billing/org/{orgId}/resume">client.billing.org.resume.<a href="./src/vaif_client/resources/billing/org/resume.py">resume</a>(org_id) -> None</code>

### Summary

Methods:

- <code title="get /billing/org/{orgId}/summary">client.billing.org.summary.<a href="./src/vaif_client/resources/billing/org/summary.py">get_summary</a>(org_id) -> None</code>

### TaxInfo

Types:

```python
from vaif_client.types.billing.org import TaxInfoTaxInfoResponse
```

Methods:

- <code title="get /billing/org/{orgId}/tax-info">client.billing.org.tax_info.<a href="./src/vaif_client/resources/billing/org/tax_info.py">get_tax_info</a>(org_id) -> None</code>
- <code title="put /billing/org/{orgId}/tax-info">client.billing.org.tax_info.<a href="./src/vaif_client/resources/billing/org/tax_info.py">tax_info</a>(org_id, \*\*<a href="src/vaif_client/types/billing/org/tax_info_tax_info_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/tax_info_tax_info_response.py">TaxInfoTaxInfoResponse</a></code>

### Usage

Methods:

- <code title="get /billing/org/{orgId}/usage/history">client.billing.org.usage.<a href="./src/vaif_client/resources/billing/org/usage.py">get_history</a>(org_id) -> None</code>
- <code title="get /billing/org/{orgId}/usage/realtime">client.billing.org.usage.<a href="./src/vaif_client/resources/billing/org/usage.py">get_realtime</a>(org_id) -> None</code>
- <code title="get /billing/org/{orgId}/usage">client.billing.org.usage.<a href="./src/vaif_client/resources/billing/org/usage.py">get_usage</a>(org_id) -> None</code>

### UsageAlerts

Types:

```python
from vaif_client.types.billing.org import UsageAlertUpdateResponse, UsageAlertUsageAlertsResponse
```

Methods:

- <code title="patch /billing/org/{orgId}/usage-alerts/{alertId}">client.billing.org.usage_alerts.<a href="./src/vaif_client/resources/billing/org/usage_alerts.py">update</a>(alert_id, \*, org_id, \*\*<a href="src/vaif_client/types/billing/org/usage_alert_update_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/usage_alert_update_response.py">UsageAlertUpdateResponse</a></code>
- <code title="delete /billing/org/{orgId}/usage-alerts/{alertId}">client.billing.org.usage_alerts.<a href="./src/vaif_client/resources/billing/org/usage_alerts.py">delete</a>(alert_id, \*, org_id) -> None</code>
- <code title="get /billing/org/{orgId}/usage-alerts/configured">client.billing.org.usage_alerts.<a href="./src/vaif_client/resources/billing/org/usage_alerts.py">get_configured</a>(org_id) -> None</code>
- <code title="get /billing/org/{orgId}/usage-alerts/history">client.billing.org.usage_alerts.<a href="./src/vaif_client/resources/billing/org/usage_alerts.py">get_history</a>(org_id) -> None</code>
- <code title="get /billing/org/{orgId}/usage-alerts">client.billing.org.usage_alerts.<a href="./src/vaif_client/resources/billing/org/usage_alerts.py">get_usage_alerts</a>(org_id) -> None</code>
- <code title="post /billing/org/{orgId}/usage-alerts">client.billing.org.usage_alerts.<a href="./src/vaif_client/resources/billing/org/usage_alerts.py">usage_alerts</a>(org_id, \*\*<a href="src/vaif_client/types/billing/org/usage_alert_usage_alerts_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/org/usage_alert_usage_alerts_response.py">UsageAlertUsageAlertsResponse</a></code>

## Plans

Methods:

- <code title="get /billing/plans">client.billing.plans.<a href="./src/vaif_client/resources/billing/plans.py">list</a>() -> None</code>

## Portal

Types:

```python
from vaif_client.types.billing import PortalCreateResponse
```

Methods:

- <code title="post /billing/portal">client.billing.portal.<a href="./src/vaif_client/resources/billing/portal.py">create</a>(\*\*<a href="src/vaif_client/types/billing/portal_create_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/portal_create_response.py">PortalCreateResponse</a></code>

## PromoCodes

### Validate

Types:

```python
from vaif_client.types.billing.promo_codes import ValidateCreateResponse
```

Methods:

- <code title="post /billing/promo-codes/validate">client.billing.promo_codes.validate.<a href="./src/vaif_client/resources/billing/promo_codes/validate.py">create</a>(\*\*<a href="src/vaif_client/types/billing/promo_codes/validate_create_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/promo_codes/validate_create_response.py">ValidateCreateResponse</a></code>

## RedeemPromo

Types:

```python
from vaif_client.types.billing import RedeemPromoCreateResponse
```

Methods:

- <code title="post /billing/redeem-promo">client.billing.redeem_promo.<a href="./src/vaif_client/resources/billing/redeem_promo.py">create</a>(\*\*<a href="src/vaif_client/types/billing/redeem_promo_create_params.py">params</a>) -> <a href="./src/vaif_client/types/billing/redeem_promo_create_response.py">RedeemPromoCreateResponse</a></code>

## Webhook

Methods:

- <code title="post /billing/webhook">client.billing.webhook.<a href="./src/vaif_client/resources/billing/webhook.py">create</a>() -> None</code>

# Bootstrap

Methods:

- <code title="get /bootstrap/">client.bootstrap.<a href="./src/vaif_client/resources/bootstrap.py">list</a>() -> None</code>

# Buckets

Types:

```python
from vaif_client.types import BucketUpdateResponse
```

Methods:

- <code title="get /buckets/{bucketId}">client.buckets.<a href="./src/vaif_client/resources/buckets/buckets.py">retrieve</a>(bucket_id) -> None</code>
- <code title="put /buckets/{bucketId}">client.buckets.<a href="./src/vaif_client/resources/buckets/buckets.py">update</a>(bucket_id, \*\*<a href="src/vaif_client/types/bucket_update_params.py">params</a>) -> <a href="./src/vaif_client/types/bucket_update_response.py">BucketUpdateResponse</a></code>
- <code title="delete /buckets/{bucketId}">client.buckets.<a href="./src/vaif_client/resources/buckets/buckets.py">delete</a>(bucket_id) -> None</code>

## Files

Methods:

- <code title="delete /buckets/{bucketId}/files">client.buckets.files.<a href="./src/vaif_client/resources/buckets/files.py">files</a>(bucket_id) -> None</code>
- <code title="get /buckets/{bucketId}/files">client.buckets.files.<a href="./src/vaif_client/resources/buckets/files.py">get_files</a>(bucket_id) -> None</code>

## Project

Methods:

- <code title="get /buckets/project/{projectId}">client.buckets.project.<a href="./src/vaif_client/resources/buckets/project.py">retrieve</a>(project_id) -> None</code>

## SignedURL

Methods:

- <code title="post /buckets/{bucketId}/signed-url">client.buckets.signed_url.<a href="./src/vaif_client/resources/buckets/signed_url.py">signed_url</a>(bucket_id) -> None</code>

## Upload

Methods:

- <code title="post /buckets/{bucketId}/upload">client.buckets.upload.<a href="./src/vaif_client/resources/buckets/upload.py">upload</a>(bucket_id) -> None</code>

## UploadURL

Methods:

- <code title="post /buckets/{bucketId}/upload-url">client.buckets.upload_url.<a href="./src/vaif_client/resources/buckets/upload_url.py">upload_url</a>(bucket_id) -> None</code>

# Cms

## Careers

Methods:

- <code title="get /cms/careers">client.cms.careers.<a href="./src/vaif_client/resources/cms/careers.py">list</a>() -> None</code>

## Faqs

Methods:

- <code title="get /cms/faqs/{pageSlug}">client.cms.faqs.<a href="./src/vaif_client/resources/cms/faqs.py">retrieve</a>(page_slug) -> None</code>

## Pages

Methods:

- <code title="get /cms/pages/{slug}">client.cms.pages.<a href="./src/vaif_client/resources/cms/pages.py">retrieve</a>(slug) -> None</code>

## Partners

Methods:

- <code title="get /cms/partners">client.cms.partners.<a href="./src/vaif_client/resources/cms/partners.py">list</a>() -> None</code>

## Team

Methods:

- <code title="get /cms/team">client.cms.team.<a href="./src/vaif_client/resources/cms/team.py">list</a>() -> None</code>

## Testimonials

Methods:

- <code title="get /cms/testimonials">client.cms.testimonials.<a href="./src/vaif_client/resources/cms/testimonials.py">list</a>() -> None</code>

# Contact

Types:

```python
from vaif_client.types import ContactCreateResponse
```

Methods:

- <code title="post /contact">client.contact.<a href="./src/vaif_client/resources/contact.py">create</a>(\*\*<a href="src/vaif_client/types/contact_create_params.py">params</a>) -> <a href="./src/vaif_client/types/contact_create_response.py">ContactCreateResponse</a></code>

# Credits

## Org

Methods:

- <code title="get /credits/org/{orgId}">client.credits.org.<a href="./src/vaif_client/resources/credits/org/org.py">retrieve</a>(org_id) -> None</code>

### Balance

Methods:

- <code title="get /credits/org/{orgId}/balance">client.credits.org.balance.<a href="./src/vaif_client/resources/credits/org/balance.py">get_balance</a>(org_id) -> None</code>

# Database

## Connector

### Query

Methods:

- <code title="post /database/connector/{projectId}/query">client.database.connector.query.<a href="./src/vaif_client/resources/database/connector/query.py">query</a>(project_id, \*\*<a href="src/vaif_client/types/database/connector/query_query_params.py">params</a>) -> object</code>

### Tables

Methods:

- <code title="get /database/connector/{projectId}/tables">client.database.connector.tables.<a href="./src/vaif_client/resources/database/connector/tables.py">get_tables</a>(project_id) -> None</code>

### Test

Methods:

- <code title="post /database/connector/{projectId}/test">client.database.connector.test.<a href="./src/vaif_client/resources/database/connector/test.py">test</a>(project_id) -> None</code>

## Extensions

### Available

Methods:

- <code title="get /database/extensions/available">client.database.extensions.available.<a href="./src/vaif_client/resources/database/extensions/available.py">list</a>() -> None</code>

### Project

Methods:

- <code title="get /database/extensions/project/{projectId}">client.database.extensions.project.<a href="./src/vaif_client/resources/database/extensions/project/project.py">retrieve</a>(project_id) -> None</code>
- <code title="delete /database/extensions/project/{projectId}/{extensionId}">client.database.extensions.project.<a href="./src/vaif_client/resources/database/extensions/project/project.py">delete</a>(extension_id, \*, project_id) -> None</code>

#### Install

Methods:

- <code title="post /database/extensions/project/{projectId}/install">client.database.extensions.project.install.<a href="./src/vaif_client/resources/database/extensions/project/install.py">install</a>(project_id, \*\*<a href="src/vaif_client/types/database/extensions/project/install_install_params.py">params</a>) -> object</code>

## Tiers

Methods:

- <code title="get /database/tiers">client.database.tiers.<a href="./src/vaif_client/resources/database/tiers.py">list</a>() -> None</code>

## Wrappers

### Available

Methods:

- <code title="get /database/wrappers/available">client.database.wrappers.available.<a href="./src/vaif_client/resources/database/wrappers/available.py">list</a>() -> None</code>

### Project

Methods:

- <code title="get /database/wrappers/project/{projectId}">client.database.wrappers.project.<a href="./src/vaif_client/resources/database/wrappers/project/project.py">retrieve</a>(project_id) -> None</code>
- <code title="patch /database/wrappers/project/{projectId}/{wrapperId}">client.database.wrappers.project.<a href="./src/vaif_client/resources/database/wrappers/project/project.py">update</a>(wrapper_id, \*, project_id, \*\*<a href="src/vaif_client/types/database/wrappers/project_update_params.py">params</a>) -> object</code>
- <code title="delete /database/wrappers/project/{projectId}/{wrapperId}">client.database.wrappers.project.<a href="./src/vaif_client/resources/database/wrappers/project/project.py">delete</a>(wrapper_id, \*, project_id) -> None</code>

#### Install

Methods:

- <code title="post /database/wrappers/project/{projectId}/install">client.database.wrappers.project.install.<a href="./src/vaif_client/resources/database/wrappers/project/install.py">install</a>(project_id, \*\*<a href="src/vaif_client/types/database/wrappers/project/install_install_params.py">params</a>) -> object</code>

# Deployments

Methods:

- <code title="get /deployments/{deploymentId}">client.deployments.<a href="./src/vaif_client/resources/deployments/deployments.py">retrieve</a>(deployment_id) -> None</code>

## Project

Methods:

- <code title="get /deployments/project/{projectId}">client.deployments.project.<a href="./src/vaif_client/resources/deployments/project.py">retrieve</a>(project_id) -> None</code>

## Promote

Methods:

- <code title="post /deployments/promote">client.deployments.promote.<a href="./src/vaif_client/resources/deployments/promote.py">create</a>() -> None</code>

## Rollback

Methods:

- <code title="post /deployments/{deploymentId}/rollback">client.deployments.rollback.<a href="./src/vaif_client/resources/deployments/rollback.py">rollback</a>(deployment_id) -> None</code>

## Steps

Methods:

- <code title="get /deployments/{deploymentId}/steps">client.deployments.steps.<a href="./src/vaif_client/resources/deployments/steps.py">get_steps</a>(deployment_id) -> None</code>

## Tokens

Types:

```python
from vaif_client.types.deployments import TokenCreateResponse
```

Methods:

- <code title="post /deployments/tokens">client.deployments.tokens.<a href="./src/vaif_client/resources/deployments/tokens/tokens.py">create</a>(\*\*<a href="src/vaif_client/types/deployments/token_create_params.py">params</a>) -> <a href="./src/vaif_client/types/deployments/token_create_response.py">TokenCreateResponse</a></code>

### Project

Types:

```python
from vaif_client.types.deployments.tokens import ProjectRetrieveResponse
```

Methods:

- <code title="get /deployments/tokens/project/{projectId}">client.deployments.tokens.project.<a href="./src/vaif_client/resources/deployments/tokens/project.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/deployments/tokens/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

### Revoke

Types:

```python
from vaif_client.types.deployments.tokens import RevokeRevokeResponse
```

Methods:

- <code title="post /deployments/tokens/{tokenId}/revoke">client.deployments.tokens.revoke.<a href="./src/vaif_client/resources/deployments/tokens/revoke.py">revoke</a>(token_id) -> <a href="./src/vaif_client/types/deployments/tokens/revoke_revoke_response.py">RevokeRevokeResponse</a></code>

## Trigger

Methods:

- <code title="post /deployments/trigger">client.deployments.trigger.<a href="./src/vaif_client/resources/deployments/trigger.py">create</a>() -> None</code>

# Docs

## AIAnswer

Methods:

- <code title="post /docs/ai-answer">client.docs.ai_answer.<a href="./src/vaif_client/resources/docs/ai_answer.py">create</a>(\*\*<a href="src/vaif_client/types/docs/ai_answer_create_params.py">params</a>) -> None</code>

## AISearch

Methods:

- <code title="get /docs/ai-search">client.docs.ai_search.<a href="./src/vaif_client/resources/docs/ai_search.py">list</a>() -> None</code>

## APIEndpoints

Methods:

- <code title="get /docs/api-endpoints/{id}">client.docs.api_endpoints.<a href="./src/vaif_client/resources/docs/api_endpoints.py">retrieve</a>(id) -> None</code>
- <code title="get /docs/api-endpoints">client.docs.api_endpoints.<a href="./src/vaif_client/resources/docs/api_endpoints.py">list</a>() -> None</code>

## Categories

Methods:

- <code title="get /docs/categories">client.docs.categories.<a href="./src/vaif_client/resources/docs/categories.py">list</a>() -> None</code>

## Changelog

Methods:

- <code title="get /docs/changelog/{id}">client.docs.changelog.<a href="./src/vaif_client/resources/docs/changelog.py">retrieve</a>(id) -> None</code>
- <code title="get /docs/changelog">client.docs.changelog.<a href="./src/vaif_client/resources/docs/changelog.py">list</a>() -> None</code>

## Examples

Methods:

- <code title="get /docs/examples/{slug}">client.docs.examples.<a href="./src/vaif_client/resources/docs/examples.py">retrieve</a>(slug) -> None</code>
- <code title="get /docs/examples">client.docs.examples.<a href="./src/vaif_client/resources/docs/examples.py">list</a>() -> None</code>

## Feedback

Methods:

- <code title="post /docs/feedback">client.docs.feedback.<a href="./src/vaif_client/resources/docs/feedback.py">create</a>() -> None</code>

## Project

### Quickstart

Methods:

- <code title="get /docs/project/{projectId}/quickstart">client.docs.project.quickstart.<a href="./src/vaif_client/resources/docs/project/quickstart.py">get_quickstart</a>(project_id) -> None</code>

## SDKs

Methods:

- <code title="get /docs/sdks/{platform}">client.docs.sdks.<a href="./src/vaif_client/resources/docs/sdks/sdks.py">retrieve</a>(platform) -> None</code>
- <code title="get /docs/sdks">client.docs.sdks.<a href="./src/vaif_client/resources/docs/sdks/sdks.py">list</a>() -> None</code>

### Examples

Methods:

- <code title="get /docs/sdks/{sdkId}/examples">client.docs.sdks.examples.<a href="./src/vaif_client/resources/docs/sdks/examples.py">get_examples</a>(sdk_id) -> None</code>

## Search

Methods:

- <code title="get /docs/search">client.docs.search.<a href="./src/vaif_client/resources/docs/search.py">list</a>() -> None</code>

## SearchClick

Methods:

- <code title="post /docs/search-click">client.docs.search_click.<a href="./src/vaif_client/resources/docs/search_click.py">create</a>() -> None</code>

## V2

### Pages

Methods:

- <code title="get /docs/v2/pages/{slug}">client.docs.v2.pages.<a href="./src/vaif_client/resources/docs/v2/pages.py">retrieve</a>(slug) -> None</code>
- <code title="get /docs/v2/pages">client.docs.v2.pages.<a href="./src/vaif_client/resources/docs/v2/pages.py">list</a>() -> None</code>

# Enterprise

## Inquire

Types:

```python
from vaif_client.types.enterprise import InquireCreateResponse
```

Methods:

- <code title="post /enterprise/inquire">client.enterprise.inquire.<a href="./src/vaif_client/resources/enterprise/inquire.py">create</a>(\*\*<a href="src/vaif_client/types/enterprise/inquire_create_params.py">params</a>) -> <a href="./src/vaif_client/types/enterprise/inquire_create_response.py">InquireCreateResponse</a></code>

## Org

### Contract

Methods:

- <code title="get /enterprise/org/{orgId}/contract">client.enterprise.org.contract.<a href="./src/vaif_client/resources/enterprise/org/contract.py">get_contract</a>(org_id) -> None</code>

### Invoices

Methods:

- <code title="get /enterprise/org/{orgId}/invoices">client.enterprise.org.invoices.<a href="./src/vaif_client/resources/enterprise/org/invoices.py">get_invoices</a>(org_id) -> None</code>

### Onboarding

Types:

```python
from vaif_client.types.enterprise.org import OnboardingOnboardingResponse
```

Methods:

- <code title="get /enterprise/org/{orgId}/onboarding">client.enterprise.org.onboarding.<a href="./src/vaif_client/resources/enterprise/org/onboarding.py">get_onboarding</a>(org_id) -> None</code>
- <code title="patch /enterprise/org/{orgId}/onboarding">client.enterprise.org.onboarding.<a href="./src/vaif_client/resources/enterprise/org/onboarding.py">onboarding</a>(org_id, \*\*<a href="src/vaif_client/types/enterprise/org/onboarding_onboarding_params.py">params</a>) -> <a href="./src/vaif_client/types/enterprise/org/onboarding_onboarding_response.py">OnboardingOnboardingResponse</a></code>

### Usage

Methods:

- <code title="get /enterprise/org/{orgId}/usage/history">client.enterprise.org.usage.<a href="./src/vaif_client/resources/enterprise/org/usage.py">get_history</a>(org_id) -> None</code>
- <code title="get /enterprise/org/{orgId}/usage/projects">client.enterprise.org.usage.<a href="./src/vaif_client/resources/enterprise/org/usage.py">get_projects</a>(org_id) -> None</code>
- <code title="get /enterprise/org/{orgId}/usage">client.enterprise.org.usage.<a href="./src/vaif_client/resources/enterprise/org/usage.py">get_usage</a>(org_id) -> None</code>

## Quotes

Methods:

- <code title="get /enterprise/quotes/{quoteId}">client.enterprise.quotes.<a href="./src/vaif_client/resources/enterprise/quotes/quotes.py">retrieve</a>(quote_id) -> None</code>

### Accept

Methods:

- <code title="post /enterprise/quotes/{quoteId}/accept">client.enterprise.quotes.accept.<a href="./src/vaif_client/resources/enterprise/quotes/accept.py">accept</a>(quote_id) -> None</code>

## Subdomain

Methods:

- <code title="get /enterprise/subdomain/{subdomain}">client.enterprise.subdomain.<a href="./src/vaif_client/resources/enterprise/subdomain.py">retrieve</a>(subdomain) -> None</code>

# Entitlements

## Org

Methods:

- <code title="get /entitlements/org/{orgId}">client.entitlements.org.<a href="./src/vaif_client/resources/entitlements/org/org.py">retrieve</a>(org_id) -> None</code>

### Check

Methods:

- <code title="post /entitlements/org/{orgId}/check">client.entitlements.org.check.<a href="./src/vaif_client/resources/entitlements/org/check.py">check</a>(org_id) -> None</code>

# Functions

Methods:

- <code title="post /functions/">client.functions.<a href="./src/vaif_client/resources/functions/functions.py">create</a>(\*\*<a href="src/vaif_client/types/function_create_params.py">params</a>) -> object</code>
- <code title="get /functions/{functionId}">client.functions.<a href="./src/vaif_client/resources/functions/functions.py">retrieve</a>(function_id) -> None</code>
- <code title="patch /functions/{functionId}">client.functions.<a href="./src/vaif_client/resources/functions/functions.py">update</a>(function_id, \*\*<a href="src/vaif_client/types/function_update_params.py">params</a>) -> object</code>
- <code title="delete /functions/{functionId}">client.functions.<a href="./src/vaif_client/resources/functions/functions.py">delete</a>(function_id) -> None</code>

## DeployStatus

Methods:

- <code title="get /functions/{functionId}/deploy-status">client.functions.deploy_status.<a href="./src/vaif_client/resources/functions/deploy_status.py">get_deploy_status</a>(function_id) -> None</code>

## Invocations

Methods:

- <code title="get /functions/invocations">client.functions.invocations.<a href="./src/vaif_client/resources/functions/invocations/invocations.py">list</a>() -> None</code>
- <code title="get /functions/{functionId}/invocations">client.functions.invocations.<a href="./src/vaif_client/resources/functions/invocations/invocations.py">get_invocations</a>(function_id) -> None</code>

### Function

Methods:

- <code title="get /functions/invocations/function/{functionId}">client.functions.invocations.function.<a href="./src/vaif_client/resources/functions/invocations/function.py">retrieve</a>(function_id) -> None</code>

## Invoke

Methods:

- <code title="post /functions/{functionIdOrName}/invoke">client.functions.invoke.<a href="./src/vaif_client/resources/functions/invoke.py">invoke</a>(function_id_or_name) -> None</code>

## Logs

Methods:

- <code title="get /functions/{functionId}/logs">client.functions.logs.<a href="./src/vaif_client/resources/functions/logs.py">get_logs</a>(function_id) -> None</code>

## Metrics

Methods:

- <code title="get /functions/{functionId}/metrics">client.functions.metrics.<a href="./src/vaif_client/resources/functions/metrics.py">get_metrics</a>(function_id) -> None</code>

## Project

Methods:

- <code title="get /functions/project/{projectId}">client.functions.project.<a href="./src/vaif_client/resources/functions/project/project.py">retrieve</a>(project_id) -> None</code>

### Name

Methods:

- <code title="get /functions/project/{projectId}/name/{functionName}">client.functions.project.name.<a href="./src/vaif_client/resources/functions/project/name.py">retrieve</a>(function_name, \*, project_id) -> None</code>

## Schedule

Methods:

- <code title="get /functions/{functionId}/schedule">client.functions.schedule.<a href="./src/vaif_client/resources/functions/schedule.py">get_schedule</a>(function_id) -> None</code>
- <code title="put /functions/{functionId}/schedule">client.functions.schedule.<a href="./src/vaif_client/resources/functions/schedule.py">schedule</a>(function_id, \*\*<a href="src/vaif_client/types/functions/schedule_schedule_params.py">params</a>) -> object</code>
- <code title="delete /functions/{functionId}/schedule">client.functions.schedule.<a href="./src/vaif_client/resources/functions/schedule.py">schedule2</a>(function_id) -> None</code>

## Secrets

Methods:

- <code title="post /functions/secrets">client.functions.secrets.<a href="./src/vaif_client/resources/functions/secrets/secrets.py">create</a>(\*\*<a href="src/vaif_client/types/functions/secret_create_params.py">params</a>) -> object</code>
- <code title="put /functions/secrets/{secretId}">client.functions.secrets.<a href="./src/vaif_client/resources/functions/secrets/secrets.py">update</a>(secret_id, \*\*<a href="src/vaif_client/types/functions/secret_update_params.py">params</a>) -> object</code>
- <code title="delete /functions/secrets/{secretId}">client.functions.secrets.<a href="./src/vaif_client/resources/functions/secrets/secrets.py">delete</a>(secret_id) -> None</code>

### Project

Methods:

- <code title="get /functions/secrets/project/{projectId}">client.functions.secrets.project.<a href="./src/vaif_client/resources/functions/secrets/project.py">retrieve</a>(project_id) -> None</code>

### Value

Methods:

- <code title="get /functions/secrets/{secretId}/value">client.functions.secrets.value.<a href="./src/vaif_client/resources/functions/secrets/value.py">get_value</a>(secret_id) -> None</code>

## Source

Types:

```python
from vaif_client.types.functions import SourceSourceResponse
```

Methods:

- <code title="put /functions/{functionId}/source">client.functions.source.<a href="./src/vaif_client/resources/functions/source.py">source</a>(function_id, \*\*<a href="src/vaif_client/types/functions/source_source_params.py">params</a>) -> <a href="./src/vaif_client/types/functions/source_source_response.py">SourceSourceResponse</a></code>

## Triggers

Methods:

- <code title="delete /functions/triggers/{triggerId}">client.functions.triggers.<a href="./src/vaif_client/resources/functions/triggers.py">delete</a>(trigger_id) -> None</code>
- <code title="get /functions/{functionId}/triggers">client.functions.triggers.<a href="./src/vaif_client/resources/functions/triggers.py">get_triggers</a>(function_id) -> None</code>
- <code title="post /functions/{functionId}/triggers">client.functions.triggers.<a href="./src/vaif_client/resources/functions/triggers.py">triggers</a>(function_id, \*\*<a href="src/vaif_client/types/functions/trigger_triggers_params.py">params</a>) -> object</code>

# Generated

Methods:

- <code title="post /generated/{table}">client.generated.<a href="./src/vaif_client/resources/generated/generated.py">create</a>(table) -> None</code>
- <code title="get /generated/{table}">client.generated.<a href="./src/vaif_client/resources/generated/generated.py">retrieve</a>(table) -> None</code>
- <code title="patch /generated/{table}/{id}">client.generated.<a href="./src/vaif_client/resources/generated/generated.py">update</a>(id, \*, table) -> None</code>
- <code title="delete /generated/{table}/{id}">client.generated.<a href="./src/vaif_client/resources/generated/generated.py">delete</a>(id, \*, table) -> None</code>
- <code title="get /generated/{table}/{id}">client.generated.<a href="./src/vaif_client/resources/generated/generated.py">retrieve2</a>(id, \*, table) -> None</code>

## Aggregate

Methods:

- <code title="get /generated/{table}/aggregate">client.generated.aggregate.<a href="./src/vaif_client/resources/generated/aggregate.py">get_aggregate</a>(table) -> None</code>

## Bulk

Methods:

- <code title="post /generated/{table}/bulk">client.generated.bulk.<a href="./src/vaif_client/resources/generated/bulk.py">bulk</a>(table) -> None</code>
- <code title="patch /generated/{table}/bulk">client.generated.bulk.<a href="./src/vaif_client/resources/generated/bulk.py">bulk2</a>(table) -> None</code>
- <code title="delete /generated/{table}/bulk">client.generated.bulk.<a href="./src/vaif_client/resources/generated/bulk.py">bulk3</a>(table) -> None</code>

## Query

Methods:

- <code title="post /generated/{table}/query">client.generated.query.<a href="./src/vaif_client/resources/generated/query.py">query</a>(table) -> None</code>

## Search

Methods:

- <code title="get /generated/{table}/search">client.generated.search.<a href="./src/vaif_client/resources/generated/search.py">get_search</a>(table) -> None</code>

# GitHub

## OAuth

### Authorize

Methods:

- <code title="get /github/oauth/authorize">client.github.oauth.authorize.<a href="./src/vaif_client/resources/github/oauth/authorize.py">list</a>() -> None</code>

### Callback

Methods:

- <code title="get /github/oauth/callback">client.github.oauth.callback.<a href="./src/vaif_client/resources/github/oauth/callback.py">list</a>() -> None</code>

# Incidents

## Ack

Types:

```python
from vaif_client.types.incidents import AckAckResponse
```

Methods:

- <code title="post /incidents/{incidentId}/ack">client.incidents.ack.<a href="./src/vaif_client/resources/incidents/ack.py">ack</a>(incident_id) -> <a href="./src/vaif_client/types/incidents/ack_ack_response.py">AckAckResponse</a></code>

## Bulk

Types:

```python
from vaif_client.types.incidents import BulkCreateResponse
```

Methods:

- <code title="post /incidents/bulk">client.incidents.bulk.<a href="./src/vaif_client/resources/incidents/bulk.py">create</a>(\*\*<a href="src/vaif_client/types/incidents/bulk_create_params.py">params</a>) -> <a href="./src/vaif_client/types/incidents/bulk_create_response.py">BulkCreateResponse</a></code>

## Project

Types:

```python
from vaif_client.types.incidents import ProjectRetrieveResponse
```

Methods:

- <code title="get /incidents/project/{projectId}">client.incidents.project.<a href="./src/vaif_client/resources/incidents/project.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/incidents/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

## Resolve

Types:

```python
from vaif_client.types.incidents import ResolveResolveResponse
```

Methods:

- <code title="post /incidents/{incidentId}/resolve">client.incidents.resolve.<a href="./src/vaif_client/resources/incidents/resolve.py">resolve</a>(incident_id) -> <a href="./src/vaif_client/types/incidents/resolve_resolve_response.py">ResolveResolveResponse</a></code>

# Infrastructure

## PollStatus

Methods:

- <code title="post /infrastructure/poll-status">client.infrastructure.poll_status.<a href="./src/vaif_client/resources/infrastructure/poll_status.py">create</a>() -> None</code>

## Sizes

Methods:

- <code title="get /infrastructure/sizes">client.infrastructure.sizes.<a href="./src/vaif_client/resources/infrastructure/sizes.py">list</a>() -> None</code>

# Integrations

## Analytics

### Project

#### Events

Methods:

- <code title="get /integrations/analytics/project/{projectId}/events">client.integrations.analytics.project.events.<a href="./src/vaif_client/resources/integrations/analytics/project/events.py">get_events</a>(project_id) -> None</code>

#### Stats

Methods:

- <code title="get /integrations/analytics/project/{projectId}/stats">client.integrations.analytics.project.stats.<a href="./src/vaif_client/resources/integrations/analytics/project/stats.py">get_stats</a>(project_id) -> None</code>

## Deliveries

### Event

Types:

```python
from vaif_client.types.integrations.deliveries import EventRetrieveResponse
```

Methods:

- <code title="get /integrations/deliveries/event/{eventId}">client.integrations.deliveries.event.<a href="./src/vaif_client/resources/integrations/deliveries/event.py">retrieve</a>(event_id) -> <a href="./src/vaif_client/types/integrations/deliveries/event_retrieve_response.py">EventRetrieveResponse</a></code>

### Retry

Types:

```python
from vaif_client.types.integrations.deliveries import RetryRetryResponse
```

Methods:

- <code title="post /integrations/deliveries/{deliveryId}/retry">client.integrations.deliveries.retry.<a href="./src/vaif_client/resources/integrations/deliveries/retry.py">retry</a>(delivery_id) -> <a href="./src/vaif_client/types/integrations/deliveries/retry_retry_response.py">RetryRetryResponse</a></code>

### Subscription

Types:

```python
from vaif_client.types.integrations.deliveries import SubscriptionRetrieveResponse
```

Methods:

- <code title="get /integrations/deliveries/subscription/{subscriptionId}">client.integrations.deliveries.subscription.<a href="./src/vaif_client/resources/integrations/deliveries/subscription.py">retrieve</a>(subscription_id) -> <a href="./src/vaif_client/types/integrations/deliveries/subscription_retrieve_response.py">SubscriptionRetrieveResponse</a></code>

## Dlq

### Project

Types:

```python
from vaif_client.types.integrations.dlq import ProjectRetrieveResponse
```

Methods:

- <code title="get /integrations/dlq/project/{projectId}">client.integrations.dlq.project.<a href="./src/vaif_client/resources/integrations/dlq/project.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/integrations/dlq/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

## Subscriptions

Types:

```python
from vaif_client.types.integrations import (
    SubscriptionCreateResponse,
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /integrations/subscriptions">client.integrations.subscriptions.<a href="./src/vaif_client/resources/integrations/subscriptions/subscriptions.py">create</a>(\*\*<a href="src/vaif_client/types/integrations/subscription_create_params.py">params</a>) -> <a href="./src/vaif_client/types/integrations/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="patch /integrations/subscriptions/{id}">client.integrations.subscriptions.<a href="./src/vaif_client/resources/integrations/subscriptions/subscriptions.py">update</a>(id) -> <a href="./src/vaif_client/types/integrations/subscription_update_response.py">SubscriptionUpdateResponse</a></code>
- <code title="delete /integrations/subscriptions/{id}">client.integrations.subscriptions.<a href="./src/vaif_client/resources/integrations/subscriptions/subscriptions.py">delete</a>(id) -> <a href="./src/vaif_client/types/integrations/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

### Project

Types:

```python
from vaif_client.types.integrations.subscriptions import ProjectRetrieveResponse
```

Methods:

- <code title="get /integrations/subscriptions/project/{projectId}">client.integrations.subscriptions.project.<a href="./src/vaif_client/resources/integrations/subscriptions/project.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/integrations/subscriptions/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

### Test

Types:

```python
from vaif_client.types.integrations.subscriptions import TestTestResponse
```

Methods:

- <code title="post /integrations/subscriptions/{id}/test">client.integrations.subscriptions.test.<a href="./src/vaif_client/resources/integrations/subscriptions/test.py">test</a>(id) -> <a href="./src/vaif_client/types/integrations/subscriptions/test_test_response.py">TestTestResponse</a></code>

# Jobs

## Dlq

### Project

Methods:

- <code title="get /jobs/dlq/project/{projectId}">client.jobs.dlq.project.<a href="./src/vaif_client/resources/jobs/dlq/project.py">retrieve</a>(project_id) -> None</code>

## Webhooks

### Delivery

Methods:

- <code title="get /jobs/webhooks/delivery/{deliveryId}">client.jobs.webhooks.delivery.<a href="./src/vaif_client/resources/jobs/webhooks/delivery.py">retrieve</a>(delivery_id) -> None</code>

### Project

Methods:

- <code title="get /jobs/webhooks/project/{projectId}">client.jobs.webhooks.project.<a href="./src/vaif_client/resources/jobs/webhooks/project.py">retrieve</a>(project_id) -> None</code>

# Logs

## Project

Types:

```python
from vaif_client.types.logs import ProjectRetrieveResponse
```

Methods:

- <code title="get /logs/project/{projectId}">client.logs.project.<a href="./src/vaif_client/resources/logs/project/project.py">retrieve</a>(project_id, \*\*<a href="src/vaif_client/types/logs/project_retrieve_params.py">params</a>) -> <a href="./src/vaif_client/types/logs/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

### Stream

Methods:

- <code title="get /logs/project/{projectId}/stream">client.logs.project.stream.<a href="./src/vaif_client/resources/logs/project/stream.py">get_stream</a>(project_id) -> None</code>

# Maintenance

Methods:

- <code title="get /maintenance">client.maintenance.<a href="./src/vaif_client/resources/maintenance.py">list</a>() -> None</code>

# Metrics

## Org

Methods:

- <code title="get /metrics/org/{orgId}">client.metrics.org.<a href="./src/vaif_client/resources/metrics/org.py">retrieve</a>(org_id) -> None</code>

## Project

Methods:

- <code title="get /metrics/project/{projectId}">client.metrics.project.<a href="./src/vaif_client/resources/metrics/project/project.py">retrieve</a>(project_id) -> None</code>

### Overview

Methods:

- <code title="get /metrics/project/{projectId}/overview">client.metrics.project.overview.<a href="./src/vaif_client/resources/metrics/project/overview.py">get_overview</a>(project_id) -> None</code>

# MongoDB

## Aggregate

Methods:

- <code title="post /mongodb/{collection}/aggregate">client.mongodb.aggregate.<a href="./src/vaif_client/resources/mongodb/aggregate.py">aggregate</a>(collection) -> None</code>
- <code title="post /mongodb/{collection}/aggregate/cursor">client.mongodb.aggregate.<a href="./src/vaif_client/resources/mongodb/aggregate.py">cursor</a>(collection) -> None</code>

## BulkWrite

Methods:

- <code title="post /mongodb/{collection}/bulkWrite">client.mongodb.bulk_write.<a href="./src/vaif_client/resources/mongodb/bulk_write.py">bulk_write</a>(collection) -> None</code>

## Collections

Methods:

- <code title="post /mongodb/collections">client.mongodb.collections.<a href="./src/vaif_client/resources/mongodb/collections/collections.py">create</a>() -> None</code>
- <code title="get /mongodb/collections">client.mongodb.collections.<a href="./src/vaif_client/resources/mongodb/collections/collections.py">list</a>() -> None</code>
- <code title="delete /mongodb/collections/{name}">client.mongodb.collections.<a href="./src/vaif_client/resources/mongodb/collections/collections.py">delete</a>(name) -> None</code>

### Rename

Methods:

- <code title="post /mongodb/collections/{name}/rename">client.mongodb.collections.rename.<a href="./src/vaif_client/resources/mongodb/collections/rename.py">rename</a>(name) -> None</code>

## Command

Methods:

- <code title="post /mongodb/command">client.mongodb.command.<a href="./src/vaif_client/resources/mongodb/command.py">create</a>() -> None</code>

## Count

Methods:

- <code title="post /mongodb/{collection}/count">client.mongodb.count.<a href="./src/vaif_client/resources/mongodb/count.py">count</a>(collection) -> None</code>

## Cursor

### Close

Methods:

- <code title="post /mongodb/{collection}/cursor/{cursorId}/close">client.mongodb.cursor.close.<a href="./src/vaif_client/resources/mongodb/cursor/close.py">close</a>(cursor_id, \*, collection) -> None</code>

### Next

Methods:

- <code title="post /mongodb/{collection}/cursor/{cursorId}/next">client.mongodb.cursor.next.<a href="./src/vaif_client/resources/mongodb/cursor/next.py">next</a>(cursor_id, \*, collection) -> None</code>

## DeleteMany

Methods:

- <code title="post /mongodb/{collection}/deleteMany">client.mongodb.delete_many.<a href="./src/vaif_client/resources/mongodb/delete_many.py">delete_many</a>(collection) -> None</code>

## DeleteOne

Methods:

- <code title="post /mongodb/{collection}/deleteOne">client.mongodb.delete_one.<a href="./src/vaif_client/resources/mongodb/delete_one.py">delete_one</a>(collection) -> None</code>

## Distinct

Methods:

- <code title="post /mongodb/{collection}/distinct">client.mongodb.distinct.<a href="./src/vaif_client/resources/mongodb/distinct.py">distinct</a>(collection) -> None</code>

## EstimatedCount

Methods:

- <code title="get /mongodb/{collection}/estimatedCount">client.mongodb.estimated_count.<a href="./src/vaif_client/resources/mongodb/estimated_count.py">get_estimated_count</a>(collection) -> None</code>

## Find

Methods:

- <code title="post /mongodb/{collection}/find/cursor">client.mongodb.find.<a href="./src/vaif_client/resources/mongodb/find.py">cursor</a>(collection) -> None</code>
- <code title="post /mongodb/{collection}/find">client.mongodb.find.<a href="./src/vaif_client/resources/mongodb/find.py">find</a>(collection) -> None</code>

## FindByID

Methods:

- <code title="get /mongodb/{collection}/findById/{id}">client.mongodb.find_by_id.<a href="./src/vaif_client/resources/mongodb/find_by_id.py">retrieve</a>(id, \*, collection) -> None</code>

## FindOne

Methods:

- <code title="post /mongodb/{collection}/findOne">client.mongodb.find_one.<a href="./src/vaif_client/resources/mongodb/find_one.py">find_one</a>(collection) -> None</code>

## FindOneAndDelete

Methods:

- <code title="post /mongodb/{collection}/findOneAndDelete">client.mongodb.find_one_and_delete.<a href="./src/vaif_client/resources/mongodb/find_one_and_delete.py">find_one_and_delete</a>(collection) -> None</code>

## FindOneAndReplace

Methods:

- <code title="post /mongodb/{collection}/findOneAndReplace">client.mongodb.find_one_and_replace.<a href="./src/vaif_client/resources/mongodb/find_one_and_replace.py">find_one_and_replace</a>(collection) -> None</code>

## FindOneAndUpdate

Methods:

- <code title="post /mongodb/{collection}/findOneAndUpdate">client.mongodb.find_one_and_update.<a href="./src/vaif_client/resources/mongodb/find_one_and_update.py">find_one_and_update</a>(collection) -> None</code>

## Indexes

Methods:

- <code title="delete /mongodb/{collection}/indexes/{indexName}">client.mongodb.indexes.<a href="./src/vaif_client/resources/mongodb/indexes.py">delete</a>(index_name, \*, collection) -> None</code>
- <code title="get /mongodb/{collection}/indexes">client.mongodb.indexes.<a href="./src/vaif_client/resources/mongodb/indexes.py">get_indexes</a>(collection) -> None</code>
- <code title="post /mongodb/{collection}/indexes">client.mongodb.indexes.<a href="./src/vaif_client/resources/mongodb/indexes.py">indexes</a>(collection) -> None</code>

## InsertMany

Methods:

- <code title="post /mongodb/{collection}/insertMany">client.mongodb.insert_many.<a href="./src/vaif_client/resources/mongodb/insert_many.py">insert_many</a>(collection) -> None</code>

## InsertOne

Methods:

- <code title="post /mongodb/{collection}/insertOne">client.mongodb.insert_one.<a href="./src/vaif_client/resources/mongodb/insert_one.py">insert_one</a>(collection) -> None</code>

## ReplaceOne

Methods:

- <code title="post /mongodb/{collection}/replaceOne">client.mongodb.replace_one.<a href="./src/vaif_client/resources/mongodb/replace_one.py">replace_one</a>(collection) -> None</code>

## UpdateMany

Methods:

- <code title="post /mongodb/{collection}/updateMany">client.mongodb.update_many.<a href="./src/vaif_client/resources/mongodb/update_many.py">update_many</a>(collection) -> None</code>

## UpdateOne

Methods:

- <code title="post /mongodb/{collection}/updateOne">client.mongodb.update_one.<a href="./src/vaif_client/resources/mongodb/update_one.py">update_one</a>(collection) -> None</code>

# OAuth

## Callback

Methods:

- <code title="post /oauth/callback">client.oauth.callback.<a href="./src/vaif_client/resources/oauth/callback.py">create</a>() -> None</code>

## Org

Types:

```python
from vaif_client.types.oauth import OrgRetrieveResponse
```

Methods:

- <code title="get /oauth/org/{orgId}">client.oauth.org.<a href="./src/vaif_client/resources/oauth/org/org.py">retrieve</a>(org_id) -> <a href="./src/vaif_client/types/oauth/org_retrieve_response.py">OrgRetrieveResponse</a></code>

### Configure

Types:

```python
from vaif_client.types.oauth.org import ConfigureConfigureResponse
```

Methods:

- <code title="post /oauth/org/{orgId}/configure">client.oauth.org.configure.<a href="./src/vaif_client/resources/oauth/org/configure.py">configure</a>(org_id, \*\*<a href="src/vaif_client/types/oauth/org/configure_configure_params.py">params</a>) -> <a href="./src/vaif_client/types/oauth/org/configure_configure_response.py">ConfigureConfigureResponse</a></code>

### Provider

Types:

```python
from vaif_client.types.oauth.org import ProviderUpdateResponse, ProviderDeleteResponse
```

Methods:

- <code title="patch /oauth/org/{orgId}/provider/{provider}">client.oauth.org.provider.<a href="./src/vaif_client/resources/oauth/org/provider/provider.py">update</a>(provider, \*, org_id, \*\*<a href="src/vaif_client/types/oauth/org/provider_update_params.py">params</a>) -> <a href="./src/vaif_client/types/oauth/org/provider_update_response.py">ProviderUpdateResponse</a></code>
- <code title="delete /oauth/org/{orgId}/provider/{provider}">client.oauth.org.provider.<a href="./src/vaif_client/resources/oauth/org/provider/provider.py">delete</a>(provider, \*, org_id) -> <a href="./src/vaif_client/types/oauth/org/provider_delete_response.py">ProviderDeleteResponse</a></code>

#### Authorize

Types:

```python
from vaif_client.types.oauth.org.provider import AuthorizeGetAuthorizeResponse
```

Methods:

- <code title="get /oauth/org/{orgId}/provider/{provider}/authorize">client.oauth.org.provider.authorize.<a href="./src/vaif_client/resources/oauth/org/provider/authorize.py">get_authorize</a>(provider, \*, org_id) -> <a href="./src/vaif_client/types/oauth/org/provider/authorize_get_authorize_response.py">AuthorizeGetAuthorizeResponse</a></code>

#### Refresh

Types:

```python
from vaif_client.types.oauth.org.provider import RefreshRefreshResponse
```

Methods:

- <code title="post /oauth/org/{orgId}/provider/{provider}/refresh">client.oauth.org.provider.refresh.<a href="./src/vaif_client/resources/oauth/org/provider/refresh.py">refresh</a>(provider, \*, org_id) -> <a href="./src/vaif_client/types/oauth/org/provider/refresh_refresh_response.py">RefreshRefreshResponse</a></code>

# Onboarding

## Org

Methods:

- <code title="get /onboarding/org/{orgId}">client.onboarding.org.<a href="./src/vaif_client/resources/onboarding/org/org.py">retrieve</a>(org_id) -> None</code>

### AutoSetup

Methods:

- <code title="post /onboarding/org/{orgId}/auto-setup">client.onboarding.org.auto_setup.<a href="./src/vaif_client/resources/onboarding/org/auto_setup.py">auto_setup</a>(org_id) -> None</code>

### CompleteStep

Methods:

- <code title="post /onboarding/org/{orgId}/complete-step">client.onboarding.org.complete_step.<a href="./src/vaif_client/resources/onboarding/org/complete_step.py">complete_step</a>(org_id) -> None</code>

# OpenAPI

## Full

Methods:

- <code title="get /openapi/full">client.openapi.full.<a href="./src/vaif_client/resources/openapi/full.py">list</a>() -> None</code>

## Project

Methods:

- <code title="get /openapi/project/{projectId}">client.openapi.project.<a href="./src/vaif_client/resources/openapi/project.py">retrieve</a>(project_id) -> None</code>

# Orgs

Methods:

- <code title="post /orgs/">client.orgs.<a href="./src/vaif_client/resources/orgs/orgs.py">create</a>() -> None</code>
- <code title="get /orgs/">client.orgs.<a href="./src/vaif_client/resources/orgs/orgs.py">list</a>() -> None</code>

## BillingContacts

Types:

```python
from vaif_client.types.orgs import (
    BillingContactDeleteResponse,
    BillingContactBillingContactsResponse,
    BillingContactGetBillingContactsResponse,
)
```

Methods:

- <code title="delete /orgs/{orgId}/billing-contacts/{contactId}">client.orgs.billing_contacts.<a href="./src/vaif_client/resources/orgs/billing_contacts.py">delete</a>(contact_id, \*, org_id) -> <a href="./src/vaif_client/types/orgs/billing_contact_delete_response.py">BillingContactDeleteResponse</a></code>
- <code title="post /orgs/{orgId}/billing-contacts">client.orgs.billing_contacts.<a href="./src/vaif_client/resources/orgs/billing_contacts.py">billing_contacts</a>(org_id, \*\*<a href="src/vaif_client/types/orgs/billing_contact_billing_contacts_params.py">params</a>) -> <a href="./src/vaif_client/types/orgs/billing_contact_billing_contacts_response.py">BillingContactBillingContactsResponse</a></code>
- <code title="get /orgs/{orgId}/billing-contacts">client.orgs.billing_contacts.<a href="./src/vaif_client/resources/orgs/billing_contacts.py">get_billing_contacts</a>(org_id) -> <a href="./src/vaif_client/types/orgs/billing_contact_get_billing_contacts_response.py">BillingContactGetBillingContactsResponse</a></code>

## CheckName

Methods:

- <code title="get /orgs/check-name">client.orgs.check_name.<a href="./src/vaif_client/resources/orgs/check_name.py">list</a>() -> None</code>

## Invites

Methods:

- <code title="delete /orgs/{orgId}/invites/{inviteId}">client.orgs.invites.<a href="./src/vaif_client/resources/orgs/invites/invites.py">delete</a>(invite_id, \*, org_id) -> None</code>
- <code title="get /orgs/{orgId}/invites">client.orgs.invites.<a href="./src/vaif_client/resources/orgs/invites/invites.py">get_invites</a>(org_id) -> None</code>

### Accept

Methods:

- <code title="post /orgs/invites/accept">client.orgs.invites.accept.<a href="./src/vaif_client/resources/orgs/invites/accept.py">create</a>() -> None</code>

## Members

Methods:

- <code title="get /orgs/{orgId}/members">client.orgs.members.<a href="./src/vaif_client/resources/orgs/members.py">get_members</a>(org_id) -> None</code>
- <code title="post /orgs/{orgId}/members/invite">client.orgs.members.<a href="./src/vaif_client/resources/orgs/members.py">invite</a>(org_id) -> None</code>

## Membership

Methods:

- <code title="get /orgs/{orgId}/membership">client.orgs.membership.<a href="./src/vaif_client/resources/orgs/membership.py">get_membership</a>(org_id) -> None</code>

## Profile

Methods:

- <code title="get /orgs/{orgId}/profile">client.orgs.profile.<a href="./src/vaif_client/resources/orgs/profile.py">get_profile</a>(org_id) -> None</code>
- <code title="patch /orgs/{orgId}/profile">client.orgs.profile.<a href="./src/vaif_client/resources/orgs/profile.py">profile</a>(org_id) -> None</code>

# Plans

Types:

```python
from vaif_client.types import PlanRetrieveResponse
```

Methods:

- <code title="get /plans/{planId}">client.plans.<a href="./src/vaif_client/resources/plans/plans.py">retrieve</a>(plan_id) -> <a href="./src/vaif_client/types/plan_retrieve_response.py">PlanRetrieveResponse</a></code>

## Apply

Types:

```python
from vaif_client.types.plans import ApplyCreateResponse
```

Methods:

- <code title="post /plans/apply">client.plans.apply.<a href="./src/vaif_client/resources/plans/apply.py">create</a>(\*\*<a href="src/vaif_client/types/plans/apply_create_params.py">params</a>) -> <a href="./src/vaif_client/types/plans/apply_create_response.py">ApplyCreateResponse</a></code>

## Org

Types:

```python
from vaif_client.types.plans import OrgRetrieveResponse
```

Methods:

- <code title="get /plans/org/{orgId}">client.plans.org.<a href="./src/vaif_client/resources/plans/org.py">retrieve</a>(org_id) -> <a href="./src/vaif_client/types/plans/org_retrieve_response.py">OrgRetrieveResponse</a></code>

## Save

Types:

```python
from vaif_client.types.plans import SaveCreateResponse
```

Methods:

- <code title="post /plans/save">client.plans.save.<a href="./src/vaif_client/resources/plans/save.py">create</a>(\*\*<a href="src/vaif_client/types/plans/save_create_params.py">params</a>) -> <a href="./src/vaif_client/types/plans/save_create_response.py">SaveCreateResponse</a></code>

# Pricing

## AIFeatures

Methods:

- <code title="get /pricing/ai-features">client.pricing.ai_features.<a href="./src/vaif_client/resources/pricing/ai_features.py">list</a>() -> None</code>

## Compare

Methods:

- <code title="get /pricing/compare">client.pricing.compare.<a href="./src/vaif_client/resources/pricing/compare.py">list</a>() -> None</code>

## Enterprise

Methods:

- <code title="get /pricing/enterprise">client.pricing.enterprise.<a href="./src/vaif_client/resources/pricing/enterprise.py">list</a>() -> None</code>

## Plans

Methods:

- <code title="get /pricing/plans/{plan}">client.pricing.plans.<a href="./src/vaif_client/resources/pricing/plans.py">retrieve</a>(plan) -> None</code>
- <code title="get /pricing/plans">client.pricing.plans.<a href="./src/vaif_client/resources/pricing/plans.py">list</a>() -> None</code>

# Projects

Types:

```python
from vaif_client.types import ProjectCreateResponse, ProjectUpdateResponse
```

Methods:

- <code title="post /projects/">client.projects.<a href="./src/vaif_client/resources/projects/projects.py">create</a>(\*\*<a href="src/vaif_client/types/project_create_params.py">params</a>) -> <a href="./src/vaif_client/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /projects/{projectId}">client.projects.<a href="./src/vaif_client/resources/projects/projects.py">retrieve</a>(project_id) -> None</code>
- <code title="patch /projects/{projectId}">client.projects.<a href="./src/vaif_client/resources/projects/projects.py">update</a>(project_id, \*\*<a href="src/vaif_client/types/project_update_params.py">params</a>) -> <a href="./src/vaif_client/types/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="get /projects/">client.projects.<a href="./src/vaif_client/resources/projects/projects.py">list</a>() -> None</code>
- <code title="delete /projects/{projectId}">client.projects.<a href="./src/vaif_client/resources/projects/projects.py">delete</a>(project_id) -> None</code>

## APIKeys

Types:

```python
from vaif_client.types.projects import APIKeyUpdateResponse, APIKeyAPIKeysResponse
```

Methods:

- <code title="patch /projects/{projectId}/api-keys/{keyId}">client.projects.api_keys.<a href="./src/vaif_client/resources/projects/api_keys/api_keys.py">update</a>(key_id, \*, project_id, \*\*<a href="src/vaif_client/types/projects/api_key_update_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/api_key_update_response.py">APIKeyUpdateResponse</a></code>
- <code title="post /projects/{projectId}/api-keys">client.projects.api_keys.<a href="./src/vaif_client/resources/projects/api_keys/api_keys.py">api_keys</a>(project_id, \*\*<a href="src/vaif_client/types/projects/api_key_api_keys_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/api_key_api_keys_response.py">APIKeyAPIKeysResponse</a></code>
- <code title="get /projects/{projectId}/api-keys">client.projects.api_keys.<a href="./src/vaif_client/resources/projects/api_keys/api_keys.py">get_api_keys</a>(project_id) -> None</code>

### Revoke

Methods:

- <code title="post /projects/{projectId}/api-keys/{keyId}/revoke">client.projects.api_keys.revoke.<a href="./src/vaif_client/resources/projects/api_keys/revoke.py">revoke</a>(key_id, \*, project_id) -> None</code>

### Rotate

Methods:

- <code title="post /projects/{projectId}/api-keys/{keyId}/rotate">client.projects.api_keys.rotate.<a href="./src/vaif_client/resources/projects/api_keys/rotate.py">rotate</a>(key_id, \*, project_id) -> None</code>

## Auth

Types:

```python
from vaif_client.types.projects import (
    AuthUpdateResponse,
    AuthConfirmResponse,
    AuthForgotPasswordResponse,
    AuthLoginResponse,
    AuthResetPasswordResponse,
    AuthSettingsResponse,
    AuthSignupResponse,
)
```

Methods:

- <code title="put /projects/{projectId}/auth/oauth-apps/{provider}">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">update</a>(provider, \*, project_id, \*\*<a href="src/vaif_client/types/projects/auth_update_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_update_response.py">AuthUpdateResponse</a></code>
- <code title="delete /projects/{projectId}/auth/oauth-apps/{provider}">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">delete</a>(provider, \*, project_id) -> None</code>
- <code title="post /projects/{projectId}/auth/verify-email/confirm">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">confirm</a>(project_id, \*\*<a href="src/vaif_client/types/projects/auth_confirm_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_confirm_response.py">AuthConfirmResponse</a></code>
- <code title="post /projects/{projectId}/auth/forgot-password">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">forgot_password</a>(project_id, \*\*<a href="src/vaif_client/types/projects/auth_forgot_password_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_forgot_password_response.py">AuthForgotPasswordResponse</a></code>
- <code title="get /projects/{projectId}/auth/me">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">get_me</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/auth/oauth-apps">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">get_oauth_apps</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/auth/settings">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">get_settings</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/auth/login">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">login</a>(project_id, \*\*<a href="src/vaif_client/types/projects/auth_login_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="post /projects/{projectId}/auth/logout">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">logout</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/auth/refresh">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">refresh</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/auth/reset-password">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">reset_password</a>(project_id, \*\*<a href="src/vaif_client/types/projects/auth_reset_password_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_reset_password_response.py">AuthResetPasswordResponse</a></code>
- <code title="post /projects/{projectId}/auth/verify-email/send">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">send</a>(project_id) -> None</code>
- <code title="patch /projects/{projectId}/auth/settings">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">settings</a>(project_id, \*\*<a href="src/vaif_client/types/projects/auth_settings_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_settings_response.py">AuthSettingsResponse</a></code>
- <code title="post /projects/{projectId}/auth/signup">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">signup</a>(project_id, \*\*<a href="src/vaif_client/types/projects/auth_signup_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/auth_signup_response.py">AuthSignupResponse</a></code>
- <code title="post /projects/{projectId}/auth/sync-users">client.projects.auth.<a href="./src/vaif_client/resources/projects/auth.py">sync_users</a>(project_id) -> None</code>

## Database

Methods:

- <code title="post /projects/{projectId}/database/dedicated">client.projects.database.<a href="./src/vaif_client/resources/projects/database.py">dedicated</a>(project_id, \*\*<a href="src/vaif_client/types/projects/database_dedicated_params.py">params</a>) -> object</code>
- <code title="delete /projects/{projectId}/database/dedicated">client.projects.database.<a href="./src/vaif_client/resources/projects/database.py">dedicated2</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/database/dedicated/connection">client.projects.database.<a href="./src/vaif_client/resources/projects/database.py">get_connection</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/database/dedicated">client.projects.database.<a href="./src/vaif_client/resources/projects/database.py">get_dedicated</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/database/dedicated/status">client.projects.database.<a href="./src/vaif_client/resources/projects/database.py">get_status</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/database/dedicated/restart">client.projects.database.<a href="./src/vaif_client/resources/projects/database.py">restart</a>(project_id) -> None</code>

## EnvVars

Methods:

- <code title="patch /projects/{projectId}/env-vars/{envVarId}">client.projects.env_vars.<a href="./src/vaif_client/resources/projects/env_vars/env_vars.py">update</a>(env_var_id, \*, project_id) -> None</code>
- <code title="delete /projects/{projectId}/env-vars/{envVarId}">client.projects.env_vars.<a href="./src/vaif_client/resources/projects/env_vars/env_vars.py">delete</a>(env_var_id, \*, project_id) -> None</code>
- <code title="post /projects/{projectId}/env-vars">client.projects.env_vars.<a href="./src/vaif_client/resources/projects/env_vars/env_vars.py">env_vars</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/env-vars">client.projects.env_vars.<a href="./src/vaif_client/resources/projects/env_vars/env_vars.py">get_env_vars</a>(project_id) -> None</code>

### Value

Methods:

- <code title="get /projects/{projectId}/env-vars/{envVarId}/value">client.projects.env_vars.value.<a href="./src/vaif_client/resources/projects/env_vars/value.py">get_value</a>(env_var_id, \*, project_id) -> None</code>

## Environments

Methods:

- <code title="patch /projects/{projectId}/environments/{envId}">client.projects.environments.<a href="./src/vaif_client/resources/projects/environments/environments.py">update</a>(env_id, \*, project_id) -> None</code>
- <code title="delete /projects/{projectId}/environments/{envId}">client.projects.environments.<a href="./src/vaif_client/resources/projects/environments/environments.py">delete</a>(env_id, \*, project_id) -> None</code>
- <code title="post /projects/{projectId}/environments/backfill-urls">client.projects.environments.<a href="./src/vaif_client/resources/projects/environments/environments.py">backfill_urls</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/environments/bootstrap">client.projects.environments.<a href="./src/vaif_client/resources/projects/environments/environments.py">bootstrap</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/environments">client.projects.environments.<a href="./src/vaif_client/resources/projects/environments/environments.py">environments</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/environments">client.projects.environments.<a href="./src/vaif_client/resources/projects/environments/environments.py">get_environments</a>(project_id) -> None</code>

### DomainStatus

Methods:

- <code title="get /projects/{projectId}/environments/{envId}/domain-status">client.projects.environments.domain_status.<a href="./src/vaif_client/resources/projects/environments/domain_status.py">get_domain_status</a>(env_id, \*, project_id) -> None</code>

### DomainVerification

Methods:

- <code title="get /projects/{projectId}/environments/{envId}/domain-verification">client.projects.environments.domain_verification.<a href="./src/vaif_client/resources/projects/environments/domain_verification.py">get_domain_verification</a>(env_id, \*, project_id) -> None</code>

### ProvisionSsl

Methods:

- <code title="post /projects/{projectId}/environments/{envId}/provision-ssl">client.projects.environments.provision_ssl.<a href="./src/vaif_client/resources/projects/environments/provision_ssl.py">provision_ssl</a>(env_id, \*, project_id) -> None</code>

### VerifyCname

Methods:

- <code title="post /projects/{projectId}/environments/{envId}/verify-cname">client.projects.environments.verify_cname.<a href="./src/vaif_client/resources/projects/environments/verify_cname.py">verify_cname</a>(env_id, \*, project_id) -> None</code>

### VerifyDomain

Methods:

- <code title="post /projects/{projectId}/environments/{envId}/verify-domain">client.projects.environments.verify_domain.<a href="./src/vaif_client/resources/projects/environments/verify_domain.py">verify_domain</a>(env_id, \*, project_id) -> None</code>

## GitHub

Methods:

- <code title="post /projects/{projectId}/github/branch">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">branch</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/github/connect">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">connect</a>(project_id) -> None</code>
- <code title="delete /projects/{projectId}/github/disconnect">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">disconnect</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/github/branches">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">get_branches</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/github/repos">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">get_repos</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/github/status">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">get_status</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/github/tracked-repos">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">get_tracked_repos</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/github/pull">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">pull</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/github/push">client.projects.github.<a href="./src/vaif_client/resources/projects/github.py">push</a>(project_id) -> None</code>

## Infrastructure

Methods:

- <code title="delete /projects/{projectId}/infrastructure/{instanceId}">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">delete</a>(instance_id, \*, project_id) -> None</code>
- <code title="get /projects/{projectId}/infrastructure">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">get_infrastructure</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/infrastructure/migration-status">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">get_migration_status</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/infrastructure/migration/progress">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">get_progress</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/infrastructure/provision">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">provision</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/infrastructure/provision-custom">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">provision_custom</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/infrastructure/migration/retry">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">retry</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/infrastructure/migration/rollback">client.projects.infrastructure.<a href="./src/vaif_client/resources/projects/infrastructure/infrastructure.py">rollback</a>(project_id) -> None</code>

### Metrics

Methods:

- <code title="get /projects/{projectId}/infrastructure/{instanceId}/metrics">client.projects.infrastructure.metrics.<a href="./src/vaif_client/resources/projects/infrastructure/metrics.py">get_metrics</a>(instance_id, \*, project_id) -> None</code>

### MigrateNow

Methods:

- <code title="post /projects/{projectId}/infrastructure/{instanceId}/migrate-now">client.projects.infrastructure.migrate_now.<a href="./src/vaif_client/resources/projects/infrastructure/migrate_now.py">migrate_now</a>(instance_id, \*, project_id) -> None</code>

### Replicas

Methods:

- <code title="get /projects/{projectId}/infrastructure/{instanceId}/replicas">client.projects.infrastructure.replicas.<a href="./src/vaif_client/resources/projects/infrastructure/replicas.py">get_replicas</a>(instance_id, \*, project_id) -> None</code>
- <code title="post /projects/{projectId}/infrastructure/{instanceId}/replica">client.projects.infrastructure.replicas.<a href="./src/vaif_client/resources/projects/infrastructure/replicas.py">replica</a>(instance_id, \*, project_id) -> None</code>

### Resize

Methods:

- <code title="post /projects/{projectId}/infrastructure/{instanceId}/resize">client.projects.infrastructure.resize.<a href="./src/vaif_client/resources/projects/infrastructure/resize.py">resize</a>(instance_id, \*, project_id) -> None</code>

### ResizeCustom

Methods:

- <code title="post /projects/{projectId}/infrastructure/{instanceId}/resize-custom">client.projects.infrastructure.resize_custom.<a href="./src/vaif_client/resources/projects/infrastructure/resize_custom.py">resize_custom</a>(instance_id, \*, project_id) -> None</code>

### Start

Methods:

- <code title="post /projects/{projectId}/infrastructure/{instanceId}/start">client.projects.infrastructure.start.<a href="./src/vaif_client/resources/projects/infrastructure/start.py">start</a>(instance_id, \*, project_id) -> None</code>

### Stop

Methods:

- <code title="post /projects/{projectId}/infrastructure/{instanceId}/stop">client.projects.infrastructure.stop.<a href="./src/vaif_client/resources/projects/infrastructure/stop.py">stop</a>(instance_id, \*, project_id) -> None</code>

### UpgradeOptions

Methods:

- <code title="get /projects/{projectId}/infrastructure/{instanceId}/upgrade-options">client.projects.infrastructure.upgrade_options.<a href="./src/vaif_client/resources/projects/infrastructure/upgrade_options.py">get_upgrade_options</a>(instance_id, \*, project_id) -> None</code>

## Members

Methods:

- <code title="delete /projects/{projectId}/members/{userId}">client.projects.members.<a href="./src/vaif_client/resources/projects/members.py">delete</a>(user_id, \*, project_id) -> None</code>
- <code title="get /projects/{projectId}/members">client.projects.members.<a href="./src/vaif_client/resources/projects/members.py">get_members</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/members">client.projects.members.<a href="./src/vaif_client/resources/projects/members.py">members</a>(project_id) -> None</code>

## Region

Types:

```python
from vaif_client.types.projects import RegionRegionResponse
```

Methods:

- <code title="get /projects/{projectId}/region">client.projects.region.<a href="./src/vaif_client/resources/projects/region.py">get_region</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/region">client.projects.region.<a href="./src/vaif_client/resources/projects/region.py">region</a>(project_id, \*\*<a href="src/vaif_client/types/projects/region_region_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/region_region_response.py">RegionRegionResponse</a></code>

## Settings

Methods:

- <code title="patch /projects/{projectId}/settings/addons">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">addons</a>(project_id) -> None</code>
- <code title="patch /projects/{projectId}/settings/api">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">api</a>(project_id) -> None</code>
- <code title="patch /projects/{projectId}/settings/compute">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">compute</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/settings/addons">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">get_addons</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/settings/api">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">get_api</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/settings/compute">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">get_compute</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/settings/jwt">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">get_jwt</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/settings">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">get_settings</a>(project_id) -> None</code>
- <code title="patch /projects/{projectId}/settings/jwt">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">jwt</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/settings/jwt/rotate">client.projects.settings.<a href="./src/vaif_client/resources/projects/settings.py">rotate</a>(project_id) -> None</code>

## Storage

Types:

```python
from vaif_client.types.projects import StorageSettingsResponse
```

Methods:

- <code title="get /projects/{projectId}/storage/settings">client.projects.storage.<a href="./src/vaif_client/resources/projects/storage.py">get_settings</a>(project_id) -> None</code>
- <code title="patch /projects/{projectId}/storage/settings">client.projects.storage.<a href="./src/vaif_client/resources/projects/storage.py">settings</a>(project_id, \*\*<a href="src/vaif_client/types/projects/storage_settings_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/storage_settings_response.py">StorageSettingsResponse</a></code>

## Terminal

Methods:

- <code title="post /projects/{projectId}/terminal/exec">client.projects.terminal.<a href="./src/vaif_client/resources/projects/terminal.py">exec</a>(project_id) -> None</code>
- <code title="get /projects/{projectId}/terminal/sessions">client.projects.terminal.<a href="./src/vaif_client/resources/projects/terminal.py">get_sessions</a>(project_id) -> None</code>

## Users

Types:

```python
from vaif_client.types.projects import UserUpdateResponse, UserUsersResponse
```

Methods:

- <code title="get /projects/{projectId}/users/{userId}">client.projects.users.<a href="./src/vaif_client/resources/projects/users/users.py">retrieve</a>(user_id, \*, project_id) -> None</code>
- <code title="patch /projects/{projectId}/users/{userId}">client.projects.users.<a href="./src/vaif_client/resources/projects/users/users.py">update</a>(user_id, \*, project_id, \*\*<a href="src/vaif_client/types/projects/user_update_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/user_update_response.py">UserUpdateResponse</a></code>
- <code title="delete /projects/{projectId}/users/{userId}">client.projects.users.<a href="./src/vaif_client/resources/projects/users/users.py">delete</a>(user_id, \*, project_id) -> None</code>
- <code title="get /projects/{projectId}/users">client.projects.users.<a href="./src/vaif_client/resources/projects/users/users.py">get_users</a>(project_id) -> None</code>
- <code title="post /projects/{projectId}/users">client.projects.users.<a href="./src/vaif_client/resources/projects/users/users.py">users</a>(project_id, \*\*<a href="src/vaif_client/types/projects/user_users_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/user_users_response.py">UserUsersResponse</a></code>

### Ban

Types:

```python
from vaif_client.types.projects.users import BanBanResponse
```

Methods:

- <code title="post /projects/{projectId}/users/{userId}/ban">client.projects.users.ban.<a href="./src/vaif_client/resources/projects/users/ban.py">ban</a>(user_id, \*, project_id, \*\*<a href="src/vaif_client/types/projects/users/ban_ban_params.py">params</a>) -> <a href="./src/vaif_client/types/projects/users/ban_ban_response.py">BanBanResponse</a></code>

### Sessions

Methods:

- <code title="delete /projects/{projectId}/users/{userId}/sessions/{sessionId}">client.projects.users.sessions.<a href="./src/vaif_client/resources/projects/users/sessions.py">delete</a>(session_id, \*, project_id, user_id) -> None</code>
- <code title="get /projects/{projectId}/users/{userId}/sessions">client.projects.users.sessions.<a href="./src/vaif_client/resources/projects/users/sessions.py">get_sessions</a>(user_id, \*, project_id) -> None</code>
- <code title="post /projects/{projectId}/users/{userId}/sessions/revoke-all">client.projects.users.sessions.<a href="./src/vaif_client/resources/projects/users/sessions.py">revoke_all</a>(user_id, \*, project_id) -> None</code>

### Unban

Methods:

- <code title="post /projects/{projectId}/users/{userId}/unban">client.projects.users.unban.<a href="./src/vaif_client/resources/projects/users/unban.py">unban</a>(user_id, \*, project_id) -> None</code>

# Quickstart

## Project

Types:

```python
from vaif_client.types.quickstart import ProjectRetrieveResponse
```

Methods:

- <code title="get /quickstart/project/{projectId}">client.quickstart.project.<a href="./src/vaif_client/resources/quickstart/project/project.py">retrieve</a>(project_id, \*\*<a href="src/vaif_client/types/quickstart/project_retrieve_params.py">params</a>) -> str</code>

### Json

Types:

```python
from vaif_client.types.quickstart.project import JsonGetJsonResponse
```

Methods:

- <code title="get /quickstart/project/{projectId}/json">client.quickstart.project.json.<a href="./src/vaif_client/resources/quickstart/project/json.py">get_json</a>(project_id) -> <a href="./src/vaif_client/types/quickstart/project/json_get_json_response.py">JsonGetJsonResponse</a></code>

# Realtime

## Connections

### Project

Methods:

- <code title="get /realtime/connections/project/{projectId}">client.realtime.connections.project.<a href="./src/vaif_client/resources/realtime/connections/project.py">retrieve</a>(project_id) -> None</code>

## EnableAll

Methods:

- <code title="post /realtime/enable-all">client.realtime.enable_all.<a href="./src/vaif_client/resources/realtime/enable_all.py">create</a>() -> None</code>

## Events

### Project

Methods:

- <code title="get /realtime/events/project/{projectId}">client.realtime.events.project.<a href="./src/vaif_client/resources/realtime/events/project.py">retrieve</a>(project_id) -> None</code>

## Install

Methods:

- <code title="post /realtime/install">client.realtime.install.<a href="./src/vaif_client/resources/realtime/install.py">create</a>() -> None</code>

## Stats

### Project

Methods:

- <code title="get /realtime/stats/project/{projectId}">client.realtime.stats.project.<a href="./src/vaif_client/resources/realtime/stats/project.py">retrieve</a>(project_id) -> None</code>

## Status

### Project

Methods:

- <code title="get /realtime/status/project/{projectId}">client.realtime.status.project.<a href="./src/vaif_client/resources/realtime/status/project.py">retrieve</a>(project_id) -> None</code>

## Subscriptions

### Project

Methods:

- <code title="get /realtime/subscriptions/project/{projectId}">client.realtime.subscriptions.project.<a href="./src/vaif_client/resources/realtime/subscriptions/project.py">retrieve</a>(project_id) -> None</code>

# Refunds

Methods:

- <code title="get /refunds/{id}">client.refunds.<a href="./src/vaif_client/resources/refunds/refunds.py">retrieve</a>(id) -> None</code>

## Org

Methods:

- <code title="get /refunds/org/{orgId}">client.refunds.org.<a href="./src/vaif_client/resources/refunds/org.py">retrieve</a>(org_id) -> None</code>

# Regions

Methods:

- <code title="post /regions/">client.regions.<a href="./src/vaif_client/resources/regions/regions.py">create</a>() -> None</code>
- <code title="get /regions/{key}">client.regions.<a href="./src/vaif_client/resources/regions/regions.py">retrieve</a>(key) -> None</code>
- <code title="patch /regions/{key}">client.regions.<a href="./src/vaif_client/resources/regions/regions.py">update</a>(key) -> None</code>
- <code title="get /regions/">client.regions.<a href="./src/vaif_client/resources/regions/regions.py">list</a>() -> None</code>

## All

Methods:

- <code title="get /regions/all">client.regions.all.<a href="./src/vaif_client/resources/regions/all.py">list</a>() -> None</code>

## Health

Methods:

- <code title="get /regions/health">client.regions.health.<a href="./src/vaif_client/resources/regions/health/health.py">list</a>() -> None</code>

### Check

Methods:

- <code title="post /regions/health/check">client.regions.health.check.<a href="./src/vaif_client/resources/regions/health/check.py">create</a>() -> None</code>

## Metrics

Methods:

- <code title="get /regions/{key}/metrics">client.regions.metrics.<a href="./src/vaif_client/resources/regions/metrics.py">get_metrics</a>(key) -> None</code>

# Rls

## Policies

Methods:

- <code title="post /rls/policies/{projectId}">client.rls.policies.<a href="./src/vaif_client/resources/rls/policies/policies.py">create</a>(project_id) -> None</code>
- <code title="get /rls/policies/{projectId}">client.rls.policies.<a href="./src/vaif_client/resources/rls/policies/policies.py">retrieve</a>(project_id) -> None</code>
- <code title="patch /rls/policies/{policyId}">client.rls.policies.<a href="./src/vaif_client/resources/rls/policies/policies.py">update</a>(policy_id) -> None</code>
- <code title="delete /rls/policies/{policyId}">client.rls.policies.<a href="./src/vaif_client/resources/rls/policies/policies.py">delete</a>(policy_id) -> None</code>

### Toggle

Methods:

- <code title="post /rls/policies/{policyId}/toggle">client.rls.policies.toggle.<a href="./src/vaif_client/resources/rls/policies/toggle.py">toggle</a>(policy_id) -> None</code>

# SchemaEngine

## Apply

Types:

```python
from vaif_client.types.schema_engine import ApplyCreateResponse
```

Methods:

- <code title="post /schema-engine/apply">client.schema_engine.apply.<a href="./src/vaif_client/resources/schema_engine/apply.py">create</a>(\*\*<a href="src/vaif_client/types/schema_engine/apply_create_params.py">params</a>) -> <a href="./src/vaif_client/types/schema_engine/apply_create_response.py">ApplyCreateResponse</a></code>

## Changes

Types:

```python
from vaif_client.types.schema_engine import ChangeGetChangesResponse
```

Methods:

- <code title="get /schema-engine/{projectId}/changes">client.schema_engine.changes.<a href="./src/vaif_client/resources/schema_engine/changes.py">get_changes</a>(project_id) -> <a href="./src/vaif_client/types/schema_engine/change_get_changes_response.py">ChangeGetChangesResponse</a></code>

## Introspect

Types:

```python
from vaif_client.types.schema_engine import IntrospectRetrieveResponse
```

Methods:

- <code title="get /schema-engine/introspect/{projectId}">client.schema_engine.introspect.<a href="./src/vaif_client/resources/schema_engine/introspect.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/schema_engine/introspect_retrieve_response.py">IntrospectRetrieveResponse</a></code>

## Migrations

### Project

Types:

```python
from vaif_client.types.schema_engine.migrations import ProjectRetrieveResponse
```

Methods:

- <code title="get /schema-engine/migrations/project/{projectId}">client.schema_engine.migrations.project.<a href="./src/vaif_client/resources/schema_engine/migrations/project.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/schema_engine/migrations/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

## Preview

Types:

```python
from vaif_client.types.schema_engine import PreviewCreateResponse
```

Methods:

- <code title="post /schema-engine/preview">client.schema_engine.preview.<a href="./src/vaif_client/resources/schema_engine/preview.py">create</a>(\*\*<a href="src/vaif_client/types/schema_engine/preview_create_params.py">params</a>) -> <a href="./src/vaif_client/types/schema_engine/preview_create_response.py">PreviewCreateResponse</a></code>

## Query

Types:

```python
from vaif_client.types.schema_engine import QueryCreateResponse
```

Methods:

- <code title="post /schema-engine/query/{projectId}">client.schema_engine.query.<a href="./src/vaif_client/resources/schema_engine/query.py">create</a>(project_id, \*\*<a href="src/vaif_client/types/schema_engine/query_create_params.py">params</a>) -> <a href="./src/vaif_client/types/schema_engine/query_create_response.py">QueryCreateResponse</a></code>

# Schemas

Types:

```python
from vaif_client.types import SchemaCreateResponse
```

Methods:

- <code title="post /schemas/">client.schemas.<a href="./src/vaif_client/resources/schemas/schemas.py">create</a>(\*\*<a href="src/vaif_client/types/schema_create_params.py">params</a>) -> <a href="./src/vaif_client/types/schema_create_response.py">SchemaCreateResponse</a></code>

## Project

Types:

```python
from vaif_client.types.schemas import ProjectRetrieveResponse
```

Methods:

- <code title="get /schemas/project/{projectId}">client.schemas.project.<a href="./src/vaif_client/resources/schemas/project.py">retrieve</a>(project_id) -> <a href="./src/vaif_client/types/schemas/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

# SDK

## Generate

Methods:

- <code title="post /sdk/generate">client.sdk.generate.<a href="./src/vaif_client/resources/sdk/generate.py">create</a>() -> None</code>

# Security

## Audit

Methods:

- <code title="get /security/audit/{projectId}">client.security.audit.<a href="./src/vaif_client/resources/security/audit.py">retrieve</a>(project_id) -> None</code>

## Overview

Methods:

- <code title="get /security/overview/{projectId}">client.security.overview.<a href="./src/vaif_client/resources/security/overview.py">retrieve</a>(project_id) -> None</code>

# SSO

## Org

Methods:

- <code title="get /sso/org/{orgId}">client.sso.org.<a href="./src/vaif_client/resources/sso/org/org.py">retrieve</a>(org_id) -> None</code>

### Configure

Methods:

- <code title="post /sso/org/{orgId}/configure">client.sso.org.configure.<a href="./src/vaif_client/resources/sso/org/configure.py">configure</a>(org_id) -> None</code>

# Status

Methods:

- <code title="get /status">client.status.<a href="./src/vaif_client/resources/status/status.py">list</a>() -> None</code>

## Atom

Methods:

- <code title="get /status/atom">client.status.atom.<a href="./src/vaif_client/resources/status/atom.py">list</a>() -> None</code>

## Incidents

Methods:

- <code title="get /status/incidents">client.status.incidents.<a href="./src/vaif_client/resources/status/incidents.py">list</a>() -> None</code>

## Rss

Methods:

- <code title="get /status/rss">client.status.rss.<a href="./src/vaif_client/resources/status/rss.py">list</a>() -> None</code>

## Subscribe

Types:

```python
from vaif_client.types.status import SubscribeCreateResponse
```

Methods:

- <code title="post /status/subscribe">client.status.subscribe.<a href="./src/vaif_client/resources/status/subscribe.py">create</a>(\*\*<a href="src/vaif_client/types/status/subscribe_create_params.py">params</a>) -> <a href="./src/vaif_client/types/status/subscribe_create_response.py">SubscribeCreateResponse</a></code>

## Subscribers

### Count

Methods:

- <code title="get /status/subscribers/count">client.status.subscribers.count.<a href="./src/vaif_client/resources/status/subscribers/count.py">list</a>() -> None</code>

## Unsubscribe

Types:

```python
from vaif_client.types.status import UnsubscribeRetrieveResponse
```

Methods:

- <code title="get /status/unsubscribe/{token}">client.status.unsubscribe.<a href="./src/vaif_client/resources/status/unsubscribe.py">retrieve</a>(token) -> <a href="./src/vaif_client/types/status/unsubscribe_retrieve_response.py">UnsubscribeRetrieveResponse</a></code>

## Uptime

Types:

```python
from vaif_client.types.status import UptimeRetrieveResponse
```

Methods:

- <code title="get /status/uptime/{componentId}">client.status.uptime.<a href="./src/vaif_client/resources/status/uptime.py">retrieve</a>(component_id) -> <a href="./src/vaif_client/types/status/uptime_retrieve_response.py">UptimeRetrieveResponse</a></code>

# Storage

## Buckets

Types:

```python
from vaif_client.types.storage import BucketCreateResponse
```

Methods:

- <code title="post /storage/buckets">client.storage.buckets.<a href="./src/vaif_client/resources/storage/buckets/buckets.py">create</a>(\*\*<a href="src/vaif_client/types/storage/bucket_create_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/bucket_create_response.py">BucketCreateResponse</a></code>
- <code title="get /storage/buckets">client.storage.buckets.<a href="./src/vaif_client/resources/storage/buckets/buckets.py">list</a>() -> None</code>

### Policies

Methods:

- <code title="put /storage/buckets/{bucketId}/policies/{policyId}">client.storage.buckets.policies.<a href="./src/vaif_client/resources/storage/buckets/policies/policies.py">update</a>(policy_id, \*, bucket_id) -> None</code>
- <code title="delete /storage/buckets/{bucketId}/policies/{policyId}">client.storage.buckets.policies.<a href="./src/vaif_client/resources/storage/buckets/policies/policies.py">delete</a>(policy_id, \*, bucket_id) -> None</code>
- <code title="get /storage/buckets/{bucketId}/policies">client.storage.buckets.policies.<a href="./src/vaif_client/resources/storage/buckets/policies/policies.py">get_policies</a>(bucket_id) -> None</code>
- <code title="post /storage/buckets/{bucketId}/policies">client.storage.buckets.policies.<a href="./src/vaif_client/resources/storage/buckets/policies/policies.py">policies</a>(bucket_id) -> None</code>

#### Toggle

Methods:

- <code title="post /storage/buckets/{bucketId}/policies/{policyId}/toggle">client.storage.buckets.policies.toggle.<a href="./src/vaif_client/resources/storage/buckets/policies/toggle.py">toggle</a>(policy_id, \*, bucket_id) -> None</code>

## Download

Methods:

- <code title="get /storage/download">client.storage.download.<a href="./src/vaif_client/resources/storage/download.py">list</a>() -> None</code>

## DownloadURL

Types:

```python
from vaif_client.types.storage import DownloadURLCreateResponse
```

Methods:

- <code title="post /storage/download-url">client.storage.download_url.<a href="./src/vaif_client/resources/storage/download_url.py">create</a>(\*\*<a href="src/vaif_client/types/storage/download_url_create_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/download_url_create_response.py">DownloadURLCreateResponse</a></code>

## Files

### Copy

Methods:

- <code title="post /storage/files/copy">client.storage.files.copy.<a href="./src/vaif_client/resources/storage/files/copy.py">create</a>() -> None</code>

### DeleteBatch

Methods:

- <code title="post /storage/files/delete-batch">client.storage.files.delete_batch.<a href="./src/vaif_client/resources/storage/files/delete_batch.py">create</a>() -> None</code>

### Metadata

Methods:

- <code title="get /storage/files/{bucketId}/metadata">client.storage.files.metadata.<a href="./src/vaif_client/resources/storage/files/metadata.py">get_metadata</a>(bucket_id) -> None</code>
- <code title="patch /storage/files/{bucketId}/metadata">client.storage.files.metadata.<a href="./src/vaif_client/resources/storage/files/metadata.py">metadata</a>(bucket_id) -> None</code>

### Move

Methods:

- <code title="post /storage/files/move">client.storage.files.move.<a href="./src/vaif_client/resources/storage/files/move.py">create</a>() -> None</code>

## Multipart

### Abort

Types:

```python
from vaif_client.types.storage.multipart import AbortAbortResponse
```

Methods:

- <code title="post /storage/multipart/{uploadId}/abort">client.storage.multipart.abort.<a href="./src/vaif_client/resources/storage/multipart/abort.py">abort</a>(upload_id, \*\*<a href="src/vaif_client/types/storage/multipart/abort_abort_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/multipart/abort_abort_response.py">AbortAbortResponse</a></code>

### Complete

Types:

```python
from vaif_client.types.storage.multipart import CompleteCompleteResponse
```

Methods:

- <code title="post /storage/multipart/{uploadId}/complete">client.storage.multipart.complete.<a href="./src/vaif_client/resources/storage/multipart/complete.py">complete</a>(upload_id, \*\*<a href="src/vaif_client/types/storage/multipart/complete_complete_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/multipart/complete_complete_response.py">CompleteCompleteResponse</a></code>

### Create

Types:

```python
from vaif_client.types.storage.multipart import CreateCreateResponse
```

Methods:

- <code title="post /storage/multipart/create">client.storage.multipart.create.<a href="./src/vaif_client/resources/storage/multipart/create.py">create</a>(\*\*<a href="src/vaif_client/types/storage/multipart/create_create_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/multipart/create_create_response.py">CreateCreateResponse</a></code>

### PartURL

Types:

```python
from vaif_client.types.storage.multipart import PartURLPartURLResponse
```

Methods:

- <code title="post /storage/multipart/{uploadId}/part-url">client.storage.multipart.part_url.<a href="./src/vaif_client/resources/storage/multipart/part_url.py">part_url</a>(upload_id, \*\*<a href="src/vaif_client/types/storage/multipart/part_url_part_url_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/multipart/part_url_part_url_response.py">PartURLPartURLResponse</a></code>

## Upload

Methods:

- <code title="post /storage/upload">client.storage.upload.<a href="./src/vaif_client/resources/storage/upload.py">create</a>() -> None</code>

## UploadBase64

Types:

```python
from vaif_client.types.storage import UploadBase64CreateResponse
```

Methods:

- <code title="post /storage/upload-base64">client.storage.upload_base64.<a href="./src/vaif_client/resources/storage/upload_base64.py">create</a>(\*\*<a href="src/vaif_client/types/storage/upload_base64_create_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/upload_base64_create_response.py">UploadBase64CreateResponse</a></code>

## UploadFromURL

Methods:

- <code title="post /storage/upload-from-url">client.storage.upload_from_url.<a href="./src/vaif_client/resources/storage/upload_from_url.py">create</a>() -> None</code>

## UploadURL

Types:

```python
from vaif_client.types.storage import UploadURLCreateResponse
```

Methods:

- <code title="post /storage/upload-url">client.storage.upload_url.<a href="./src/vaif_client/resources/storage/upload_url.py">create</a>(\*\*<a href="src/vaif_client/types/storage/upload_url_create_params.py">params</a>) -> <a href="./src/vaif_client/types/storage/upload_url_create_response.py">UploadURLCreateResponse</a></code>

# Templates

Methods:

- <code title="post /templates/">client.templates.<a href="./src/vaif_client/resources/templates/templates.py">create</a>() -> None</code>
- <code title="get /templates/{slug}">client.templates.<a href="./src/vaif_client/resources/templates/templates.py">retrieve</a>(slug) -> None</code>
- <code title="get /templates/">client.templates.<a href="./src/vaif_client/resources/templates/templates.py">list</a>() -> None</code>

## CreateProject

Methods:

- <code title="post /templates/create-project">client.templates.create_project.<a href="./src/vaif_client/resources/templates/create_project.py">create</a>() -> None</code>

## Install

### Apply

Methods:

- <code title="post /templates/install/apply">client.templates.install.apply.<a href="./src/vaif_client/resources/templates/install/apply.py">create</a>() -> None</code>

### Preview

Methods:

- <code title="post /templates/install/preview">client.templates.install.preview.<a href="./src/vaif_client/resources/templates/install/preview.py">create</a>() -> None</code>

### Rollback

Methods:

- <code title="post /templates/install/{installId}/rollback">client.templates.install.rollback.<a href="./src/vaif_client/resources/templates/install/rollback.py">rollback</a>(install_id) -> None</code>

# Users

## Me

Methods:

- <code title="patch /users/me">client.users.me.<a href="./src/vaif_client/resources/users/me/me.py">update</a>() -> None</code>
- <code title="get /users/me">client.users.me.<a href="./src/vaif_client/resources/users/me/me.py">list</a>() -> None</code>

### ChangePassword

Methods:

- <code title="post /users/me/change-password">client.users.me.change_password.<a href="./src/vaif_client/resources/users/me/change_password.py">create</a>() -> None</code>

### Preferences

Methods:

- <code title="patch /users/me/preferences">client.users.me.preferences.<a href="./src/vaif_client/resources/users/me/preferences.py">update</a>() -> None</code>
- <code title="get /users/me/preferences">client.users.me.preferences.<a href="./src/vaif_client/resources/users/me/preferences.py">list</a>() -> None</code>

### RequestAccountDelete

Methods:

- <code title="post /users/me/request-account-delete">client.users.me.request_account_delete.<a href="./src/vaif_client/resources/users/me/request_account_delete.py">create</a>() -> None</code>

# V1

## Health

Methods:

- <code title="get /v1/health">client.v1.health.<a href="./src/vaif_client/resources/v1/health.py">list</a>() -> None</code>

## Project

Methods:

- <code title="get /v1/project">client.v1.project.<a href="./src/vaif_client/resources/v1/project.py">list</a>() -> None</code>
