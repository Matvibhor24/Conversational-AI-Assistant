from pydantic import BaseModel
from typing import Literal


class IngestedDocument(BaseModel):
    raw_text: str
    source_type: Literal["pdf", "docx", "image", "audio"]
    extraction_method: Literal["pymupdf", "docling", "whisper"]
