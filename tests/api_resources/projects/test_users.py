# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.projects import UserUsersResponse, UserUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        user = client.projects.users.retrieve(
            user_id="userId",
            project_id="projectId",
        )
        assert user is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.projects.users.with_raw_response.retrieve(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.projects.users.with_streaming_response.retrieve(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.with_raw_response.retrieve(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.with_raw_response.retrieve(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        user = client.projects.users.update(
            user_id="userId",
            project_id="projectId",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        user = client.projects.users.update(
            user_id="userId",
            project_id="projectId",
            app_metadata={"foo": "bar"},
            banned=True,
            banned_reason="bannedReason",
            email="dev@stainless.com",
            metadata={"foo": "bar"},
            phone="phone",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.projects.users.with_raw_response.update(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.projects.users.with_streaming_response.update(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.with_raw_response.update(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.with_raw_response.update(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        user = client.projects.users.delete(
            user_id="userId",
            project_id="projectId",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.projects.users.with_raw_response.delete(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.projects.users.with_streaming_response.delete(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.with_raw_response.delete(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.projects.users.with_raw_response.delete(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_get_users(self, client: Vaif) -> None:
        user = client.projects.users.get_users(
            "projectId",
        )
        assert user is None

    @parametrize
    def test_raw_response_get_users(self, client: Vaif) -> None:
        response = client.projects.users.with_raw_response.get_users(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_get_users(self, client: Vaif) -> None:
        with client.projects.users.with_streaming_response.get_users(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_users(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.with_raw_response.get_users(
                "",
            )

    @parametrize
    def test_method_users(self, client: Vaif) -> None:
        user = client.projects.users.users(
            project_id="projectId",
        )
        assert_matches_type(UserUsersResponse, user, path=["response"])

    @parametrize
    def test_method_users_with_all_params(self, client: Vaif) -> None:
        user = client.projects.users.users(
            project_id="projectId",
            email="dev@stainless.com",
            metadata={"foo": "bar"},
            password="x",
            phone="phone",
            provider="provider",
        )
        assert_matches_type(UserUsersResponse, user, path=["response"])

    @parametrize
    def test_raw_response_users(self, client: Vaif) -> None:
        response = client.projects.users.with_raw_response.users(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUsersResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_users(self, client: Vaif) -> None:
        with client.projects.users.with_streaming_response.users(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUsersResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_users(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.users.with_raw_response.users(
                project_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.retrieve(
            user_id="userId",
            project_id="projectId",
        )
        assert user is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.with_raw_response.retrieve(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.with_streaming_response.retrieve(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.with_raw_response.retrieve(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.with_raw_response.retrieve(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.update(
            user_id="userId",
            project_id="projectId",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.update(
            user_id="userId",
            project_id="projectId",
            app_metadata={"foo": "bar"},
            banned=True,
            banned_reason="bannedReason",
            email="dev@stainless.com",
            metadata={"foo": "bar"},
            phone="phone",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.with_raw_response.update(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.with_streaming_response.update(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.with_raw_response.update(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.with_raw_response.update(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.delete(
            user_id="userId",
            project_id="projectId",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.with_raw_response.delete(
            user_id="userId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.with_streaming_response.delete(
            user_id="userId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.with_raw_response.delete(
                user_id="userId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.projects.users.with_raw_response.delete(
                user_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_get_users(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.get_users(
            "projectId",
        )
        assert user is None

    @parametrize
    async def test_raw_response_get_users(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.with_raw_response.get_users(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_get_users(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.with_streaming_response.get_users(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_users(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.with_raw_response.get_users(
                "",
            )

    @parametrize
    async def test_method_users(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.users(
            project_id="projectId",
        )
        assert_matches_type(UserUsersResponse, user, path=["response"])

    @parametrize
    async def test_method_users_with_all_params(self, async_client: AsyncVaif) -> None:
        user = await async_client.projects.users.users(
            project_id="projectId",
            email="dev@stainless.com",
            metadata={"foo": "bar"},
            password="x",
            phone="phone",
            provider="provider",
        )
        assert_matches_type(UserUsersResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_users(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.users.with_raw_response.users(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUsersResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_users(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.users.with_streaming_response.users(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUsersResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_users(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.users.with_raw_response.users(
                project_id="",
            )
