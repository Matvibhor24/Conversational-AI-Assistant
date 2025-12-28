from pydantic import BaseModel
from typing import Optional, Literal


class Understanding(BaseModel):
    """
    Represents the system's understanding of a user request.
    This is metadata ONLY - not an answer.
    """

    user_goal: str
    clarity: Literal["clear", "ambiguous"]
    clarification_question: Optional[str] = None
    response_depth: Literal["short", "medium", "deep"]
    tool_requirements: Literal["none", "optional", "required"]
    confidence: float
