# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["JobCreateResponse"]


class JobCreateResponse(BaseModel):
    events_url: str = FieldInfo(alias="eventsUrl")

    job_id: str = FieldInfo(alias="jobId")

    model: str

    ok: Literal[True]

    status: str

    status_url: str = FieldInfo(alias="statusUrl")

    tier: str
