# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitHub:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_branch(self, client: Vaif) -> None:
        github = client.projects.github.branch(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_branch(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.branch(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_branch(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.branch(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_branch(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.branch(
                "",
            )

    @parametrize
    def test_method_connect(self, client: Vaif) -> None:
        github = client.projects.github.connect(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_connect(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.connect(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_connect(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.connect(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.connect(
                "",
            )

    @parametrize
    def test_method_disconnect(self, client: Vaif) -> None:
        github = client.projects.github.disconnect(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_disconnect(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.disconnect(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_disconnect(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.disconnect(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disconnect(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.disconnect(
                "",
            )

    @parametrize
    def test_method_get_branches(self, client: Vaif) -> None:
        github = client.projects.github.get_branches(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_get_branches(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.get_branches(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_get_branches(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.get_branches(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_branches(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.get_branches(
                "",
            )

    @parametrize
    def test_method_get_repos(self, client: Vaif) -> None:
        github = client.projects.github.get_repos(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_get_repos(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.get_repos(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_get_repos(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.get_repos(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_repos(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.get_repos(
                "",
            )

    @parametrize
    def test_method_get_status(self, client: Vaif) -> None:
        github = client.projects.github.get_status(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_get_status(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.get_status(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_get_status(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.get_status(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_status(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.get_status(
                "",
            )

    @parametrize
    def test_method_get_tracked_repos(self, client: Vaif) -> None:
        github = client.projects.github.get_tracked_repos(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_get_tracked_repos(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.get_tracked_repos(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_get_tracked_repos(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.get_tracked_repos(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_tracked_repos(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.get_tracked_repos(
                "",
            )

    @parametrize
    def test_method_pull(self, client: Vaif) -> None:
        github = client.projects.github.pull(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_pull(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.pull(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_pull(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.pull(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pull(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.pull(
                "",
            )

    @parametrize
    def test_method_push(self, client: Vaif) -> None:
        github = client.projects.github.push(
            "projectId",
        )
        assert github is None

    @parametrize
    def test_raw_response_push(self, client: Vaif) -> None:
        response = client.projects.github.with_raw_response.push(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @parametrize
    def test_streaming_response_push(self, client: Vaif) -> None:
        with client.projects.github.with_streaming_response.push(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_push(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.github.with_raw_response.push(
                "",
            )


class TestAsyncGitHub:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_branch(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.branch(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_branch(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.branch(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_branch(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.branch(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_branch(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.branch(
                "",
            )

    @parametrize
    async def test_method_connect(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.connect(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.connect(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.connect(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.connect(
                "",
            )

    @parametrize
    async def test_method_disconnect(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.disconnect(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.disconnect(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.disconnect(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.disconnect(
                "",
            )

    @parametrize
    async def test_method_get_branches(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.get_branches(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_get_branches(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.get_branches(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_get_branches(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.get_branches(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_branches(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.get_branches(
                "",
            )

    @parametrize
    async def test_method_get_repos(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.get_repos(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_get_repos(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.get_repos(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_get_repos(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.get_repos(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_repos(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.get_repos(
                "",
            )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.get_status(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.get_status(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.get_status(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.get_status(
                "",
            )

    @parametrize
    async def test_method_get_tracked_repos(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.get_tracked_repos(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_get_tracked_repos(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.get_tracked_repos(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_get_tracked_repos(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.get_tracked_repos(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_tracked_repos(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.get_tracked_repos(
                "",
            )

    @parametrize
    async def test_method_pull(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.pull(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_pull(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.pull(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_pull(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.pull(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pull(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.pull(
                "",
            )

    @parametrize
    async def test_method_push(self, async_client: AsyncVaif) -> None:
        github = await async_client.projects.github.push(
            "projectId",
        )
        assert github is None

    @parametrize
    async def test_raw_response_push(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.github.with_raw_response.push(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @parametrize
    async def test_streaming_response_push(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.github.with_streaming_response.push(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_push(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.github.with_raw_response.push(
                "",
            )
