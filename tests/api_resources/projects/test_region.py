# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from vaif_client import Vaif, AsyncVaif
from vaif_client.types.projects import RegionRegionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_region(self, client: Vaif) -> None:
        region = client.projects.region.get_region(
            "projectId",
        )
        assert region is None

    @parametrize
    def test_raw_response_get_region(self, client: Vaif) -> None:
        response = client.projects.region.with_raw_response.get_region(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert region is None

    @parametrize
    def test_streaming_response_get_region(self, client: Vaif) -> None:
        with client.projects.region.with_streaming_response.get_region(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert region is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_region(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.region.with_raw_response.get_region(
                "",
            )

    @parametrize
    def test_method_region(self, client: Vaif) -> None:
        region = client.projects.region.region(
            project_id="projectId",
            region_key="x",
            tenancy_type="shared",
        )
        assert_matches_type(RegionRegionResponse, region, path=["response"])

    @parametrize
    def test_raw_response_region(self, client: Vaif) -> None:
        response = client.projects.region.with_raw_response.region(
            project_id="projectId",
            region_key="x",
            tenancy_type="shared",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = response.parse()
        assert_matches_type(RegionRegionResponse, region, path=["response"])

    @parametrize
    def test_streaming_response_region(self, client: Vaif) -> None:
        with client.projects.region.with_streaming_response.region(
            project_id="projectId",
            region_key="x",
            tenancy_type="shared",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = response.parse()
            assert_matches_type(RegionRegionResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_region(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.region.with_raw_response.region(
                project_id="",
                region_key="x",
                tenancy_type="shared",
            )


class TestAsyncRegion:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_region(self, async_client: AsyncVaif) -> None:
        region = await async_client.projects.region.get_region(
            "projectId",
        )
        assert region is None

    @parametrize
    async def test_raw_response_get_region(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.region.with_raw_response.get_region(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert region is None

    @parametrize
    async def test_streaming_response_get_region(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.region.with_streaming_response.get_region(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert region is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_region(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.region.with_raw_response.get_region(
                "",
            )

    @parametrize
    async def test_method_region(self, async_client: AsyncVaif) -> None:
        region = await async_client.projects.region.region(
            project_id="projectId",
            region_key="x",
            tenancy_type="shared",
        )
        assert_matches_type(RegionRegionResponse, region, path=["response"])

    @parametrize
    async def test_raw_response_region(self, async_client: AsyncVaif) -> None:
        response = await async_client.projects.region.with_raw_response.region(
            project_id="projectId",
            region_key="x",
            tenancy_type="shared",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        region = await response.parse()
        assert_matches_type(RegionRegionResponse, region, path=["response"])

    @parametrize
    async def test_streaming_response_region(self, async_client: AsyncVaif) -> None:
        async with async_client.projects.region.with_streaming_response.region(
            project_id="projectId",
            region_key="x",
            tenancy_type="shared",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            region = await response.parse()
            assert_matches_type(RegionRegionResponse, region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_region(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.region.with_raw_response.region(
                project_id="",
                region_key="x",
                tenancy_type="shared",
            )
