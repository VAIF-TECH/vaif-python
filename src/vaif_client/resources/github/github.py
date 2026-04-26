# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .oauth.oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def oauth(self) -> OAuthResource:
        return OAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        return AsyncOAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self._github.oauth)


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self._github.oauth)


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self._github.oauth)


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self._github.oauth)
