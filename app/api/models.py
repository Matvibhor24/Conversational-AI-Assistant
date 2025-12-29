from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile, File, Form


class ChatRequest(BaseModel):
    message: str = (Form(...),)
    session_id: str = (Form(...),)
    file: UploadFile | None = File(None)


class ChatResponse(BaseModel):
    request_id: str
    answer: str
