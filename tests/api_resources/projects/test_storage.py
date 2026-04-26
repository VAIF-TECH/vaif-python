# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.projects import StorageSettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStorage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_settings(self, client: Vaif) -> None:
        storage = client.projects.storage.get_settings(
            "projectId",
        )
        assert storage is None

    @parametrize
    def test_raw_response_get_settings(self, client: Vaif) -> None:
        response = client.projects.storage.with_raw_response.get_settings(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert storage is None

    @parametrize
    def test_streaming_response_get_settings(self, client: Vaif) -> None:
        with client.projects.storage.with_streaming_response.get_settings(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_settings(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.storage.with_raw_response.get_settings(
                "",
            )

    @parametrize
    def test_method_settings(self, client: Vaif) -> None:
        storage = client.projects.storage.settings(
            project_id="projectId",
        )
        assert_matches_type(StorageSettingsResponse, storage, path=["response"])

    @parametrize
    def test_method_settings_with_all_params(self, client: Vaif) -> None:
        storage = client.projects.storage.settings(
            project_id="projectId",
            allowed_mime_types=["string"],
            allowed_transforms=["string"],
            blocked_mime_types=["string"],
            cdn_enabled=True,
            default_cache_ttl=0,
            default_file_size_limit=0,
            edge_caching_enabled=True,
            enable_image_transform=True,
            max_file_size_limit=0,
            max_image_dimension=1,
            signed_url_default_expiry=1,
            signed_url_max_expiry=1,
            webhook_enabled=True,
            webhook_events=["string"],
            webhook_url="https://example.com",
        )
        assert_matches_type(StorageSettingsResponse, storage, path=["response"])

    @parametrize
    def test_raw_response_settings(self, client: Vaif) -> None:
        response = client.projects.storage.with_raw_response.settings(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert_matches_type(StorageSettingsResponse, storage, path=["response"])

    @parametrize
    def test_streaming_response_settings(self, client: Vaif) -> None:
        with client.projects.storage.with_streaming_response.settings(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert_matches_type(StorageSettingsResponse, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_settings(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.storage.with_raw_response.settings(
                project_id="",
            )


class TestAsyncStorage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_settings(self, async_client: AsyncVaif) -> None:
        storage = await async_client.projects.storage.get_settings(
            "projectId",
        )
        assert storage is None

    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.storage.with_raw_response.get_settings(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert storage is None

    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.storage.with_streaming_response.get_settings(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_settings(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.storage.with_raw_response.get_settings(
                "",
            )

    @parametrize
    async def test_method_settings(self, async_client: AsyncVaif) -> None:
        storage = await async_client.projects.storage.settings(
            project_id="projectId",
        )
        assert_matches_type(StorageSettingsResponse, storage, path=["response"])

    @parametrize
    async def test_method_settings_with_all_params(self, async_client: AsyncVaif) -> None:
        storage = await async_client.projects.storage.settings(
            project_id="projectId",
            allowed_mime_types=["string"],
            allowed_transforms=["string"],
            blocked_mime_types=["string"],
            cdn_enabled=True,
            default_cache_ttl=0,
            default_file_size_limit=0,
            edge_caching_enabled=True,
            enable_image_transform=True,
            max_file_size_limit=0,
            max_image_dimension=1,
            signed_url_default_expiry=1,
            signed_url_max_expiry=1,
            webhook_enabled=True,
            webhook_events=["string"],
            webhook_url="https://example.com",
        )
        assert_matches_type(StorageSettingsResponse, storage, path=["response"])

    @parametrize
    async def test_raw_response_settings(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.storage.with_raw_response.settings(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert_matches_type(StorageSettingsResponse, storage, path=["response"])

    @parametrize
    async def test_streaming_response_settings(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.storage.with_streaming_response.settings(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert_matches_type(StorageSettingsResponse, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_settings(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.storage.with_raw_response.settings(
                project_id="",
            )
