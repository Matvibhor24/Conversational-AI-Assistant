from pydantic import BaseModel
from typing import Optional, Literal


class Understanding(BaseModel):
    """
    Represents the system's understanding of a user request.
    This is metadata ONLY - not an answer.
    """

    clarity: Literal["clear", "ambiguous"]
    clarification_question: Optional[str] = None
    attachment_use: Literal["use", "ignore"]
    attachment_scope: Literal["none", "global", "local"]
    response_depth: Literal["short", "medium", "deep"]
    reasoning_complexity: Literal["simple", "multi-step", "research"]
    tool_requirements: Literal["none", "optional", "required"]
    confidence: float
