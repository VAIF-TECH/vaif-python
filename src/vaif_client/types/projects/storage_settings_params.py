# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["StorageSettingsParams"]


class StorageSettingsParams(TypedDict, total=False):
    allowed_mime_types: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="allowedMimeTypes")]

    allowed_transforms: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedTransforms")]

    blocked_mime_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="blockedMimeTypes")]

    cdn_enabled: Annotated[bool, PropertyInfo(alias="cdnEnabled")]

    default_cache_ttl: Annotated[int, PropertyInfo(alias="defaultCacheTtl")]

    default_file_size_limit: Annotated[int, PropertyInfo(alias="defaultFileSizeLimit")]

    edge_caching_enabled: Annotated[bool, PropertyInfo(alias="edgeCachingEnabled")]

    enable_image_transform: Annotated[bool, PropertyInfo(alias="enableImageTransform")]

    max_file_size_limit: Annotated[int, PropertyInfo(alias="maxFileSizeLimit")]

    max_image_dimension: Annotated[int, PropertyInfo(alias="maxImageDimension")]

    signed_url_default_expiry: Annotated[int, PropertyInfo(alias="signedUrlDefaultExpiry")]

    signed_url_max_expiry: Annotated[int, PropertyInfo(alias="signedUrlMaxExpiry")]

    webhook_enabled: Annotated[bool, PropertyInfo(alias="webhookEnabled")]

    webhook_events: Annotated[SequenceNotStr[str], PropertyInfo(alias="webhookEvents")]

    webhook_url: Annotated[Optional[str], PropertyInfo(alias="webhookUrl")]
