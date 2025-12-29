from pydantic import BaseModel
from typing import Optional


class DocumentSession(BaseModel):
    document_id: str
    raw_text: str
    summary: Optional[str] = None
    vector_index_id: Optional[str] = None
    has_summary: bool = False
    has_index: bool = False
