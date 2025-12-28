from pydantic import BaseModel
from typing import Literal, Optional


class RoutedResponse(BaseModel):
    mode: Literal["clarification", "direct", "deep"]
    message: Optional[str] = None
