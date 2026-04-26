# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .find import (
    FindResource,
    AsyncFindResource,
    FindResourceWithRawResponse,
    AsyncFindResourceWithRawResponse,
    FindResourceWithStreamingResponse,
    AsyncFindResourceWithStreamingResponse,
)
from .count import (
    CountResource,
    AsyncCountResource,
    CountResourceWithRawResponse,
    AsyncCountResourceWithRawResponse,
    CountResourceWithStreamingResponse,
    AsyncCountResourceWithStreamingResponse,
)
from .command import (
    CommandResource,
    AsyncCommandResource,
    CommandResourceWithRawResponse,
    AsyncCommandResourceWithRawResponse,
    CommandResourceWithStreamingResponse,
    AsyncCommandResourceWithStreamingResponse,
)
from .indexes import (
    IndexesResource,
    AsyncIndexesResource,
    IndexesResourceWithRawResponse,
    AsyncIndexesResourceWithRawResponse,
    IndexesResourceWithStreamingResponse,
    AsyncIndexesResourceWithStreamingResponse,
)
from .distinct import (
    DistinctResource,
    AsyncDistinctResource,
    DistinctResourceWithRawResponse,
    AsyncDistinctResourceWithRawResponse,
    DistinctResourceWithStreamingResponse,
    AsyncDistinctResourceWithStreamingResponse,
)
from .find_one import (
    FindOneResource,
    AsyncFindOneResource,
    FindOneResourceWithRawResponse,
    AsyncFindOneResourceWithRawResponse,
    FindOneResourceWithStreamingResponse,
    AsyncFindOneResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .aggregate import (
    AggregateResource,
    AsyncAggregateResource,
    AggregateResourceWithRawResponse,
    AsyncAggregateResourceWithRawResponse,
    AggregateResourceWithStreamingResponse,
    AsyncAggregateResourceWithStreamingResponse,
)
from .bulk_write import (
    BulkWriteResource,
    AsyncBulkWriteResource,
    BulkWriteResourceWithRawResponse,
    AsyncBulkWriteResourceWithRawResponse,
    BulkWriteResourceWithStreamingResponse,
    AsyncBulkWriteResourceWithStreamingResponse,
)
from .delete_one import (
    DeleteOneResource,
    AsyncDeleteOneResource,
    DeleteOneResourceWithRawResponse,
    AsyncDeleteOneResourceWithRawResponse,
    DeleteOneResourceWithStreamingResponse,
    AsyncDeleteOneResourceWithStreamingResponse,
)
from .find_by_id import (
    FindByIDResource,
    AsyncFindByIDResource,
    FindByIDResourceWithRawResponse,
    AsyncFindByIDResourceWithRawResponse,
    FindByIDResourceWithStreamingResponse,
    AsyncFindByIDResourceWithStreamingResponse,
)
from .insert_one import (
    InsertOneResource,
    AsyncInsertOneResource,
    InsertOneResourceWithRawResponse,
    AsyncInsertOneResourceWithRawResponse,
    InsertOneResourceWithStreamingResponse,
    AsyncInsertOneResourceWithStreamingResponse,
)
from .update_one import (
    UpdateOneResource,
    AsyncUpdateOneResource,
    UpdateOneResourceWithRawResponse,
    AsyncUpdateOneResourceWithRawResponse,
    UpdateOneResourceWithStreamingResponse,
    AsyncUpdateOneResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .delete_many import (
    DeleteManyResource,
    AsyncDeleteManyResource,
    DeleteManyResourceWithRawResponse,
    AsyncDeleteManyResourceWithRawResponse,
    DeleteManyResourceWithStreamingResponse,
    AsyncDeleteManyResourceWithStreamingResponse,
)
from .insert_many import (
    InsertManyResource,
    AsyncInsertManyResource,
    InsertManyResourceWithRawResponse,
    AsyncInsertManyResourceWithRawResponse,
    InsertManyResourceWithStreamingResponse,
    AsyncInsertManyResourceWithStreamingResponse,
)
from .replace_one import (
    ReplaceOneResource,
    AsyncReplaceOneResource,
    ReplaceOneResourceWithRawResponse,
    AsyncReplaceOneResourceWithRawResponse,
    ReplaceOneResourceWithStreamingResponse,
    AsyncReplaceOneResourceWithStreamingResponse,
)
from .update_many import (
    UpdateManyResource,
    AsyncUpdateManyResource,
    UpdateManyResourceWithRawResponse,
    AsyncUpdateManyResourceWithRawResponse,
    UpdateManyResourceWithStreamingResponse,
    AsyncUpdateManyResourceWithStreamingResponse,
)
from .cursor.cursor import (
    CursorResource,
    AsyncCursorResource,
    CursorResourceWithRawResponse,
    AsyncCursorResourceWithRawResponse,
    CursorResourceWithStreamingResponse,
    AsyncCursorResourceWithStreamingResponse,
)
from .estimated_count import (
    EstimatedCountResource,
    AsyncEstimatedCountResource,
    EstimatedCountResourceWithRawResponse,
    AsyncEstimatedCountResourceWithRawResponse,
    EstimatedCountResourceWithStreamingResponse,
    AsyncEstimatedCountResourceWithStreamingResponse,
)
from .find_one_and_delete import (
    FindOneAndDeleteResource,
    AsyncFindOneAndDeleteResource,
    FindOneAndDeleteResourceWithRawResponse,
    AsyncFindOneAndDeleteResourceWithRawResponse,
    FindOneAndDeleteResourceWithStreamingResponse,
    AsyncFindOneAndDeleteResourceWithStreamingResponse,
)
from .find_one_and_update import (
    FindOneAndUpdateResource,
    AsyncFindOneAndUpdateResource,
    FindOneAndUpdateResourceWithRawResponse,
    AsyncFindOneAndUpdateResourceWithRawResponse,
    FindOneAndUpdateResourceWithStreamingResponse,
    AsyncFindOneAndUpdateResourceWithStreamingResponse,
)
from .find_one_and_replace import (
    FindOneAndReplaceResource,
    AsyncFindOneAndReplaceResource,
    FindOneAndReplaceResourceWithRawResponse,
    AsyncFindOneAndReplaceResourceWithRawResponse,
    FindOneAndReplaceResourceWithStreamingResponse,
    AsyncFindOneAndReplaceResourceWithStreamingResponse,
)
from .collections.collections import (
    CollectionsResource,
    AsyncCollectionsResource,
    CollectionsResourceWithRawResponse,
    AsyncCollectionsResourceWithRawResponse,
    CollectionsResourceWithStreamingResponse,
    AsyncCollectionsResourceWithStreamingResponse,
)

__all__ = ["MongoDBResource", "AsyncMongoDBResource"]


class MongoDBResource(SyncAPIResource):
    @cached_property
    def aggregate(self) -> AggregateResource:
        return AggregateResource(self._client)

    @cached_property
    def bulk_write(self) -> BulkWriteResource:
        return BulkWriteResource(self._client)

    @cached_property
    def collections(self) -> CollectionsResource:
        return CollectionsResource(self._client)

    @cached_property
    def command(self) -> CommandResource:
        return CommandResource(self._client)

    @cached_property
    def count(self) -> CountResource:
        return CountResource(self._client)

    @cached_property
    def cursor(self) -> CursorResource:
        return CursorResource(self._client)

    @cached_property
    def delete_many(self) -> DeleteManyResource:
        return DeleteManyResource(self._client)

    @cached_property
    def delete_one(self) -> DeleteOneResource:
        return DeleteOneResource(self._client)

    @cached_property
    def distinct(self) -> DistinctResource:
        return DistinctResource(self._client)

    @cached_property
    def estimated_count(self) -> EstimatedCountResource:
        return EstimatedCountResource(self._client)

    @cached_property
    def find(self) -> FindResource:
        return FindResource(self._client)

    @cached_property
    def find_by_id(self) -> FindByIDResource:
        return FindByIDResource(self._client)

    @cached_property
    def find_one(self) -> FindOneResource:
        return FindOneResource(self._client)

    @cached_property
    def find_one_and_delete(self) -> FindOneAndDeleteResource:
        return FindOneAndDeleteResource(self._client)

    @cached_property
    def find_one_and_replace(self) -> FindOneAndReplaceResource:
        return FindOneAndReplaceResource(self._client)

    @cached_property
    def find_one_and_update(self) -> FindOneAndUpdateResource:
        return FindOneAndUpdateResource(self._client)

    @cached_property
    def indexes(self) -> IndexesResource:
        return IndexesResource(self._client)

    @cached_property
    def insert_many(self) -> InsertManyResource:
        return InsertManyResource(self._client)

    @cached_property
    def insert_one(self) -> InsertOneResource:
        return InsertOneResource(self._client)

    @cached_property
    def replace_one(self) -> ReplaceOneResource:
        return ReplaceOneResource(self._client)

    @cached_property
    def update_many(self) -> UpdateManyResource:
        return UpdateManyResource(self._client)

    @cached_property
    def update_one(self) -> UpdateOneResource:
        return UpdateOneResource(self._client)

    @cached_property
    def with_raw_response(self) -> MongoDBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return MongoDBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MongoDBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return MongoDBResourceWithStreamingResponse(self)


class AsyncMongoDBResource(AsyncAPIResource):
    @cached_property
    def aggregate(self) -> AsyncAggregateResource:
        return AsyncAggregateResource(self._client)

    @cached_property
    def bulk_write(self) -> AsyncBulkWriteResource:
        return AsyncBulkWriteResource(self._client)

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        return AsyncCollectionsResource(self._client)

    @cached_property
    def command(self) -> AsyncCommandResource:
        return AsyncCommandResource(self._client)

    @cached_property
    def count(self) -> AsyncCountResource:
        return AsyncCountResource(self._client)

    @cached_property
    def cursor(self) -> AsyncCursorResource:
        return AsyncCursorResource(self._client)

    @cached_property
    def delete_many(self) -> AsyncDeleteManyResource:
        return AsyncDeleteManyResource(self._client)

    @cached_property
    def delete_one(self) -> AsyncDeleteOneResource:
        return AsyncDeleteOneResource(self._client)

    @cached_property
    def distinct(self) -> AsyncDistinctResource:
        return AsyncDistinctResource(self._client)

    @cached_property
    def estimated_count(self) -> AsyncEstimatedCountResource:
        return AsyncEstimatedCountResource(self._client)

    @cached_property
    def find(self) -> AsyncFindResource:
        return AsyncFindResource(self._client)

    @cached_property
    def find_by_id(self) -> AsyncFindByIDResource:
        return AsyncFindByIDResource(self._client)

    @cached_property
    def find_one(self) -> AsyncFindOneResource:
        return AsyncFindOneResource(self._client)

    @cached_property
    def find_one_and_delete(self) -> AsyncFindOneAndDeleteResource:
        return AsyncFindOneAndDeleteResource(self._client)

    @cached_property
    def find_one_and_replace(self) -> AsyncFindOneAndReplaceResource:
        return AsyncFindOneAndReplaceResource(self._client)

    @cached_property
    def find_one_and_update(self) -> AsyncFindOneAndUpdateResource:
        return AsyncFindOneAndUpdateResource(self._client)

    @cached_property
    def indexes(self) -> AsyncIndexesResource:
        return AsyncIndexesResource(self._client)

    @cached_property
    def insert_many(self) -> AsyncInsertManyResource:
        return AsyncInsertManyResource(self._client)

    @cached_property
    def insert_one(self) -> AsyncInsertOneResource:
        return AsyncInsertOneResource(self._client)

    @cached_property
    def replace_one(self) -> AsyncReplaceOneResource:
        return AsyncReplaceOneResource(self._client)

    @cached_property
    def update_many(self) -> AsyncUpdateManyResource:
        return AsyncUpdateManyResource(self._client)

    @cached_property
    def update_one(self) -> AsyncUpdateOneResource:
        return AsyncUpdateOneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMongoDBResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMongoDBResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMongoDBResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/VAIF-TECH/vaif-python#with_streaming_response
        """
        return AsyncMongoDBResourceWithStreamingResponse(self)


class MongoDBResourceWithRawResponse:
    def __init__(self, mongodb: MongoDBResource) -> None:
        self._mongodb = mongodb

    @cached_property
    def aggregate(self) -> AggregateResourceWithRawResponse:
        return AggregateResourceWithRawResponse(self._mongodb.aggregate)

    @cached_property
    def bulk_write(self) -> BulkWriteResourceWithRawResponse:
        return BulkWriteResourceWithRawResponse(self._mongodb.bulk_write)

    @cached_property
    def collections(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self._mongodb.collections)

    @cached_property
    def command(self) -> CommandResourceWithRawResponse:
        return CommandResourceWithRawResponse(self._mongodb.command)

    @cached_property
    def count(self) -> CountResourceWithRawResponse:
        return CountResourceWithRawResponse(self._mongodb.count)

    @cached_property
    def cursor(self) -> CursorResourceWithRawResponse:
        return CursorResourceWithRawResponse(self._mongodb.cursor)

    @cached_property
    def delete_many(self) -> DeleteManyResourceWithRawResponse:
        return DeleteManyResourceWithRawResponse(self._mongodb.delete_many)

    @cached_property
    def delete_one(self) -> DeleteOneResourceWithRawResponse:
        return DeleteOneResourceWithRawResponse(self._mongodb.delete_one)

    @cached_property
    def distinct(self) -> DistinctResourceWithRawResponse:
        return DistinctResourceWithRawResponse(self._mongodb.distinct)

    @cached_property
    def estimated_count(self) -> EstimatedCountResourceWithRawResponse:
        return EstimatedCountResourceWithRawResponse(self._mongodb.estimated_count)

    @cached_property
    def find(self) -> FindResourceWithRawResponse:
        return FindResourceWithRawResponse(self._mongodb.find)

    @cached_property
    def find_by_id(self) -> FindByIDResourceWithRawResponse:
        return FindByIDResourceWithRawResponse(self._mongodb.find_by_id)

    @cached_property
    def find_one(self) -> FindOneResourceWithRawResponse:
        return FindOneResourceWithRawResponse(self._mongodb.find_one)

    @cached_property
    def find_one_and_delete(self) -> FindOneAndDeleteResourceWithRawResponse:
        return FindOneAndDeleteResourceWithRawResponse(self._mongodb.find_one_and_delete)

    @cached_property
    def find_one_and_replace(self) -> FindOneAndReplaceResourceWithRawResponse:
        return FindOneAndReplaceResourceWithRawResponse(self._mongodb.find_one_and_replace)

    @cached_property
    def find_one_and_update(self) -> FindOneAndUpdateResourceWithRawResponse:
        return FindOneAndUpdateResourceWithRawResponse(self._mongodb.find_one_and_update)

    @cached_property
    def indexes(self) -> IndexesResourceWithRawResponse:
        return IndexesResourceWithRawResponse(self._mongodb.indexes)

    @cached_property
    def insert_many(self) -> InsertManyResourceWithRawResponse:
        return InsertManyResourceWithRawResponse(self._mongodb.insert_many)

    @cached_property
    def insert_one(self) -> InsertOneResourceWithRawResponse:
        return InsertOneResourceWithRawResponse(self._mongodb.insert_one)

    @cached_property
    def replace_one(self) -> ReplaceOneResourceWithRawResponse:
        return ReplaceOneResourceWithRawResponse(self._mongodb.replace_one)

    @cached_property
    def update_many(self) -> UpdateManyResourceWithRawResponse:
        return UpdateManyResourceWithRawResponse(self._mongodb.update_many)

    @cached_property
    def update_one(self) -> UpdateOneResourceWithRawResponse:
        return UpdateOneResourceWithRawResponse(self._mongodb.update_one)


class AsyncMongoDBResourceWithRawResponse:
    def __init__(self, mongodb: AsyncMongoDBResource) -> None:
        self._mongodb = mongodb

    @cached_property
    def aggregate(self) -> AsyncAggregateResourceWithRawResponse:
        return AsyncAggregateResourceWithRawResponse(self._mongodb.aggregate)

    @cached_property
    def bulk_write(self) -> AsyncBulkWriteResourceWithRawResponse:
        return AsyncBulkWriteResourceWithRawResponse(self._mongodb.bulk_write)

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self._mongodb.collections)

    @cached_property
    def command(self) -> AsyncCommandResourceWithRawResponse:
        return AsyncCommandResourceWithRawResponse(self._mongodb.command)

    @cached_property
    def count(self) -> AsyncCountResourceWithRawResponse:
        return AsyncCountResourceWithRawResponse(self._mongodb.count)

    @cached_property
    def cursor(self) -> AsyncCursorResourceWithRawResponse:
        return AsyncCursorResourceWithRawResponse(self._mongodb.cursor)

    @cached_property
    def delete_many(self) -> AsyncDeleteManyResourceWithRawResponse:
        return AsyncDeleteManyResourceWithRawResponse(self._mongodb.delete_many)

    @cached_property
    def delete_one(self) -> AsyncDeleteOneResourceWithRawResponse:
        return AsyncDeleteOneResourceWithRawResponse(self._mongodb.delete_one)

    @cached_property
    def distinct(self) -> AsyncDistinctResourceWithRawResponse:
        return AsyncDistinctResourceWithRawResponse(self._mongodb.distinct)

    @cached_property
    def estimated_count(self) -> AsyncEstimatedCountResourceWithRawResponse:
        return AsyncEstimatedCountResourceWithRawResponse(self._mongodb.estimated_count)

    @cached_property
    def find(self) -> AsyncFindResourceWithRawResponse:
        return AsyncFindResourceWithRawResponse(self._mongodb.find)

    @cached_property
    def find_by_id(self) -> AsyncFindByIDResourceWithRawResponse:
        return AsyncFindByIDResourceWithRawResponse(self._mongodb.find_by_id)

    @cached_property
    def find_one(self) -> AsyncFindOneResourceWithRawResponse:
        return AsyncFindOneResourceWithRawResponse(self._mongodb.find_one)

    @cached_property
    def find_one_and_delete(self) -> AsyncFindOneAndDeleteResourceWithRawResponse:
        return AsyncFindOneAndDeleteResourceWithRawResponse(self._mongodb.find_one_and_delete)

    @cached_property
    def find_one_and_replace(self) -> AsyncFindOneAndReplaceResourceWithRawResponse:
        return AsyncFindOneAndReplaceResourceWithRawResponse(self._mongodb.find_one_and_replace)

    @cached_property
    def find_one_and_update(self) -> AsyncFindOneAndUpdateResourceWithRawResponse:
        return AsyncFindOneAndUpdateResourceWithRawResponse(self._mongodb.find_one_and_update)

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithRawResponse:
        return AsyncIndexesResourceWithRawResponse(self._mongodb.indexes)

    @cached_property
    def insert_many(self) -> AsyncInsertManyResourceWithRawResponse:
        return AsyncInsertManyResourceWithRawResponse(self._mongodb.insert_many)

    @cached_property
    def insert_one(self) -> AsyncInsertOneResourceWithRawResponse:
        return AsyncInsertOneResourceWithRawResponse(self._mongodb.insert_one)

    @cached_property
    def replace_one(self) -> AsyncReplaceOneResourceWithRawResponse:
        return AsyncReplaceOneResourceWithRawResponse(self._mongodb.replace_one)

    @cached_property
    def update_many(self) -> AsyncUpdateManyResourceWithRawResponse:
        return AsyncUpdateManyResourceWithRawResponse(self._mongodb.update_many)

    @cached_property
    def update_one(self) -> AsyncUpdateOneResourceWithRawResponse:
        return AsyncUpdateOneResourceWithRawResponse(self._mongodb.update_one)


class MongoDBResourceWithStreamingResponse:
    def __init__(self, mongodb: MongoDBResource) -> None:
        self._mongodb = mongodb

    @cached_property
    def aggregate(self) -> AggregateResourceWithStreamingResponse:
        return AggregateResourceWithStreamingResponse(self._mongodb.aggregate)

    @cached_property
    def bulk_write(self) -> BulkWriteResourceWithStreamingResponse:
        return BulkWriteResourceWithStreamingResponse(self._mongodb.bulk_write)

    @cached_property
    def collections(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self._mongodb.collections)

    @cached_property
    def command(self) -> CommandResourceWithStreamingResponse:
        return CommandResourceWithStreamingResponse(self._mongodb.command)

    @cached_property
    def count(self) -> CountResourceWithStreamingResponse:
        return CountResourceWithStreamingResponse(self._mongodb.count)

    @cached_property
    def cursor(self) -> CursorResourceWithStreamingResponse:
        return CursorResourceWithStreamingResponse(self._mongodb.cursor)

    @cached_property
    def delete_many(self) -> DeleteManyResourceWithStreamingResponse:
        return DeleteManyResourceWithStreamingResponse(self._mongodb.delete_many)

    @cached_property
    def delete_one(self) -> DeleteOneResourceWithStreamingResponse:
        return DeleteOneResourceWithStreamingResponse(self._mongodb.delete_one)

    @cached_property
    def distinct(self) -> DistinctResourceWithStreamingResponse:
        return DistinctResourceWithStreamingResponse(self._mongodb.distinct)

    @cached_property
    def estimated_count(self) -> EstimatedCountResourceWithStreamingResponse:
        return EstimatedCountResourceWithStreamingResponse(self._mongodb.estimated_count)

    @cached_property
    def find(self) -> FindResourceWithStreamingResponse:
        return FindResourceWithStreamingResponse(self._mongodb.find)

    @cached_property
    def find_by_id(self) -> FindByIDResourceWithStreamingResponse:
        return FindByIDResourceWithStreamingResponse(self._mongodb.find_by_id)

    @cached_property
    def find_one(self) -> FindOneResourceWithStreamingResponse:
        return FindOneResourceWithStreamingResponse(self._mongodb.find_one)

    @cached_property
    def find_one_and_delete(self) -> FindOneAndDeleteResourceWithStreamingResponse:
        return FindOneAndDeleteResourceWithStreamingResponse(self._mongodb.find_one_and_delete)

    @cached_property
    def find_one_and_replace(self) -> FindOneAndReplaceResourceWithStreamingResponse:
        return FindOneAndReplaceResourceWithStreamingResponse(self._mongodb.find_one_and_replace)

    @cached_property
    def find_one_and_update(self) -> FindOneAndUpdateResourceWithStreamingResponse:
        return FindOneAndUpdateResourceWithStreamingResponse(self._mongodb.find_one_and_update)

    @cached_property
    def indexes(self) -> IndexesResourceWithStreamingResponse:
        return IndexesResourceWithStreamingResponse(self._mongodb.indexes)

    @cached_property
    def insert_many(self) -> InsertManyResourceWithStreamingResponse:
        return InsertManyResourceWithStreamingResponse(self._mongodb.insert_many)

    @cached_property
    def insert_one(self) -> InsertOneResourceWithStreamingResponse:
        return InsertOneResourceWithStreamingResponse(self._mongodb.insert_one)

    @cached_property
    def replace_one(self) -> ReplaceOneResourceWithStreamingResponse:
        return ReplaceOneResourceWithStreamingResponse(self._mongodb.replace_one)

    @cached_property
    def update_many(self) -> UpdateManyResourceWithStreamingResponse:
        return UpdateManyResourceWithStreamingResponse(self._mongodb.update_many)

    @cached_property
    def update_one(self) -> UpdateOneResourceWithStreamingResponse:
        return UpdateOneResourceWithStreamingResponse(self._mongodb.update_one)


class AsyncMongoDBResourceWithStreamingResponse:
    def __init__(self, mongodb: AsyncMongoDBResource) -> None:
        self._mongodb = mongodb

    @cached_property
    def aggregate(self) -> AsyncAggregateResourceWithStreamingResponse:
        return AsyncAggregateResourceWithStreamingResponse(self._mongodb.aggregate)

    @cached_property
    def bulk_write(self) -> AsyncBulkWriteResourceWithStreamingResponse:
        return AsyncBulkWriteResourceWithStreamingResponse(self._mongodb.bulk_write)

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self._mongodb.collections)

    @cached_property
    def command(self) -> AsyncCommandResourceWithStreamingResponse:
        return AsyncCommandResourceWithStreamingResponse(self._mongodb.command)

    @cached_property
    def count(self) -> AsyncCountResourceWithStreamingResponse:
        return AsyncCountResourceWithStreamingResponse(self._mongodb.count)

    @cached_property
    def cursor(self) -> AsyncCursorResourceWithStreamingResponse:
        return AsyncCursorResourceWithStreamingResponse(self._mongodb.cursor)

    @cached_property
    def delete_many(self) -> AsyncDeleteManyResourceWithStreamingResponse:
        return AsyncDeleteManyResourceWithStreamingResponse(self._mongodb.delete_many)

    @cached_property
    def delete_one(self) -> AsyncDeleteOneResourceWithStreamingResponse:
        return AsyncDeleteOneResourceWithStreamingResponse(self._mongodb.delete_one)

    @cached_property
    def distinct(self) -> AsyncDistinctResourceWithStreamingResponse:
        return AsyncDistinctResourceWithStreamingResponse(self._mongodb.distinct)

    @cached_property
    def estimated_count(self) -> AsyncEstimatedCountResourceWithStreamingResponse:
        return AsyncEstimatedCountResourceWithStreamingResponse(self._mongodb.estimated_count)

    @cached_property
    def find(self) -> AsyncFindResourceWithStreamingResponse:
        return AsyncFindResourceWithStreamingResponse(self._mongodb.find)

    @cached_property
    def find_by_id(self) -> AsyncFindByIDResourceWithStreamingResponse:
        return AsyncFindByIDResourceWithStreamingResponse(self._mongodb.find_by_id)

    @cached_property
    def find_one(self) -> AsyncFindOneResourceWithStreamingResponse:
        return AsyncFindOneResourceWithStreamingResponse(self._mongodb.find_one)

    @cached_property
    def find_one_and_delete(self) -> AsyncFindOneAndDeleteResourceWithStreamingResponse:
        return AsyncFindOneAndDeleteResourceWithStreamingResponse(self._mongodb.find_one_and_delete)

    @cached_property
    def find_one_and_replace(self) -> AsyncFindOneAndReplaceResourceWithStreamingResponse:
        return AsyncFindOneAndReplaceResourceWithStreamingResponse(self._mongodb.find_one_and_replace)

    @cached_property
    def find_one_and_update(self) -> AsyncFindOneAndUpdateResourceWithStreamingResponse:
        return AsyncFindOneAndUpdateResourceWithStreamingResponse(self._mongodb.find_one_and_update)

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithStreamingResponse:
        return AsyncIndexesResourceWithStreamingResponse(self._mongodb.indexes)

    @cached_property
    def insert_many(self) -> AsyncInsertManyResourceWithStreamingResponse:
        return AsyncInsertManyResourceWithStreamingResponse(self._mongodb.insert_many)

    @cached_property
    def insert_one(self) -> AsyncInsertOneResourceWithStreamingResponse:
        return AsyncInsertOneResourceWithStreamingResponse(self._mongodb.insert_one)

    @cached_property
    def replace_one(self) -> AsyncReplaceOneResourceWithStreamingResponse:
        return AsyncReplaceOneResourceWithStreamingResponse(self._mongodb.replace_one)

    @cached_property
    def update_many(self) -> AsyncUpdateManyResourceWithStreamingResponse:
        return AsyncUpdateManyResourceWithStreamingResponse(self._mongodb.update_many)

    @cached_property
    def update_one(self) -> AsyncUpdateOneResourceWithStreamingResponse:
        return AsyncUpdateOneResourceWithStreamingResponse(self._mongodb.update_one)
