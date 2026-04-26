# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif._utils import parse_datetime
from vaif.types.projects import (
    APIKeyUpdateResponse,
    APIKeyAPIKeysResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        api_key = client.projects.api_keys.update(
            key_id="keyId",
            project_id="projectId",
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        api_key = client.projects.api_keys.update(
            key_id="keyId",
            project_id="projectId",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            scopes=["crud"],
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.projects.api_keys.with_raw_response.update(
            key_id="keyId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.projects.api_keys.with_streaming_response.update(
            key_id="keyId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.api_keys.with_raw_response.update(
                key_id="keyId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.projects.api_keys.with_raw_response.update(
                key_id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_api_keys(self, client: Vaif) -> None:
        api_key = client.projects.api_keys.api_keys(
            project_id="projectId",
        )
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @parametrize
    def test_method_api_keys_with_all_params(self, client: Vaif) -> None:
        api_key = client.projects.api_keys.api_keys(
            project_id="projectId",
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            scopes=["crud"],
        )
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @parametrize
    def test_raw_response_api_keys(self, client: Vaif) -> None:
        response = client.projects.api_keys.with_raw_response.api_keys(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @parametrize
    def test_streaming_response_api_keys(self, client: Vaif) -> None:
        with client.projects.api_keys.with_streaming_response.api_keys(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_api_keys(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.api_keys.with_raw_response.api_keys(
                project_id="",
            )

    @parametrize
    def test_method_get_api_keys(self, client: Vaif) -> None:
        api_key = client.projects.api_keys.get_api_keys(
            "projectId",
        )
        assert api_key is None

    @parametrize
    def test_raw_response_get_api_keys(self, client: Vaif) -> None:
        response = client.projects.api_keys.with_raw_response.get_api_keys(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert api_key is None

    @parametrize
    def test_streaming_response_get_api_keys(self, client: Vaif) -> None:
        with client.projects.api_keys.with_streaming_response.get_api_keys(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_api_keys(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.api_keys.with_raw_response.get_api_keys(
                "",
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        api_key = await async_client.projects.api_keys.update(
            key_id="keyId",
            project_id="projectId",
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        api_key = await async_client.projects.api_keys.update(
            key_id="keyId",
            project_id="projectId",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            scopes=["crud"],
        )
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.api_keys.with_raw_response.update(
            key_id="keyId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.api_keys.with_streaming_response.update(
            key_id="keyId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyUpdateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.api_keys.with_raw_response.update(
                key_id="keyId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.projects.api_keys.with_raw_response.update(
                key_id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_api_keys(self, async_client: AsyncVaif) -> None:
        api_key = await async_client.projects.api_keys.api_keys(
            project_id="projectId",
        )
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @parametrize
    async def test_method_api_keys_with_all_params(self, async_client: AsyncVaif) -> None:
        api_key = await async_client.projects.api_keys.api_keys(
            project_id="projectId",
            env_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            scopes=["crud"],
        )
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @parametrize
    async def test_raw_response_api_keys(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.api_keys.with_raw_response.api_keys(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

    @parametrize
    async def test_streaming_response_api_keys(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.api_keys.with_streaming_response.api_keys(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_api_keys(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.api_keys.with_raw_response.api_keys(
                project_id="",
            )

    @parametrize
    async def test_method_get_api_keys(self, async_client: AsyncVaif) -> None:
        api_key = await async_client.projects.api_keys.get_api_keys(
            "projectId",
        )
        assert api_key is None

    @parametrize
    async def test_raw_response_get_api_keys(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.api_keys.with_raw_response.get_api_keys(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert api_key is None

    @parametrize
    async def test_streaming_response_get_api_keys(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.api_keys.with_streaming_response.get_api_keys(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_api_keys(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.api_keys.with_raw_response.get_api_keys(
                "",
            )
