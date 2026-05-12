# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AuthSettingsParams"]


class AuthSettingsParams(TypedDict, total=False):
    access_token_lifetime_minutes: Annotated[int, PropertyInfo(alias="accessTokenLifetimeMinutes")]

    allowed_redirect_urls: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedRedirectUrls")]

    allow_password_recovery: Annotated[bool, PropertyInfo(alias="allowPasswordRecovery")]

    allow_sign_up: Annotated[bool, PropertyInfo(alias="allowSignUp")]

    lockout_duration_minutes: Annotated[int, PropertyInfo(alias="lockoutDurationMinutes")]

    max_sign_in_attempts: Annotated[int, PropertyInfo(alias="maxSignInAttempts")]

    mfa_enabled: Annotated[bool, PropertyInfo(alias="mfaEnabled")]

    mfa_enforced: Annotated[bool, PropertyInfo(alias="mfaEnforced")]

    min_password_length: Annotated[int, PropertyInfo(alias="minPasswordLength")]

    refresh_token_lifetime_days: Annotated[int, PropertyInfo(alias="refreshTokenLifetimeDays")]

    require_email_verification: Annotated[bool, PropertyInfo(alias="requireEmailVerification")]

    require_numbers: Annotated[bool, PropertyInfo(alias="requireNumbers")]

    require_phone_verification: Annotated[bool, PropertyInfo(alias="requirePhoneVerification")]

    require_special_chars: Annotated[bool, PropertyInfo(alias="requireSpecialChars")]

    require_uppercase: Annotated[bool, PropertyInfo(alias="requireUppercase")]

    single_session_mode: Annotated[bool, PropertyInfo(alias="singleSessionMode")]

    user_table_auto_create: Annotated[bool, PropertyInfo(alias="userTableAutoCreate")]

    user_table_name: Annotated[Optional[str], PropertyInfo(alias="userTableName")]

    user_table_sync_fields: Annotated[SequenceNotStr[str], PropertyInfo(alias="userTableSyncFields")]
