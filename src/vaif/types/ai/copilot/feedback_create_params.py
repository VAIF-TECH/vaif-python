# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    feedback_type: Required[Annotated[Literal["correct", "incorrect", "partial"], PropertyInfo(alias="feedbackType")]]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageId")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]

    corrected_intent: Annotated[str, PropertyInfo(alias="correctedIntent")]

    user_feedback: Annotated[str, PropertyInfo(alias="userFeedback")]
