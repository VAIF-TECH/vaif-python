# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_addons(self, client: Vaif) -> None:
        setting = client.projects.settings.addons(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_addons(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.addons(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_addons(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.addons(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_addons(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.addons(
                "",
            )

    @parametrize
    def test_method_api(self, client: Vaif) -> None:
        setting = client.projects.settings.api(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_api(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.api(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_api(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.api(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_api(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.api(
                "",
            )

    @parametrize
    def test_method_compute(self, client: Vaif) -> None:
        setting = client.projects.settings.compute(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_compute(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.compute(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_compute(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.compute(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_compute(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.compute(
                "",
            )

    @parametrize
    def test_method_get_addons(self, client: Vaif) -> None:
        setting = client.projects.settings.get_addons(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_get_addons(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.get_addons(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_get_addons(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.get_addons(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_addons(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.get_addons(
                "",
            )

    @parametrize
    def test_method_get_api(self, client: Vaif) -> None:
        setting = client.projects.settings.get_api(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_get_api(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.get_api(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_get_api(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.get_api(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_api(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.get_api(
                "",
            )

    @parametrize
    def test_method_get_compute(self, client: Vaif) -> None:
        setting = client.projects.settings.get_compute(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_get_compute(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.get_compute(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_get_compute(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.get_compute(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_compute(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.get_compute(
                "",
            )

    @parametrize
    def test_method_get_jwt(self, client: Vaif) -> None:
        setting = client.projects.settings.get_jwt(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_get_jwt(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.get_jwt(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_get_jwt(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.get_jwt(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_jwt(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.get_jwt(
                "",
            )

    @parametrize
    def test_method_get_settings(self, client: Vaif) -> None:
        setting = client.projects.settings.get_settings(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_get_settings(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.get_settings(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_get_settings(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.get_settings(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_settings(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.get_settings(
                "",
            )

    @parametrize
    def test_method_jwt(self, client: Vaif) -> None:
        setting = client.projects.settings.jwt(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_jwt(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.jwt(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_jwt(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.jwt(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_jwt(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.jwt(
                "",
            )

    @parametrize
    def test_method_rotate(self, client: Vaif) -> None:
        setting = client.projects.settings.rotate(
            "projectId",
        )
        assert setting is None

    @parametrize
    def test_raw_response_rotate(self, client: Vaif) -> None:
        response = client.projects.settings.with_raw_response.rotate(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @parametrize
    def test_streaming_response_rotate(self, client: Vaif) -> None:
        with client.projects.settings.with_streaming_response.rotate(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.settings.with_raw_response.rotate(
                "",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_addons(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.addons(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_addons(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.addons(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_addons(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.addons(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_addons(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.addons(
                "",
            )

    @parametrize
    async def test_method_api(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.api(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_api(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.api(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_api(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.api(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_api(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.api(
                "",
            )

    @parametrize
    async def test_method_compute(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.compute(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_compute(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.compute(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_compute(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.compute(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_compute(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.compute(
                "",
            )

    @parametrize
    async def test_method_get_addons(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.get_addons(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_get_addons(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.get_addons(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_get_addons(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.get_addons(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_addons(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.get_addons(
                "",
            )

    @parametrize
    async def test_method_get_api(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.get_api(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_get_api(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.get_api(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_get_api(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.get_api(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_api(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.get_api(
                "",
            )

    @parametrize
    async def test_method_get_compute(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.get_compute(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_get_compute(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.get_compute(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_get_compute(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.get_compute(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_compute(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.get_compute(
                "",
            )

    @parametrize
    async def test_method_get_jwt(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.get_jwt(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_get_jwt(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.get_jwt(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_get_jwt(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.get_jwt(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_jwt(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.get_jwt(
                "",
            )

    @parametrize
    async def test_method_get_settings(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.get_settings(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.get_settings(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.get_settings(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_settings(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.get_settings(
                "",
            )

    @parametrize
    async def test_method_jwt(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.jwt(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_jwt(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.jwt(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_jwt(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.jwt(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_jwt(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.jwt(
                "",
            )

    @parametrize
    async def test_method_rotate(self, async_client: AsyncVaif) -> None:
        setting = await async_client.projects.settings.rotate(
            "projectId",
        )
        assert setting is None

    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.settings.with_raw_response.rotate(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.settings.with_streaming_response.rotate(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.settings.with_raw_response.rotate(
                "",
            )
