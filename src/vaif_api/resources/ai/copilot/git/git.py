# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .log import (
    LogResource,
    AsyncLogResource,
    LogResourceWithRawResponse,
    AsyncLogResourceWithRawResponse,
    LogResourceWithStreamingResponse,
    AsyncLogResourceWithStreamingResponse,
)
from .init import (
    InitResource,
    AsyncInitResource,
    InitResourceWithRawResponse,
    AsyncInitResourceWithRawResponse,
    InitResourceWithStreamingResponse,
    AsyncInitResourceWithStreamingResponse,
)
from .pull import (
    PullResource,
    AsyncPullResource,
    PullResourceWithRawResponse,
    AsyncPullResourceWithRawResponse,
    PullResourceWithStreamingResponse,
    AsyncPullResourceWithStreamingResponse,
)
from .push import (
    PushResource,
    AsyncPushResource,
    PushResourceWithRawResponse,
    AsyncPushResourceWithRawResponse,
    PushResourceWithStreamingResponse,
    AsyncPushResourceWithStreamingResponse,
)
from .clone import (
    CloneResource,
    AsyncCloneResource,
    CloneResourceWithRawResponse,
    AsyncCloneResourceWithRawResponse,
    CloneResourceWithStreamingResponse,
    AsyncCloneResourceWithStreamingResponse,
)
from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .write import (
    WriteResource,
    AsyncWriteResource,
    WriteResourceWithRawResponse,
    AsyncWriteResourceWithRawResponse,
    WriteResourceWithStreamingResponse,
    AsyncWriteResourceWithStreamingResponse,
)
from .commit import (
    CommitResource,
    AsyncCommitResource,
    CommitResourceWithRawResponse,
    AsyncCommitResourceWithRawResponse,
    CommitResourceWithStreamingResponse,
    AsyncCommitResourceWithStreamingResponse,
)
from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from .branches import (
    BranchesResource,
    AsyncBranchesResource,
    BranchesResourceWithRawResponse,
    AsyncBranchesResourceWithRawResponse,
    BranchesResourceWithStreamingResponse,
    AsyncBranchesResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GitResource", "AsyncGitResource"]


class GitResource(SyncAPIResource):
    @cached_property
    def branches(self) -> BranchesResource:
        return BranchesResource(self._client)

    @cached_property
    def clone(self) -> CloneResource:
        return CloneResource(self._client)

    @cached_property
    def commit(self) -> CommitResource:
        return CommitResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def init(self) -> InitResource:
        return InitResource(self._client)

    @cached_property
    def log(self) -> LogResource:
        return LogResource(self._client)

    @cached_property
    def pull(self) -> PullResource:
        return PullResource(self._client)

    @cached_property
    def push(self) -> PushResource:
        return PushResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def write(self) -> WriteResource:
        return WriteResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return GitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return GitResourceWithStreamingResponse(self)


class AsyncGitResource(AsyncAPIResource):
    @cached_property
    def branches(self) -> AsyncBranchesResource:
        return AsyncBranchesResource(self._client)

    @cached_property
    def clone(self) -> AsyncCloneResource:
        return AsyncCloneResource(self._client)

    @cached_property
    def commit(self) -> AsyncCommitResource:
        return AsyncCommitResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def init(self) -> AsyncInitResource:
        return AsyncInitResource(self._client)

    @cached_property
    def log(self) -> AsyncLogResource:
        return AsyncLogResource(self._client)

    @cached_property
    def pull(self) -> AsyncPullResource:
        return AsyncPullResource(self._client)

    @cached_property
    def push(self) -> AsyncPushResource:
        return AsyncPushResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def write(self) -> AsyncWriteResource:
        return AsyncWriteResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncGitResourceWithStreamingResponse(self)


class GitResourceWithRawResponse:
    def __init__(self, git: GitResource) -> None:
        self._git = git

    @cached_property
    def branches(self) -> BranchesResourceWithRawResponse:
        return BranchesResourceWithRawResponse(self._git.branches)

    @cached_property
    def clone(self) -> CloneResourceWithRawResponse:
        return CloneResourceWithRawResponse(self._git.clone)

    @cached_property
    def commit(self) -> CommitResourceWithRawResponse:
        return CommitResourceWithRawResponse(self._git.commit)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._git.files)

    @cached_property
    def init(self) -> InitResourceWithRawResponse:
        return InitResourceWithRawResponse(self._git.init)

    @cached_property
    def log(self) -> LogResourceWithRawResponse:
        return LogResourceWithRawResponse(self._git.log)

    @cached_property
    def pull(self) -> PullResourceWithRawResponse:
        return PullResourceWithRawResponse(self._git.pull)

    @cached_property
    def push(self) -> PushResourceWithRawResponse:
        return PushResourceWithRawResponse(self._git.push)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._git.status)

    @cached_property
    def write(self) -> WriteResourceWithRawResponse:
        return WriteResourceWithRawResponse(self._git.write)


class AsyncGitResourceWithRawResponse:
    def __init__(self, git: AsyncGitResource) -> None:
        self._git = git

    @cached_property
    def branches(self) -> AsyncBranchesResourceWithRawResponse:
        return AsyncBranchesResourceWithRawResponse(self._git.branches)

    @cached_property
    def clone(self) -> AsyncCloneResourceWithRawResponse:
        return AsyncCloneResourceWithRawResponse(self._git.clone)

    @cached_property
    def commit(self) -> AsyncCommitResourceWithRawResponse:
        return AsyncCommitResourceWithRawResponse(self._git.commit)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._git.files)

    @cached_property
    def init(self) -> AsyncInitResourceWithRawResponse:
        return AsyncInitResourceWithRawResponse(self._git.init)

    @cached_property
    def log(self) -> AsyncLogResourceWithRawResponse:
        return AsyncLogResourceWithRawResponse(self._git.log)

    @cached_property
    def pull(self) -> AsyncPullResourceWithRawResponse:
        return AsyncPullResourceWithRawResponse(self._git.pull)

    @cached_property
    def push(self) -> AsyncPushResourceWithRawResponse:
        return AsyncPushResourceWithRawResponse(self._git.push)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._git.status)

    @cached_property
    def write(self) -> AsyncWriteResourceWithRawResponse:
        return AsyncWriteResourceWithRawResponse(self._git.write)


class GitResourceWithStreamingResponse:
    def __init__(self, git: GitResource) -> None:
        self._git = git

    @cached_property
    def branches(self) -> BranchesResourceWithStreamingResponse:
        return BranchesResourceWithStreamingResponse(self._git.branches)

    @cached_property
    def clone(self) -> CloneResourceWithStreamingResponse:
        return CloneResourceWithStreamingResponse(self._git.clone)

    @cached_property
    def commit(self) -> CommitResourceWithStreamingResponse:
        return CommitResourceWithStreamingResponse(self._git.commit)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._git.files)

    @cached_property
    def init(self) -> InitResourceWithStreamingResponse:
        return InitResourceWithStreamingResponse(self._git.init)

    @cached_property
    def log(self) -> LogResourceWithStreamingResponse:
        return LogResourceWithStreamingResponse(self._git.log)

    @cached_property
    def pull(self) -> PullResourceWithStreamingResponse:
        return PullResourceWithStreamingResponse(self._git.pull)

    @cached_property
    def push(self) -> PushResourceWithStreamingResponse:
        return PushResourceWithStreamingResponse(self._git.push)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._git.status)

    @cached_property
    def write(self) -> WriteResourceWithStreamingResponse:
        return WriteResourceWithStreamingResponse(self._git.write)


class AsyncGitResourceWithStreamingResponse:
    def __init__(self, git: AsyncGitResource) -> None:
        self._git = git

    @cached_property
    def branches(self) -> AsyncBranchesResourceWithStreamingResponse:
        return AsyncBranchesResourceWithStreamingResponse(self._git.branches)

    @cached_property
    def clone(self) -> AsyncCloneResourceWithStreamingResponse:
        return AsyncCloneResourceWithStreamingResponse(self._git.clone)

    @cached_property
    def commit(self) -> AsyncCommitResourceWithStreamingResponse:
        return AsyncCommitResourceWithStreamingResponse(self._git.commit)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._git.files)

    @cached_property
    def init(self) -> AsyncInitResourceWithStreamingResponse:
        return AsyncInitResourceWithStreamingResponse(self._git.init)

    @cached_property
    def log(self) -> AsyncLogResourceWithStreamingResponse:
        return AsyncLogResourceWithStreamingResponse(self._git.log)

    @cached_property
    def pull(self) -> AsyncPullResourceWithStreamingResponse:
        return AsyncPullResourceWithStreamingResponse(self._git.pull)

    @cached_property
    def push(self) -> AsyncPushResourceWithStreamingResponse:
        return AsyncPushResourceWithStreamingResponse(self._git.push)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._git.status)

    @cached_property
    def write(self) -> AsyncWriteResourceWithStreamingResponse:
        return AsyncWriteResourceWithStreamingResponse(self._git.write)
