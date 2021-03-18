# generated by datamodel-codegen:
#   filename:  tickets.json
#   timestamp: 2021-03-17T08:08:36+00:00

from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, Field


class Ticket(BaseModel):
    id: str = Field(..., alias='_id')
    url: str
    external_id: str
    created_at: str
    type: Optional[str] = None
    subject: str
    description: Optional[str] = None
    priority: str
    status: str
    submitter_id: int
    assignee_id: Optional[int] = None
    organization_id: Optional[int] = None
    tags: List[str]
    has_incidents: bool
    due_at: Optional[str] = None
    via: str


class Tickets(BaseModel):
    __root__: List[Ticket]
