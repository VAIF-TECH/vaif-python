# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif import Vaif, AsyncVaif
from tests.utils import assert_matches_type
from vaif.types.oauth.org import ProviderDeleteResponse, ProviderUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProvider:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        provider = client.oauth.org.provider.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Vaif) -> None:
        provider = client.oauth.org.provider.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            client_id="x",
            client_secret="x",
            enabled=True,
            redirect_uri="https://example.com",
        )
        assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.oauth.org.provider.with_raw_response.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.oauth.org.provider.with_streaming_response.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.oauth.org.provider.with_raw_response.update(
                provider="x",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.oauth.org.provider.with_raw_response.update(
                provider="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        provider = client.oauth.org.provider.delete(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProviderDeleteResponse, provider, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.oauth.org.provider.with_raw_response.delete(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderDeleteResponse, provider, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.oauth.org.provider.with_streaming_response.delete(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderDeleteResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.oauth.org.provider.with_raw_response.delete(
                provider="x",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.oauth.org.provider.with_raw_response.delete(
                provider="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncProvider:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        provider = await async_client.oauth.org.provider.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncVaif) -> None:
        provider = await async_client.oauth.org.provider.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            client_id="x",
            client_secret="x",
            enabled=True,
            redirect_uri="https://example.com",
        )
        assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.oauth.org.provider.with_raw_response.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.oauth.org.provider.with_streaming_response.update(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderUpdateResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.oauth.org.provider.with_raw_response.update(
                provider="x",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.oauth.org.provider.with_raw_response.update(
                provider="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        provider = await async_client.oauth.org.provider.delete(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProviderDeleteResponse, provider, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.oauth.org.provider.with_raw_response.delete(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderDeleteResponse, provider, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.oauth.org.provider.with_streaming_response.delete(
            provider="x",
            org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderDeleteResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.oauth.org.provider.with_raw_response.delete(
                provider="x",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.oauth.org.provider.with_raw_response.delete(
                provider="",
                org_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
