# generated by datamodel-codegen:
#   filename:  users.json
#   timestamp: 2021-03-17T08:08:46+00:00

from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(..., alias='_id')
    url: str
    external_id: str
    name: str
    alias: Optional[str] = None
    created_at: str
    active: bool
    verified: Optional[bool] = None
    shared: bool
    locale: Optional[str] = None
    timezone: Optional[str] = None
    last_login_at: str
    email: Optional[str] = None
    phone: str
    signature: str
    organization_id: Optional[int] = None
    tags: List[str]
    suspended: bool
    role: str


class Users(BaseModel):
    __root__: List[User]
