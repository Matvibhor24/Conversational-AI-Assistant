from pydantic import BaseModel
from typing import List, Literal, Optional


class Turn(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class SessionMemory(BaseModel):
    session_id: str
    turns: List[Turn]
    summary: str | None = None
    document_ids: Optional[List[str]] = None
