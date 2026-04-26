# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        addon = client.billing.org.addons.update(
            addon_id="addonId",
            org_id="orgId",
        )
        assert addon is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.billing.org.addons.with_raw_response.update(
            addon_id="addonId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert addon is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.billing.org.addons.with_streaming_response.update(
            addon_id="addonId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.addons.with_raw_response.update(
                addon_id="addonId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            client.billing.org.addons.with_raw_response.update(
                addon_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        addon = client.billing.org.addons.delete(
            addon_id="addonId",
            org_id="orgId",
        )
        assert addon is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.billing.org.addons.with_raw_response.delete(
            addon_id="addonId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert addon is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.billing.org.addons.with_streaming_response.delete(
            addon_id="addonId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.addons.with_raw_response.delete(
                addon_id="addonId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            client.billing.org.addons.with_raw_response.delete(
                addon_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_addons(self, client: Vaif) -> None:
        addon = client.billing.org.addons.addons(
            "orgId",
        )
        assert addon is None

    @parametrize
    def test_raw_response_addons(self, client: Vaif) -> None:
        response = client.billing.org.addons.with_raw_response.addons(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert addon is None

    @parametrize
    def test_streaming_response_addons(self, client: Vaif) -> None:
        with client.billing.org.addons.with_streaming_response.addons(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_addons(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.addons.with_raw_response.addons(
                "",
            )

    @parametrize
    def test_method_get_addons(self, client: Vaif) -> None:
        addon = client.billing.org.addons.get_addons(
            "orgId",
        )
        assert addon is None

    @parametrize
    def test_raw_response_get_addons(self, client: Vaif) -> None:
        response = client.billing.org.addons.with_raw_response.get_addons(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert addon is None

    @parametrize
    def test_streaming_response_get_addons(self, client: Vaif) -> None:
        with client.billing.org.addons.with_streaming_response.get_addons(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_addons(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.billing.org.addons.with_raw_response.get_addons(
                "",
            )


class TestAsyncAddons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        addon = await async_client.billing.org.addons.update(
            addon_id="addonId",
            org_id="orgId",
        )
        assert addon is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.addons.with_raw_response.update(
            addon_id="addonId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert addon is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.addons.with_streaming_response.update(
            addon_id="addonId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.addons.with_raw_response.update(
                addon_id="addonId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            await async_client.billing.org.addons.with_raw_response.update(
                addon_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        addon = await async_client.billing.org.addons.delete(
            addon_id="addonId",
            org_id="orgId",
        )
        assert addon is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.addons.with_raw_response.delete(
            addon_id="addonId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert addon is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.addons.with_streaming_response.delete(
            addon_id="addonId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.addons.with_raw_response.delete(
                addon_id="addonId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `addon_id` but received ''"):
            await async_client.billing.org.addons.with_raw_response.delete(
                addon_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_addons(self, async_client: AsyncVaif) -> None:
        addon = await async_client.billing.org.addons.addons(
            "orgId",
        )
        assert addon is None

    @parametrize
    async def test_raw_response_addons(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.addons.with_raw_response.addons(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert addon is None

    @parametrize
    async def test_streaming_response_addons(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.addons.with_streaming_response.addons(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_addons(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.addons.with_raw_response.addons(
                "",
            )

    @parametrize
    async def test_method_get_addons(self, async_client: AsyncVaif) -> None:
        addon = await async_client.billing.org.addons.get_addons(
            "orgId",
        )
        assert addon is None

    @parametrize
    async def test_raw_response_get_addons(self, async_client: AsyncVaif) -> None:
        response = await async_client.billing.org.addons.with_raw_response.get_addons(
            "orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert addon is None

    @parametrize
    async def test_streaming_response_get_addons(self, async_client: AsyncVaif) -> None:
        async with async_client.billing.org.addons.with_streaming_response.get_addons(
            "orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert addon is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_addons(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.billing.org.addons.with_raw_response.get_addons(
                "",
            )
