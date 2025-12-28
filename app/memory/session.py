from pydantic import BaseModel
from typing import List, Literal


class Turn(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class SessionMemory(BaseModel):
    session_id: str
    turns: List[Turn]
    summary: str | None = None
