# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from vaif_client import Vaif, AsyncVaif

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerated:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Vaif) -> None:
        generated = client.generated.create(
            "table",
        )
        assert generated is None

    @parametrize
    def test_raw_response_create(self, client: Vaif) -> None:
        response = client.generated.with_raw_response.create(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = response.parse()
        assert generated is None

    @parametrize
    def test_streaming_response_create(self, client: Vaif) -> None:
        with client.generated.with_streaming_response.create(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Vaif) -> None:
        generated = client.generated.retrieve(
            "table",
        )
        assert generated is None

    @parametrize
    def test_raw_response_retrieve(self, client: Vaif) -> None:
        response = client.generated.with_raw_response.retrieve(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = response.parse()
        assert generated is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Vaif) -> None:
        with client.generated.with_streaming_response.retrieve(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Vaif) -> None:
        generated = client.generated.update(
            id="id",
            table="table",
        )
        assert generated is None

    @parametrize
    def test_raw_response_update(self, client: Vaif) -> None:
        response = client.generated.with_raw_response.update(
            id="id",
            table="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = response.parse()
        assert generated is None

    @parametrize
    def test_streaming_response_update(self, client: Vaif) -> None:
        with client.generated.with_streaming_response.update(
            id="id",
            table="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.with_raw_response.update(
                id="id",
                table="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generated.with_raw_response.update(
                id="",
                table="table",
            )

    @parametrize
    def test_method_delete(self, client: Vaif) -> None:
        generated = client.generated.delete(
            id="id",
            table="table",
        )
        assert generated is None

    @parametrize
    def test_raw_response_delete(self, client: Vaif) -> None:
        response = client.generated.with_raw_response.delete(
            id="id",
            table="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = response.parse()
        assert generated is None

    @parametrize
    def test_streaming_response_delete(self, client: Vaif) -> None:
        with client.generated.with_streaming_response.delete(
            id="id",
            table="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.with_raw_response.delete(
                id="id",
                table="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generated.with_raw_response.delete(
                id="",
                table="table",
            )

    @parametrize
    def test_method_retrieve2(self, client: Vaif) -> None:
        generated = client.generated.retrieve2(
            id="id",
            table="table",
        )
        assert generated is None

    @parametrize
    def test_raw_response_retrieve2(self, client: Vaif) -> None:
        response = client.generated.with_raw_response.retrieve2(
            id="id",
            table="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = response.parse()
        assert generated is None

    @parametrize
    def test_streaming_response_retrieve2(self, client: Vaif) -> None:
        with client.generated.with_streaming_response.retrieve2(
            id="id",
            table="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve2(self, client: Vaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            client.generated.with_raw_response.retrieve2(
                id="id",
                table="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.generated.with_raw_response.retrieve2(
                id="",
                table="table",
            )


class TestAsyncGenerated:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncVaif) -> None:
        generated = await async_client.generated.create(
            "table",
        )
        assert generated is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.with_raw_response.create(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = await response.parse()
        assert generated is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.with_streaming_response.create(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = await response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncVaif) -> None:
        generated = await async_client.generated.retrieve(
            "table",
        )
        assert generated is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.with_raw_response.retrieve(
            "table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = await response.parse()
        assert generated is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.with_streaming_response.retrieve(
            "table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = await response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncVaif) -> None:
        generated = await async_client.generated.update(
            id="id",
            table="table",
        )
        assert generated is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.with_raw_response.update(
            id="id",
            table="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = await response.parse()
        assert generated is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.with_streaming_response.update(
            id="id",
            table="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = await response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.with_raw_response.update(
                id="id",
                table="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generated.with_raw_response.update(
                id="",
                table="table",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncVaif) -> None:
        generated = await async_client.generated.delete(
            id="id",
            table="table",
        )
        assert generated is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.with_raw_response.delete(
            id="id",
            table="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = await response.parse()
        assert generated is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.with_streaming_response.delete(
            id="id",
            table="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = await response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.with_raw_response.delete(
                id="id",
                table="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generated.with_raw_response.delete(
                id="",
                table="table",
            )

    @parametrize
    async def test_method_retrieve2(self, async_client: AsyncVaif) -> None:
        generated = await async_client.generated.retrieve2(
            id="id",
            table="table",
        )
        assert generated is None

    @parametrize
    async def test_raw_response_retrieve2(self, async_client: AsyncVaif) -> None:
        response = await async_client.generated.with_raw_response.retrieve2(
            id="id",
            table="table",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generated = await response.parse()
        assert generated is None

    @parametrize
    async def test_streaming_response_retrieve2(self, async_client: AsyncVaif) -> None:
        async with async_client.generated.with_streaming_response.retrieve2(
            id="id",
            table="table",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generated = await response.parse()
            assert generated is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve2(self, async_client: AsyncVaif) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table` but received ''"):
            await async_client.generated.with_raw_response.retrieve2(
                id="id",
                table="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.generated.with_raw_response.retrieve2(
                id="",
                table="table",
            )
