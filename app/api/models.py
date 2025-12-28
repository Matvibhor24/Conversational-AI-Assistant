from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    session_id: str


class ChatResponse(BaseModel):
    request_id: str
    answer: str
