# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AIAnswerCreateParams", "ConversationHistory"]


class AIAnswerCreateParams(TypedDict, total=False):
    context: Required[str]

    question: Required[str]

    conversation_history: Annotated[Iterable[ConversationHistory], PropertyInfo(alias="conversationHistory")]


class ConversationHistory(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "assistant"]]
