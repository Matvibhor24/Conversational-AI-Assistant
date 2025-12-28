from typing import Literal
from pydantic import BaseModel
from typing import List, Literal


class ReasoningTask(BaseModel):
    description: str
    tool: Literal["none", "summarize", "search", "code", "retrieve"]
