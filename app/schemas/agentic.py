from typing import Literal
from pydantic import BaseModel


class ReasoningTask(BaseModel):
    description: str
    tool: Literal["none", "summarize", "search", "code", "retrieve"]
